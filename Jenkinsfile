import os
import json
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load trained model with exception handling
try:
    model_path = 'D:/machinelearning/trained_models/build_error_prediction_model.pkl'
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print(f"Error loading model: {e}")
    raise

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
    try:
        prediction = model.predict(input_data)[0]
        build_status = 'Success' if prediction == 0 else 'Fail'
    except Exception as e:
        print(f"Error during prediction: {e}")
        raise

    return {
        "status": build_status.lower(),
        "message": "No potential issues detected in the build." if build_status == 'Success' else "Potential issues detected in the build.",
        "details": []
    }

# Function to update build logs
def update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, build_status):
    try:
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
    except Exception as e:
        print(f"Error updating build logs: {e}")
        raise

# Function to save prediction results
def save_prediction_to_json(prediction, prediction_folder, prediction_count):
    try:
        os.makedirs(prediction_folder, exist_ok=True)
        prediction_file = os.path.join(prediction_folder, f"prediction{prediction_count}.json")

        with open(prediction_file, 'w') as f:
            json.dump(prediction, f, indent=4)

        print(f"✅ Prediction written to: {prediction_file}")
    except Exception as e:
        print(f"Error saving prediction to JSON: {e}")
        raise

# Main function
def main():
    try:
        csv_file = 'D:/machinelearning/build_logs.csv'
        prediction_folder = 'D:/machinelearning/build_log/build_logs'

        # Check prediction count
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            prediction_count = len(df) + 1
        else:
            prediction_count = 1

        # Test Case: High-risk build (Should FAIL)
        build_duration = 400
        dependency_changes = 7
        failed_previous_builds = 1

        # Make prediction
        prediction = make_prediction(build_duration, dependency_changes, failed_previous_builds)

        # Update logs
        update_build_logs(csv_file, build_duration, dependency_changes, failed_previous_builds, prediction["status"])

        # Save output
        save_prediction_to_json(prediction, prediction_folder, prediction_count)

        print("✅ Prediction and historical data updated successfully.")
    except Exception as e:
        print(f"❌ Error in main execution: {e}")
        raise

if __name__ == "__main__":
    main()




// pipeline {
//     agent any

//     environment {
//         WORKSPACE_DIR = "D:/machinelearning"
//         VENV_PATH = "${WORKSPACE_DIR}/venv"
//         SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"
//         PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"
//         CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"
//         PYTHON_SCRIPT = "${SCRIPT_PATH}/ml_error_prediction.py"
//         GIT_REPO = "https://github.com/vamsimohanyacham/machine.git"
//         GIT_BRANCH = "main"
//         PYTHON_PATH = "C:/Users/MTL1020/AppData/Local/Programs/Python/Python39/python.exe"
//     }

//     stages {
//         stage('Set up Python Environment') {
//             steps {
//                 script {
//                     dir(env.WORKSPACE_DIR) {
//                         echo '🔍 Checking if virtual environment exists...'

//                         if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
//                             echo '⚠️ Virtual environment not found. Creating a new one...'
//                             bat "rmdir /s /q ${env.VENV_PATH} || exit 0"
//                             bat "\"${env.PYTHON_PATH}\" -m venv ${env.VENV_PATH}"
//                         }

//                         echo '⬆️ Upgrading pip and installing dependencies...'
//                         bat """
//                             call ${env.VENV_PATH}/Scripts/activate
//                             call python -m pip install --upgrade pip
//                             call pip install pandas scikit-learn
//                         """
//                     }
//                 }
//             }
//         }

//         stage('Run ML Error Prediction') {
//     steps {
//         script {
//             dir(env.WORKSPACE_DIR) {
//                 echo "🚀 Running prediction model..."
//                 bat """
//                     call ${env.VENV_PATH}/Scripts/activate
//                     call python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 > prediction_output.log 2>&1
//                 """

//                 echo "📜 Displaying Python script output..."
//                 bat "type prediction_output.log"

//                 if (!fileExists("prediction_output.log")) {
//                     error("❌ ERROR: prediction_output.log not found! The script did not execute correctly.")
//                 }
//             }
//         }
//     }
// }


//     }

//    post {
//     always {
//         echo 'Cleaning up...'
//         // No need to deactivate the virtual environment explicitly on Windows
//         echo 'Virtual environment will be deactivated automatically on Windows.'
//     }
//     success {
//         echo '✅ Pipeline completed successfully!'
//     }
//     failure {
//         echo '❌ Pipeline failed. Check logs for more details.'
//     }
// }

// } 

// pipeline {
//     agent any

//     environment {
//         WORKSPACE_DIR = "D:/machinelearning"
//         VENV_PATH = "${WORKSPACE_DIR}/venv"
//         SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"
//         PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"
//         CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"
//         PYTHON_SCRIPT = "${SCRIPT_PATH}/ml_error_prediction.py"
//         GIT_REPO = "https://github.com/vamsimohanyacham/machine.git"
//         GIT_BRANCH = "main"
//         PYTHON_PATH = "C:/Users/MTL1020/AppData/Local/Programs/Python/Python39/python.exe"
//     }

//     parameters {
//         string(name: 'build_duration', defaultValue: '300', description: 'Build Duration (in seconds)')
//         string(name: 'dependency_changes', defaultValue: '0', description: 'Number of Dependency Changes')
//         string(name: 'failed_previous_builds', defaultValue: '0', description: 'Number of Failed Previous Builds')
//     }

//     stages {
//         stage('Set up Python Environment') {
//             steps {
//                 script {
//                     dir(env.WORKSPACE_DIR) {
//                         echo '🔍 Checking if virtual environment exists...'

//                         if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
//                             echo '⚠️ Virtual environment not found. Creating a new one...'
//                             bat "rmdir /s /q ${env.VENV_PATH} || exit 0"
//                             bat "\"${env.PYTHON_PATH}\" -m venv ${env.VENV_PATH}"
//                         }

//                         echo '⬆️ Upgrading pip and installing dependencies...'
//                         bat """
//                             call ${env.VENV_PATH}/Scripts/activate
//                             call python -m pip install --upgrade pip
//                             call pip install pandas scikit-learn
//                         """
//                     }
//                 }
//             }
//         }

//         stage('Clone Git Repository') {
//             steps {
//                 script {
//                     echo '🔄 Cloning Git repository...'
//                     git branch: 'main', url: 'https://github.com/vamsimohanyacham/machine.git'
//                 }
//             }
//         }

//         stage('Run ML Error Prediction') {
//             steps {
//                 script {
//                     echo "🚀 Running prediction model with dynamic input values..."

//                     dir(env.WORKSPACE_DIR) {
//                         bat """
//                             call ${env.VENV_PATH}/Scripts/activate
//                             call python ${env.PYTHON_SCRIPT} --build_duration ${params.build_duration} --dependency_changes ${params.dependency_changes} --failed_previous_builds ${params.failed_previous_builds} > prediction_output.log 2>&1
//                         """

//                         echo "📜 Displaying Python script output..."
//                         bat "type prediction_output.log"

//                         if (!fileExists("prediction_output.log")) {
//                             error("❌ ERROR: prediction_output.log not found! The script did not execute correctly.")
//                         }
//                     }
//                 }
//             }
//         }

//         stage('Save Prediction Result') {
//             steps {
//                 script {
//                     echo '💾 Saving prediction results...'

//                     dir(env.PREDICTION_FOLDER) {
//                         def predictionCount = 1
//                         // Check if the CSV file exists and determine the prediction count
//                         if (fileExists(env.CSV_FILE)) {
//                             def df = readCSV(file: env.CSV_FILE)
//                             predictionCount = df.size() + 1
//                         }

//                         def predictionFile = "prediction${predictionCount}.json"
//                         // Load the generated prediction from the log or an existing file
//                         def prediction = readJSON file: 'prediction_output.log'

//                         // Save the prediction result
//                         writeJSON file: predictionFile, json: prediction, pretty: true
//                         echo "✅ Prediction saved to: ${predictionFile}"
//                     }
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             echo 'Cleaning up...'
//             // No need to deactivate the virtual environment explicitly on Windows
//             echo 'Virtual environment will be deactivated automatically on Windows.'
//         }

//         success {
//             echo '✅ Pipeline completed successfully!'
//         }

//         failure {
//             echo '❌ Pipeline failed. Check logs for more details.'
//         }
//     }
// }
