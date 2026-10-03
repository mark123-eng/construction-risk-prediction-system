# Dataset Documentation

## Source
BIM AI Civil Engineering Project Dataset — Kaggle

## Description
1000 construction project records with 28 features
covering project timeline, structural conditions,
environmental factors, resource usage, and safety metrics.

## Target Variable
Risk_Level: Low, Medium, High

## Key Features
- Project_Type, Location
- Planned_Cost, Planned_Duration
- Vibration_Level, Crack_Width, Load_Bearing_Capacity
- Temperature, Humidity, Weather_Condition
- Air_Quality_Index, Energy_Consumption
- Material_Usage, Labor_Hours, Equipment_Utilization
- Accident_Count, Image_Analysis_Score
- Anomaly_Detected, Completion_Percentage

## Preprocessing Steps
1. Removed data leakage features
2. Encoded categorical variables
3. Mapped risk levels to numeric classes
4. Engineered date features (Start/End Year and Month)