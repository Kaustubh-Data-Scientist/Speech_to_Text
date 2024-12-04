import requests
import os
from dotenv import load_dotenv
import assemblyai as aai

aai.settings.api_key = "5e04ba5066204a7786c6067dfce20525"
transcriber = aai.Transcriber()

# transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
transcript = transcriber.transcribe(r"C:\Users\Ajay\Desktop\Data Science\Project\Speech_to_Text\audio\resources_sample-calls.mp3")

print(transcript.text)