import streamlit as st
import joblib
import numpy as np

# 1. تحميل النموذج المحفوظ
model = joblib.load('graduat_model.pkl')

# (إذا كان لديك scaler تم حفظه، افكّي التعليق عن السطر التالي)
# scaler = joblib.load('graduat_scaler.pkl')

# 2. تصميم عنوان الواجهة
st.set_page_config(page_title="Graduate Admission Predictor", page_icon="🎓")
st.title("🎓 Graduate Admission Chance Predictor")
st.write("Enter student details to predict the chance of admission:")

# 3. حقول الإدخال بناءً على متغيرات المشروع
gre_score = st.number_input("GRE Score (260 - 340)", min_value=260, max_value=340, value=310)
toefl_score = st.number_input("TOEFL Score (0 - 120)", min_value=0, max_value=120, value=105)
university_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5], index=2)
sop = st.slider("Statement of Purpose (SOP)", 1.0, 5.0, 3.5, 0.5)
lor = st.slider("Letter of Recommendation (LOR)", 1.0, 5.0, 3.5, 0.5)
cgpa = st.number_input("CGPA (Out of 10)", min_value=1.0, max_value=10.0, value=8.5, step=0.1)
research = st.radio("Research Experience", ["Yes", "No"])

research_val = 1 if research == "Yes" else 0

# 4. زر التنبؤ
if st.button("Predict Admission Chance"):
    # تجميع المدخلات في مصفوفة
    features = np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research_val]])
    
    # إذا كنتِ استخدمتِ Scaler:
    # features = scaler.transform(features)
    
    # التوقع بالنموذج
    prediction = model.predict(features)[0]
    
    # تحويل النتيجة لنسبة مئوية
    chance = round(prediction * 100, 2) if prediction <= 1.0 else round(prediction, 2)
    
    st.markdown("---")
    st.success(f"🎯 Estimated Admission Chance: **{chance}%**")