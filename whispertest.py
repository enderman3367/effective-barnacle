from gradio_client import Client

# Set up the Gradio client for the local endpoint
API_URL = "http://localhost:7860/"
client = Client(API_URL)

def transcribe_audio(audio_path, task="transcribe", return_timestamps=False):
    """Function to transcribe an audio file using our endpoint"""
    text, runtime = client.predict(
        audio_path,
        task,
        return_timestamps,
        api_name="/predict_1",
    )
    return text

# Example usage:
output = transcribe_audio("path_to_audio_file.mp3")
print(output)