from django.shortcuts import render
import pandas as pd

from .ml_models import model


# =========================================================
# HELPER FUNCTION — SAFE FLOAT CONVERSION
# =========================================================

def get_float(post_data, field_name, default=0.0):
    value = post_data.get(field_name, "")
    if value is None:
        return default
    value = str(value).strip()
    if value == "":
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


# =========================================================
# HELPER FUNCTION — RISK RECOMMENDATION
# =========================================================

def get_recommendation(risk_level):
    recommendations = {
        "0": {
            "label": "Low Risk",
            "color": "green",
            "points": [
                "Project conditions are stable. Maintain current monitoring frequency.",
                "Ensure routine safety inspections remain on schedule.",
                "Continue tracking resource utilisation and completion milestones.",
                "Document current practices — they are working.",
            ],
        },
        "1": {
            "label": "Medium Risk",
            "color": "orange",
            "points": [
                "Elevated risk detected. Increase site inspection frequency immediately.",
                "Review structural readings — vibration levels and crack widths require attention.",
                "Audit resource allocation: labour hours, equipment utilisation, and material usage.",
                "Ensure accident reporting is up to date and safety briefings are conducted.",
                "Reassess project timeline — calculated duration may be diverging from plan.",
            ],
        },
        "2": {
            "label": "High Risk",
            "color": "red",
            "points": [
                "Critical risk level. Immediate intervention required.",
                "Halt non-essential site activities and conduct a full safety audit.",
                "Escalate to senior project management and notify relevant stakeholders.",
                "Inspect all load-bearing structures and anomaly-flagged zones without delay.",
                "Review and update the project risk register and mitigation plan.",
                "Consider engaging an independent structural or safety engineer for assessment.",
            ],
        },
    }
    return recommendations.get(str(risk_level), None)


# =========================================================
# HELPER FUNCTION — VALIDATE INPUTS
# =========================================================

def validate_inputs(post_data):
    errors = {}

    # --- Project Type ---
    project_type = post_data.get("project_type", "").strip()
    if not project_type:
        errors["project_type"] = "Project type is required."

    # --- Location ---
    location = post_data.get("location", "").strip()
    if not location:
        errors["location"] = "Location is required."

    # --- Start Year ---
    try:
        start_year = float(post_data.get("start_year", ""))
        if not (2000 <= start_year <= 2100):
            errors["start_year"] = "Start year must be between 2000 and 2100."
    except (ValueError, TypeError):
        errors["start_year"] = "Start year must be a valid number."

    # --- Start Month ---
    try:
        start_month = float(post_data.get("start_month", ""))
        if not (1 <= start_month <= 12):
            errors["start_month"] = "Start month must be between 1 and 12."
    except (ValueError, TypeError):
        errors["start_month"] = "Start month must be a valid number."

    # --- End Year ---
    try:
        end_year = float(post_data.get("end_year", ""))
        if not (2000 <= end_year <= 2100):
            errors["end_year"] = "End year must be between 2000 and 2100."
        elif "start_year" not in errors:
            start_year = float(post_data.get("start_year", ""))
            if end_year < start_year:
                errors["end_year"] = "End year must be greater than or equal to start year."
    except (ValueError, TypeError):
        errors["end_year"] = "End year must be a valid number."

    # --- End Month ---
    try:
        end_month = float(post_data.get("end_month", ""))
        if not (1 <= end_month <= 12):
            errors["end_month"] = "End month must be between 1 and 12."
    except (ValueError, TypeError):
        errors["end_month"] = "End month must be a valid number."

    # --- Planned Cost ---
    try:
        planned_cost = float(post_data.get("planned_cost", ""))
        if planned_cost <= 0:
            errors["planned_cost"] = "Planned cost must be greater than 0."
    except (ValueError, TypeError):
        errors["planned_cost"] = "Planned cost must be a valid number."

    # --- Planned Duration ---
    try:
        planned_duration = float(post_data.get("planned_duration", ""))
        if planned_duration <= 0:
            errors["planned_duration"] = "Planned duration must be greater than 0."
    except (ValueError, TypeError):
        errors["planned_duration"] = "Planned duration must be a valid number."

    # --- Calculated Duration ---
    try:
        calculated_duration_days = float(post_data.get("calculated_duration_days", ""))
        if calculated_duration_days <= 0:
            errors["calculated_duration_days"] = "Calculated duration must be greater than 0."
    except (ValueError, TypeError):
        errors["calculated_duration_days"] = "Calculated duration must be a valid number."

    # --- Vibration Level ---
    try:
        vibration_level = float(post_data.get("vibration_level", ""))
        if vibration_level < 0:
            errors["vibration_level"] = "Vibration level must be 0 or greater."
    except (ValueError, TypeError):
        errors["vibration_level"] = "Vibration level must be a valid number."

    # --- Crack Width ---
    try:
        crack_width = float(post_data.get("crack_width", ""))
        if crack_width < 0:
            errors["crack_width"] = "Crack width must be 0 or greater."
    except (ValueError, TypeError):
        errors["crack_width"] = "Crack width must be a valid number."

    # --- Load Bearing Capacity ---
    try:
        load_bearing_capacity = float(post_data.get("load_bearing_capacity", ""))
        if load_bearing_capacity <= 0:
            errors["load_bearing_capacity"] = "Load bearing capacity must be greater than 0."
    except (ValueError, TypeError):
        errors["load_bearing_capacity"] = "Load bearing capacity must be a valid number."

    # --- Temperature ---
    try:
        temperature = float(post_data.get("temperature", ""))
        if not (-50 <= temperature <= 60):
            errors["temperature"] = "Temperature must be between -50 and 60°C."
    except (ValueError, TypeError):
        errors["temperature"] = "Temperature must be a valid number."

    # --- Humidity ---
    try:
        humidity = float(post_data.get("humidity", ""))
        if not (0 <= humidity <= 100):
            errors["humidity"] = "Humidity must be between 0 and 100%."
    except (ValueError, TypeError):
        errors["humidity"] = "Humidity must be a valid number."

    # --- Weather Condition ---
    weather_condition = post_data.get("weather_condition", "").strip()
    if not weather_condition:
        errors["weather_condition"] = "Weather condition is required."

    # --- Air Quality Index ---
    try:
        air_quality_index = float(post_data.get("air_quality_index", ""))
        if air_quality_index < 0:
            errors["air_quality_index"] = "Air quality index must be 0 or greater."
    except (ValueError, TypeError):
        errors["air_quality_index"] = "Air quality index must be a valid number."

    # --- Energy Consumption ---
    try:
        energy_consumption = float(post_data.get("energy_consumption", ""))
        if energy_consumption < 0:
            errors["energy_consumption"] = "Energy consumption must be 0 or greater."
    except (ValueError, TypeError):
        errors["energy_consumption"] = "Energy consumption must be a valid number."

    # --- Material Usage ---
    try:
        material_usage = float(post_data.get("material_usage", ""))
        if material_usage < 0:
            errors["material_usage"] = "Material usage must be 0 or greater."
    except (ValueError, TypeError):
        errors["material_usage"] = "Material usage must be a valid number."

    # --- Labor Hours ---
    try:
        labor_hours = float(post_data.get("labor_hours", ""))
        if labor_hours < 0:
            errors["labor_hours"] = "Labor hours must be 0 or greater."
    except (ValueError, TypeError):
        errors["labor_hours"] = "Labor hours must be a valid number."

    # --- Equipment Utilization ---
    try:
        equipment_utilization = float(post_data.get("equipment_utilization", ""))
        if not (0 <= equipment_utilization <= 100):
            errors["equipment_utilization"] = "Equipment utilization must be between 0 and 100%."
    except (ValueError, TypeError):
        errors["equipment_utilization"] = "Equipment utilization must be a valid number."

    # --- Accident Count ---
    try:
        accident_count = float(post_data.get("accident_count", ""))
        if accident_count < 0:
            errors["accident_count"] = "Accident count must be 0 or greater."
    except (ValueError, TypeError):
        errors["accident_count"] = "Accident count must be a valid number."

    # --- Image Analysis Score ---
    try:
        image_analysis_score = float(post_data.get("image_analysis_score", ""))
        if image_analysis_score < 0:
            errors["image_analysis_score"] = "Image analysis score must be 0 or greater."
    except (ValueError, TypeError):
        errors["image_analysis_score"] = "Image analysis score must be a valid number."

    # --- Anomaly Detected ---
    try:
        anomaly_detected = float(post_data.get("anomaly_detected", ""))
        if anomaly_detected not in [0, 1]:
            errors["anomaly_detected"] = "Anomaly detected must be 0 or 1."
    except (ValueError, TypeError):
        errors["anomaly_detected"] = "Anomaly detected must be a valid value."

    # --- Completion Percentage ---
    try:
        completion_percentage = float(post_data.get("completion_percentage", ""))
        if not (0 <= completion_percentage <= 100):
            errors["completion_percentage"] = "Completion percentage must be between 0 and 100%."
    except (ValueError, TypeError):
        errors["completion_percentage"] = "Completion percentage must be a valid number."

    return errors


# =========================================================
# HOME / CONSTRUCTION RISK PREDICTION
# =========================================================

def home(request):

    prediction = None
    confidence = None
    recommendation = None
    class_probabilities = []
    errors = {}
    error = None

    if request.method == "POST":

        # =============================================
        # VALIDATE INPUTS FIRST
        # =============================================

        errors = validate_inputs(request.POST)

        if not errors:

            # =========================================
            # CHECK MODEL IS LOADED
            # =========================================

            if model is None:
                error = "The prediction model is currently unavailable. Please contact support."
                print("\n[ERROR] Model is None — joblib file may be missing or corrupt.")

            else:

                try:

                    # =====================================
                    # 1. COLLECT FORM INPUTS
                    # =====================================

                    project_type = request.POST.get("project_type", "").strip()
                    location = request.POST.get("location", "").strip()
                    start_year = get_float(request.POST, "start_year")
                    start_month = get_float(request.POST, "start_month")
                    end_year = get_float(request.POST, "end_year")
                    end_month = get_float(request.POST, "end_month")
                    planned_cost = get_float(request.POST, "planned_cost")
                    planned_duration = get_float(request.POST, "planned_duration")
                    calculated_duration_days = get_float(request.POST, "calculated_duration_days")
                    vibration_level = get_float(request.POST, "vibration_level")
                    crack_width = get_float(request.POST, "crack_width")
                    load_bearing_capacity = get_float(request.POST, "load_bearing_capacity")
                    temperature = get_float(request.POST, "temperature")
                    humidity = get_float(request.POST, "humidity")
                    weather_condition = request.POST.get("weather_condition", "").strip()
                    air_quality_index = get_float(request.POST, "air_quality_index")
                    energy_consumption = get_float(request.POST, "energy_consumption")
                    material_usage = get_float(request.POST, "material_usage")
                    labor_hours = get_float(request.POST, "labor_hours")
                    equipment_utilization = get_float(request.POST, "equipment_utilization")
                    accident_count = get_float(request.POST, "accident_count")
                    image_analysis_score = get_float(request.POST, "image_analysis_score")
                    anomaly_detected = get_float(request.POST, "anomaly_detected")
                    completion_percentage = get_float(request.POST, "completion_percentage")


                    # =====================================
                    # 2. CREATE DATAFRAME
                    # =====================================

                    data = pd.DataFrame([{
                        "Project_Type": project_type,
                        "Location": location,
                        "Planned_Cost": planned_cost,
                        "Planned_Duration": planned_duration,
                        "Vibration_Level": vibration_level,
                        "Crack_Width": crack_width,
                        "Load_Bearing_Capacity": load_bearing_capacity,
                        "Temperature": temperature,
                        "Humidity": humidity,
                        "Weather_Condition": weather_condition,
                        "Air_Quality_Index": air_quality_index,
                        "Energy_Consumption": energy_consumption,
                        "Material_Usage": material_usage,
                        "Labor_Hours": labor_hours,
                        "Equipment_Utilization": equipment_utilization,
                        "Accident_Count": accident_count,
                        "Image_Analysis_Score": image_analysis_score,
                        "Anomaly_Detected": anomaly_detected,
                        "Completion_Percentage": completion_percentage,
                        "Calculated_Duration_Days": calculated_duration_days,
                        "Start_Year": start_year,
                        "Start_Month": start_month,
                        "End_Year": end_year,
                        "End_Month": end_month,
                    }])


                    # =====================================
                    # 3. PRINT INPUTS TO TERMINAL
                    # =====================================

                    print("\n" + "=" * 60)
                    print("CONSTRUCTION PROJECT RISK PREDICTION")
                    print("=" * 60)
                    print("Project Type:", project_type)
                    print("Location:", location)
                    print("Start Year:", start_year, "| Month:", start_month)
                    print("End Year:", end_year, "| Month:", end_month)
                    print("Planned Cost:", planned_cost)
                    print("Planned Duration:", planned_duration)
                    print("Calculated Duration:", calculated_duration_days)
                    print("Vibration Level:", vibration_level)
                    print("Crack Width:", crack_width)
                    print("Load Bearing Capacity:", load_bearing_capacity)
                    print("Temperature:", temperature)
                    print("Humidity:", humidity)
                    print("Weather Condition:", weather_condition)
                    print("Air Quality Index:", air_quality_index)
                    print("Energy Consumption:", energy_consumption)
                    print("Material Usage:", material_usage)
                    print("Labor Hours:", labor_hours)
                    print("Equipment Utilization:", equipment_utilization)
                    print("Accident Count:", accident_count)
                    print("Image Analysis Score:", image_analysis_score)
                    print("Anomaly Detected:", anomaly_detected)
                    print("Completion Percentage:", completion_percentage)
                    print("-" * 60)


                    # =====================================
                    # 4. MAKE PREDICTION
                    # =====================================

                    try:
                        raw_prediction = model.predict(data)[0]
                        print("RAW MODEL PREDICTION:", raw_prediction)
                        prediction = str(raw_prediction)

                    except Exception as model_error:
                        error = "Some input values could not be processed. Please check your entries and try again."
                        print("\n[ERROR] Model prediction failed:", str(model_error))


                    # =====================================
                    # 5. GET CONFIDENCE AND PROBABILITIES
                    # =====================================

                    if prediction is not None:

                        try:
                            if hasattr(model, "predict_proba"):
                                probabilities = model.predict_proba(data)[0]
                                confidence = float(max(probabilities) * 100)
                                class_probabilities = [
                                    {
                                        "label": "Low Risk",
                                        "probability": round(float(probabilities[0]) * 100, 2)
                                    },
                                    {
                                        "label": "Medium Risk",
                                        "probability": round(float(probabilities[1]) * 100, 2)
                                    },
                                    {
                                        "label": "High Risk",
                                        "probability": round(float(probabilities[2]) * 100, 2)
                                    },
                                ]
                            else:
                                confidence = None
                                class_probabilities = []

                        except Exception as proba_error:
                            confidence = None
                            class_probabilities = []
                            print("\n[ERROR] Confidence calculation failed:", str(proba_error))


                    # =====================================
                    # 6. GET RECOMMENDATION
                    # =====================================

                    if prediction is not None:

                        recommendation = get_recommendation(prediction)

                        if recommendation is None:
                            error = "An unexpected result was returned. Please try again."
                            print("\n[ERROR] Unexpected prediction value:", prediction)
                            prediction = None


                    # =====================================
                    # 7. PRINT RESULT
                    # =====================================

                    if prediction is not None:
                        print("Predicted Risk Level:", prediction)
                        if confidence is not None:
                            print("Model Confidence:", round(confidence, 2), "%")
                        print("Class Probabilities:")
                        for cp in class_probabilities:
                            print(f"  {cp['label']}: {cp['probability']}%")
                        print("Recommendation Label:", recommendation["label"])
                    print("=" * 60 + "\n")


                except Exception as e:
                    error = "Something went wrong. Please try again or contact support."
                    print("\n" + "=" * 60)
                    print("[ERROR] Unexpected error in prediction pipeline:")
                    print(str(e))
                    print("=" * 60 + "\n")


    return render(
        request,
        "predictor/home.html",
        {
            "prediction": prediction,
            "confidence": confidence,
            "recommendation": recommendation,
            "class_probabilities": class_probabilities,
            "errors": errors,
            "error": error,
        }
    )