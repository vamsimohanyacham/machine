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
//         GIT_REPO = "https://github.com/vamsimohanyacham/machine.git"  // Replace with your Git repository URL
//         GIT_BRANCH = "main"  // Replace with your target branch
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
//                     if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
//                         echo 'Creating virtual environment...'
//                         bat """
//                             python -m venv ${env.VENV_PATH}
//                         """
//                     }
                    
//                     echo 'Installing Python dependencies...'
//                     bat """
//                         call ${env.VENV_PATH}/Scripts/activate && pip install pandas scikit-learn
//                     """
//                 }
//             }
//         }

//         stage('Run ML Error Prediction') {
//             steps {
//                 echo 'Running error prediction...'

//                 script {
//                     // Run the ML prediction script and capture the output
//                     echo "Running prediction model..."
//                     bat """
//                         call ${env.VENV_PATH}/Scripts/activate && python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 > prediction_output.log 2>&1
//                     """

//                     echo "Displaying Python script output..."
//                     bat "type prediction_output.log"

//                     // Extract the latest prediction file from the log
//                     def logContent = readFile(file: "prediction_output.log")
//                     def predictionFile = logContent.find(/Prediction written to: (.*\.json)/)  // Extract the file name

//                     if (predictionFile) {
//                         predictionFile = predictionFile.replace("Prediction written to: ", "").trim()
//                         echo "✅ Using dynamically detected prediction file: ${predictionFile}"
//                     } else {
//                         echo "❌ ERROR: Could not determine the prediction file name."
//                         error("Prediction file was not generated correctly. Check 'prediction_output.log' for details.")
//                     }

//                     // Ensure the prediction file exists before displaying it
//                     if (fileExists(predictionFile)) {
//                         echo "Displaying contents of the prediction file: ${predictionFile}"
//                         bat "type \"${predictionFile}\""
//                     } else {
//                         echo "❌ ERROR: Prediction file not found at ${predictionFile}"
//                         error("Prediction file was not generated. Check 'prediction_output.log' for errors.")
//                     }

//                     // Store the detected filename in an environment variable for later use
//                     env.PREDICTION_FILE_PATH = predictionFile
//                 }
//             }
//         }

//     steps {
//         echo 'Committing and pushing updated logs to Git...'

//         script {
//             def gitUser = "vamsimohanyacham"
//             def gitEmail = "vamsimohanyacham@gmail.com"

//             bat """
//                 cd /d ${env.WORKSPACE_DIR}  && ^
//                 git config --global user.name "${gitUser}"  && ^
//                 git config --global user.email "${gitEmail}"  && ^
//                 git add "${env.PREDICTION_FILE_PATH}"  && ^
//                 git add "${env.CSV_FILE}"  && ^
//                 git commit -m "Updated prediction logs and build logs from Jenkins"  && ^
//                 git push origin ${env.GIT_BRANCH}
//             """
//         }
//     }
// }

//     }
// }



pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "D:/machinelearning"  // Root directory
        VENV_PATH = "${WORKSPACE_DIR}/venv"  // Virtual environment
        SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"  // Scripts folder
        PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"  // Prediction log folder
        CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"  // CSV file path
        PYTHON_SCRIPT = "${SCRIPT_PATH}/ml_error_prediction.py"  // ML script
        GIT_REPO = "https://github.com/vamsimohanyacham/machine.git"  // Git repository
        GIT_BRANCH = "main"  // Target branch
        PYTHON_PATH = "C:\Users\MTL1020\AppData\Local\Programs\Python\Python39\python.exe"  // Update this to match your system
    }

    stages {
        stage('Set up Python Environment') {
            steps {
                echo 'Setting up Python virtual environment and installing dependencies...'
                script {
                    dir(env.WORKSPACE_DIR) {
                        if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
                            echo 'Creating virtual environment...'
                            bat "\"${env.PYTHON_PATH}\" -m venv ${env.VENV_PATH}"
                        }

                        echo 'Upgrading pip and installing dependencies...'
                        bat """
                            call ${env.VENV_PATH}/Scripts/activate && ^
                            python -m pip install --upgrade pip && ^
                            pip install pandas scikit-learn
                        """
                    }
                }
            }
        }

        stage('Run ML Error Prediction') {
            steps {
                echo 'Running error prediction...'
                script {
                    dir(env.WORKSPACE_DIR) {
                        echo "Running prediction model..."
                        bat """
                            call ${env.VENV_PATH}/Scripts/activate && ^
                            python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 > prediction_output.log 2>&1
                        """

                        echo "Displaying Python script output..."
                        bat "type prediction_output.log"

                        if (!fileExists("prediction_output.log")) {
                            echo "❌ ERROR: prediction_output.log not found!"
                            error("Prediction script did not run correctly.")
                        }

                        def logContent = readFile(file: "prediction_output.log")
                        def predictionFileMatch = logContent =~ /Prediction written to:\s*(.*\.json)/

                        if (predictionFileMatch) {
                            env.PREDICTION_FILE_PATH = predictionFileMatch[0][1].trim()
                            echo "✅ Using dynamically detected prediction file: ${env.PREDICTION_FILE_PATH}"
                        } else {
                            echo "❌ ERROR: Could not determine the prediction file name."
                            error("Prediction file was not generated correctly. Check 'prediction_output.log' for details.")
                        }

                        if (fileExists(env.PREDICTION_FILE_PATH)) {
                            echo "Displaying contents of the prediction file: ${env.PREDICTION_FILE_PATH}"
                            bat "type \"${env.PREDICTION_FILE_PATH}\""
                        } else {
                            echo "❌ ERROR: Prediction file not found at ${env.PREDICTION_FILE_PATH}"
                            error("Prediction file was not generated. Check 'prediction_output.log' for errors.")
                        }
                    }
                }
            }
        }

        stage('Commit & Push to Git') {
            steps {
                echo 'Committing and pushing updated logs to Git...'
                script {
                    dir(env.WORKSPACE_DIR) {
                        def gitUser = "vamsimohanyacham"
                        def gitEmail = "vamsimohanyacham@gmail.com"

                        bat """
                            git config --global user.name "${gitUser}" && ^
                            git config --global user.email "${gitEmail}" && ^
                            git add "${env.PREDICTION_FILE_PATH}" && ^
                            git add "${env.CSV_FILE}" && ^
                            git commit -m "Updated prediction logs and build logs from Jenkins" && ^
                            git push origin ${env.GIT_BRANCH}
                        """
                    }
                }
            }
        }
    }
}

