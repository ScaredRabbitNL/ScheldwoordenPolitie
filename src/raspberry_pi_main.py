import os
import subprocess
import assemblyai
import speech_to_text as stt
import siren
import datetime
import json
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
assemblyai_api_key = os.getenv("ASSEMBLYAI_API_KEY")
mistralai_api_key = os.getenv("MISTRALAI_API_KEY")

os.makedirs("logs/api_requests/", exist_ok=True)
os.makedirs("./assets/audio", exist_ok=True)
audio_file = "./assets/audio/voice.wav"

assemblyai.settings.api_key = assemblyai_api_key
assemblyai_config = stt.createAssemblyAIConfig(
    speech_models=["universal-3-pro", "universal-2"],
    language_detection=True
)
assemblyai_transcriber = stt.createAssemblyAITranscriber(config=assemblyai_config)

mistral_client = Mistral(api_key=mistralai_api_key)

AGENT_ID_FILE = ".mistral_agent_id"

class CachedAgent:
    def __init__(self, id):
        self.id = id

def get_or_create_agent():
    if os.path.exists(AGENT_ID_FILE):
        with open(AGENT_ID_FILE) as f:
            return CachedAgent(f.read().strip())
    agent = stt.createSimpleAgent(
        model="mistral-small-latest",
        name="Politie Agent Same",
        description="Let op met wat je zegt want Politie Agent Sam luistert mee!!",
        client=mistral_client
    )
    with open(AGENT_ID_FILE, "w") as f:
        f.write(agent.id)
    return agent

mistral_agent = get_or_create_agent()
print("Installatie compleet! (Ctrl+C om te stoppen).\n")

def record():
    print("Opnemen voor 10 seconden...")
    subprocess.run(
        [
            "arecord",
            "--device=hw:3,0",
            "--format", "S16_LE",
            "--rate", "44100",
            "-V", "mono",
            "-c1",
            "--duration=10",
            audio_file,
        ],
        check=True
    )
    print("Recording done.")

def transcribe():
    transcript = assemblyai_transcriber.transcribe(audio_file)
    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return transcript

def save_log(formatted):
    date_str = datetime.datetime.now().date()
    number = 1
    while os.path.exists(f"logs/api_requests/api_request_log_{date_str}+{number}.json"):
        number += 1
    file_path = f"logs/api_requests/api_request_log_{date_str}+{number}.json"
    with open(file_path, "w") as f:
        f.write(formatted)
    print(f"Log saved: {file_path}") 

while True:
    try:
        record()
        assemblyai_transcript = transcribe()

        if os.path.exists(audio_file):
            os.remove(audio_file)
            print("Audio bestand verwijderd")

        mistral_conversation_inputs = [
            {
                "role": "user",
                "content": (
                    f"Beoordeel de volgende tekst (aangegeven met Tekst:), is het heel onvriendlijk (1) "
                    f"of heel vriendelijk (10) of ergens er tussen in (2-9). Geef alleen het nummer. "
                    f"Tekst: {assemblyai_transcript.text}"
                ),
            }
        ]

        response = stt.GET(agent=mistral_agent, client=mistral_client, inputs=mistral_conversation_inputs)
        ai_text_rating = int(response.outputs[0].content)
        print(f"De beoordeling van deze audio is: {ai_text_rating}")

        if ai_text_rating <= 3:
            siren.siren(3 * ai_text_rating)
   

        response_dict = response.model_dump() if hasattr(response, 'model_dump') else response.__dict__
        save_log(json.dumps(response_dict, indent=4, default=str))

    except KeyboardInterrupt:
        print("\nGestopt door gebruiker.")
        break
    except Exception as e:
        print(f"Error gedurende lus iteratie: {e}")
        if os.path.exists(audio_file):
            os.remove(audio_file)
        continue

