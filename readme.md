# 🌸 Détection de fleurs avec Raspberry Pi

Un projet de détection automatique de fleurs utilisant une Raspberry Pi Camera Module V2 et un modèle TensorFlow Lite.

## 🎯 Objectif

Ce projet utilise une Raspberry Pi 3 Model B équipée d'une caméra pour capturer des images de fleurs et les classifier automatiquement grâce à un modèle de machine learning pré-entraîné.

## 🔧 Matériel requis

- **Raspberry Pi 3 Model B**
- **Raspberry Pi Camera Module V2**
- Carte SD (16 GB minimum recommandé)
- Alimentation pour Raspberry Pi

## 📁 Structure du projet

```
raspberry-flower/
├── img/                     # Images à analyser
│   └── fleure.jpg          # Image d'exemple
├── models/                  # Modèles TensorFlow Lite
│   └── flower_model.tflite # Modèle pré-entraîné
├── detect_flower.py        # Script principal de détection
├── requirements.txt        # Dépendances Python
├── README.md              # Documentation du projet
└── .gitignore             # Fichiers à ignorer par Git
```

## 🌺 Fleurs détectables

Le modèle peut identifier les fleurs suivantes :
- Phlox
- Rose
- Calendula
- Iris
- Leucanthemum maximum (Shasta daisy)
- Campanula (bellflower)
- Viola
- Rudbeckia laciniata (Goldquelle)
- Peony
- Aquilegia

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/DaSilvaThomas/raspberry-flower.git
cd raspberry-flower
```

### 2. Activer la caméra
```bash
sudo raspi-config
```
Aller dans `Interfacing Options` → `Camera` → `Enable`

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## 📸 Utilisation

### Lancement du script de détection
```bash
python detect_flower.py
```

### Processus de détection
1. **Capture** : La caméra prend une photo automatiquement
2. **Préparation** : L'image est redimensionnée et normalisée
3. **Inference** : Le modèle TensorFlow Lite analyse l'image
4. **Résultat** : La fleur est identifiée avec un niveau de confiance

### Exemple de sortie
```
📷 Préparation de la caméra...
📸 Capture de l'image : img/captured_flower.jpg
🔍 Chargement du modèle...
✅ Détection terminée !
🌸 Fleur détectée : rose (confiance : 87.3%)
```

## ⚙️ Configuration

### Paramètres modifiables dans `detect_flower.py`
- `img_height, img_width` : Taille de l'image d'entrée (150x150 par défaut)
- `confidence_threshold` : Seuil de confiance minimum (0.5 par défaut)
- `camera.resolution` : Résolution de capture (640x480 par défaut)

### Seuil de confiance
Le script n'affiche un résultat que si la confiance est supérieure à 50%. Vous pouvez ajuster cette valeur selon vos besoins.

## 📦 Dépendances

- `tflite-runtime` : Runtime TensorFlow Lite optimisé
- `numpy` : Calculs numériques
- `Pillow` : Traitement d'images
- `picamera` : Interface caméra Raspberry Pi (pré-installé sur Raspbian)

## 🔍 Fonctionnement technique

1. **Capture d'image** : Utilisation de `picamera` pour capturer une photo
2. **Prétraitement** : Redimensionnement à 150x150 pixels et normalisation (0-1)
3. **Inference** : Utilisation d'un modèle TensorFlow Lite pré-entraîné
4. **Post-traitement** : Extraction de la classe avec la plus haute probabilité

## 🐛 Dépannage

### Erreur de caméra
```bash
# Vérifier si la caméra est détectée
vcgencmd get_camera

# Résultat attendu : supported=1 detected=1
```

### Permissions insuffisantes
```bash
# Ajouter l'utilisateur au groupe video
sudo usermod -a -G video $USER
```

### Modèle non trouvé
Vérifiez que le fichier `flower_model.tflite` est présent dans le dossier `models/`.

## 📝 Notes

- Le modèle est optimisé pour fonctionner sur Raspberry Pi
- Les images capturées sont sauvegardées dans le dossier `img/`
- Le script remplace automatiquement l'image précédente à chaque exécution

## 🎓 Contexte académique

Ce projet a été développé dans le cadre d'un cours sur la vision par ordinateur et l'intelligence artificielle embarquée, démontrant l'utilisation pratique de modèles de machine learning sur des systèmes à ressources limitées.
