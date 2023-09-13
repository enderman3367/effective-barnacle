import pyaudio
import numpy as np

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
NOISE_MEMORY = 20  # Number of chunks to consider for averaging noise floor
THRESHOLD_FACTOR = 1.01  # Multiplier to set threshold above noise floor

# Initialize pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Noise floor estimation setup
noise_levels = []

try:
    while True:
        # Read audio chunk
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        
        # Calculate RMS of the chunk
        rms = np.sqrt(np.mean(data**2))
        
        # Add RMS to noise levels and maintain its length
        noise_levels.append(rms)
        if len(noise_levels) > NOISE_MEMORY:
            noise_levels.pop(0)
        
        # Estimate noise floor
        noise_floor = np.mean(noise_levels)
        threshold = noise_floor * THRESHOLD_FACTOR
        
        # Check if current RMS exceeds the dynamic threshold
        if rms > threshold:
            print("Meaningful audio detected!")
            p.terminate()
        
        # Print for debugging
        print(f"Noise Floor: {noise_floor:.2f}, Current RMS: {rms:.2f}, Threshold: {threshold:.2f}")

except KeyboardInterrupt:
    # Stop the stream and close
    stream.stop_stream()
    stream.close()
    p.terminate()
