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
//                         if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
//                             echo 'Creating virtual environment...'
//                             bat "rmdir /s /q ${env.VENV_PATH} || exit 0"
//                             bat "\"${env.PYTHON_PATH}\" -m venv ${env.VENV_PATH}"
//                         }

//                         echo 'Upgrading pip and installing dependencies...'
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
//             steps {
//                 script {
//                     dir(env.WORKSPACE_DIR) {
//                         echo "Running prediction model..."
//                         bat """
//                             call ${env.VENV_PATH}/Scripts/activate
//                             call python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 > prediction_output.log 2>&1
//                         """

//                         echo "Displaying Python script output..."
//                         bat "type prediction_output.log"

//                         if (!fileExists("prediction_output.log")) {
//                             error("❌ ERROR: prediction_output.log not found! The script did not execute correctly.")
//                         }

//                         // Extract the prediction file path from the log
//                         def logContent = readFile(file: "prediction_output.log")
//                         def predictionFilePath = ""
//                         def predictionFileMatch = (logContent =~ /Prediction written to:\s*(.*\.json)/)

//                         if (predictionFileMatch.find()) {
//                             predictionFilePath = predictionFileMatch.group(1).trim().replace("\\", "/")
//                             echo "✅ Prediction file detected: ${predictionFilePath}"
//                         } else {
//                             error("❌ ERROR: Could not extract prediction file name. Check 'prediction_output.log'.")
//                         }

//                         // ✅ Debugging: Print file path before checking existence
//                         echo "🔍 Checking if prediction file exists at: ${predictionFilePath}"

//                         // ✅ Normalize & Convert Path
//                         if (!predictionFilePath.startsWith("D:/")) {
//                             predictionFilePath = "D:/machinelearning/build_log/build_logs/" + predictionFilePath
//                         }

//                         // ✅ Print Directory Contents (Debugging)
//                         echo "📂 Listing all files in ${env.PREDICTION_FOLDER}:"
//                         bat "dir /B \"${env.PREDICTION_FOLDER}\""

//                         // ✅ Wait for File Creation
//                         sleep(time: 5, unit: 'SECONDS')

//                         // ✅ Ensure file path is not empty
//                         if (predictionFilePath == null || predictionFilePath.trim().isEmpty()) {
//                             error("❌ ERROR: Extracted prediction file path is empty!")
//                         }

//                         // ✅ Check if File Exists
//                         if (fileExists(predictionFilePath)) {
//                             echo "✅ Verified: Prediction file exists at ${predictionFilePath}."
//                             env.PREDICTION_FILE_PATH = "${predictionFilePath}"
//                         } else {
//                             error("❌ ERROR: Prediction file **still** not found at ${predictionFilePath}.")
//                         }
//                     }
//                 }
//             }
//         }

//         stage('Commit & Push to Git') {
//             steps {
//                 script {
//                     dir(env.WORKSPACE_DIR) {
//                         def gitUser = "vamsimohanyacham"
//                         def gitEmail = "vamsimohanyacham@gmail.com"

//                         // ✅ Prevent Git from Asking for Credentials
//                         bat """
//                             git config --global user.name "${gitUser}"
//                             git config --global user.email "${gitEmail}"
//                             git config --global credential.helper store
//                         """

//                         // ✅ Ensure files exist before adding to Git
//                         if (fileExists(env.PREDICTION_FILE_PATH)) {
//                             echo "✅ Adding prediction file to Git: ${env.PREDICTION_FILE_PATH}"
//                             bat "git add \"${env.PREDICTION_FILE_PATH}\""
//                         } else {
//                             error("❌ ERROR: Prediction file does not exist. Cannot commit.")
//                         }

//                         if (fileExists(env.CSV_FILE)) {
//                             echo "✅ Adding CSV file to Git: ${env.CSV_FILE}"
//                             bat "git add \"${env.CSV_FILE}\""
//                         } else {
//                             echo "⚠️ WARNING: CSV file not found, skipping commit."
//                         }

//                         // ✅ Sleep to Avoid Git Lock Issues
//                         echo "⏳ Waiting before pushing to Git..."
//                         sleep(time: 2, unit: 'SECONDS')

//                         // ✅ Ensure a commit happens only if there are changes
//                         bat """
//                             git diff --cached --exit-code || (
//                                 git commit -m "Updated prediction logs and build logs from Jenkins"
//                                 git push origin ${env.GIT_BRANCH}
//                             )
//                         """
//                     }
//                 }
//             }
//         }
//     }
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
//             steps {
//                 script {
//                     dir(env.WORKSPACE_DIR) {
//                         echo "🚀 Running prediction model..."
//                         bat """
//                             call ${env.VENV_PATH}/Scripts/activate
//                             call python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 > prediction_output.log 2>&1
//                         """

//                         echo "📜 Displaying Python script output..."
//                         bat "type prediction_output.log"

//                         if (!fileExists("prediction_output.log")) {
//                             error("❌ ERROR: prediction_output.log not found! The script did not execute correctly.")
//                         }

//                         // Extract the prediction file path from the log
//                         def logContent = readFile(file: "prediction_output.log")
//                         def predictionFilePath = ""

//                         def predictionFileMatch = (logContent =~ /Prediction written to:\s*(.*\.json)/)

//                         if (predictionFileMatch.find()) {
//                             predictionFilePath = predictionFileMatch[0][1].trim()  // ✅ Extract only the filename as a string
//                             echo "✅ Prediction file detected: ${predictionFilePath}"
//                         } else {
//                             error("❌ ERROR: Could not extract prediction file name. Check 'prediction_output.log'.")
//                         }

//                         // ✅ Normalize & Convert Path
//                         if (!predictionFilePath.startsWith("D:/")) {
//                             predictionFilePath = "D:/machinelearning/build_log/build_logs/" + predictionFilePath
//                         }

//                         // ✅ Debugging: Print Directory Contents
//                         echo "📂 Listing all files in ${env.PREDICTION_FOLDER}:"
//                         bat "dir /B \"${env.PREDICTION_FOLDER}\""

//                         // ✅ Wait for File Creation
//                         sleep(time: 5, unit: 'SECONDS')

//                         // ✅ Ensure file path is not empty
//                         if (predictionFilePath == null || predictionFilePath.trim().isEmpty()) {
//                             error("❌ ERROR: Extracted prediction file path is empty!")
//                         }

//                         // ✅ Check if File Exists
//                         if (fileExists(predictionFilePath)) {
//                             echo "✅ Verified: Prediction file exists at ${predictionFilePath}."
//                             env.PREDICTION_FILE_PATH = predictionFilePath
//                         } else {
//                             error("❌ ERROR: Prediction file **still** not found at ${predictionFilePath}.")
//                         }
//                     }
//                 }
//             }
//         }

//         // stage('Commit & Push to Git') {
//         //     steps {
//         //         script {
//         //             dir(env.WORKSPACE_DIR) {
//         //                 def gitUser = "vamsimohanyacham"
//         //                 def gitEmail = "vamsimohanyacham@gmail.com"

//         //                 // ✅ Prevent Git from Asking for Credentials
//         //                 bat """
//         //                     git config --global user.name "${gitUser}"
//         //                     git config --global user.email "${gitEmail}"
//         //                     git config --global credential.helper store
//         //                 """

//         //                 // ✅ Ensure files exist before adding to Git
//         //                 if (fileExists(env.PREDICTION_FILE_PATH)) {
//         //                     echo "✅ Adding prediction file to Git: ${env.PREDICTION_FILE_PATH}"
//         //                     bat "git add \"${env.PREDICTION_FILE_PATH}\""
//         //                 } else {
//         //                     error("❌ ERROR: Prediction file does not exist. Cannot commit.")
//         //                 }

//         //                 if (fileExists(env.CSV_FILE)) {
//         //                     echo "✅ Adding CSV file to Git: ${env.CSV_FILE}"
//         //                     bat "git add \"${env.CSV_FILE}\""
//         //                 } else {
//         //                     echo "⚠️ WARNING: CSV file not found, skipping commit."
//         //                 }

//         //                 // ✅ Sleep to Avoid Git Lock Issues
//         //                 echo "⏳ Waiting before pushing to Git..."
//         //                 sleep(time: 2, unit: 'SECONDS')

//         //                 // ✅ Ensure a commit happens only if there are changes
//         //                 bat """
//         //                     git diff --cached --exit-code || (
//         //                         git commit -m "Updated prediction logs and build logs from Jenkins"
//         //                         git push origin ${env.GIT_BRANCH}
//         //                     )
//         //                 """
//         //             }
//         //         }
//         //     }
//         // }
//     }
// }

pipeline {
    agent any  // This allows the pipeline to run on any available node.

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
        GIT_CREDENTIALS_ID = "githubcred"  // Replace with actual credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Cloning the Git repository...'
                    deleteDir() // Clean the workspace before cloning the repository
                    checkout([ 
                        $class: 'GitSCM', 
                        branches: [[name: '*/main']], 
                        userRemoteConfigs: [[
                            url: env.GIT_REPO, 
                            credentialsId: env.GIT_CREDENTIALS_ID
                        ]]
                    ])
                }
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    echo '🔍 Checking if virtual environment exists...'
                    dir(env.WORKSPACE_DIR) {
                        // Check if virtual environment exists, if not, create it.
                        if (!fileExists("${env.VENV_PATH}/Scripts/activate")) {
                            echo '⚠️ Virtual environment not found. Creating a new one...'
                            bat "rmdir /s /q ${env.VENV_PATH} || exit 0"  // Delete existing env if present
                            bat "\"${env.PYTHON_PATH}\" -m venv ${env.VENV_PATH}"  // Create new venv
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

        stage('Run ML Error Prediction') {
            steps {
                script {
                    echo "🚀 Running prediction model..."
                    dir(env.WORKSPACE_DIR) {
                        // Run the Python script and capture the output in a log file
                        bat """
                            call ${env.VENV_PATH}/Scripts/activate
                            call python ${env.PYTHON_SCRIPT} --build_duration 300 --dependency_changes 0 --failed_previous_builds 0 > prediction_output.log 2>&1
                        """

                        echo "📜 Displaying Python script output..."
                        bat "type prediction_output.log"  // Display log file content for debugging

                        // Check if log file was generated
                        if (!fileExists("prediction_output.log")) {
                            error("❌ ERROR: prediction_output.log not found! The script did not execute correctly.")
                        }

                        // Extract the prediction file path from the log file content
                        def logContent = readFile(file: "prediction_output.log")
                        def predictionFilePath = extractPredictionFilePath(logContent)  // Use the @NonCPS method to handle regex

                        // Ensure the prediction file path is not empty
                        if (predictionFilePath == null || predictionFilePath.trim().isEmpty()) {
                            error("❌ ERROR: Extracted prediction file path is empty!")
                        }

                        // Normalize & Convert Path if necessary
                        if (!predictionFilePath.startsWith("D:/")) {
                            predictionFilePath = "D:/machinelearning/build_log/build_logs/" + predictionFilePath
                        }

                        // Debugging: Print the directory contents
                        echo "📂 Listing all files in ${env.PREDICTION_FOLDER}:"
                        bat "dir /B \"${env.PREDICTION_FOLDER}\""

                        // Wait for the file to be created if necessary
                        sleep(time: 5, unit: 'SECONDS')

                        // Ensure the file exists before proceeding
                        if (fileExists(predictionFilePath)) {
                            echo "✅ Verified: Prediction file exists at ${predictionFilePath}."
                            env.PREDICTION_FILE_PATH = predictionFilePath  // Set the path to an environment variable
                        } else {
                            error("❌ ERROR: Prediction file **still** not found at ${predictionFilePath}.")
                        }
                    }
                }
            }
        }

        // Uncomment and modify this section if you want to push changes to the Git repository
        /*
        stage('Push Changes to Git') {
            steps {
                script {
                    echo '📤 Pushing changes to Git repository...'
                    bat """
                        git add .
                        git commit -m "Update model prediction results"
                        git push origin main
                    """
                }
            }
        }
        */
    }

    post {
        always {
            echo 'Cleaning up...'
            // Clean up if necessary, like deactivating the virtual environment or removing temp files
            bat "deactivate || exit 0"  // Deactivate virtual environment if still active
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for more details.'
        }
    }
}

@NonCPS
def extractPredictionFilePath(String logContent) {
    // Extract the prediction file path from the log content using regex
    def predictionFileMatch = (logContent =~ /Prediction written to:\s*(.*\.json)/)
    if (predictionFileMatch.find()) {
        return predictionFileMatch[0][1].trim()  // Return the file path as a string
    }
    return null  // Return null if no match is found
}

