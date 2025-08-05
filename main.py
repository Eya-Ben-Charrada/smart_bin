
import time
import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image
from picamera2 import Picamera2
import cv2

# Trash class labels (in your model's order)
labels = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

# Load TFLite model
interpreter = tflite.Interpreter(model_path="/home/eya/Downloads/garbage_classifier_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Initialize camera
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (224, 224)})
picam2.configure(config)
picam2.start()
time.sleep(2)  # Camera warm-up

try:
    while True:
        # Capture image
        frame = picam2.capture_array()

        # Convert from 4 channels to 3 (drop alpha)
        image_rgb = frame[:, :, :3]

        # Convert to PIL Image and preprocess
        img = Image.fromarray(image_rgb).resize((224, 224))
        input_data = np.expand_dims(img, axis=0).astype(np.float32) / 255.0

        # Run inference
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        # Get prediction
        predicted_index = np.argmax(output_data)
        predicted_label = labels[predicted_index]
        confidence = output_data[0][predicted_index]

        # Draw label on frame
        display_text = f"{predicted_label} ({confidence*100:.1f}%)"
        cv2.putText(frame, display_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        # Show frame
        cv2.imshow("Trash Classifier", frame)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    picam2.close()
    cv2.destroyAllWindows()


