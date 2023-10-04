import pyaudio
from elevenlabs import generate, set_api_key

set_api_key("bb73cb3343b6c5408e2c9bb1cdc881bb")

def text_stream():
    yield "Hi there, I'm Eleven"
    yield "I'm a text to speech API"

audio_stream = generate(
    text=text_stream(),
    voice="Nicole",
    model="eleven_monolingual_v1",
    stream=True
)

# PyAudio stream configuration
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=22050,
                output=True)

# Stream the audio data through PyAudio
for audio_chunk in audio_stream:
    stream.write(audio_chunk)

# Close the PyAudio stream and terminate the audio player
stream.stop_stream()
stream.close()
p.terminate()
