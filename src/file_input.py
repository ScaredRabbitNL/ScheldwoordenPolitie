import assemblyai as aai
import os
from dotenv import load_dotenv as ld

outputDir = "output"

ld()
key = os.getenv("API_KEY")
aai.settings.api_key = key
audio_file = "./voice1.wav"
config = aai.TranscriptionConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)
transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
    raise RuntimeError(f"Transcription failed: {transcript.error}")

try:
    os.mkdir(outputDir)
    print(f"Directory '{outputDir}' created successfully.")
except FileExistsError:
    print(f"Directory '{outputDir}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{outputDir}'.")
except Exception as e:
    print(f"An error occurred: {e}")


with open("output/wavContent.txt", "x") as file:
    file.write(transcript.text)

print(transcript.text)