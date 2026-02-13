import assemblyai as aai
import os
from dotenv import load_dotenv as ld

ld()

key = os.getenv("API_KEY")
aai.settings.api_key = key
audio_file = "./voice1.wav"
config = aai.TranscriptionConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)
transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
    raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)