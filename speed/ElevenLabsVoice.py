from elevenlabs import set_api_key,generate,stream,Voice,VoiceSettings
def process_text(content):
    audio_stream = generate(text=content, stream=True)
    stream(audio_stream)
    print(f"[speaking as]: {content}")

process_text('hey')