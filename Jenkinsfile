pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "D:\\machinelearning"  // Path to your project directory (Adjust accordingly)
        VENV_PATH = "${WORKSPACE_DIR}\\venv"  // Path to your virtual environment
        MODEL_PATH = "${WORKSPACE_DIR}\\trained_models\\build_error_prediction_model.pkl"  // Path to model
        SCRIPT_PATH = "${WORKSPACE_DIR}\\scripts"  // Path to scripts folder
        PREDICTION_FOLDER = "${WORKSPACE_DIR}\\build_log\\build_logs"  // Path for prediction log
        CSV_FILE = "${WORKSPACE_DIR}\\build_logs.csv"  // Path to the CSV file
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Checking out the SCM'
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo 'Setting up Python virtual environment and installing dependencies...'
                script {
                    // Step 1: Check if virtual environment exists, create if not
                    if (!fileExists("${env.VENV_PATH}\\Scripts\\activate")) {
                        echo 'Creating virtual environment...'
                        bat """
                            python -m venv ${env.VENV_PATH}
                        """
                    }
                    
                    // Step 2: Install necessary dependencies manually
                    echo 'Installing Python dependencies...'
                    bat """
                        ${env.VENV_PATH}\\Scripts\\activate && pip install pandas scikit-learn
                    """
                }
            }
        }

        stage('Train Model') {
            steps {
                echo 'Training the model...'

                script {
                    // Step 1: Check if model already exists, if not train the model
                    if (!fileExists("${env.MODEL_PATH}")) {
                        echo 'Training model...'
                        bat """
                            ${env.VENV_PATH}\\Scripts\\activate && python ${env.SCRIPT_PATH}\\train_model.py
                        """
                    } else {
                        echo 'Model already exists. Skipping training.'
                    }
                }
            }
        }

        stage('Run ML Error Prediction') {
            steps {
                echo 'Running error prediction...'

                script {
                    // Get the next prediction count
                    def prediction_count = 1
                    if (fileExists("${env.CSV_FILE}")) {
                        def df = readCSV file: "${env.CSV_FILE}"
                        prediction_count = df.size() + 1
                    }

                    // Define prediction file name dynamically
                    def predictionFile = "prediction${prediction_count}.json"

                    // Ensure Python is available
                    echo "Checking Python version..."
                    bat """
                        ${env.VENV_PATH}\\Scripts\\activate && python --version
                    """

                    // Run the error prediction model and save to dynamically named file
                    echo "Running prediction model..."
                    bat """
                        ${env.VENV_PATH}\\Scripts\\activate && python ${env.SCRIPT_PATH}\\ml_error_prediction.py --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 --prediction_file ${env.PREDICTION_FOLDER}\\${predictionFile}
                    """

                    // Display the contents of the prediction file
                    echo "Displaying prediction log contents..."
                    bat "type ${env.PREDICTION_FOLDER}\\${predictionFile}"
                }
            }
        }

        stage('Post Build Actions') {
            steps {
                echo 'Build Status: SUCCESS'
                script {
                    echo "Build log contents:"
                    // Output any relevant logs if needed
                    bat "type ${env.WORKSPACE_DIR}\\build_log\\build_logs\\build_${env.BUILD_ID}.log"
                }
            }
        }
    }
}
