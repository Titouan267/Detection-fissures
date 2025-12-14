# ✈️ Aircraft Fuselage Crack Detection  
### Project Portfolio – Team X

---

## 👥 Team Information

**Team Number:** Team X  

**Team Members:**
- **Tom Nicolaï**
- **Titouan Lepesqueur**
- **Paul Fortune Corroy**

---

## 🧠 Project Title

**Automatic Detection of Cracks on Aircraft Fuselages using Computer Vision**

---

## 📌 Project Overview

This project focuses on the development of an **artificial intelligence system capable of detecting structural cracks on aircraft fuselages from images**.

The system allows a user to upload an image, which is then analysed by a trained **computer vision model**.  
If a crack is detected, it is automatically highlighted using a **red bounding box**.

The objective of this project is to demonstrate how **AI-based image analysis** can support aircraft inspection and maintenance processes by:

- improving reliability  
- reducing inspection time  
- enhancing overall aviation safety  

---

## 📑 Table of Contents

1. Project Objectives  
2. System Architecture  
3. Process Evidence  
4. Project Methodology  
5. Project Artefacts  
6. Results and Performance  
7. Work Distribution  
8. Project Timeline  
9. Conclusion  

---

## 🎯 Project Objectives

The main objectives of this project are:

- Design a computer vision solution for detecting cracks on aircraft fuselages  
- Train an AI model using a large annotated image dataset  
- Deploy the trained model using an API-based approach  
- Develop a Python program that communicates with the AI model  
- Visualise detected cracks using red bounding boxes  

---

## 🏗️ System Architecture

The system follows a simple and efficient pipeline:

1. The user provides an image of an aircraft fuselage  
2. The image is sent to a **Roboflow-hosted AI model** using an API  
3. The model analyses the image and detects cracks  
4. Detection results are returned in **JSON format**  
5. The Python script processes the results  
6. Red bounding boxes are drawn on detected cracks  
7. The final annotated image is displayed to the user  

---

## 🧾 Process Evidence

This section documents the organisation, planning, and execution of the project.

### 📅 Meeting Minutes  
📁 `/process_evidence/meeting_minutes/`

- **Week 1 – Brainstorming & Topic Selection**  
  Identification of project ideas and selection of fuselage crack detection as the final topic.

- **Week 2 – Research & Tool Selection**  
  Research on computer vision solutions and selection of **Roboflow** for model training and deployment.

- **Week 3 – Dataset & Model Training**  
  Collection of nearly 1000 images and training of the model using more than 800 annotated samples.

- **Week 4 – Integration & Debugging**  
  API integration, Python implementation, debugging, and validation of the final pipeline.

---

## 🔁 Project Methodology  
📁 `/process_evidence/methodology/`

The project follows an iterative development approach inspired by **Agile methodology**:

- Ideation and feasibility analysis  
- Technical research and tool selection  
- Dataset collection and annotation  
- Model training and evaluation  
- API integration and software development  
- Testing, validation, and documentation  

---

## 🧰 Project Artefacts

### 💻 Source Code  
📁 `/artefacts/source_code/`

The Python source code implements the full inference pipeline:
- image loading  
- API communication with Roboflow  
- processing of detection results  
- visualisation of cracks using red bounding boxes  

---

### 🗃️ Dataset  
📁 `/artefacts/datasets/`

The dataset contains close to **1000 images** of aircraft fuselages, including cracked and non-cracked surfaces.

- Over **800 images** were used for training  
- Images were manually annotated using bounding boxes  
- Annotation focuses on precise crack localisation  

---

### 📊 Results and Performance  
📁 `/artefacts/results/`

The trained model demonstrates **strong detection capabilities** on test images.

Evaluation metrics include:
- Precision  
- Recall  
- Mean Average Precision (mAP)  

The model performs best on:
- high-quality images  
- good lighting conditions  
- clear surface visibility  

---

## 👷 Work Distribution

| Team Member | Contribution |
|------------|-------------|
| **Tom Nicolaï** | Model training, API integration, Python development (45%) |
| **Titouan Lepesqueur** | Dataset collection, annotation, research & documentation (30%) |
| **Paul Fortune Corroy** | System design, testing, results analysis & documentation (25%) |

---

## ⏱️ Project Timeline

- **Week 1:** Brainstorming, project definition, initial research  
- **Week 2:** Dataset collection and technical research  
- **Week 3:** Image annotation and AI model training (~5 hours)  
- **Week 4:** API integration, debugging, final validation & portfolio preparation  

---

## ✅ Conclusion

This project successfully demonstrates the feasibility of using **computer vision and machine learning** to support aircraft fuselage inspection.

By combining:
- a **Roboflow-trained AI model**  
- a **Python-based inference pipeline**  

the team developed a functional system capable of **detecting and highlighting cracks on aircraft fuselage images**.

Beyond technical implementation, the project highlights:
- solid engineering practices  
- effective teamwork  
- structured project management  

over a four-week development period.

---

✈️ **End of Project Portfolio**

