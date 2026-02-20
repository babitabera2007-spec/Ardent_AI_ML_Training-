# 😊 Real-Time Emotion Detection System

> Detect human emotions live from your webcam using a pre-trained deep learning model and OpenCV — no cloud APIs, no DeepFace, runs fully offline.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-TensorFlow-red?logo=keras&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 What It Does

This project uses your webcam to detect faces in real time and predict the **emotion** displayed on each face. It draws a bounding box around every detected face and overlays the predicted emotion label — all at live video speed.

**Detectable emotions:**

| Label | Emotion |
|-------|---------|
| 😡 | Angry |
| 🤢 | Disgust |
| 😨 | Fear |
| 😄 | Happy |
| 😢 | Sad |
| 😲 | Surprise |
| 😐 | Neutral |

---

## 🗂 Project Files

```
emotion-detection/
│
├── emotion_detection.py                    # Main script — run this
├── emotion_model.hdf5                      # Pre-trained CNN emotion model (Keras)
├── haarcascade_frontalface_default.xml     # Haar Cascade face detector (OpenCV)
└── README.md                               # This file
```

### File breakdown

**`emotion_detection.py`** — Core application script. Captures webcam frames, detects faces using the Haar Cascade, preprocesses each face ROI, feeds it into the emotion model, and renders results live.

**`emotion_model.hdf5`** — A pre-trained Convolutional Neural Network (CNN) saved in Keras HDF5 format. Trained to classify grayscale face images (resized to 64×64) into 7 emotion categories.

**`haarcascade_frontalface_default.xml`** — OpenCV's classic Haar Cascade classifier for frontal face detection. Used for fast, lightweight face localization before passing the ROI to the deep learning model.

---

## ⚙️ How It Works

```
Webcam Frame
     │
     ▼
Convert to Grayscale
     │
     ▼
Haar Cascade Face Detection  ──►  No faces → skip frame
     │
     ▼
Crop Face ROI (Region of Interest)
     │
     ▼
Resize to 64×64 px
     │
     ▼
Normalize pixel values (÷ 255.0)
     │
     ▼
Reshape → (1, 64, 64, 1)  [batch, height, width, channels]
     │
     ▼
CNN Emotion Model Prediction
     │
     ▼
argmax → Emotion Label
     │
     ▼
Draw Rectangle + Label on Frame
     │
     ▼
Display in OpenCV Window
```

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.8 or higher
- A working webcam

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
```

### 2. Install dependencies

```bash
pip install opencv-python numpy tensorflow
```

> **Note:** `keras` is bundled inside `tensorflow` (v2.x). You do **not** need to install Keras separately.

### 3. Verify all required files are present

```
emotion_detection.py                   ✅
emotion_model.hdf5                     ✅
haarcascade_frontalface_default.xml    ✅
```

### 4. Run the script

```bash
python emotion_detection.py
```

---

## 🖥 Platform Notes

| OS | Webcam Flag | Notes |
|----|-------------|-------|
| **macOS** | `cv2.CAP_AVFOUNDATION` | Already set in code. Grant camera access in **System Settings → Privacy → Camera** |
| **Windows** | `cv2.CAP_DSHOW` | Replace `CAP_AVFOUNDATION` with `CAP_DSHOW` |
| **Linux** | _(remove flag)_ | Use `cv2.VideoCapture(0)` only |

**To change camera index** (if you have multiple cameras):
```python
cap = cv2.VideoCapture(0)  # 0 = default, 1 = second camera, etc.
```

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| `q` | Quit the application |

---

## 🧠 Model Details

| Property | Value |
|----------|-------|
| Format | Keras HDF5 (`.hdf5`) |
| Input shape | `(1, 64, 64, 1)` — grayscale |
| Normalization | Pixel values divided by `255.0` |
| Output | Softmax probabilities over 7 emotion classes |
| Architecture | Convolutional Neural Network (CNN) |
| Load mode | `compile=False` — inference only |

---

## 🐛 Troubleshooting

**`ModuleNotFoundError: No module named 'cv2'`**
```bash
pip install opencv-python
```

**`ModuleNotFoundError: No module named 'keras'`**
```bash
pip install tensorflow
```

**`Error: Cannot access webcam` / blank screen**
- Make sure no other app is using the camera
- Try changing the camera index: `VideoCapture(0)` → `VideoCapture(1)`
- macOS: grant Terminal/IDE camera permission in System Settings

**`FileNotFoundError` for `.hdf5` or `.xml`**
- Make sure all three files are in the **same directory** as the script
- Run the script from that directory: `cd path/to/project && python emotion_detection.py`

**Low accuracy / wrong emotions detected**
- Ensure good, even lighting on your face
- Face the camera directly — this uses frontal face detection
- Avoid extreme angles or partial occlusion

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `opencv-python` | Webcam capture, face detection, drawing, display |
| `numpy` | Array reshaping and pixel normalization |
| `tensorflow` / `keras` | Loading and running the `.hdf5` emotion model |

---

## 🔮 Future Improvements

- [ ] Show confidence percentage on screen (e.g., `Happy: 94%`)
- [ ] Support detecting multiple faces simultaneously
- [ ] Save snapshots with detected emotion labels
- [ ] Export emotion log to CSV for analysis
- [ ] Add a real-time emotion history graph overlay
- [ ] Train a custom model on the FER-2013 dataset for improved accuracy

---

## 👩‍💻 Author

**Babita Bera**  
B.Sc (Computer Science) · Haldia Institute of Management  
Mentored by **SK Sahil** — AI Developer & Tutor · [@code_scholar_eu](https://www.instagram.com/code_scholar_eu/)

---

## 🙏 Credits

| Resource | Source |
|----------|--------|
| Face detection | OpenCV Haar Cascade (`haarcascade_frontalface_default.xml`) |
| Emotion model | Pre-trained CNN (`emotion_model.hdf5`) |
| CV library | [OpenCV](https://opencv.org/) |
| Deep learning | [TensorFlow / Keras](https://keras.io/) |

---

<p align="center">Built with Python · OpenCV · Keras · TensorFlow</p>
