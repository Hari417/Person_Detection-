from ultralytics import YOLO
import torch
print(torch.cuda.is_available())

if __name__ == '__main__':
    # Load the YOLOv8n model architecture without pre-trained weights
    model = YOLO(r'G:\runs\detect\yolov8n_person_scratch\weights\last.pt')  # Load the model architecture

    # Train the model from scratch using the provided YAML file
    results = model.train(resume=True)
