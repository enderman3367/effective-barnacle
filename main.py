import sys
sys.path.append("/usr/bin/python3")
import openai
import os
import threading
import requests
import pyglet
from gradio_client import Client
import gradio as gr
from whisper_jax import FlaxWhisperPipline

# Initialize the Whisper JAX pipeline
pipeline = FlaxWhisperPipline()

#taking a crap on the establishment, i salute you.
openai.api_key = os.getenv("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")

# i dont belive in consistency
API_URL = "http://localhost:7860/"
client = Client(API_URL)


# THIS IS WHERE I WOULD PUT THE WINDOW SETUP...
# IF I HAD ONE



 

#defines arties usable commands

#defines text command
def text(arg):
    print('fuckyou')

#defines emo command
def emotion(arg):
    print(f"RUN function with argument {arg}")

#defines save command
def save(bigman):
   # opens the file in append mode
    with open("my_file.txt", "a") as file:
        file.write(bigman)

#command processing
def process_command(command):
    function_map = {
        "TXT": text,
        "EMO": emotion,
        "SAV": save,
    }

    parts = command.split(":")
    if len(parts) == 2:
        cmd, arg = parts
        if cmd in function_map:
            function = function_map[cmd]
            thread = threading.Thread(target=function, args=(arg,))
            thread.start()
        else:
            print("Invalid command.")
    else:
        print("Invalid input format.")

def get_commands_from_openai():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": ""
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if "choices" in response and response["choices"]:
            commands = response["choices"][0]["message"]["content"].split("\n")
            for cmd in commands:
                process_command(cmd)
        else:
            print("No commands received from OpenAI.")
    except Exception as e:
        print(f"An error occurred: {e}")


get_commands_from_openai()




    

def transcribe(audio):
    # Transcribe the audio using the Whisper JAX pipeline
    result = pipeline(audio)
    return result

# Create the Gradio interface
interface = gr.Interface(
    fn=transcribe,
    inputs=gr.inputs.Audio(source="microphone"),  # Capture audio from the microphone
    outputs="text"
)

interface.launch()