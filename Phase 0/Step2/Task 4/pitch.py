import librosa
import numpy as np

audio_path = "Recording.wav"

y, sr = librosa.load(audio_path)

f0 = librosa.yin(y, fmin=80, fmax=400)
pitch = np.nanmean(f0)

print("Pitch (Hz):", pitch)
