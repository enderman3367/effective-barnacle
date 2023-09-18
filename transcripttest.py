import jax.numpy as jnp
from whisper_jax import FlaxWhisperPipline

# Instantiate the pipeline with batching and half-precision
pipeline = FlaxWhisperPipline("openai/whisper-large-v2", dtype=jnp.bfloat16, batch_size=16)

# Use the pipeline to transcribe audio
text = pipeline("usraudfile.wav")
print(text)