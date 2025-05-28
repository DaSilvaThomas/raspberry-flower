import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
import picamera
import time
import os

# === Paramètres ===
img_height, img_width = 150, 150
image_filename = "captured_flower.jpg"
image_path = os.path.join("img", image_filename)
model_path = "models/flower_model.tflite"
confidence_threshold = 0.5

# === Labels ===
class_labels = {
    0: "phlox",
    1: "rose",
    2: "calendula",
    3: "iris",
    4: "leucanthemum maximum (Shasta daisy)",
    5: "campanula (bellflower)",
    6: "viola",
    7: "rudbeckia laciniata (Goldquelle)",
    8: "peony",
    9: "aquilegia"
}

# === Étape 1 : Prendre une photo avec la caméra ===
print("📷 Préparation de la caméra...")
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(2)  # Laisse le temps à la caméra de s'ajuster
    print(f"📸 Capture de l'image : {image_path}")
    camera.capture(image_path)
    camera.stop_preview()

# === Étape 2 : Charger le modèle ===
print("🔍 Chargement du modèle...")
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# === Étape 3 : Préparer l'image ===
img = Image.open(image_path).convert("RGB").resize((img_width, img_height))
input_data = np.expand_dims(np.array(img, dtype=np.float32) / 255.0, axis=0)

# === Étape 4 : Inference ===
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])

# === Étape 5 : Résultat ===
predicted_index = np.argmax(output_data[0])
confidence = float(output_data[0][predicted_index])
predicted_label = class_labels[predicted_index]

print("✅ Détection terminée !")
if confidence >= confidence_threshold:
    print(f"🌸 Fleur détectée : {predicted_label} (confiance : {confidence * 100:.1f}%)")
else:
    print(f"⚠️ Confiance trop faible ({confidence * 100:.1f}%). Aucune fleur détectée avec certitude.")
