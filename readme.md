# 🌸 Raspberry Flower Detector

Un projet de détection de fleurs utilisant TensorFlow Lite, optimisé pour fonctionner sur Raspberry Pi avec Debian 11.

## 📋 Description

Ce projet permet de détecter et classifier 10 types de fleurs différentes à partir d'une image en utilisant un modèle de machine learning léger (TensorFlow Lite). Il a été spécialement conçu pour être déployé sur des dispositifs à ressources limitées comme la Raspberry Pi.

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

## 🔧 Prérequis

### Matériel
- Raspberry Pi 3 ou 4 (recommandé)
- Carte microSD (16GB minimum)
- Connexion Internet pour l'installation

### Logiciels
- **OS** : Raspberry Pi OS (Debian 11) ou Debian 11
- **Python** : Version 3.7 ou supérieure
- **Git** pour cloner le projet

## 🚀 Installation

### 1. Préparation du système

Mettez à jour votre système et installez les outils nécessaires :

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3-pip python3-venv python3-dev -y
```

### 2. Clonage du projet

```bash
git clone https://github.com/DaSilvaThomas/raspberry-flower.git
cd raspberry-flower
```

### 3. Configuration de l'environnement virtuel

```bash
# Création de l'environnement virtuel
python -m venv env

# Activation de l'environnement
source env/bin/activate

# Mise à jour de pip
pip install --upgrade pip
```

### 4. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 5. Installation de TensorFlow Lite Runtime

Pour Raspberry Pi, installez la version spécifique de TensorFlow Lite :

**Pour Raspberry Pi 3/4 (ARM 32-bit) :**
```bash
pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
```

**Pour Raspberry Pi 4 (ARM 64-bit) :**
```bash
pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_aarch64.whl
```

> **Note** : Adaptez la version Python (cp37, cp38, cp39) selon votre installation.

## 🖼️ Utilisation

### Préparation de l'image

1. Placez votre image dans le dossier `img/`
2. Modifiez le chemin dans `detect_flower.py` si nécessaire :

```python
image_path = "img/votre_image.jpg"
```

**Formats supportés :** JPG, PNG  
**Résolution recommandée :** 150x150 pixels minimum

### Exécution du script

```bash
# Lancez la détection
python detect_flower.py
```

### Exemple de sortie

```bash
🌸 Analyse de l'image : img/fleure.jpg
🔍 Chargement du modèle...
✅ Détection terminée !

Résultat : viola (confiance: 92.3%)
```

## 🌺 Classes de fleurs reconnues

Le modèle peut identifier les 10 types de fleurs suivants :

| ID | Nom scientifique | Nom commun |
|----|------------------|------------|
| 0  | Phlox | Phlox |
| 1  | Rosa | Rose |
| 2  | Calendula | Souci |
| 3  | Iris | Iris |
| 4  | Leucanthemum maximum | Marguerite Shasta |
| 5  | Campanula | Campanule |
| 6  | Viola | Pensée/Violette |
| 7  | Rudbeckia laciniata | Rudbeckie |
| 8  | Paeonia | Pivoine |
| 9  | Aquilegia | Ancolie |

## ⚙️ Configuration

### Paramètres modifiables dans `detect_flower.py`

```python
# Chemin vers l'image à analyser
image_path = "img/fleure.jpg"

# Seuil de confiance minimum (0.0 à 1.0)
confidence_threshold = 0.5

# Taille d'entrée du modèle
input_size = (224, 224)
```

## 🐛 Dépannage

### Problèmes courants

**Erreur d'importation TensorFlow Lite :**
```bash
ModuleNotFoundError: No module named 'tflite_runtime'
```
**Solution :** Vérifiez que vous avez installé la bonne version de `tflite_runtime` pour votre architecture.

**Erreur de mémoire :**
```bash
ResourceExhaustedError: OOM
```
**Solution :** Réduisez la taille de l'image ou augmentez le swap de la Raspberry Pi.

**Image non trouvée :**
```bash
FileNotFoundError: [Errno 2] No such file or directory
```
**Solution :** Vérifiez le chemin vers votre image dans `detect_flower.py`.

### Performance

Pour améliorer les performances :
- Utilisez des images de taille raisonnable (224x224 à 512x512)
- Fermez les applications non nécessaires
- Augmentez la mémoire GPU si disponible :
  ```bash
  sudo raspi-config
  # Advanced Options → Memory Split → 128
  ```

## 📊 Benchmarks

Temps d'inférence moyens sur différents modèles de Raspberry Pi :

| Modèle | RAM | Temps moyen | FPS max |
|--------|-----|-------------|---------|
| Pi 3B+ | 1GB | ~2.5s | 0.4 |
| Pi 4 4GB | 4GB | ~1.8s | 0.6 |
| Pi 4 8GB | 8GB | ~1.5s | 0.7 |

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

- TensorFlow Lite pour le framework de ML léger
- La communauté Raspberry Pi pour les ressources et guides
- Les contributeurs du dataset de fleurs utilisé pour l'entraînement

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Consultez la documentation de TensorFlow Lite
- Visitez les forums Raspberry Pi

---

**Version :** 1.0.0  
**Dernière mise à jour :** Mai 2025