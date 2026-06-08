# Mental-Tiredness-Score-Project
## Project Description
Mental fatigue is one of the most underreported yet impactful conditions in modern knowledge work. Unlike physical tiredness, mental tiredness is invisible — it quietly reduces decision-making quality, increases errors, and lowers productivity without obvious symptoms.
This project builds an end-to-end machine learning system to quantify mental tiredness as a numeric score (0–10) based on measurable daily inputs such as sleep quality, workload, screen time, caffeine intake, and work environment.
## Problem Statement

Given a person's daily cognitive and lifestyle data, predict their mental tiredness score so they can take proactive steps to manage their mental health and productivity.

## Why This Matters

Burnout prevention — Catch high tiredness early before it becomes burnout
Productivity optimization — Understand which factors drain mental energy the most
Personalised insights — Everyone has different tiredness triggers; ML captures that complexity
Data-driven wellness — Moves mental health tracking from subjective guessing to objective measurement

## How It Works

Data — A dataset of daily records with cognitive load indicators, sleep metrics, environmental factors, and self-reported mood
Preprocessing — Numerical features are scaled; categorical features (mood, work type, environment) are one-hot encoded using a ColumnTransformer pipeline
Hyperparameter Tuning — Optuna's TPE sampler intelligently searches the hyperparameter space for each of 6 regression models, with a MedianPruner that kills unpromising trials early to save time
Experiment Tracking — Every trial and its metrics are logged to MLflow for full reproducibility and comparison
Best Model Selection — The model with the highest Test R² is automatically saved as model.pkl
Deployment — A Streamlit web app loads the saved model and serves real-time predictions with a colour-coded result

## Target Variable
mental_tiredness_score — a continuous score from 0 (no tiredness) to 10 (extreme tiredness)
## What Makes This Pipeline Robust

No data leakage — preprocessing is inside the sklearn Pipeline, fitted only on training data
Smart tuning — TPE sampler finds good hyperparameters in fewer trials than random/grid search
Speed optimised — sub-sampling, parallel CV, and trial pruning cut training time significantly
Production ready — the saved pipeline handles all preprocessing automatically at prediction time, no manual feature engineering needed in the app
