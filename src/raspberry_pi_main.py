import os
import subprocess
import assemblyai
import speech_to_text as stt
import datetime
import json
import siren
from mistralai import Mistral
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
assemblyai_api_key = os.getenv("ASSEMBLYAI_API_KEY")
mistralai_api_key = os.getenv("MISTRALAI_API_KEY")

os.makedirs("logs", exist_ok=True)
audio_file = "./assets/audio/voice.wav"  

print("Recording for 10 seconds...")
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

assemblyai.settings.api_key = assemblyai_api_key
assemblyai_config = stt.createAssemblyAIConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)
assemblyai_transcriber = stt.createAssemblyAITranscriber(config=assemblyai_config)

mistral_client = Mistral(api_key=mistralai_api_key)

AGENT_ID_FILE = ".mistral_agent_id"

def transcribe():
    transcript = assemblyai_transcriber.transcribe(audio_file)
    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return transcript

def get_or_create_agent():
    if os.path.exists(AGENT_ID_FILE):
        with open(AGENT_ID_FILE) as f:
            agent_id = f.read().strip()
        class CachedAgent:
            def __init__(self, id): self.id = id
        return CachedAgent(agent_id)
    else:
        agent = stt.createSimpleAgent(
            model="mistral-small-latest",
            name="Politie Agent Same",
            description="Let op met wat je zegt want Politie Agent Sam luistert mee!!",
            client=mistral_client
        )
        with open(AGENT_ID_FILE, "w") as f:
            f.write(agent.id)
        return agent

with ThreadPoolExecutor() as executor:
    transcript_future = executor.submit(transcribe)
    agent_future = executor.submit(get_or_create_agent)

assemblyai_transcript = transcript_future.result()
mistral_agent = agent_future.result()


if os.path.exists(audio_file):
    os.remove(audio_file)
    print(f"Deleted audio file: {audio_file}")

mistral_conversation_inputs = [
    {
        "role": "user",
        "content": f"Beoordeel de volgende tekst (aangegeven met Tekst:), is het heel onvriendlijk (10) of heel vriendelijk (1) of ergens er tussen in (2-9). Geef alleen het nummer. Tekst: {assemblyai_transcript.text}",
    }
]

response = stt.GET(agent=mistral_agent, client=mistral_client, inputs=mistral_conversation_inputs)
response_dict = response.model_dump() if hasattr(response, 'model_dump') else response.__dict__
formatted = json.dumps(response_dict, indent=4, default=str)

date_str = datetime.datetime.now().date()
number = 1

while os.path.exists(f"logs/{date_str}+{number}.txt"):
    number += 1

file_path = f"logs/log_{date_str}+{number}.txt"

with open(file_path, "w") as responseFile:
    responseFile.write(formatted)

ai_text_rating = int(response.outputs[0].content)
print(f"De beoordeling van deze audio is: {ai_text_rating}")

if ai_text_rating >= 7:
    siren.siren(3 * ai_text_rating)