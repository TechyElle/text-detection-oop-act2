<div align="center">

# 👁️ OCR Text Detection

### *See the text. Detect the words. Read the image.*

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract-OCR-DD0031?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)

> A Python project that detects and highlights text from images —  
> rebuilt from Activity 1 with clean coding standards and proper git practices.

</div>

---

## 🌟 What It Does

| Feature | Description |
|--------|-------------|
| 📝 **Word Detection** | Highlights full words with labeled boxes |
| 🔢 **Digit-Only OCR** | Filters and detects only numerical characters |
| 🖨️ **Image to String** | Extracts all text from an image as a plain string |

---

## 📁 Project Structure

```
text-detection-oop-act2/
│
├── 📄 text_simple.py          # Minimal character detection with bounding boxes
├── 📄 text_more_examples.py   # Extended OCR examples (words, digits)
├── 🖼️  1.png                   # Sample input image
└── 📘 README.md
```

---

## ⚙️ Setup & Installation

### 1. Install Tesseract OCR
Download and install from the official site:  
🔗 https://tesseract-ocr.github.io/tessdoc/Home.html

Default path used in scripts:
```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

### 2. Install Python Dependencies
```bash
pip install opencv-python pytesseract numpy pillow
```

---

## 🚀 Run the Project

```bash
# Run minimal character detection
python text_simple.py

# Run extended examples
python text_more_examples.py
```

> 💡 To switch between modes in `text_more_examples.py`, simply uncomment the block you want to test.

---

## ✅ Coding Standards Applied

This project was refactored from Activity 1 to follow proper coding conventions:

```
✔  snake_case        →  file names, variables, functions
✔  kebab-case        →  repository name
✔  Descriptive names →  input_image, char_label, word_height, digit_label
✔  Comments          →  only before blocks, functions, or non-obvious lines
```

---

## 🔁 Git Commit History

| Commit | File | Description |
|--------|------|-------------|
| `01` | `text_simple.py` | Basic image loading and display setup |
| `02` | `text_simple.py` | Add character detection with bounding boxes |
| `03` | `text_more_examples.py` | Add word detection and image to string examples |
| `04` | `text_more_examples.py` | Add digit only detection using tesseract oem psm config |
| `05` | `text_simple.py`, `text_more_examples.py`, `README.md` | Apply snake case naming descriptive variables and comments |

---

## 📌 References

Based on the tutorial by **Murtaza Hassan**:  
🔗 [OpenCV-Python-Tutorials-and-Projects / TextDetection](https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects/tree/master/Intermediate/TextDetection)

---

<div align="center">

⚠️ *For educational purposes only. Please do not plagiarize.*

</div>
