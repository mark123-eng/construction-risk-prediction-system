# 🏗️ Construction Risk Intelligence

### Machine Learning–Powered Construction Project Risk Screening System

Construction Risk Intelligence is a **Construction Technology (ConTech) and Machine Learning application** that provides an early assessment of construction project risk using project, structural, environmental, resource, safety, and progress-related information.

The system combines a trained **LightGBM machine learning pipeline** with a **Django web application**, allowing users to enter construction project information through a browser and receive:

* Predicted risk category
* Model confidence
* Risk probability distribution
* Risk-management recommendations

> **Project focus:** Construction Engineering and Management + Machine Learning + Django + Deployment

---

## 🚀 Live Application

**Live Demo:**
https://construction-risk-prediction-system-2.onrender.com

The application is publicly deployed and can be accessed through a web browser.

---

## 📌 Project Overview

Construction projects are influenced by multiple interacting factors, including project cost, duration, structural conditions, environmental conditions, resource utilization, safety indicators, equipment utilization, and project progress.

Traditional project monitoring relies heavily on manual assessment and professional judgement. While professional judgement remains essential, machine learning can provide an additional data-driven screening layer that helps identify conditions that may require further investigation.

This project explores how machine learning can be applied to construction-management data to create an automated **early risk-screening and decision-support tool**.

The trained model is integrated into a Django web application so that users can interact with the model without directly working with Python or machine-learning code.

---

## 🎯 Project Objectives

The project was developed to:

* Apply machine learning to a real-world construction-management problem.
* Develop a construction project risk classification model.
* Explore and preprocess construction-related data.
* Engineer relevant project and monitoring features.
* Compare and evaluate classification approaches.
* Train a machine learning model for risk classification.
* Preserve preprocessing and prediction steps in a reusable ML pipeline.
* Integrate the trained pipeline into a Django web application.
* Display predicted risk categories and model confidence.
* Display probability distributions across risk categories.
* Provide risk-management recommendations.
* Deploy the application to a public cloud platform.
* Demonstrate the potential of AI/ML within Construction Technology.

---
## 🏗️ Construction Project Types

Construction Risk Intelligence is intended to support early risk screening across a range of construction and infrastructure projects, including:

* **Road construction**
* **Tunnel construction**
* **Bridge construction**
* **Commercial construction**
* **Residential construction**
* **Industrial construction**

The system uses project, structural, environmental, resource, safety, and monitoring-related information to generate an estimated risk classification for the construction project.

> **Note:** This application is a machine-learning prototype for early risk screening and decision support. Its predictions depend on the patterns and project information represented in the underlying dataset and should be complemented by professional engineering, construction, and project-management judgement.


## 🏗️ Construction Problem

Construction projects can encounter risks associated with:

* Cost and schedule performance
* Structural conditions
* Environmental conditions
* Labour and resource utilization
* Equipment utilization
* Safety incidents
* Project progress
* Site anomalies
* Construction monitoring indicators

The purpose of this system is **not to replace construction professionals or formal risk-management procedures**.

Instead, it is designed as an **early screening and decision-support tool** that can help highlight conditions that may deserve additional professional attention.

---

## ✨ Key Features

### 🔹 Risk Classification

The application classifies construction-project conditions into:

* 🟢 Low Risk
* 🟠 Medium Risk
* 🔴 High Risk

### 🔹 Model Confidence

The application reports the model's confidence associated with the predicted risk category.

### 🔹 Risk Probabilities

Users can view the probability distribution across the available risk categories rather than receiving only a single prediction.

### 🔹 Risk Recommendations

The system provides recommendations corresponding to the predicted risk category.

### 🔹 Input Validation

The application validates user inputs and handles invalid values to reduce prediction errors.

### 🔹 Web-Based Interface

The machine-learning model is accessible through a browser using a Django web application.

### 🔹 Cloud Deployment

The application is deployed using Render, making the predictor publicly accessible.

---

## 🧠 Machine Learning Workflow

The project follows the following workflow:

```text
Construction Dataset
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
Joblib Serialization
        ↓
Django Integration
        ↓
Web Application
        ↓
Cloud Deployment
```

The preprocessing and prediction stages are incorporated into the trained pipeline so that new application inputs are processed consistently with the model-development workflow.

---

## 🤖 Machine Learning Model

The deployed application uses a **LightGBM classification model** integrated into a preprocessing and prediction pipeline.

The pipeline is serialized using **Joblib** and loaded by the Django application when the application starts.

### Prediction Flow

```text
User enters project information
            ↓
Django receives input
            ↓
Input validation
            ↓
ML preprocessing pipeline
            ↓
LightGBM model
            ↓
Risk probabilities
            ↓
Predicted risk category
            ↓
Confidence + recommendation
```

---

## 📊 Dataset

The project uses the:

**BIM AI Civil Engineering Project Dataset — Kaggle**

The dataset contains:

* **1,000 construction project records**
* **28 features**
* A categorical risk-level target

### Target Variable

`Risk_Level`

The target contains three categories:

| Risk Category | Description                                             |
| ------------- | ------------------------------------------------------- |
| Low           | Lower observed risk conditions                          |
| Medium        | Moderate risk conditions requiring attention            |
| High          | Elevated risk conditions requiring increased monitoring |

---

## 🧱 Major Feature Groups

### Project Information

* `Project_Type`
* `Location`
* `Planned_Cost`
* `Planned_Duration`

### Structural / Site Conditions

* `Vibration_Level`
* `Crack_Width`
* `Load_Bearing_Capacity`

### Environmental Conditions

* `Temperature`
* `Humidity`
* `Weather_Condition`
* `Air_Quality_Index`

### Resources and Operations

* `Energy_Consumption`
* `Material_Usage`
* `Labor_Hours`
* `Equipment_Utilization`

### Safety and Monitoring

* `Accident_Count`
* `Image_Analysis_Score`
* `Anomaly_Detected`
* `Completion_Percentage`

### Project Timeline

* Project start and end information
* Date-related features
* Calculated project-duration information

More information about the dataset and preparation process is available in [`DATASET.md`](DATASET.md).

---

## 🔧 Data Preprocessing

The dataset was prepared through several stages:

1. Dataset inspection and exploratory analysis.
2. Missing-value assessment.
3. Duplicate-record assessment.
4. Identification of potential data-leakage features.
5. Categorical-variable encoding.
6. Numerical-feature preparation.
7. Feature engineering.
8. Target preparation.
9. Stratified train-test splitting.
10. Integration of preprocessing into the ML pipeline.

The final preprocessing workflow is preserved within the serialized pipeline used by the deployed application.

---

## 📈 Model Evaluation

The machine-learning models were evaluated using appropriate classification metrics and visual evaluation techniques.

Evaluation included:

* Classification performance
* Confusion matrices
* Class-level performance analysis
* Model comparison
* Prediction probability analysis

Detailed evaluation information is documented in:

[`ML_EVALUATION.md`](ML_EVALUATION.md)

---

## 🌐 Web Application Architecture

The application uses Django to provide the web interface and connect the trained ML pipeline to user inputs.

```text
                    USER
                     │
                     ▼
              Django Web UI
                     │
                     ▼
              Input Validation
                     │
                     ▼
          ML Prediction Pipeline
                     │
              ┌──────┴──────┐
              ▼             ▼
        Preprocessing     LightGBM
              │             │
              └──────┬──────┘
                     ▼
             Prediction Output
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Risk Level  Confidence  Probabilities
                     │
                     ▼
              Recommendation
```

---

## 🛠️ Technology Stack

### Programming & Data

* Python
* NumPy
* Pandas
* SciPy

### Machine Learning

* Scikit-learn
* LightGBM
* Joblib

### Web Development

* Django
* HTML/CSS

### Deployment

* Render
* WhiteNoise

### Development & Version Control

* Jupyter Notebook
* Git
* GitHub

---

## 📁 Project Structure

```text
construction-risk-prediction-system/
│
├── construction_risk_system/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── predictor/
│   ├── migrations/
│   ├── ml/
│   │   └── construction_risk_pipeline.joblib
│   │
│   ├── templates/
│   │   └── predictor/
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── ml_models.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── DATASET.md
├── ML_EVALUATION.md
├── README.md
├── build.sh
├── manage.py
├── requirements.txt
└── runtime.txt
```

---

## 💻 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/mark123-eng/construction-risk-prediction-system.git
cd construction-risk-prediction-system
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file containing the required Django configuration, including:

```text
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
```

Do not commit `.env` or production secrets to GitHub.

### 5. Apply migrations

```powershell
python manage.py migrate
```

### 6. Run system checks

```powershell
python manage.py check
```

### 7. Run tests

```powershell
python manage.py test
```

### 8. Start the development server

```powershell
python manage.py runserver
```

The application can then be accessed locally through the Django development server.

---

## ☁️ Deployment

The application is deployed on **Render**.

The deployment configuration includes:

* Production Django settings
* Environment-based secret management
* `ALLOWED_HOSTS` configuration
* HTTPS enforcement
* WhiteNoise static-file serving
* Python runtime specification
* Automated build script

### Live Application

https://construction-risk-prediction-system-2.onrender.com

---

## 🧪 Testing

The project includes automated Django tests covering key application behavior.

Current test suite:

```text
Found 3 test(s).

Ran 3 tests

OK
```

The Django project also passes:

```text
python manage.py check
```

with no system-check issues.

---

## 🔐 Security Considerations

The deployed application uses production-oriented configuration including:

* Environment-based `SECRET_KEY`
* Production `DEBUG` configuration
* Configurable `ALLOWED_HOSTS`
* HTTPS redirection
* Secure session cookies
* Secure CSRF cookies
* HSTS configuration
* WhiteNoise for static files

Sensitive environment variables are excluded from version control through `.gitignore`.

---

## ⚠️ Limitations

This project is a **prototype decision-support and risk-screening system**.

Important limitations include:

* The dataset contains a relatively small number of records.
* Model predictions depend on the quality and representativeness of the training data.
* Predictions should not be interpreted as definitive engineering or safety conclusions.
* Real construction projects contain complex contextual factors that may not be represented in the dataset.
* Professional construction, engineering, safety, and project-management judgement remains necessary.
* Further validation using larger and geographically diverse construction datasets would be required before operational deployment in real projects.

---

## 🔮 Future Improvements

Potential future development includes:

* Larger and more diverse construction datasets.
* Real-time project monitoring.
* Integration with construction-site IoT sensors.
* Drone-based site monitoring.
* Computer-vision-based anomaly detection.
* BIM integration.
* Construction progress tracking.
* Explainable AI for individual predictions.
* Project risk dashboards.
* Historical prediction tracking.
* Integration with project-management systems.
* Automated construction reports.

These improvements could extend the system from a risk-screening prototype toward a broader **Construction Intelligence platform**.

---

## 🏗️ ConTech Relevance

This project demonstrates the intersection of:

```text
Construction Management
        +
Machine Learning
        +
Web Application Development
        +
Cloud Deployment
```

The broader objective is to explore how AI and machine learning can support construction professionals in areas such as:

* Risk management
* Project monitoring
* Decision support
* Site intelligence
* Construction analytics
* Digital transformation

The project represents an early step toward developing practical **AI-powered Construction Technology (ConTech)** solutions.

---

## 👨‍💻 Author

**Mark Rono**

Construction Engineering and Management + Machine Learning

GitHub: [@mark123-eng](https://github.com/mark123-eng)

---

## 📄 Documentation

* [`DATASET.md`](DATASET.md) — Dataset description and preparation
* [`ML_EVALUATION.md`](ML_EVALUATION.md) — Machine-learning evaluation and results

---

## 📜 Disclaimer

This application is intended for **educational, research, and demonstration purposes**.

Risk predictions generated by the system should not be used as a substitute for professional engineering judgement, construction-site inspection, safety assessment, or formal project risk-management procedures.

