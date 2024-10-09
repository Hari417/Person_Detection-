# Person-detection-YOLO-
This repository contains a project focused on training a YOLOv8n (You Only Look Once, version 8) model specifically to detect persons in images.

YOLOv8n: Detecting Persons in the COCO Dataset
This repository contains a project focused on training a YOLOv8n (You Only Look Once, version 8) model specifically to detect persons in images. The model is fine-tuned using a subset of the COCO dataset (Common Objects in Context) to improve its accuracy and performance for the person class, making it lightweight and suitable for real-time applications.

Features
Model Architecture: YOLOv8n (Nano) - an efficient and fast object detection model.
Dataset: Custom fine-tuning of the COCO dataset, limited to the 'person' class.
Training: Detailed training pipeline with custom hyperparameters optimized for detecting persons.
Inference: Fast real-time person detection on both images and video streams.
Model Size: The YOLOv8n version is chosen for its balance between size, speed, and accuracy, suitable for deployment on edge devices.
Requirements
Python 3.8+
PyTorch 2.x
ultralytics/yolov8 package
COCO dataset (download instructions included)
