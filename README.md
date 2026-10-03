# 🏗️ Construction Risk Intelligence

### Machine Learning–Powered Construction Project Risk Prediction System

Construction Risk Intelligence is a machine learning and Django-based web application designed to provide an early assessment of construction project risk using project, structural, environmental, resource, safety, and monitoring-related data.

The system takes construction project information as input and uses a trained machine learning pipeline to classify the project into a risk category and provide the corresponding model confidence and risk probabilities.

> **Project focus:** Construction Management + Machine Learning + Web Application Development

---

## 📌 Project Overview

Construction projects are affected by multiple interacting factors, including project duration, planned cost, structural conditions, environmental conditions, resource utilization, safety indicators, and project progress.

Identifying elevated risk early can support project teams in deciding where additional monitoring and intervention may be required.

This project explores how machine learning can be applied to construction project data to provide an automated risk-screening tool.

The trained model has been integrated into a Django web application, allowing users to enter project information through a browser and receive an estimated risk classification.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Apply machine learning to a real-world construction management problem.
- Develop a construction project risk classification model.
- Process and prepare construction project data for machine learning.
- Evaluate the performance of classification models.
- Save the trained preprocessing and prediction pipeline.
- Integrate the trained pipeline into a Django web application.
- Provide predicted risk level and model confidence.
- Display probability distribution across risk categories.
- Provide risk-management recommendations based on the predicted category.
- Demonstrate the potential of AI/ML in Construction Technology (ConTech).

---

## 🏗️ Construction Problem

Construction projects can experience difficulties related to:

- Project cost
- Project duration
- Structural conditions
- Environmental conditions
- Resource utilization
- Equipment utilization
- Labour requirements
- Safety incidents
- Project progress
- Site anomalies

The purpose of this system is not to replace professional construction judgement.

Instead, it acts as a **decision-support and early risk-screening tool** that can help identify projects or conditions that may require additional attention.

---

## 📊 Dataset

The project uses a construction project dataset containing:

- **1,000 construction project records**
- **28 features**
- A categorical target variable representing project risk level.

### Source

**BIM AI Civil Engineering Project Dataset — Kaggle**

### Target Variable

`Risk_Level`

The target contains three risk categories:

- Low
- Medium
- High

### Major Feature Groups

#### Project Information
- `Project_Type`
- `Location`
- `Planned_Cost`
- `Planned_Duration`

#### Structural / Site Conditions
- `Vibration_Level`
- `Crack_Width`
- `Load_Bearing_Capacity`

#### Environmental Conditions
- `Temperature`
- `Humidity`
- `Weather_Condition`
- `Air_Quality_Index`

#### Resource and Operations
- `Energy_Consumption`
- `Material_Usage`
- `Labor_Hours`
- `Equipment_Utilization`

#### Safety and Monitoring
- `Accident_Count`
- `Image_Analysis_Score`
- `Anomaly_Detected`
- `Completion_Percentage`

#### Project Timeline
- Start and end year/month information
- Calculated project duration

---

## 🔧 Data Preprocessing

The dataset was prepared before model training.

Major preprocessing steps included:

1. Data inspection and quality assessment.
2. Identification of missing values and duplicate records.
3. Identification and removal of data leakage-prone features.
4. Encoding of categorical variables.
5. Mapping of risk categories to numerical classes where required.
6. Engineering of date-related features.
7. Preparation of numerical and categorical features.
8. Stratified train-test splitting.
9. Integration of preprocessing with the machine learning pipeline.

The preprocessing operations used during model development are preserved as part of the trained pipeline to ensure that the deployed application processes new inputs consistently with the training workflow.

---

## 🤖 Machine Learning Workflow

The overall machine learning workflow follows:

```text
Raw Construction Dataset
          ↓
Data Exploration
          ↓
Data Cleaning
          ↓
Feature Engineering
          ↓
Data Preprocessing
          ↓
Train / Test Split
          ↓
Model Training
          ↓
Model Evaluation
          ↓
Pipeline Creation
          ↓
Joblib Model Serialization
          ↓
Django Web Application