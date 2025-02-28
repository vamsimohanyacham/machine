pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "d:/machinelearning"  // Base project directory
        VENV_PATH = "${WORKSPACE_DIR}/venv"  // Virtual environment path
        MODEL_PATH = "${WORKSPACE_DIR}/trained_models/build_error_prediction_model.pkl"  // Model path
        SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"  // Scripts folder
        PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"  // Prediction log folder
        CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"  // CSV file path
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
                    // Ensure virtual environment exists
                    if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
                        echo 'Creating virtual environment...'
                        bat """
                            python -m venv ${env.VENV_PATH}
                        """
                    }
                    
                    // Install required dependencies
                    echo 'Installing Python dependencies...'
                    bat """
                        call ${env.VENV_PATH}/Scripts/activate && pip install pandas scikit-learn
                    """
                }
            }
        }

        stage('Train Model') {
            steps {
                echo 'Training the model...'

                script {
                    if (!fileExists("${env.MODEL_PATH}")) {
                        echo 'Training model...'
                        bat """
                            call ${env.VENV_PATH}/Scripts/activate && python ${env.SCRIPT_PATH}/train_model.py
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
                    // Determine prediction count from CSV file
                    def prediction_count = 1
                    if (fileExists("${env.CSV_FILE}")) {
                        def csvContent = readFile(file: "${env.CSV_FILE}")
                        def lines = csvContent.split("\n")
                        prediction_count = lines.size() + 1
                    }

                    // Define prediction file
                    def predictionFile = "prediction54.json"
                    def predictionFilePath = "${env.PREDICTION_FOLDER}/${predictionFile}"

                    // Ensure Python is available
                    echo "Checking Python version..."
                    bat """
                        call ${env.VENV_PATH}/Scripts/activate && python --version
                    """

                    // Run the ML prediction script
                    echo "Running prediction model..."
                    bat """
                        call ${env.VENV_PATH}/Scripts/activate && python ${env.SCRIPT_PATH}/ml_error_prediction.py --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 --prediction_file ${predictionFilePath}
                    """

                    // Ensure the prediction file exists before displaying it
                    if (fileExists(predictionFilePath)) {
                        echo "Displaying contents of the prediction file: ${predictionFilePath}"
                        bat """
                            type "${predictionFilePath}"
                        """
                    } else {
                        echo "Error: Prediction file not found at ${predictionFilePath}"
                        error("Prediction file was not generated. Check script execution logs.")
                    }
                }
            }
        }

        stage('Post Build Actions') {
            steps {
                echo 'Build Status: SUCCESS'
                script {
                    def buildLog = "${env.WORKSPACE_DIR}/build_log/build_logs/build_${env.BUILD_ID}.log"
                    if (fileExists(buildLog)) {
                        echo "Displaying build log contents..."
                        bat "type \"${buildLog}\""
                    } else {
                        echo "Build log not found: ${buildLog}"
                    }
                }
            }
        }
    }
}
