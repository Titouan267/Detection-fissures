# ✈️ Aircraft Fuselage Crack Detection  
### Computer Vision Project Portfolio 

---

## 👥 Team Information  

**Team members:**  
- Tom Nicolaï  
- Titouan Lepesqueur  
- Paul Fortune Corroy  

---

## 🧠 Project Title

**Automatic Detection of Cracks on Aircraft Fuselages Using Computer Vision**

---

## 📌 Project Overview

This project focuses on the development of an artificial intelligence system capable of detecting structural cracks on aircraft fuselages from images.

The system allows a user to provide an image of an aircraft fuselage, which is then analysed by a trained computer vision model.  
When a crack is detected, its location is highlighted using a **red bounding box**.

The main objective is to demonstrate how AI-based image analysis can support aircraft inspection and maintenance by improving reliability, reducing inspection time, and enhancing overall safety ✈️.

---

## 📑 Contents

1. Project Objectives  
2. System Architecture  
3. Project Organisation and Process Evidence  
4. Development Methodology  
5. Project Deliverables  
6. Results and Performance  
7. Work Distribution  
8. Project Schedule  
9. Conclusion  

---

## 🎯 Project Objectives

The objectives of this project are:

- Design a computer vision-based solution for aircraft fuselage crack detection  
- Train an AI model using a labelled image dataset  
- Deploy the trained model through an API-based approach  
- Develop a Python program for inference and result processing  
- Visualise detected cracks using bounding boxes  

---

## 🏗️ System Architecture

The system follows a clear and efficient pipeline:

1. The user provides an image of an aircraft fuselage  
2. The image is sent to an AI model hosted on Roboflow  
3. The model analyses the image and detects potential cracks  
4. Detection results are returned in JSON format  
5. The Python program processes the results  
6. Red bounding boxes are drawn around detected cracks  
7. The final annotated image is displayed to the user  

---

## 🧾 Project Organisation and Process Evidence

This section summarises the planning and execution of the project.

**Meeting Records**  
Directory: `/process_evidence/meeting_minutes/`

- **Week 1:** Brainstorming, topic selection, and project definition  
- **Week 2:** Research on computer vision techniques and dataset exploration 🔍  
- **Week 3:** Dataset annotation and AI model training  
- **Week 4:** API integration, debugging, and validation of the system  

---

## 🔁 Development Methodology

Directory: `/process_evidence/methodology/`

An iterative development approach inspired by Agile practices was adopted:

- Project scoping and feasibility analysis  
- Technical research and dataset preparation  
- Image annotation and data exploration  
- AI model training and evaluation  
- Software integration and testing  
- Documentation and final validation  

---

## 🧰 Project Deliverables

### 💻 Source Code  
Directory: `/artefacts/source_code/`

The source code implements the complete inference pipeline, including image handling, API communication, processing of detection results, and visualisation of cracks.

---

### 🗃️ Dataset  
Directory: `/artefacts/datasets/`

The dataset contains approximately 1000 images of aircraft fuselages, including cracked and non-cracked surfaces.  
More than 800 annotated images were used for training the AI model.

---

### 📊 Results and Performance  
Directory: `/artefacts/results/`

The trained model demonstrates good crack detection performance on test images.  
Evaluation was conducted using standard object detection metrics such as precision, recall, and mean average precision (mAP).  
The model performs best on high-quality images with adequate lighting conditions.

---

## 👷 Work Distribution 🙂

| Team member | Main responsibilities | Contribution |
|------------|----------------------|--------------|
| **Tom Nicolaï** | Project coordination, model evaluation, testing, documentation | ~33% |
| **Titouan Lepesqueur** | Python development, API integration, dataset research and analysis, annotation | ~34% |
| **Paul Fortune Corroy** | System design, validation, result analysis, documentation | ~33% |

---

## ⏱️ Project Schedule

- **Week 1:** Project definition, brainstorming, initial research  
- **Week 2:** Dataset collection and technical research  
- **Week 3:** Image annotation and AI model training  
- **Week 4:** API integration, debugging, testing, and final portfolio preparation  

---

## ✅ Conclusion

This project demonstrates the feasibility of using computer vision and machine learning techniques to support aircraft fuselage inspection.

By combining a trained AI model with a Python-based inference pipeline, the team developed a functional system capable of detecting and highlighting cracks on aircraft fuselage images.

Overall, the project highlights both technical learning outcomes and effective teamwork over a four-week development period 👍.

---

