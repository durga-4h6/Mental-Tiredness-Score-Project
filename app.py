import streamlit as st
import pandas as pd
import pickle
import os

# ── Load model ────────────────────────────────────────────
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="Mental Tiredness Predictor",
    page_icon="🧠",
    layout="centered"
)
st.title("🧠 Mental Tiredness Predictor")
st.write("Enter your details below:")

# ── Numerical Inputs ──────────────────────────────────────
number_of_decisions_made = st.number_input("Number of Decisions Made",       min_value=0,    value=10)
context_switch_count     = st.number_input("Context Switch Count",            min_value=0,    value=5)
notifications_received   = st.number_input("Notifications Received",          min_value=0,    value=30)
screen_time_min          = st.number_input("Screen Time (minutes)",           min_value=0,    value=360)
deep_work_min            = st.number_input("Deep Work (minutes)",             min_value=0,    value=90)
task_complexity_avg      = st.number_input("Task Complexity Avg (1-10)",      min_value=1,    max_value=10, value=5)
caffeine_mg              = st.number_input("Caffeine Intake (mg)",            min_value=0,    value=200)
break_frequency          = st.number_input("Break Frequency (per day)",       min_value=0,    value=3)
sleep_hours              = st.number_input("Sleep Hours Last Night",          min_value=0.0,  max_value=24.0, value=7.0)
deep_sleep_pct           = st.number_input("Deep Sleep (%)",                  min_value=0,    max_value=100, value=20)
hydration_l              = st.number_input("Hydration (litres)",              min_value=0.0,  value=2.0)
noise_level_db           = st.number_input("Noise Level (dB)",               min_value=0,    max_value=120, value=45)
temperature_c            = st.number_input("Temperature (°C)",               min_value=-10,  max_value=50, value=22)
workload_score           = st.number_input("Workload Score (1-10)",           min_value=1,    max_value=10, value=6)

# ── Categorical Inputs (must match training data labels exactly) ──
# ⚠️  If your dataset uses different labels, update these lists to match.
mood = st.selectbox("Mood", options=[
    "Very Bad", "Bad", "Neutral", "Good", "Excellent"
])

work_type = st.selectbox("Work Type", options=[
    "Creative", "Administrative", "Technical", "Managerial", "Repetitive"
])

work_environment = st.selectbox("Work Environment", options=[
    "Remote", "Office", "Hybrid", "Outdoor", "Co-working"
])

# ── Predict ───────────────────────────────────────────────
if st.button("Predict"):
    input_data = pd.DataFrame({
        "number_of_decisions_made": [number_of_decisions_made],
        "context_switch_count":     [context_switch_count],
        "notifications_received":   [notifications_received],
        "screen_time_min":          [screen_time_min],
        "deep_work_min":            [deep_work_min],
        "task_complexity_avg":      [task_complexity_avg],
        "caffeine_mg":              [caffeine_mg],
        "break_frequency":          [break_frequency],
        "sleep_hours":              [sleep_hours],
        "deep_sleep_pct":           [deep_sleep_pct],
        "hydration_l":              [hydration_l],
        "mood":                     [str(mood)],            # ← string, not number
        "work_type":                [str(work_type)],       # ← string, not number
        "work_environment":         [str(work_environment)],# ← string, not number
        "noise_level_db":           [noise_level_db],
        "temperature_c":            [temperature_c],
        "workload_score":           [workload_score],
    })

    prediction = model.predict(input_data)[0]
    score = round(float(prediction), 1)

    # Colour-coded result
    if score <= 3:
        st.success(f"🟢 Predicted Mental Tiredness Score: **{score}** — Low tiredness")
    elif score <= 6:
        st.warning(f"🟡 Predicted Mental Tiredness Score: **{score}** — Moderate tiredness")
    else:
        st.error(f"🔴 Predicted Mental Tiredness Score: **{score}** — High tiredness")