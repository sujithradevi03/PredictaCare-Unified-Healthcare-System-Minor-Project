# PredictaCare-Unified-Healthcare-System-Minor-Project

# 🩺PredictaCare - Unified Healthcare care System (ML + Streamlit)

This project is a **Streamlit-based web application** that allows users to predict the likelihood of three diseases: **Diabetes**, **Heart Disease**, and **Parkinson's Disease** using pre-trained machine learning models. It also provides Doctor recommendations for top specialists based on the prediction results.

## 🚀 Features

- 🌐 User-friendly Streamlit interface
- 🔍 Predictions using trained ML models (Diabetes, Heart Disease, Parkinson's)
- 🧠 Parkinson’s disease detection with vocal measurements
- 🩻 Heart disease risk analysis with medical attributes
- 🧪 Diabetes prediction based on medical input parameters
- 🧑‍⚕️ Dynamic doctor recommendation system
- 📋 Preventive measures and next steps provided post-diagnosis

---

## Prerequisites
Python 3.7 or above

## 📊 Models Used
Diabetes: Trained on PIMA Indian dataset

Heart Disease: Trained on UCI Heart Disease dataset

Parkinson's: Trained on UCI Parkinson’s vocal dataset

All models are saved in .sav format using pickle.

## 📌 Input Parameters
🔸 Diabetes
Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

🔸 Heart Disease
Age, Sex, Chest Pain Type

Blood Pressure, Cholesterol

Fasting Blood Sugar, ECG, Max Heart Rate

Exercise Angina, Oldpeak, Slope, CA, Thal

🔸 Parkinson’s
MDVP:Fo(Hz), MDVP:Fhi(Hz), MDVP:Flo(Hz), Jitter, Shimmer, HNR, etc.

## 👨‍⚕️ Doctor Recommendation
The app recommends top-rated doctors based on the diagnosis result:

Diabetes: Diabetologists & Endocrinologists

Heart Disease: Cardiologists & Heart Surgeons

Parkinson’s: Neurologists & Neurosurgeons

Each doctor card includes:

Name, specialization, experience

Rating

Contact and hospital

Appointment booking link

## ⚠️ Disclaimer
This application is built for educational purposes only. The predictions made by the models are not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical guidance.

## 📬 Contact
For any queries or collaboration:

Sujithra Devi M
- 📧 suji.email@example.com
- 📍 SRM Institute of Science and Technology
