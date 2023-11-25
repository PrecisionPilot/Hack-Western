from google.cloud import speech

client = speech.SpeechClient.from_service_account_file("auth.json")
file_name = "speech1.mp3"
with open(file_name, "rb") as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)
config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=False,
        language_code="zh",
    )
response = client.recognize(config=config, audio=audio_file)

print(response.results[0].alternatives[0].transcript)