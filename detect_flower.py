import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

# Paramètres
img_height, img_width = 150, 150
image_path = "img/fleure.jpg"

# Labels
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

# Charger le modèle TFLite
interpreter = tflite.Interpreter(model_path="models/flower_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Charger et préparer l'image
img = Image.open(image_path).convert("RGB").resize((img_width, img_height))
input_data = np.expand_dims(np.array(img, dtype=np.float32) / 255.0, axis=0)

# Faire une prédiction
interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])

# Identifier la classe prédite
predicted_index = np.argmax(output_data[0])
predicted_label = class_labels[predicted_index]

print(f"🌸 Fleur détectée : {predicted_label}")
