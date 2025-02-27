import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Ensure the 'build_logs.csv' file exists in the correct location
csv_file_path = 'D:/machinelearning/build_logs.csv'  # Update the path if needed

# Check if the file exists
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"CSV file not found at: {csv_file_path}")

# Load the historical build data from build_logs.csv
df = pd.read_csv(csv_file_path)

# Check if necessary columns exist in the CSV file
required_columns = ['build_duration', 'dependency_changes', 'failed_previous_builds', 'build_status']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Error: Missing required columns in 'build_logs.csv'. Expected columns: {required_columns}")

# Preprocess the data: Convert build_status to numeric labels (Success = 0, Fail = 1)
df['build_status'] = df['build_status'].map({'Success': 0, 'Fail': 1})

# Define the features (X) and the target (y)
X = df[['build_duration', 'dependency_changes', 'failed_previous_builds']]
y = df['build_status']

# Split the data into training and testing sets (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict the test set results and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Print the model accuracy
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Create a directory to save the trained model if it doesn't exist
model_dir = 'D:/machinelearning/trained_models'  # Specify the correct path for your trained model folder
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Save the trained model as build_error_prediction_model.pkl
model_path = os.path.join(model_dir, 'build_error_prediction_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model saved at {model_path}")
