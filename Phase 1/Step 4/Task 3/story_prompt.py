import random
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Image path
image_path = "room.jpg"

# Run object detection
results = model(image_path)

# Store detected objects
detected_objects = []

for result in results:
    for cls in result.boxes.cls:
        detected_objects.append(model.names[int(cls)])

# Remove duplicates
detected_objects = list(set(detected_objects))

# Select 3–5 objects
if len(detected_objects) >= 3:
    selected_objects = random.sample(
        detected_objects,
        min(len(detected_objects), random.randint(3, 5))
    )
else:
    selected_objects = detected_objects

# Print story prompt
if selected_objects:
    print("Detected:", ", ".join(selected_objects))
    print("Write a story about them.")
else:
    print("No objects detected.")
