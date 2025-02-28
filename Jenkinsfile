pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "d:/machinelearning"  // Project root directory
        VENV_PATH = "${WORKSPACE_DIR}/venv"  // Virtual environment path
        MODEL_PATH = "${WORKSPACE_DIR}/trained_models/build_error_prediction_model.pkl"  // Model path
        SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"  // Path to scripts folder
        PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"  // Prediction log folder
        CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"  // CSV file path
        PYTHON_SCRIPT = "${SCRIPT_PATH}/ml_error_prediction.py"  // Path to Python script
        GIT_REPO = "https://github.com/vamsimohanyacham/machine.git"  // Replace with your Git repository URL
        GIT_BRANCH = "main"  // Replace with your target branch
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
                    if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
                        echo 'Creating virtual environment...'
                        bat """
                            python -m venv ${env.VENV_PATH}
                        """
                    }
                    
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
                    def predictionFile = "prediction54.json"
                    def predictionFilePath = "${env.PREDICTION_FOLDER}/${predictionFile}"

                    echo "Checking Python version and forcing UTF-8 encoding..."
                    bat """
                        chcp 65001
                        call ${env.VENV_PATH}/Scripts/activate && python --version
                    """

                    echo "Running prediction model..."
                    bat """
                        call ${env.VENV_PATH}/Scripts/activate && python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 --prediction_file ${predictionFilePath} > prediction_output.log 2>&1
                    """

                    echo "Displaying Python script output..."
                    bat "type prediction_output.log"

                    if (fileExists(predictionFilePath)) {
                        echo "Displaying contents of the prediction file: ${predictionFilePath}"
                        bat "type \"${predictionFilePath}\""
                    } else {
                        echo "❌ ERROR: Prediction file not found at ${predictionFilePath}"
                        error("Prediction file was not generated. Check 'prediction_output.log' for errors.")
                    }
                }
            }
        }

        stage('Commit & Push to Git') {
            steps {
                echo 'Committing and pushing updated logs to Git...'

                script {
                    def gitUser = "vamsimohanyacham"  // Set your Git username
                    def gitEmail = "vamsimohanyacham@gmail.com"  // Set your Git email

                    bat """
                        cd ${env.WORKSPACE_DIR}
                        git config --global user.name "${gitUser}"
                        git config --global user.email "${gitEmail}"
                        git add "${env.PREDICTION_FOLDER}/*.json"
                        git add "${env.CSV_FILE}"
                        git commit -m "Updated prediction logs and build logs from Jenkins"
                        git push origin ${env.GIT_BRANCH}
                    """
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



// pipeline {
//     agent any

//     environment {
//         WORKSPACE_DIR = "d:/machinelearning"  // Project root directory
//         VENV_PATH = "${WORKSPACE_DIR}/venv"  // Virtual environment path
//         MODEL_PATH = "${WORKSPACE_DIR}/trained_models/build_error_prediction_model.pkl"  // Model path
//         SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"  // Path to scripts folder
//         PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"  // Prediction log folder
//         CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"  // CSV file path
//         PYTHON_SCRIPT = "${SCRIPT_PATH}/ml_error_prediction.py"  // Path to Python script
//     }

//     stages {
//         stage('Checkout SCM') {
//             steps {
//                 echo 'Checking out the SCM'
//                 checkout scm
//             }
//         }

//         stage('Set up Python Environment') {
//             steps {
//                 echo 'Setting up Python virtual environment and installing dependencies...'
//                 script {
//                     // Ensure virtual environment exists
//                     if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
//                         echo 'Creating virtual environment...'
//                         bat """
//                             python -m venv ${env.VENV_PATH}
//                         """
//                     }
                    
//                     // Install required dependencies
//                     echo 'Installing Python dependencies...'
//                     bat """
//                         call ${env.VENV_PATH}/Scripts/activate && pip install pandas scikit-learn
//                     """
//                 }
//             }
//         }

//         stage('Fix Python Encoding Issue') {
//             steps {
//                 echo 'Modifying Python script to ensure UTF-8 output...'
//                 script {
//                     def encodingFix = "import sys\nsys.stdout.reconfigure(encoding='utf-8')\n"
//                     def scriptContent = readFile(file: env.PYTHON_SCRIPT)
                    
//                     if (!scriptContent.contains("sys.stdout.reconfigure")) {
//                         scriptContent = encodingFix + scriptContent
//                         writeFile(file: env.PYTHON_SCRIPT, text: scriptContent)
//                         echo "UTF-8 encoding fix added to ml_error_prediction.py"
//                     } else {
//                         echo "UTF-8 encoding fix already present in ml_error_prediction.py"
//                     }
//                 }
//             }
//         }

//         stage('Train Model') {
//             steps {
//                 echo 'Training the model...'

//                 script {
//                     if (!fileExists("${env.MODEL_PATH}")) {
//                         echo 'Training model...'
//                         bat """
//                             call ${env.VENV_PATH}/Scripts/activate && python ${env.SCRIPT_PATH}/train_model.py
//                         """
//                     } else {
//                         echo 'Model already exists. Skipping training.'
//                     }
//                 }
//             }
//         }

//         stage('Run ML Error Prediction') {
//             steps {
//                 echo 'Running error prediction...'

//                 script {
//                     // Determine prediction count from CSV file
//                     def prediction_count = 1
//                     if (fileExists("${env.CSV_FILE}")) {
//                         def csvContent = readFile(file: "${env.CSV_FILE}")
//                         def lines = csvContent.split("\n")
//                         prediction_count = lines.size() + 1
//                     }

//                     // Define prediction file
//                     def predictionFile = "prediction54.json"
//                     def predictionFilePath = "${env.PREDICTION_FOLDER}/${predictionFile}"

//                     // Ensure Python is available and force UTF-8 encoding in Windows
//                     echo "Checking Python version and forcing UTF-8 encoding..."
//                     bat """
//                         chcp 65001
//                         call ${env.VENV_PATH}/Scripts/activate && python --version
//                     """

//                     // Run the ML prediction script
//                     echo "Running prediction model..."
//                     bat """
//                         call ${env.VENV_PATH}/Scripts/activate && python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 --prediction_file ${predictionFilePath}
//                     """

//                     // Ensure the prediction file exists before displaying it
//                     if (fileExists(predictionFilePath)) {
//                         echo "Displaying contents of the prediction file: ${predictionFilePath}"
//                         bat """
//                             type "${predictionFilePath}"
//                         """
//                     } else {
//                         echo "❌ Error: Prediction file not found at ${predictionFilePath}"
//                         error("Prediction file was not generated. Check script execution logs.")
//                     }
//                 }
//             }
//         }

//         stage('Post Build Actions') {
//             steps {
//                 echo 'Build Status: SUCCESS'
//                 script {
//                     def buildLog = "${env.WORKSPACE_DIR}/build_log/build_logs/build_${env.BUILD_ID}.log"
//                     if (fileExists(buildLog)) {
//                         echo "Displaying build log contents..."
//                         bat "type \"${buildLog}\""
//                     } else {
//                         echo "Build log not found: ${buildLog}"
//                     }
//                 }
//             }
//         }
//     }
// }

