import pyaudio
import wave
import audioop
import time

FORMAT = pyaudio.paInt16 
CHANNELS = 1 
RATE = 44100 
CHUNK = 1024 
RECORD_TIME = 10  # Time to record after detecting voice
THRESHOLD = 500  # Audio threshold

def listen_for_speech(threshold=THRESHOLD):
    """
    Listens to microphone to detect phrases. 
    Stops listening after a fixed duration.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, 
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True, 
                    frames_per_buffer=CHUNK)

    print("* Listening to mic. ")
    audio2send = []
    cur_data = ''  
    started = False
    start_time = None

    while True:
        cur_data = stream.read(CHUNK)
        rms = audioop.rms(cur_data, 2)

        if rms > THRESHOLD and not started:
            print("Starting recording...")
            started = True
            start_time = time.time()

        if started:
            audio2send.append(cur_data)
            if time.time() - start_time > RECORD_TIME:
                print("Finished recording, processing audio...")
                filename = save_audio(list(audio2send))
                started = False
                audio2send = []
                print(f"Saved audio as {filename}")

    print("* Done listening")
    stream.close()
    p.terminate()

def save_audio(data):
    """Saves audio data to a file."""
    filename = f"output_{int(time.time())}.wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(data))
    wf.close()
    return filename

if __name__ == "__main__":
    listen_for_speech()
