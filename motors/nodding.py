import openai
import time
import time
import wave
import pyaudio
import subprocess
import webrtcvad
from gradio_client import Client as gradCli

# OpenAI API setup
openai.api_key = "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"

conversation_history = [
    {
        "role": "system",
        "content": "you are a helpful assistant that responds with cute answers, but only in yes or no format, like so;\n[YES]\n[NO]\ndo not add anything else to your reply. only [YES] or [NO]."
    }
]

def updated_parse_reply(reply):
    """Parse the reply to extract the new commands and their content."""
    if "[YES]" in reply:
        return {"YES": "[YES]"}
    elif "[NO]" in reply:
        return {"NO": "[NO]"}
    else:
        return {}

def process_yes():
    subprocess.run(['python', 'yes.py'])


def process_no():
    subprocess.run(['python', 'no.py'])

command_to_function_updated = {
    "YES": process_yes,
    "NO": process_no
}

def handle_reply(reply):
    """Handle the reply by parsing it and triggering the appropriate function."""
    command_dict = updated_parse_reply(reply)
    for command, func in command_dict.items():
        if command in command_to_function_updated:
            command_to_function_updated[command]()

# Initialize Gradio client
api_url = "https://sanchit-gandhi-whisper-jax.hf.space/"
client = gradCli(api_url)

def transcribe_audio(audio_path):
    """Function to transcribe an audio file using the Whisper JAX endpoint."""
    text, runtime = client.predict(audio_path, task="transcribe", api_name="/predict_1")
    return text

while True:
    # Voice activity detection setup
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    FRAMES_PER_BUFFER = 320
    vad = webrtcvad.Vad(3)
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=FRAMES_PER_BUFFER)

    inactive_session = False
    inactive_since = time.time()
    frames = []
    while True:
        data = stream.read(FRAMES_PER_BUFFER)
        is_active = vad.is_speech(data, sample_rate=RATE)
        idle_time = 1.25
        if is_active:
            inactive_session = False
        else:
            if not inactive_session:
                inactive_session = True
                inactive_since = time.time()
        if inactive_session and (time.time() - inactive_since) > idle_time:
            break
        frames.append(data)

    stream.stop_stream()
    stream.close()
    pa.terminate()

    # Save the recorded data as a WAV file
    audio_recorded_filename = 'usraudfile.wav'
    wf = wave.open(audio_recorded_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Transcribe the audio
    transcription_text = str(transcribe_audio('usraudfile.wav'))
    print('Transcription:', transcription_text)

    # Update conversation history
    conversation_history.append({"role": "user", "content": transcription_text})
    
    # Get reply from OpenAI
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation_history
    )
    reply = completion.choices[0].message['content']
    conversation_history.append({"role": "assistant", "content": reply})
    print('Response:', reply)

    # Handle the reply
    handle_reply(reply)

    # Check for conversation termination conditions
    if "bye" in transcription_text.lower():
        print('User said bye. Exiting.')
        break
