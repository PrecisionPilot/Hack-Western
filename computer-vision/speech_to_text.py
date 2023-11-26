import pyaudio
import wave
import threading
from google.cloud import speech

# -------------------- Speech to file (voice recorder) --------------------

is_recording = False
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
frames = []
stop_event = threading.Event()
def record():
    global stream, frames
    while not stop_event.is_set():
        data = stream.read(1024)
        frames.append(data)
t = threading.Thread(target=record)

def Start():
    global t, frames, is_recording
    if is_recording:
        return
    is_recording = True
    frames = []
    stop_event.clear()

    stream.start_stream()
    t = threading.Thread(target=record)
    print("Recording...")
    t.start()

def Stop():
    global t, frames, is_recording
    if not is_recording:
        return
    is_recording = False

    stop_event.set()
    t.join()

    stream.stop_stream()
    # stream.close()
    # audio.terminate()

    with wave.open("speech.wav", "wb") as sound_file:
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))


# -------------------- File to speech recognition --------------------

def SpeechToText():
    print("Transcribing...")
    client = speech.SpeechClient.from_service_account_file("auth.json")
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
            return result.alternatives[0].transcript
    else:
        print("No speech detected")
        return ""

if __name__ == "__main__":
    Start()
    input("Press enter to stop recording...")
    Stop()
    SpeechToText()

    Start()
    input("Press enter to stop recording...")
    Stop()
    SpeechToText()