import whisper
import os

os.environ["PATH"] += os.pathsep + r"C:\Users\Lenovo\OneDrive\Desktop\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"

model = whisper.load_model("base")

result = model.transcribe("melody.mp3")

print(result["text"])
