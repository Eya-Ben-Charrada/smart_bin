# 🗑️ Trash Classification on Raspberry Pi

This project implements **real-time trash type classification** using a **TensorFlow Lite** model and a Raspberry Pi camera (via `picamera2`). It captures images, classifies them into categories like **plastic, metal, paper**, etc., and displays the predicted label on the video stream.

<br/>

## 🚀 Demo

Once the system is running, the camera will open and continuously classify the object in view. The predicted label (e.g., `plastic`) will be shown on the video window.

<br/>

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## ▶️ Usage
run
```bash
python main.py

```

A camera window will open and display the live prediction of the object in front of the camera.

## 🧠 Model
The model used is a TensorFlow Lite image classification model trained to recognize different types of trash.


## 📌 Notes
- This project uses classification, not object detection.

- Only the most probable class label is shown — no bounding boxes.

- Designed for Raspberry Pi with camera setup.



## 📸 Hardware Requirements
- Raspberry Pi 4 or newer

- Pi Camera Module 

- Internet for initial setup

## 🤖 Future Improvements
- Add voice feedback (Text-to-Speech)

- Expand label set

- Improve model accuracy


## 📄 License
MIT License




