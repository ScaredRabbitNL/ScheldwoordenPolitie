import os
import assemblyai
import speech_to_text as stt
import datetime
import json
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
assemblyai_api_key = os.getenv("ASSEMBLYAI_API_KEY")
mistralai_api_key = os.getenv("MISTRALAI_API_KEY")

os.makedirs("logs", exist_ok=True)
audio_file = "./assets/audio/audio.mp3"

assemblyai.settings.api_key = assemblyai_api_key

assemblyai_config = stt.createAssemblyAIConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)
assemblyai_transcriber = stt.createAssemblyAITranscriber(config=assemblyai_config)
assemblyai_transcript = assemblyai_transcriber.transcribe(audio_file)

if assemblyai_transcript.status == "error":
    raise RuntimeError(f"Transcription failed: {assemblyai_transcript.error}")

mistral_client = Mistral(api_key=mistralai_api_key)
mistral_agent = stt.createSimpleAgent(model="mistral-medium-2505", name="Politie Agent Same", description="Let op met wat je zegt want Politie Agent Sam luistert mee!!", client=mistral_client)

mistral_conversation_inputs = [
    {
        "role": "user",
        "content": f"Beoordeel de volgende tekst (aangegeven met Tekst:), is het heel onvriendlijk (1) of heel vriendelijk (10) of ergens er tussen in (2-9). Geef alleen het nummer. Tekst: {assemblyai_transcript.text}",
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

ai_text_rating = response.outputs[0].content