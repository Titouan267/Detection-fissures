# Aircraft Fuselage Crack Detection  
## Computer Vision Project Portfolio

---

### Team Information

**Team number:** Team X  

**Team members:**  
- Tom Nicolaï  
- Titouan Lepesqueur  
- Paul Fortune Corroy  

---

### Project Title

**Automatic Detection of Cracks on Aircraft Fuselages Using Computer Vision**

---

### Project Overview

The aim of this project is to develop an artificial intelligence system capable of detecting structural cracks on aircraft fuselages using image analysis.

The system processes an input image of an aircraft fuselage and automatically identifies the presence of cracks. When a crack is detected, its location is highlighted on the image using a red bounding box.

This project illustrates how computer vision techniques can assist aircraft inspection and maintenance by improving inspection accuracy, reducing manual effort, and increasing overall safety.

---

### Contents

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

### Project Objectives

The main objectives of this project are as follows:

- Design a computer vision-based solution for crack detection on aircraft fuselages  
- Train an AI model using a labelled image dataset  
- Deploy the trained model through an API interface  
- Implement a Python-based inference pipeline  
- Visualise detected cracks using bounding boxes  

---

### System Architecture

The system is composed of the following steps:

1. An image of an aircraft fuselage is provided by the user  
2. The image is transmitted to an AI model hosted on Roboflow  
3. The model analyses the image and identifies potential cracks  
4. Detection results are returned in JSON format  
5. The Python application processes the output  
6. Bounding boxes are drawn on detected cracks  
7. The annotated image is displayed to the user  

---

### Project Organisation and Process Evidence

This section summarises the planning and execution of the project.

**Meeting Records**  
Directory: `/process_evidence/meeting_minutes/`

- **Week 1:** Idea generation and selection of fuselage crack detection as the project topic  
- **Week 2:** Research on computer vision approaches and selection of Roboflow as the development platform  
- **Week 3:** Dataset preparation and model training using annotated images  
- **Week 4:** API integration, debugging, and system validation  

---

### Development Methodology

Directory: `/process_evidence/methodology/`

The project followed an iterative development approach inspired by Agile practices:

- Definition of project scope and feasibility  
- Technical research and tool selection  
- Dataset collection and annotation  
- AI model training and evaluation  
- Software integration and testing  
- Final documentation  

---

### Project Deliverables

**Source Code**  
Directory: `/artefacts/source_code/`

The source code implements the complete inference pipeline, including image input handling, API communication, result processing, and visualisation of detected cracks.

**Dataset**  
Directory: `/artefacts/datasets/`

The dataset consists of approximately 1000 images of aircraft fuselages, covering both cracked and non-cracked surfaces. More than 800 annotated images were used for training the model.

**Results**  
Directory: `/artefacts/results/`

The trained model demonstrates effective crack detection performance. Evaluation was carried out using standard object detection metrics such as precision, recall, and mean average precision (mAP).

---

### Work Distribution

| Team member | Responsibilities | Contribution |
|------------|------------------|--------------|
| Tom Nicolaï | Model training, API integration, Python development | 45% |
| Titouan Lepesqueur | Dataset preparation, annotation, research, documentation | 30% |
| Paul Fortune Corroy | System design, testing, result analysis, documentation | 25% |

---

### Project Schedule

- **Week 1:** Project definition, brainstorming, initial research  
- **Week 2:** Dataset collection and technical investigation  
- **Week 3:** Image annotation and AI model training  
- **Week 4:** System integration, debugging, validation, and final reporting  

---

### Conclusion

This project demonstrates the applicability of computer vision and machine learning techniques to aircraft fuselage inspection.

By combining a trained AI model with a Python-based inference pipeline, the team developed a functional system capable of detecting and highlighting cracks on aircraft fuselage images.

The project highlights both the technical aspects of AI-based image analysis and the importance of structured teamwork throughout the development process.

---


