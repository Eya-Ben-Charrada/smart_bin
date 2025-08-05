# 🗑️ Trash Classification on Raspberry Pi

This project uses a Raspberry Pi equipped with a PiCamera2 to classify trash objects in real-time. It displays the detected trash label directly on the screen for each frame captured by the camera.

📌 Project Description
This is a real-time image classification project that detects the type of trash from the camera feed. Once the camera captures a frame, the model predicts the class of the object (such as "cardboard", "glass", "metal", etc.), and displays the label on the screen.

⚠️ This project does not perform object detection (no bounding boxes around multiple objects). It classifies the whole image/frame as a single trash category.

🧠 Model & Dataset
Model used: TensorFlow Lite (converted from a pre-trained TensorFlow model).

Dataset: Garbage Classification Dataset from Kaggle

Number of classes: 6 (cardboard, glass, metal, paper, plastic, trash)

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## ▶️ Usage
1- Clone this repository:
```bash
git clone https://github.com/Eya-Ben-Charrada/smart_bin.git
cd trash-classification-pi
```
2- Make sure your camera is connected and enabled.

3- Run the main script:

```bash
python main.py

```
You will see the live camera feed, and the predicted label of the detected trash type will be shown on the screen.
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




