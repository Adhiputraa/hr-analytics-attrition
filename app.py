# Import Library
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Men-load model yang sudah di training pada file employee_model.ipynb
model = joblib.load('model/fix_model.joblib')
scaler = joblib.load('model/scaler.joblib')
label_encoder_dict = joblib.load('model/label_encoder_dict.joblib')

# Menampilkan judul
st.title(" Sistem Prediksi Attrition pada Karyawan PT Maju Jaya ")

# Function untuk membuat variabel input user
def user_input_features():
    Age = st.number_input('Age', min_value=17, max_value=65, value=30)
    BusinessTravel = st.selectbox('Business Travel', ['Travel Rarely', 'Travel Frequently', 'Non Travel'])
    DailyRate = st.number_input('Daily Rate', min_value=1, max_value=1600, value=500)
    Department = st.selectbox('Department', ['Research & Development', 'Sales', 'Human Resources'])
    DistanceFromHome = st.number_input('Distance From Home', min_value=1, max_value=50, value=7)
    Education = st.selectbox('Education Level', ['Below College','College','Bachelor','Master','Doctor'])
    EducationField = st.selectbox('Education Field', ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other'])
    EnvironmentSatisfaction = st.selectbox("EnvironmentSatisfaction", ['Low','Medium','High','Very High'])
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    HourlyRate = st.number_input('HourlyRate', min_value=30, max_value=150, value=65)
    JobInvolvement = st.selectbox("JobInvolvement",['Low','Medium','High','Very High'])
    JobLevel = st.selectbox("JobLevel", [1,2,3,4,5])
    JobRole = st.selectbox('Job Role', ['Healthcare Representative', 'Research Scientist', 'Sales Executive'])
    JobSatisfaction = st.selectbox("JobSatisfaction", ['Low','Medium','High','Very High'])
    MaritalStatus = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    MonthlyIncome = st.number_input('Monthly Income', min_value=1000, max_value=20000, value=5000)
    MonthlyRate =  st.number_input('MonthlyRate', min_value=2000, max_value=28000, value=14000)
    NumCompaniesWorked = st.number_input('NumCompaniesWorked', min_value=0, max_value=15, value=1)
    OverTime = st.selectbox('OverTime', ['Yes', 'No'])
    PercentSalaryHike = st.number_input('PercentSalaryHike', min_value=0, max_value=50, value=10)
    PerformanceRating = st.selectbox("PerformanceRating", ['Excellent','Outstanding'])
    RelationshipSatisfaction = st.selectbox("RelationshipSatisfaction", ['Low','Medium','High','Very High'])
    StockOptionLevel = st.selectbox("StockOptionLevel",[0,1,2,3])
    TotalWorkingYears = st.number_input("TotalWorkingYears", min_value=0, max_value=50, value=5)
    TrainingTimesLastYear = st.number_input("TrainingTimesLastYear", min_value=0, max_value=6, value=2)
    WorkLifeBalance = st.selectbox("WorkLifeBalance", ['Low','Good','Excellent','Outstanding'])
    YearsAtCompany = st.number_input("YearsAtCompany", min_value=0, max_value=50, value=5)
    YearsInCurrentRole = st.number_input("YearsInCurrentRole", min_value=0, max_value=20, value=2)
    YearsSinceLastPromotion = st.number_input("YearsSinceLastPromotion", min_value=0, max_value=20, value=1)
    YearsWithCurrManager = st.number_input("YearsWithCurrManager", min_value=0, max_value=20, value=3)

    data = {
        'Age': Age,
        'BusinessTravel': BusinessTravel,
        'DailyRate': DailyRate,
        'Department': Department,
        'DistanceFromHome': DistanceFromHome,
        'Education': Education,
        'EducationField': EducationField,
        'EnvironmentSatisfaction' : EnvironmentSatisfaction,
        'Gender': Gender,
        'HourlyRate': HourlyRate,
        'JobInvolvement': JobInvolvement,
        'JobLevel': JobLevel,
        'JobRole': JobRole,
        'JobSatisfaction': JobSatisfaction,
        'MaritalStatus': MaritalStatus,
        'MonthlyIncome': MonthlyIncome,
        'MonthlyRate': MonthlyRate,
        'NumCompaniesWorked': NumCompaniesWorked,
        'OverTime' : OverTime,
        'PercentSalaryHike' : PercentSalaryHike,
        'PerformanceRating' : PerformanceRating,
        'RelationshipSatisfaction' : RelationshipSatisfaction,
        'StockOptionLevel' : StockOptionLevel,
        'TotalWorkingYears' : TotalWorkingYears,
        'TrainingTimesLastYear' : TrainingTimesLastYear,
        'WorkLifeBalance' : WorkLifeBalance,
        'YearsAtCompany' : YearsAtCompany,
        'YearsInCurrentRole' : YearsInCurrentRole,
        'YearsSinceLastPromotion' : YearsSinceLastPromotion,
        "YearsWithCurrManager" : YearsWithCurrManager,
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Function untuk melakukan preprocessing menggunakan model yang telah dibuat sebelumnya
def preprocess(input_df):
    input_num = input_df.select_dtypes(include=['int64', 'float64'])
    input_cat = input_df.select_dtypes(include=['object'])


    input_num_scaled = pd.DataFrame(scaler.transform(input_num), columns=input_num.columns)


    input_cat_encoded = input_cat.copy()
    for col in input_cat.columns:
        le = label_encoder_dict[col]
        try:
            input_cat_encoded[col] = le.transform(input_cat[col])
        except:
            st.error(f"Value di kolom {col} tidak dikenal: {input_cat[col].values}")
            return None

    processed = pd.concat([input_num_scaled.reset_index(drop=True), input_cat_encoded.reset_index(drop=True)], axis=1)
    return processed

# Memanggil function input
input_df = user_input_features()

# Memanggil function pemprosesan
processed_input = preprocess(input_df)

if processed_input is not None:
    if st.button("Predict"):
        pred_proba = model.predict_proba(processed_input)[0][1]
        pred_class = model.predict(processed_input)[0]

        st.markdown("---")
        st.success(f"**Probabilitas Attrition:** {pred_proba * 100:.2f}%")
        if pred_class == 1:
            st.warning("🔴 **Potensi Karyawan Akan Resign**")
        else:
            st.info("🟢 **Potensi Karyawan Bertahan**")