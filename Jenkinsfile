pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "D:\\machinelearning"  // Path to your project directory (Adjust accordingly)
        VENV_PATH = "${WORKSPACE_DIR}\\venv"  // Path to your virtual environment
        MODEL_PATH = "${WORKSPACE_DIR}\\trained_models\\build_error_prediction_model.pkl"  // Path to model
        SCRIPT_PATH = "${WORKSPACE_DIR}\\scripts"  // Path to scripts folder
        LOG_FILE_PATH = "${WORKSPACE_DIR}\\build_log\\build_logs\\prediction_407.json"  // Path for prediction log
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
                    
                    // Step 2: Install necessary dependencies directly
                    echo 'Installing Python dependencies...'
                    bat """
                        ${env.VENV_PATH}\\Scripts\\activate && pip install -r ${env.SCRIPT_PATH}\\requirements.txt
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
                    // Ensure Python is available
                    echo "Checking Python version..."
                    bat """
                        ${env.VENV_PATH}\\Scripts\\activate && python --version
                    """

                    // Run the error prediction model
                    echo "Running prediction model..."
                    bat """
                        ${env.VENV_PATH}\\Scripts\\activate && python ${env.SCRIPT_PATH}\\ml_error_prediction.py --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 --prediction_file ${env.LOG_FILE_PATH}
                    """

                    // Display the contents of the prediction file
                    echo 'Displaying prediction log contents...'
                    bat "type ${env.LOG_FILE_PATH}"
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
