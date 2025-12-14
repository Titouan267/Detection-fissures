#!/usr/bin/env python3
"""
main.py
Script principal qui :
- envoie une image à l’API Roboflow
- récupère les prédictions (fissures)
- convertit les coordonnées
- dessine les rectangles rouges sur l’image
"""

import sys
import json
from inference_sdk import InferenceHTTPClient
from utils import draw_boxes

# ------------ CONFIGURATION ------------
API_URL = "https://serverless.roboflow.com"
API_KEY = "0ni1aLOl4URBmjk08gjY"
MODEL_ID = "my-first-project-utgik/1"
# ---------------------------------------

def convert_predictions_to_boxes(predictions):
    """
    Convertit les prédictions Roboflow (x, y, width, height)
    en format : [x1, y1, x2, y2]
    """
    boxes = []
    for pred in predictions:
        x, y = pred["x"], pred["y"]
        w, h = pred["width"], pred["height"]

        x1 = x - w / 2
        y1 = y - h / 2
        x2 = x + w / 2
        y2 = y + h / 2

        boxes.append([x1, y1, x2, y2])

    return boxes

def main():
    if len(sys.argv) < 2:
        print("Usage : python main.py image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = "output.jpg"

    # Initialisation du client Roboflow
    client = InferenceHTTPClient(
        api_url=API_URL,
        api_key=API_KEY
    )

    # Envoi de l'image
    print("Envoi de l’image au modèle...")
    result = client.infer(image_path, model_id=MODEL_ID)

    print("\n--- Réponse JSON ---")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Conversion des prédictions en boîtes
    predictions = result.get("predictions", [])
    boxes = convert_predictions_to_boxes(predictions)

    # Dessin des boîtes
    print("\nDessin des boîtes...")
    draw_boxes(image_path, boxes, output_path)

    print(f"\nImage annotée sauvegardée sous : {output_path}")

if __name__ == "__main__":
    main()
