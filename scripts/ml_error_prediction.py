# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# # import argparse
# # import pickle
# # import json
# # import os
# # import pandas as pd
# # from sklearn.ensemble import RandomForestClassifier

# # # Load the trained model
# # model_path = 'd:/machinelearning/trained_models/build_error_prediction_model.pkl'
# # if not os.path.exists(model_path):
# #     raise FileNotFoundError(f"Model file not found: {model_path}")

# # with open(model_path, 'rb') as f:
# #     model = pickle.load(f)

# # def make_prediction(build_duration, dependency_changes, failed_previous_builds):
# #     # Prepare the input data for the model
# #     input_data = [[build_duration, dependency_changes, failed_previous_builds]]

# #     # Ensure the input data is valid
# #     if any(x is None or x < 0 for x in input_data[0]):
# #         raise ValueError("Invalid input values: All inputs must be non-negative integers.")

# #     # Make the prediction
# #     prediction = model.predict(input_data)

# #     # Map the prediction to 'Success' or 'Fail'
# #     build_status = 'Success' if prediction[0] == 0 else 'Fail'

# #     # Prepare the response structure
# #     response = {
# #         "status": "success" if build_status == 'Success' else "fail",
# #         "message": "No potential issues detected in the build." if build_status == 'Success' else "Potential issues detected in the build.",
# #         "details": []
# #     }

# #     # Add additional details based on the model prediction and input features
# #     if build_duration > 300:
# #         response["details"].append("Warning: Build duration is unusually long.")
# #     if dependency_changes > 0:
# #         response["details"].append("Warning: Significant dependency changes detected.")
# #     if failed_previous_builds > 0:
# #         response["details"].append("Warning: The build has failed previously.")

# #     return response

# # def update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, build_status):
# #     # Check if the CSV file exists
# #     if os.path.exists(csv_file):
# #         # Read the existing CSV data
# #         df = pd.read_csv(csv_file)
# #     else:
# #         # If the file does not exist, create an empty DataFrame with appropriate column names
# #         df = pd.DataFrame(columns=["build_duration", "dependency_changes", "failed_previous_builds", "build_status"])

# #     # Create a new DataFrame with the new row
# #     # new_data = pd.DataFrame({
# #     #     "build_duration": [build_duration],
# #     #     "dependency_changes": [dependency_changes],
# #     #     "failed_previous_builds": [failed_previous_builds],
# #     #     "build_status": [build_status]
# #     # })

# #     new_data = pd.DataFrame({
# #     "build_duration": [400],
# #     "dependency_changes": [2],
# #     "failed_previous_builds": [1],
# #     "build_status": ["success"]
# # })


# #     # Concatenate the new data to the existing DataFrame
# #     df = pd.concat([df, new_data], ignore_index=True)

# #     # Save the updated CSV file
# #     df.to_csv(csv_file, index=False)
# #     print(f"Build logs updated in {csv_file}")

# # def save_prediction_to_json(prediction, prediction_folder, prediction_count):
# #     # Create the JSON file path
# #     prediction_file = os.path.join(prediction_folder, f"prediction{prediction_count}.json")
    
# #     # Write the prediction to the JSON file
# #     with open(prediction_file, 'w') as f:
# #         json.dump(prediction, f, indent=4)
    
# #     print(f"Prediction written to: {prediction_file}")

# # def main():
# #     # Path to the CSV and build logs folder
# #     csv_file = 'd:/machinelearning/build_logs.csv'
# #     prediction_folder = 'd:/machinelearning/build_log/build_logs'

# #     # Ensure the prediction folder exists
# #     if not os.path.exists(prediction_folder):
# #         os.makedirs(prediction_folder)

# #     # Check if the CSV file exists, and calculate the prediction count
# #     if os.path.exists(csv_file):
# #         df = pd.read_csv(csv_file)
# #         prediction_count = len(df) + 1  # This will determine the next prediction file name
# #     else:
# #         # If the file doesn't exist, set the prediction count to 1
# #         prediction_count = 1

# #     # Example build details (replace these with real values after build completion)
# #     build_duration = 50
# #     dependency_changes = 1
# #     failed_previous_builds = 0

# #     # Make the prediction
# #     prediction = make_prediction(build_duration, dependency_changes, failed_previous_builds)

# #     # Update the CSV file with new build data
# #     update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, prediction["status"])

# #     # Save the prediction to a new JSON file
# #     save_prediction_to_json(prediction, prediction_folder, prediction_count)

# #     print("Prediction and historical data updated successfully.")

# # if __name__ == "__main__":
# #     main()


# import os
# import json
# import pickle
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier

# # Load trained model
# model_path = 'D:/machinelearning/trained_models/build_error_prediction_model.pkl'
# if not os.path.exists(model_path):
#     raise FileNotFoundError(f"Model file not found: {model_path}")

# with open(model_path, 'rb') as f:
#     model = pickle.load(f)

# # Prediction function
# def make_prediction(build_duration, dependency_changes, failed_previous_builds):
#     input_data = pd.DataFrame([[build_duration, dependency_changes, failed_previous_builds]],
#                               columns=['build_duration', 'dependency_changes', 'failed_previous_builds'])

#     # Validate inputs
#     if any(x is None or x < 0 for x in [build_duration, dependency_changes, failed_previous_builds]):
#         raise ValueError("❌ Invalid input values: All inputs must be non-negative integers.")

#     # Force failure for high-risk builds (Manual Override)
#     if build_duration > 350 or dependency_changes >= 3 or failed_previous_builds > 0:
#         return {
#             "status": "fail",
#             "message": "Potential issues detected in the build.",
#             "details": [
#                 "Warning: Build duration is unusually long." if build_duration > 350 else "",
#                 "Warning: Significant dependency changes detected." if dependency_changes >= 3 else "",
#                 "Warning: The build has failed previously." if failed_previous_builds > 0 else ""
#             ]
#         }

#     # Use trained model for prediction
#     prediction = model.predict(input_data)[0]
#     build_status = 'Success' if prediction == 0 else 'Fail'

#     return {
#         "status": build_status.lower(),
#         "message": "No potential issues detected in the build." if build_status == 'Success' else "Potential issues detected in the build.",
#         "details": []
#     }

# # Function to update build logs
# def update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, build_status):
#     if os.path.exists(csv_file):
#         df = pd.read_csv(csv_file)
#     else:
#         df = pd.DataFrame(columns=["build_duration", "dependency_changes", "failed_previous_builds", "build_status"])

#     # Append new data
#     new_data = pd.DataFrame({
#         "build_duration": [build_duration],
#         "dependency_changes": [dependency_changes],
#         "failed_previous_builds": [failed_previous_builds],
#         "build_status": [build_status]  # Store actual prediction result
#     })

#     df = pd.concat([df, new_data], ignore_index=True)
#     df.to_csv(csv_file, index=False)
#     print(f"✅ Build logs updated in {csv_file}")

# # Function to save prediction results
# def save_prediction_to_json(prediction, prediction_folder, prediction_count):
#     os.makedirs(prediction_folder, exist_ok=True)
#     prediction_file = os.path.join(prediction_folder, f"prediction{prediction_count}.json")

#     with open(prediction_file, 'w') as f:
#         json.dump(prediction, f, indent=4)

#     print(f"✅ Prediction written to: {prediction_file}")

# # Main function
# def main():
#     csv_file = 'D:/machinelearning/build_logs.csv'
#     prediction_folder = 'D:/machinelearning/build_log/build_logs'

#     # Check prediction count
#     if os.path.exists(csv_file):
#         df = pd.read_csv(csv_file)
#         prediction_count = len(df) + 1
#     else:
#         prediction_count = 1

#     # Test Case: High-risk build (Should FAIL)
#     build_duration = 200
#     dependency_changes = 0
#     failed_previous_builds = 0

#     # Make prediction
#     prediction = make_prediction(build_duration, dependency_changes, failed_previous_builds)

#     # Update logs
#     update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, prediction["status"])

#     # Save output
#     save_prediction_to_json(prediction, prediction_folder, prediction_count)

#     print("✅ Prediction and historical data updated successfully.")

# if __name__ == "__main__":
#     main()

import os
import json
import pickle
import pandas as pd
import argparse
from sklearn.ensemble import RandomForestClassifier

# Load trained model
model_path = 'D:/machinelearning/trained_models/build_error_prediction_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Argument parser for dynamic input
parser = argparse.ArgumentParser(description="Build Error Prediction")
parser.add_argument('--build_duration', type=int, required=True, help="Duration of the build process")
parser.add_argument('--dependency_changes', type=int, required=True, help="Number of dependency changes")
parser.add_argument('--failed_previous_builds', type=int, required=True, help="Number of failed previous builds")
args = parser.parse_args()

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

    # Get the input parameters from command-line arguments
    build_duration = args.build_duration
    dependency_changes = args.dependency_changes
    failed_previous_builds = args.failed_previous_builds

    # Check prediction count
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        prediction_count = len(df) + 1
    else:
        prediction_count = 1

    # Make prediction
    prediction = make_prediction(build_duration, dependency_changes, failed_previous_builds)

    # Update logs
    update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, prediction["status"])

    # Save output
    save_prediction_to_json(prediction, prediction_folder, prediction_count)

    print("✅ Prediction and historical data updated successfully.")

if __name__ == "__main__":
    main() 


