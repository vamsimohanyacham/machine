import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import argparse
import json
import os

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print(f'Classification Report:\n{report}')

def save_model(model, scaler, model_path, scaler_path):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Model saved to {model_path}")
    print(f"Scaler saved to {scaler_path}")

def predict_error(model, scaler, build_data):
    scaled_data = scaler.transform([build_data])
    prediction = model.predict(scaled_data)
    return prediction[0]

def save_prediction(prediction_result, prediction_file_path):
    try:
        os.makedirs(os.path.dirname(prediction_file_path), exist_ok=True)
        with open(prediction_file_path, 'w') as f:
            json.dump(prediction_result, f, indent=4)
        print(f"Prediction saved to {prediction_file_path}")
    except Exception as e:
        print(f"Error saving prediction: {e}")

def main():
    parser = argparse.ArgumentParser(description="Error prediction for Jenkins build logs")
    parser.add_argument('--build_duration', type=int, required=True, help='Build duration in minutes')
    parser.add_argument('--dependency_changes', type=int, required=True, help='Number of dependencies changed')
    parser.add_argument('--failed_previous_builds', type=int, required=True, help='Number of failed previous builds')
    parser.add_argument('--prediction_file', required=True, help='Path to save the prediction result')

    args = parser.parse_args()

    data = load_data('C:/ProgramData/Jenkins/.jenkins/jobs/test/workspace/scripts/build_logs.csv')
    
    X = data[['build_duration', 'dependency_changes', 'failed_previous_builds']]
    y = data['build_status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = train_model(X_train_scaled, y_train)

    evaluate_model(model, X_test_scaled, y_test)

    save_model(model, scaler, 'build_error_predictor.pkl', 'scaler.pkl')

    build_data = [args.build_duration, args.dependency_changes, args.failed_previous_builds]
    prediction = predict_error(model, scaler, build_data)

    prediction_result = {
        "build_duration": args.build_duration,
        "dependency_changes": args.dependency_changes,
        "failed_previous_builds": args.failed_previous_builds,
        "prediction": "Failure" if prediction == 1 else "Success"
    }

    save_prediction(prediction_result, args.prediction_file)

if __name__ == "__main__":
    main()
