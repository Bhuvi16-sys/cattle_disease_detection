import numpy as np
import joblib
import requests
from app.config import (
    SVM_PATH, SCALER_PATH, DISPLAY_LABELS, FEATURE_DISPLAY,
    PENANGANAN_DICT, CAUSES_DICT,
    URLS, AZURE_PREDICTION_KEY, AZURE_ENDPOINT,
    WARNA_KAT, TEKSTUR_KAT, LOKASI_KAT, CLASS_LABELS
)

# Load model dan scaler
model = joblib.load(SVM_PATH)
scaler = joblib.load(SCALER_PATH)

# Kategori fitur
warna_kategori = WARNA_KAT
tekstur_kategori = TEKSTUR_KAT
lokasi_kategori = LOKASI_KAT
class_labels = CLASS_LABELS

# Exports for routes
penanganan_dict = PENANGANAN_DICT
causes_dict = CAUSES_DICT
penanganan_dict = PENANGANAN_DICT

# Azure Prediction
headers = {
    'Content-Type': 'application/octet-stream',
    'Prediction-Key': AZURE_PREDICTION_KEY
}

# Fungsi bantu
def one_hot_encode(value, categories):
    one_hot = [0] * len(categories)
    if value in categories:
        one_hot[categories.index(value)] = 1
    return one_hot

def deteksi_fitur(img_bytes):
    # Check if Azure credentials are available
    if not AZURE_PREDICTION_KEY or not AZURE_ENDPOINT:
        return None, "Azure credentials missing. Please use manual mode."

    hasil, confidence = {}, {}
    try:
        for fitur in URLS:
            res = requests.post(URLS[fitur], headers=headers, data=img_bytes, timeout=10)
            res.raise_for_status()
            pred = res.json()["predictions"]
            top = max(pred, key=lambda x: x["probability"])
            hasil[fitur] = top["tagName"].lower().replace("_", "")
            confidence[fitur] = {
                p["tagName"].lower().replace("_", ""): round(p["probability"] * 100, 2)
                for p in pred
            }
        return hasil, confidence
    except Exception as e:
        return None, f"Azure Prediction Error: {str(e)}"

def prediksi_klasifikasi(warna, tekstur, lokasi, luka):
    # Heuristic override for Body / Skin location (not in original SVM model)
    if lokasi == 'badan':
        return 'lsd' if luka == 'ya' else 'sehat'

    warna_oh = one_hot_encode(warna, warna_kategori)
    tekstur_oh = one_hot_encode(tekstur, tekstur_kategori)
    lokasi_oh = one_hot_encode(lokasi, lokasi_kategori)
    luka_bin = 1 if luka == 'ya' else 0

    input_data = np.array([[luka_bin] + warna_oh + tekstur_oh + lokasi_oh])
    input_scaled = scaler.transform(input_data)
    
    # LinearSVC doesn't have predict_proba by default. Using decision_function scores.
    scores = model.decision_function(input_scaled)[0]
    pred_idx = np.argmax(scores)
    pred_label = class_labels[pred_idx]

    if luka_bin == 1 and pred_label == 'sehat':
        # Find the next best prediction that isn't 'sehat'
        sorted_indices = np.argsort(scores)[::-1]
        for i in sorted_indices:
            if class_labels[i] != 'sehat':
                pred_label = class_labels[i]
                break
    if luka_bin == 0 and pred_label != 'sehat':
        pred_label = 'sehat'

    if pred_label == 'necrotic_stomatitis' and (warna == 'merah' or lokasi == 'kuku'):
        sorted_indices = np.argsort(scores)[::-1]
        for i in sorted_indices:
            if class_labels[i] != 'necrotic_stomatitis':
                pred_label = class_labels[i]
                break
    return pred_label
