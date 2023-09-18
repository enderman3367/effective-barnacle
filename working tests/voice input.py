import openai
from docx import Document
import openai
import webrtcvad
import openai
import pyaudio
import sys
import time
import wave


    
print("Voice Activity Monitoring")
print("1 - Activity Detected")
print("_ - No Activity Detected")
print("X - No Activity Detected for Last IDLE_TIME Seconds")
print("\nMonitor Voice Activity Below:")

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000 # 8000, 16000, 32000
FRAMES_PER_BUFFER = 320

# Initialize the VAD with a mode (e.g. aggressive, moderate, or gentle)
# 0: Least filtering noise - 3: Aggressive in filtering noise
vad = webrtcvad.Vad(3)

# Open a PyAudio stream to get audio data from the microphone
pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=FRAMES_PER_BUFFER)

inactive_session = False
inactive_since = time.time()
frames = [] # list to hold audio frames
while True:
    # Read audio data from the microphone
    data = stream.read(FRAMES_PER_BUFFER)

    # Check if the audio is active (i.e. contains speech)
    is_active = vad.is_speech(data, sample_rate=RATE)
    
    # Check Flagging for Stop after N Seconds
    idle_time = 0.32
    if is_active:
        inactive_session = False
    else:
        if inactive_session == False:
            inactive_session = True
            inactive_since = time.time()
        else:
            inactive_session = True

    # Stop hearing if no voice activity detected for N Seconds
    if (inactive_session == True) and (time.time() - inactive_since) > idle_time:
        sys.stdout.write('X')
        
        # Append data chunk of audio to frames - save later
        frames.append(data)

        # Save the recorded data as a WAV file
        audio_recorded_filename = f'usraudfile.wav'
        wf = wave.open(audio_recorded_filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pa.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # # Stop Debug
        break
        
        # # Some Sample Activity - 5 Seconds execution
        # time.sleep(5)
        # # Flagging to Listen Again
        # inactive_session = False
    else:
        sys.stdout.write('1' if is_active else '_')
    
    # Append data chunk of audio to frames - save later
    frames.append(data)

    # Flush Terminal
    sys.stdout.flush()

# Close the PyAudio stream
stream.stop_stream()

openai.api_key = "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"
audio_file = open("usraudfile.wav", "rb")

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

transcription_text = transcribe_audio('usraudfile.wav')
print(transcription_text)