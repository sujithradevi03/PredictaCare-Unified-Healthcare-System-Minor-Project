import os 
import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu 
import pandas as pd 
import numpy as np 
# Set page configuration 
st.set_page_config(page_title="Health Assistant", 
layout="wide", 
page_icon="                              ") 
# Getting the working directory of the main.py 
working_dir = "C:/Users/nhm/Downloads/MINOR PROJECT" 
# Loading the saved models 
diabetes_model = 
pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb')) 
heart_disease_model = 
pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb')) 
parkinsons_model = 
pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb')) 
# Doctor database (can be replaced with actual database 
connection) 
doctors_db = { 
51 
"diabetes": [ 
{ 
"name": "Dr. V. Mohan", 
"specialization": "Diabetologist", 
"experience": "40+ years", 
"rating": "4.9", 
"contact": "drmohan@drmohans.com", 
"hospital": "Dr. Mohan’s Diabetes Specialities Centre", 
"appointment_url": "https://drmohans.com/book-an
appointment/" 
}, 
{ 
"name": "Dr. Anoop Misra", 
"specialization": "Endocrinologist", 
"experience": "30+ years", 
"rating": "4.8", 
"contact": "anoop@fortishealthcare.com", 
"hospital": "Fortis C-DOC Hospital, Delhi", 
"appointment_url": 
"https://www.fortishealthcare.com/india/doctor/dr-anoop-misra
749" 
}, 
{ 
"name": "Dr. Jothydev Kesavadev", 
"specialization": "Diabetologist", 
"experience": "25+ years", 
"rating": "4.7", 
"contact": "jothydev@diabetes.in", 
"hospital": "Jothydev’s Diabetes Research Centre", 
"appointment_url": 
"https://www.jothydev.com/appointment" 
} 
], 
"heart": [ 
52 
{ 
"name": "Dr. Naresh Trehan", 
"specialization": "Cardiac Surgeon", 
"experience": "50+ years", 
"rating": "4.9", 
"contact": "trehan@medanta.org", 
"hospital": "Medanta – The Medicity, Gurugram", 
"appointment_url": "https://www.medanta.org/doctors/dr
naresh-trehan/" 
}, 
{ 
"name": "Dr. Devi Shetty", 
"specialization": "Cardiac Surgeon", 
"experience": "35+ years", 
"rating": "4.8", 
"contact": "devi@narayanahealth.org", 
"hospital": "Narayana Health City, Bengaluru", 
"appointment_url": 
"https://www.narayanahealth.org/bangalore/cardiology/dr-devi
prasad-shetty" 
}, 
{ 
"name": "Dr. Ashok Seth", 
"specialization": "Cardiologist", 
"experience": "40+ years", 
"rating": "4.8", 
"contact": "aseth@fortishealthcare.com", 
"hospital": "Fortis Escorts Heart Institute, Delhi", 
"appointment_url": 
"https://www.fortishealthcare.com/india/doctor/dr-ashok-seth
415" 
} 
], 
"parkinsons": [ 
53 
{ 
"name": "Dr. Bindu Menon", 
"specialization": "Neurologist", 
"experience": "20+ years", 
"rating": "4.8", 
"contact": "bindu.menon@gmail.com", 
"hospital": "Bindu Menon Foundation", 
"appointment_url": "https://www.bindumenon.org" 
}, 
{ 
}, 
{ 
} 
] 
} 
"name": "Dr. P. Sarat Chandra", 
"specialization": "Neurosurgeon", 
"experience": "25+ years", 
"rating": "4.7", 
"contact": "sarat.aiims@gmail.com", 
"hospital": "AIIMS, Delhi", 
"appointment_url": "https://www.aiims.edu" 
"name": "Dr. Nilesh M. Bhandari", 
"specialization": "Neurologist", 
"experience": "15+ years", 
"rating": "4.6", 
"contact": "nilesh.bhandari@jehangirhospital.com", 
"hospital": "Jehangir Hospital, Pune", 
"appointment_url": "https://www.jehangirhospital.com" 
def display_doctor_recommendations(disease_type): 
st.subheader("Recommended Specialists") 
st.write("Based on your results, we recommend consulting with 
54 
these specialists:") 
doctors = doctors_db.get(disease_type, []) 
for i, doctor in enumerate(doctors, 1): 
with st.expander(f"{i}. {doctor['name']} - 
{doctor['specialization']}"): 
col1, col2 = st.columns([1, 3]) 
with col1: 
st.image("male.png", width=80) 
with col2: 
st.write(f"**Experience:** {doctor['experience']}") 
st.write(f"**Rating:** {doctor['rating']}/5.0") 
st.write(f"**Hospital:** {doctor['hospital']}") 
st.write(f"**Contact:** {doctor['contact']}") 
st.markdown(f"[   
Book 
Appointment]({doctor['appointment_url']})", 
unsafe_allow_html=True) 
# Sidebar for navigation 
with st.sidebar: 
selected = option_menu('Multiple Disease Prediction System', 
['Diabetes Prediction', 
'Heart Disease Prediction', 
'Parkinsons Prediction'], 
menu_icon='hospital-fill', 
icons=['activity', 'heart', 'person'], 
default_index=0) 
# Diabetes Prediction Page 
if selected == 'Diabetes Prediction': 
# Page title 
st.title('Diabetes Prediction using ML') 
55 
# Getting the input data from the user 
col1, col2, col3 = st.columns(3) 
with col1: 
Pregnancies = st.text_input('Number of Pregnancies') 
with col2: 
Glucose = st.text_input('Glucose Level (70 mg/dL - 100 
mg/dL)') 
with col3: 
BloodPressure = st.text_input('Blood Pressure value (120/80 
mmHg or lower)') 
with col1: 
SkinThickness = st.text_input('Skin Thickness value (1.9-2.4 
mm)') 
with col2: 
Insulin = st.text_input('Insulin Level (5-12)') 
with col3: 
BMI = st.text_input('BMI value') 
with col1: 
DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree 
Function value (eg: 0.08-2.42)') 
with col2: 
Age = st.text_input('Age of the Person') 
# Code for Prediction 
diab_diagnosis = '' 
56 
# Creating a button for Prediction 
if st.button('Diabetes Test Result'): 
user_input = [Pregnancies, Glucose, BloodPressure, 
SkinThickness, Insulin, 
BMI, DiabetesPedigreeFunction, Age] 
user_input = [float(x) if x.strip() != '' else 0.0 for x in 
user_input] 
diab_prediction = diabetes_model.predict([user_input]) 
if diab_prediction[0] == 1: 
diab_diagnosis = 'The person is diabetic' 
st.success(diab_diagnosis) 
st.warning("Important: This AI prediction is not a 
substitute for professional medical advice. Please consult a 
healthcare provider.") 
# Display recommendations and doctors 
st.subheader("Next Steps") 
st.write(""" - Schedule an appointment with an endocrinologist or 
diabetologist - Monitor your blood sugar levels regularly - Maintain a balanced diet and exercise routine - Get regular HbA1c tests as recommended by your doctor 
""") 
display_doctor_recommendations("diabetes") 
else: 
diab_diagnosis = 'The person is not diabetic' 
st.success(diab_diagnosis) 
st.info(""" 
57 
**Preventive Measures:** - Maintain healthy weight - Exercise regularly - Eat balanced diet with whole grains - Get regular check-ups if you have risk factors 
""") 
# Heart Disease Prediction Page 
if selected == 'Heart Disease Prediction': 
# Page title 
st.title('Heart Disease Prediction using ML') 
col1, col2, col3 = st.columns(3) 
with col1: 
age = st.text_input('Age') 
with col2: 
sex = st.text_input('Sex (Female-0 and Male-1)') 
with col3: 
cp = st.text_input('Chest Pain types (0-No chest pain, 1
Typical heart-related chest pain, 2-less likely heart-related, 3
Chest pain not related to the heart.)') 
with col1: 
trestbps = st.text_input('Resting Blood Pressure (94 - 120)') 
with col2: 
chol = st.text_input('Serum Cholestoral in mg/dl') 
with col3: 
fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl') 
58 
with col1: 
restecg = st.text_input('Resting Electrocardiographic results') 
with col2: 
thalach = st.text_input('Maximum Heart Rate achieved') 
with col3: 
exang = st.text_input('Exercise Induced Angina') 
with col1: 
oldpeak = st.text_input('ST depression induced by exercise') 
with col2: 
slope = st.text_input('Slope of the peak exercise ST segment') 
with col3: 
ca = st.text_input('Major vessels colored by flourosopy') 
with col1: 
thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = 
reversable defect') 
# Code for Prediction 
heart_diagnosis = '' 
# Creating a button for Prediction 
if st.button('Heart Disease Test Result'): 
user_input = [age, sex, cp, trestbps, chol, fbs, restecg, 
thalach, exang, oldpeak, slope, ca, thal] 
user_input = [float(x) for x in user_input] 
heart_prediction = heart_disease_model.predict([user_input]) 
59 
if heart_prediction[0] == 1: 
heart_diagnosis = 'The person is having heart disease' 
st.success(heart_diagnosis) 
st.warning("Important: This AI prediction is not a 
substitute for professional medical advice. Please consult a 
cardiologist immediately.") 
# Emergency information 
st.error(""" 
**If you're experiencing:**   - Chest pain or discomfort   - Shortness of breath   - Pain radiating to arm/jaw   - Dizziness or nausea   
**Seek emergency medical care immediately!** 
""") 
# Display recommendations and doctors 
st.subheader("Next Steps") 
st.write(""" - Schedule an appointment with a cardiologist - Get an ECG and stress test - Monitor blood pressure regularly - Follow a heart-healthy diet (low sodium, low fat) 
""") 
display_doctor_recommendations("heart") 
else: 
heart_diagnosis = 'The person does not have any heart 
disease' 
st.success(heart_diagnosis) 
st.info(""" 
60 
**Heart Health Tips:** - Maintain healthy cholesterol levels - Exercise at least 30 minutes daily - Avoid smoking and limit alcohol - Manage stress through meditation/yoga - Get regular check-ups after age 40 
""") 
# Parkinson's Prediction Page 
if selected == "Parkinsons Prediction": 
# Page title 
st.title("Parkinson's Disease Prediction using ML") 
col1, col2, col3, col4, col5 = st.columns(5) 
with col1: 
fo = st.text_input('MDVP:Fo(Hz)') 
with col2: 
fhi = st.text_input('MDVP:Fhi(Hz)') 
with col3: 
flo = st.text_input('MDVP:Flo(Hz)') 
with col4: 
Jitter_percent = st.text_input('MDVP:Jitter(%)') 
with col5: 
Jitter_Abs = st.text_input('MDVP:Jitter(Abs)') 
with col1: 
RAP = st.text_input('MDVP:RAP') 
with col2: 
61 
PPQ = st.text_input('MDVP:PPQ') 
with col3: 
DDP = st.text_input('Jitter:DDP') 
with col4: 
Shimmer = st.text_input('MDVP:Shimmer') 
with col5: 
Shimmer_dB = st.text_input('MDVP:Shimmer(dB)') 
with col1: 
APQ3 = st.text_input('Shimmer:APQ3') 
with col2: 
APQ5 = st.text_input('Shimmer:APQ5') 
with col3: 
APQ = st.text_input('MDVP:APQ') 
with col4: 
DDA = st.text_input('Shimmer:DDA') 
with col5: 
NHR = st.text_input('NHR') 
with col1: 
HNR = st.text_input('HNR') 
with col2: 
RPDE = st.text_input('RPDE') 
with col3: 
DFA = st.text_input('DFA') 
62 
with col4: 
spread1 = st.text_input('spread1') 
with col5: 
spread2 = st.text_input('spread2') 
with col1: 
D2 = st.text_input('D2') 
with col2: 
PPE = st.text_input('PPE') 
# Code for Prediction 
parkinsons_diagnosis = '' 
# Creating a button for Prediction 
if st.button("Parkinson's Test Result"): 
user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, 
RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, 
APQ5, 
APQ, DDA, NHR, HNR, RPDE, DFA, spread1, 
spread2, D2, PPE] 
user_input = [float(x) for x in user_input] 
parkinsons_prediction = 
parkinsons_model.predict([user_input]) 
if parkinsons_prediction[0] == 1: 
parkinsons_diagnosis = "The person has Parkinson's 
disease" 
st.success(parkinsons_diagnosis) 
st.warning("Important: This AI prediction is not a 
63 
substitute for professional medical diagnosis. Please consult a 
neurologist specializing in movement disorders.") 
# Display recommendations and doctors 
st.subheader("Next Steps") 
st.write(""" - Schedule an appointment with a movement disorder 
specialist - Consider a comprehensive neurological examination - Physical therapy can help manage symptoms - Join a support group for Parkinson's patients 
""") 
display_doctor_recommendations("parkinsons") 
else: 
parkinsons_diagnosis = "The person does not have 
Parkinson's disease" 
st.success(parkinsons_diagnosis) 
st.info(""" 
**Neurological Health Tips:** - Regular physical exercise - Cognitive stimulation activities - Balanced diet rich in antioxidants - Regular sleep patterns - Stress management techniques 
""") 
# Load models (replace with your actual models) 
#diabetes_model = lambda x: np.random.randint(0, 2) 
#heart_disease_model = lambda x: np.random.randint(0, 2) 
#parkinsons_model = lambda x: np.random.randint(0, 2) 
# Integrated Disease Risk Assessment 
st.title("Disease Risk Assessment") 
64 
# Disease selection for risk assessment 
risk_disease = st.radio("Select disease for assessment:", 
["Diabetes", "Heart Disease", "Parkinson's"], 
horizontal=True) 
if risk_disease == "Diabetes": 
st.subheader("Diabetes Risk Assessment") 
col1, col2, col3 = st.columns(3) 
with col1: 
Pregnancies = st.number_input('Number of Pregnancies', 
min_value=0, max_value=20, value=0) 
Glucose = st.number_input('Glucose Level (mg/dL)', 
min_value=0, max_value=300, value=100) 
with col2: 
BloodPressure = st.number_input('Blood Pressure (mmHg)', 
min_value=0, max_value=200, value=80) 
SkinThickness = st.number_input('Skin Thickness (mm)', 
min_value=0, max_value=100, value=20) 
with col3: 
Insulin = st.number_input('Insulin Level (μU/mL)', 
min_value=0, max_value=1000, value=80) 
BMI = st.number_input('BMI', min_value=0.0, 
max_value=100.0, value=22.0) 
DiabetesPedigreeFunction = st.number_input('Diabetes 
Pedigree Function', min_value=0.0, max_value=2.5, value=0.5, 
step=0.01) 
Age = st.number_input('Age', min_value=1, max_value=120, 
value=25) 
65 
elif risk_disease == "Heart Disease": 
st.subheader("Heart Disease Risk Assessment") 
col1, col2, col3 = st.columns(3) 
with col1: 
age = st.number_input('Age', min_value=1, max_value=120, 
value=50) 
sex = st.selectbox('Sex', ['Female', 'Male']) 
with col2: 
cp = st.selectbox('Chest Pain Type',  
["0: No pain", "1: Typical angina",  
"2: Atypical angina", "3: Non-anginal pain"]) 
trestbps = st.number_input('Resting Blood Pressure (mmHg)', 
min_value=0, max_value=300, value=120) 
with col3: 
chol = st.number_input('Cholesterol (mg/dL)', min_value=0, 
max_value=600, value=200) 
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['No', 
'Yes']) 
restecg = st.selectbox('Resting ECG',  
["0: Normal", "1: ST-T wave abnormality",  
"2: Left ventricular hypertrophy"]) 
thalach = st.number_input('Maximum Heart Rate Achieved', 
min_value=0, max_value=250, value=150) 
exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes']) 
oldpeak = st.number_input('ST Depression (exercise)', 
min_value=0.0, max_value=10.0, value=1.0, step=0.1) 
slope = st.selectbox('Slope of ST Segment',  
["1: Upsloping", "2: Flat", "3: Downsloping"]) 
ca = st.number_input('Major Vessels Colored', min_value=0, 
max_value=4, value=0) 
66 
thal = st.selectbox('Thalassemia',  
["1: Normal", "2: Fixed Defect", "3: Reversible 
Defect"]) 
elif risk_disease == "Parkinson's": 
st.subheader("Parkinson's Risk Assessment") 
col1, col2 = st.columns(2) 
with col1: 
fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, 
max_value=300.0, value=150.0, step=0.1) 
fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, 
max_value=300.0, value=170.0, step=0.1) 
flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, 
max_value=300.0, value=100.0, step=0.1) 
jitter = st.number_input('MDVP:Jitter(%)', min_value=0.0, 
max_value=1.0, value=0.005, step=0.001, format="%.3f") 
with col2: 
shimmer = st.number_input('MDVP:Shimmer(dB)', 
min_value=0.0, max_value=1.0, value=0.3, step=0.1) 
nhr = st.number_input('NHR', min_value=0.0, 
max_value=1.0, value=0.01, step=0.01, format="%.2f") 
hnr = st.number_input('HNR', min_value=0.0, 
max_value=40.0, value=25.0, step=0.1) 
rpde = st.number_input('RPDE', min_value=0.0, 
max_value=1.0, value=0.5, step=0.01, format="%.2f") 
# Prediction button 
if st.button("Assess Risk"): 
try: 
if risk_disease == "Diabetes": 
user_input = [Pregnancies, Glucose, BloodPressure, 
SkinThickness, Insulin, 
67 
BMI, DiabetesPedigreeFunction, Age] 
prediction = diabetes_model.predict([user_input])[0] 
elif risk_disease == "Heart Disease": 
user_input = [ 
age, 1 if sex == 'Male' else 0, int(cp.split(":")[0]),  
trestbps, chol, 1 if fbs == 'Yes' else 0,  
int(restecg.split(":")[0]), thalach, 1 if exang == 'Yes' else 
0,  
0.006, 
hnr, 
oldpeak, int(slope.split(":")[0]), ca, int(thal.split(":")[0]) 
] 
prediction = heart_disease_model.predict([user_input])[0] 
elif risk_disease == "Parkinson's": 
user_input = [fo, fhi, flo, jitter, 0.00003, 0.002, 0.002, 
shimmer/10, shimmer, 0.02, 0.02, 0.03, 0.06, nhr, 
rpde, 0.7, -5.0, 0.2, 2.0, 0.2] 
prediction = parkinsons_model.predict([user_input])[0] 
# Display results 
st.subheader("Risk Assessment Result") 
if prediction == 1: 
st.error(f"High Risk of {risk_disease}") 
st.progress(70) 
display_doctor_recommendations(risk_disease.lower().replace("'", 
"").replace(" ", "_")) 
else: 
st.success(f"Low Risk of {risk_disease}") 
st.progress(30) 
st.warning("Note: This is a predictive assessment, not a 
68 
diagnosis. Please consult a doctor.") 
except Exception as e: 
st.error(f"Error in prediction: {str(e)}") 
