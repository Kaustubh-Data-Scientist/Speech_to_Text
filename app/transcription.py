# import azure.cognitiveservices.speech as speechsdk
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# def transcribe_audio(file_path):
#     """Transcribes the audio file using Azure Speech-to-Text API."""
#     speech_key = os.getenv("AZURE_SPEECH_API_KEY")
#     service_region = os.getenv("AZURE_REGION")

#     if not speech_key or not service_region:
#         raise ValueError("Missing Azure Speech API key or region in environment variables.")

#     # Configure speech recognition
#     speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
#     audio_input = speechsdk.audio.AudioConfig(filename=file_path)
#     recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

#     # Enable speaker diarization
#     conversation_transcriber = speechsdk.ConversationTranscriber(audio_input)
#     speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_SingleLanguageIdPriority, "Latent")

#     result = recognizer.recognize_once()

#     if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         return result.text
#     elif result.reason == speechsdk.ResultReason.NoMatch:
#         return "No speech recognized in the audio file."
#     elif result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = result.cancellation_details
#         error_msg = f"Transcription canceled: {cancellation_details.reason}"
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             error_msg += f" | Error details: {cancellation_details.error_details}"
#         return error_msg
#     else:
#         return "Unexpected error during transcription."
import os
import assemblyai as aai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# AssemblyAI API key from .env
AUDIO_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')

if not AUDIO_API_KEY:
    raise ValueError("ASSEMBLYAI_API_KEY is not set in .env file.")

aai.settings.api_key = AUDIO_API_KEY


def transcribe_audio(file_path):
    """
    Transcribes an audio file using AssemblyAI API with speaker diarization.
    """
    # Initialize the client
    transcriber = aai.Transcriber()

    # Upload the audio file
    print("Uploading the file...")
    upload_response = transcriber.upload(file_path)
    audio_url = upload_response.get("upload_url")

    print("File uploaded. Starting transcription...")

    # Start the transcription with speaker diarization enabled
    transcript_response = transcriber.transcribe(audio_url, speaker_labels=True)
    transcript_id = transcript_response.get("id")

    # Poll for results
    print("Waiting for transcription to complete...")
    result = transcriber.get_transcription(transcript_id, wait=True)

    if result.get("status") == "completed":
        return result.get("text", "Transcription not found.")
    else:
        raise Exception("Transcription failed. Status: " + result.get("status"))
