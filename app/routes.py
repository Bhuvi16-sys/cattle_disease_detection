import os
from app.config import UPLOAD_DIR, DISPLAY_LABELS, FEATURE_DISPLAY
from app.ml_service import deteksi_fitur, prediksi_klasifikasi, penanganan_dict, causes_dict
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import secure_filename

bp = Blueprint("routes", __name__)

# Main Routing
@bp.route("/", methods=["GET", "POST"])
def index():
    result = {}
    image_url = None
    error_msg = None

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_DIR, filename)
            file.save(save_path)
            image_url = url_for('static', filename=f'uploads/{filename}')

            with open(save_path, 'rb') as f:
                img_bytes = f.read()

            # Try automatic detection
            fitur, confidence = deteksi_fitur(img_bytes)

            mode_manual = False
            warna = request.form.get("warna")
            tekstur = request.form.get("tekstur")
            lokasi = request.form.get("lokasi")
            luka = request.form.get("luka")

            # Fallback to manual if Azure fails
            if fitur is None:
                mode_manual = True
                if warna and tekstur and lokasi and luka:
                    fitur = {
                        'warna': warna,
                        'tekstur': tekstur,
                        'lokasi': lokasi,
                        'luka': 'luka' if luka == 'ya' else 'tidak'
                    }
                    confidence = {
                        'warna': {warna: 100},
                        'tekstur': {tekstur: 100},
                        'lokasi': {lokasi: 100},
                        'luka': {'luka': 100 if luka == 'ya' else 0, 'tidak': 100 if luka == 'tidak' else 0}
                    }
                else:
                    error_msg = str(confidence) # Error message from ml_service

            if fitur:
                warna_val = fitur['warna']
                tekstur_val = fitur['tekstur']
                lokasi_val = fitur['lokasi']
                luka_val = 'ya' if fitur.get('luka') == 'luka' else 'tidak'

                raw_diagnosis = prediksi_klasifikasi(warna_val, tekstur_val, lokasi_val, luka_val)
                diagnosis_en = DISPLAY_LABELS.get(raw_diagnosis, raw_diagnosis)
                rekomendasi = penanganan_dict.get(raw_diagnosis, ["Diagnosis unclear."])
                info_penyakit = causes_dict.get(raw_diagnosis, {})

                # Get English names for features
                fitur_en = {
                    'warna': FEATURE_DISPLAY['warna'].get(warna_val, warna_val),
                    'tekstur': FEATURE_DISPLAY['tekstur'].get(tekstur_val, tekstur_val),
                    'lokasi': FEATURE_DISPLAY['lokasi'].get(lokasi_val, lokasi_val),
                    'luka': FEATURE_DISPLAY['luka'].get(fitur.get('luka'), fitur.get('luka'))
                }

                result = {
                    "fitur": fitur,
                    "fitur_en": fitur_en,
                    "confidence": confidence,
                    "diagnosis": diagnosis_en,
                    "rekomendasi": rekomendasi,
                    "info_penyakit": info_penyakit,
                    "luka": luka_val,
                    "manual": mode_manual
                }

    return render_template("index.html", result=result, image_url=image_url, error_msg=error_msg)