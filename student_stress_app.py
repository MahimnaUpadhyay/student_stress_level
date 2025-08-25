import streamlit as st
import pandas as pd
import joblib

model = joblib.load("stress_model.pkl")

# Feature names (must match training)
features = [
    'Gender', 'Age', 'stress_in_life', 'rapid_heartbeat', 'anxiety_or_tension',
    'sleep_problems', 'getting_headaches_often', 'irritated', 'focus_problem',
    'sadness_or_low_mood', 'illness_or_health_issues', 'lonely_or_isolated',
    'overwhelmed_workload', 'peer_pressure', 'relationship_problem',
    'difficulty_with_professors', 'academic_environment_stressful',
    'relaxation_trouble', 'environment_stressful', 'lack_confidence_academic',
    'lack_confidence_subjects', 'subject_conflicting', 'class_attendence',
    'weight_gained'
]

st.set_page_config(page_title="Student Stress Prediction", page_icon="🧠", layout="centered")

st.title("🧠 Student Stress Prediction")
st.markdown("### Fill out the form below to check your stress status")

st.subheader("👤 Demographics")
gender = st.radio("Gender", ["Male", "Female"])
gender_val = 0 if gender == "Male" else 1

age = st.slider("Age", min_value=14, max_value=25, value=18)

st.subheader("📋 Stress Indicators (0 = None, 10 = Very High)")
user_data = {}

user_data['Gender'] = gender_val
user_data['Age'] = age

cols_per_row = 3
for i, col in enumerate(features[2:]):
    if i % cols_per_row == 0:
        cols = st.columns(cols_per_row)
    user_data[col] = cols[i % cols_per_row].slider(
        label=col.replace("_", " ").capitalize(),
        min_value=0, max_value=10, value=0
    )

user_df = pd.DataFrame([user_data])

if st.button("🔮 Predict Stress Level", use_container_width=True):
    prediction = model.predict(user_df)[0]

    st.markdown("---")

    st.write(prediction)
