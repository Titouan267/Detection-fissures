# 🔍 Détection de Fissures sur Parties Métalliques d’Avion

Ce projet montre comment détecter automatiquement des fissures sur des pièces métalliques d’un avion à partir d’une image.  
Nous utilisons un modèle hébergé sur **Roboflow**, qui renvoie les coordonnées des fissures détectées.  
Ensuite, nous dessinons automatiquement des rectangles rouges autour de ces fissures.

---

## 🚀 Fonctionnalités

- Envoi d'une image à une API Roboflow  
- Récupération des prédictions (coordonnées)  
- Affichage du JSON reçu  
- Visualisation automatique : boîtes rouges autour des fissures  
- Sauvegarde d’une image annotée `output.jpg`

---

## 🗂️ Structure du Projet

| Fichier        | Description |
|----------------|-------------|
| `README.md`    | Documentation du projet |
| `main.py`      | Script principal : envoie l’image, récupère les fissures, trace les boîtes |
| `utils.py`     | Outils pour dessiner les rectangles rouges |

---

## 📦 Installation
