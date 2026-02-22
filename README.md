# 🐄 Cow Disease Detection & Prediction System

A web-based machine learning application for detecting and predicting cattle diseases from wound images.  
The system integrates **computer vision**, **machine learning**, and a **Flask web application** to assist early disease identification in cattle.

---

## 📌 Project Overview

This project aims to help identify cattle diseases by analyzing wound images and extracted visual features.  
The system works in two main stages:

1. **Feature Detection (Computer Vision)**  
   - Color  
   - Texture  
   - Wound location  
   - Presence of wound  

2. **Disease Classification (Machine Learning)**  
   - Support Vector Machine (SVM) classifier  
   - StandardScaler for feature normalization  
   - Rule-based post-processing for logical consistency  

---

## 🧠 Machine Learning Approach

- **Feature Extraction**:  
  Azure Custom Vision (image-based classification for visual features)

- **Classifier**:  
  Support Vector Machine (SVM)

- **Target Classes**:
  - PMK (Foot-and-Mouth Disease)
  - Foot Rot
  - Necrotic Stomatitis
  - Healthy

- **Post-processing Rules**:
  - Logical correction based on wound presence
  - Confidence-based label adjustment

---

## 🏗️ Project Structure

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py          # Configuration & constants
│   ├── ml_service.py      # ML logic & prediction pipeline
│   └── routes.py          # Flask routes
│
├── models/
│   ├── SVM_linear.pkl
│   └── scaler.pkl
│
├── notebook/
│   └── Diagnosis_Penyakit_Sapi.ipynb
│
├── static/
│   ├── uploads/           # Runtime image uploads (ignored in git)
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .gitignore
├── app.py                 # Flask entry point
└── README.md
```
---

## 🏗️ INTERFACE
<img width="2857" height="1351" alt="image" src="https://github.com/user-attachments/assets/b5ce05f4-f25b-49f4-a21c-cacc092d0b34" />
<img width="2879" height="1527" alt="image" src="https://github.com/user-attachments/assets/aa0ce589-0d3e-479f-b28e-75ecddec3004" />
<img width="2847" height="1351" alt="image" src="https://github.com/user-attachments/assets/39a7ca67-e43b-48a4-a5ea-9687db154805" />



