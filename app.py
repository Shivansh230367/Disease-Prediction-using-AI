import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")
# Hiding Streamlit UI Elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Background Image & Dark Overlay for Readability
background_image_url = "https://t4.ftcdn.net/jpg/04/71/37/41/360_F_471374128_8993i5Rs3r3WIFpnrlBNnxXUCLdb53V7.jpg"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Dark overlay */
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(10, 10, 10, 0.85);
}}

/* Sidebar Styling */
[data-testid="stSidebar"] {{
    background-color: #121212 !important;
    border-right: 3px solid #FFB400;
    padding: 20px;
}}

/* Improved Text Visibility */
h2 {{
    font-family: 'Poppins', sans-serif;
    color: #FFB400;  /* Bright yellow for high contrast */
    font-size: 24px;
    font-weight: bold;
    text-align: left;
}}

label {{
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 18px;
    font-weight: bold;
}}

p {{
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    color: #EAEAEA;  /* Light gray for readability */
}}

/* Custom Dropdown Styling */
div[data-testid="stSelectbox"] {{
    background-color: #2B2B2B;
    border: 2px solid #FFB400;
    border-radius: 10px;
    padding: 10px;
    color: white;
    font-size: 18px;
    font-weight: bold;
    text-align: left;
    box-shadow: 0px 4px 10px rgba(255, 180, 0, 0.3);
    transition: all 0.3s ease-in-out;
}}

div[data-testid="stSelectbox"]:hover {{
    border-color: #00C897;
    box-shadow: 0px 4px 15px rgba(0, 200, 151, 0.3);
}}

/* Dropdown Items */
div[data-baseweb="select"] > div {{
    background-color: #1E1E1E;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 6px;
    padding: 12px;
    transition: all 0.2s ease-in-out;
}}

div[data-baseweb="select"] > div:hover {{
    background-color: #FFB400;
    color: black;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Sidebar with Improved Dropdown
with st.sidebar:
    st.markdown("<h1>Select a Disease to Predict</h1>", unsafe_allow_html=True)
    selected = st.selectbox(
        '',
        ['Diabetes Prediction',
         'Heart Disease Prediction',
         'Parkinsons Prediction',
         'Lung Cancer Prediction',
         'Hypo-Thyroid Prediction']
    )

# Main Content Placeholder
st.write("")
def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict heart disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")

    GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid")
    st.write("Enter the following details to predict hypo-thyroid disease:")

    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
    tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
    t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
    t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
    tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')

    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        st.success(thyroid_diagnosis)
