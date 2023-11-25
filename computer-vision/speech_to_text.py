import pyaudio
import wave

# -------------------- Speech to file (voice recorder) --------------------

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []

try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

with wave.open("speech.wav", "wb") as sound_file:
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))

print("Analysing speech...")


# -------------------- File to speech recognition --------------------
from google.cloud import speech


client = speech.SpeechClient.from_service_account_file("computer-vision/auth.json")
file_name = "speech.wav"
with open(file_name, "rb") as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)
config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=False,
        language_code="en-US",
    )
response = client.recognize(config=config, audio=audio_file)

if len(response.results) >= 1:
    for result in response.results:
        print(result.alternatives[0].transcript)
else:
    print("No speech detected")