from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent

MODEL_DIR = BASE_DIR / "models"
SVM_PATH = MODEL_DIR / "SVM_linear.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"

UPLOAD_DIR = BASE_DIR / "static" / "uploads"

AZURE_PREDICTION_KEY = os.getenv("AZURE_PREDICTION_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")

PROJECT_ID = "fbdee0e8-0a8f-4269-91ba-942e968805d0"

URLS = {
    "lokasi": f"{AZURE_ENDPOINT}/customvision/v3.0/Prediction/{PROJECT_ID}/classify/iterations/Iteration3/image",
    "warna": f"{AZURE_ENDPOINT}/customvision/v3.0/Prediction/{PROJECT_ID}/classify/iterations/Iteration7/image",
    "tekstur": f"{AZURE_ENDPOINT}/customvision/v3.0/Prediction/{PROJECT_ID}/classify/iterations/Iteration6/image",
    "luka": f"{AZURE_ENDPOINT}/customvision/v3.0/Prediction/{PROJECT_ID}/classify/iterations/Iteration4/image"
}

WARNA_KAT  = ['hitam', 'kuning', 'merah']
TEKSTUR_KAT = ['halus', 'kasar']
LOKASI_KAT  = ['gusi', 'kuku', 'lidah']
CLASS_LABELS = ['Foot_rot', 'necrotic_stomatitis', 'pmk', 'sehat']

# English display labels for UI
DISPLAY_LABELS = {
    'pmk': 'Foot and Mouth Disease (FMD)',
    'Foot_rot': 'Foot Rot',
    'necrotic_stomatitis': 'Necrotic Stomatitis',
    'lsd': 'Lumpy Skin Disease (LSD)',
    'sehat': 'Healthy'
}

FEATURE_DISPLAY = {
    'warna': {'hitam': 'Black', 'kuning': 'Yellow', 'merah': 'Red'},
    'tekstur': {'halus': 'Smooth', 'kasar': 'Rough'},
    'lokasi': {'gusi': 'Gums', 'kuku': 'Hoof', 'lidah': 'Tongue', 'badan': 'Body / Skin'},
    'luka': {'luka': 'Yes (Wound present)', 'tidak': 'No (Healthy skin)'}
}

PENANGANAN_DICT = {
    'pmk': [
        "Isolate the infected cattle to prevent further spread.",
        "Administer antibiotics to prevent secondary infections and analgesics to reduce pain.",
        "FMD vaccination is the primary prevention step, especially in endemic areas."
    ],
    'Foot_rot': [
        "Clean the wound and apply topical antibiotics to inhibit bacterial growth.",
        "Administer systemic antibiotics in cases of more severe infection.",
        "Improve barn sanitation, especially keeping the floor dry and clean."
    ],
    'necrotic_stomatitis': [
        "Administer systemic antibiotics to inhibit bacterial growth.",
        "Wound care with oral antiseptics to speed up healing.",
        "Improve sanitation of feed and drinking water to prevent re-infection."
    ],
    'lsd': [
        "Isolate infected animals immediately.",
        "Maintain strict vector control (insects/biting flies).",
        "Administer antibiotics for secondary infections and wound care.",
        "Vaccination is the most effective way to control the spread."
    ],
    'sehat': ["No special handling needed."]
}

# Integrated Disease Knowledge Database (Causes & Background)
CAUSES_DICT = {
    'pmk': {
        'cause': "Aphthovirus (Picornaviridae family)",
        'transmission': "Highly contagious via direct contact, contaminated equipment, feed, or airborne transmission.",
        'pathogen': "Virus"
    },
    'Foot_rot': {
        'cause': "Fusobacterium necrophorum and Prevotella melaninogenicus",
        'transmission': "Bacteria entering through injured or softened skin between hooves (muddy/wet conditions).",
        'pathogen': "Bacteria"
    },
    'necrotic_stomatitis': {
        'cause': "Multifactorial (often Fusobacterium necrophorum or Vesicular Stomatitis virus)",
        'transmission': "Secondary bacterial infection following oral trauma or viral precursors.",
        'pathogen': "Bacteria/Virus Mixed"
    },
    'lsd': {
        'cause': "Lumpy Skin Disease Virus (Capripoxvirus)",
        'transmission': "Mechanical transmission by biting insects (mosquitoes, flies, ticks).",
        'pathogen': "Virus"
    },
    'sehat': {
        'cause': "None",
        'transmission': "N/A",
        'pathogen': "None"
    }
}