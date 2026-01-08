from deepface import DeepFace

result = DeepFace.analyze(
    img_path="face.jpeg",
    actions=["emotion"],
    enforce_detection=False
)

emotion = result[0]["dominant_emotion"]

print(f"The subject appears to be feeling: {emotion}.")
