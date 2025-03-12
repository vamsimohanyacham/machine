pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "D:/machinelearning"
        VENV_PATH = "${WORKSPACE_DIR}/venv"
        SCRIPT_PATH = "${WORKSPACE_DIR}/scripts"
        PREDICTION_FOLDER = "${WORKSPACE_DIR}/build_log/build_logs"
        CSV_FILE = "${WORKSPACE_DIR}/build_logs.csv"
        PYTHON_SCRIPT = "${SCRIPT_PATH}/ml_error_prediction.py"
        GIT_REPO = "https://github.com/vamsimohanyacham/machine.git"
        GIT_BRANCH = "main"
        PYTHON_PATH = "C:/Users/MTL1020/AppData/Local/Programs/Python/Python39/python.exe"
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo '📝 Checking out the repository...'
                    git branch: "${env.GIT_BRANCH}", url: "${env.GIT_REPO}"
                }
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    dir(env.WORKSPACE_DIR) {
                        echo '🔍 Checking if virtual environment exists...'

                        if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
                            echo '⚠️ Virtual environment not found. Creating a new one...'
                            bat "rmdir /s /q ${env.VENV_PATH} || exit 0"
                            bat "\"${env.PYTHON_PATH}\" -m venv ${env.VENV_PATH}"
                        }

                        echo '⬆️ Upgrading pip and installing dependencies...'
                        bat """
                            call ${env.VENV_PATH}/Scripts/activate
                            call python -m pip install --upgrade pip
                            call pip install pandas scikit-learn
                        """
                    }
                }
            }
        }

        stage('Run npm build') {
            steps {
                script {
                    // Capture start time
                    def startTime = new Date().getTime()

                    // Run npm build process
                    echo "Running npm install"
                    sh 'npm install'
                    echo "Running npm build"
                    sh 'npm run build'  // Customize according to your build command

                    // Capture end time
                    def endTime = new Date().getTime()

                    // Calculate build duration in seconds
                    def buildDuration = (endTime - startTime) / 1000  // Duration in seconds
                    echo "Build Duration: ${buildDuration} seconds"
                }
            }
        }

        stage('Check Dependency Changes') {
            steps {
                script {
                    // Get the list of changes related to package.json
                    def dependencyChanges = sh(script: 'git diff --name-only HEAD~1 HEAD package.json', returnStdout: true).trim()

                    // If there are changes in package.json, count them
                    def dependencyChangesCount = dependencyChanges ? 1 : 0
                    echo "Dependency Changes: ${dependencyChangesCount}"

                    // Save the value for later use in Python script
                    env.DEPENDENCY_CHANGES = dependencyChangesCount
                }
            }
        }

        stage('Check Previous Build Status') {
            steps {
                script {
                    // Get the last build status
                    def lastBuildResult = currentBuild.previousBuild?.result

                    // Check if the previous build failed
                    def failedPreviousBuilds = (lastBuildResult == 'FAILURE') ? 1 : 0
                    echo "Failed Previous Builds: ${failedPreviousBuilds}"

                    // Save the value for later use in Python script
                    env.FAILED_PREVIOUS_BUILDS = failedPreviousBuilds
                }
            }
        }

        stage('Run ML Error Prediction') {
            steps {
                script {
                    dir(env.WORKSPACE_DIR) {
                        echo "🚀 Running prediction model..."

                        // Use the calculated values
                        def buildDuration = "${BUILD_DURATION}"
                        def dependencyChanges = "${DEPENDENCY_CHANGES}"
                        def failedPreviousBuilds = "${FAILED_PREVIOUS_BUILDS}"

                        // Run Python script with dynamic arguments
                        bat """
                            call ${env.VENV_PATH}/Scripts/activate
                            call python ${env.PYTHON_SCRIPT} --build_duration ${buildDuration} --dependency_changes ${dependencyChanges} --failed_previous_builds ${failedPreviousBuilds} > prediction_output.log 2>&1
                        """

                        echo "📜 Displaying Python script output..."
                        bat "type prediction_output.log"

                        // Check if the output log exists and the script ran successfully
                        if (!fileExists("prediction_output.log")) {
                            error("❌ ERROR: prediction_output.log not found! The script did not execute correctly.")
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for more details.'
        }
    }
}



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
