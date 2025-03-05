import os
import json
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load trained model
model_path = 'D:/machinelearning/trained_models/build_error_prediction_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Prediction function
def make_prediction(build_duration, dependency_changes, failed_previous_builds):
    input_data = pd.DataFrame([[build_duration, dependency_changes, failed_previous_builds]],
                              columns=['build_duration', 'dependency_changes', 'failed_previous_builds'])

    # Validate inputs
    if any(x is None or x < 0 for x in [build_duration, dependency_changes, failed_previous_builds]):
        raise ValueError("❌ Invalid input values: All inputs must be non-negative integers.")

    # Force failure for high-risk builds (Manual Override)
    if build_duration > 350 or dependency_changes >= 3 or failed_previous_builds > 0:
        return {
            "status": "fail",
            "message": "Potential issues detected in the build.",
            "details": [
                "Warning: Build duration is unusually long." if build_duration > 350 else "",
                "Warning: Significant dependency changes detected." if dependency_changes >= 3 else "",
                "Warning: The build has failed previously." if failed_previous_builds > 0 else ""
            ]
        }

    # Use trained model for prediction
    prediction = model.predict(input_data)[0]
    build_status = 'Success' if prediction == 0 else 'Fail'

    return {
        "status": build_status.lower(),
        "message": "No potential issues detected in the build." if build_status == 'Success' else "Potential issues detected in the build.",
        "details": []
    }

# Function to update build logs
def update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, build_status):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(columns=["build_duration", "dependency_changes", "failed_previous_builds", "build_status"])

    # Append new data
    new_data = pd.DataFrame({
        "build_duration": [build_duration],
        "dependency_changes": [dependency_changes],
        "failed_previous_builds": [failed_previous_builds],
        "build_status": [build_status]  # Store actual prediction result
    })

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(csv_file, index=False)
    print(f"✅ Build logs updated in {csv_file}")

# Function to save prediction results
def save_prediction_to_json(prediction, prediction_folder, prediction_count):
    os.makedirs(prediction_folder, exist_ok=True)
    prediction_file = os.path.join(prediction_folder, f"prediction{prediction_count}.json")

    with open(prediction_file, 'w') as f:
        json.dump(prediction, f, indent=4)

    print(f"✅ Prediction written to: {prediction_file}")

# Main function
def main():
    csv_file = 'D:/machinelearning/build_logs.csv'
    prediction_folder = 'D:/machinelearning/build_log/build_logs'

    # Check prediction count
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        prediction_count = len(df) + 1
    else:
        prediction_count = 1

    # Test Case: High-risk build (Should FAIL)
    build_duration = 200
    dependency_changes = 0
    failed_previous_builds = 0

    # Make prediction
    prediction = make_prediction(build_duration, dependency_changes, failed_previous_builds)

    # Update logs
    update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, prediction["status"])

    # Save output
    save_prediction_to_json(prediction, prediction_folder, prediction_count)

    print("✅ Prediction and historical data updated successfully.")

if __name__ == "__main__":
    main()

