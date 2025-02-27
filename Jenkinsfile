// pipeline {
//     agent any

//     environment {
//         BUILD_DIR = 'build_log\\build_logs'  // Use double-backslashes for Windows path
//         PYTHON_PATH = 'C:\\Users\\MTL1020\\AppData\\Local\\Programs\\Python\\Python39\\'  // Path to Python installation
//         BUILD_DURATION = '300'  // Placeholder for build duration (in seconds)
//         DEPENDENCY_CHANGES = '0'  // 0 represents 'false'
//         FAILED_PREVIOUS_BUILDS = '0'  // Placeholder for number of failed previous builds
//         CSV_FILE = 'C:\\ProgramData\\Jenkins\\.jenkins\\jobs\\test\\workspace\\scripts\\build_logs.csv'  // Path to the CSV file where build data is stored
//         GIT_USER = 'vamsimohanyacham'  // Replace with your GitHub username
//         GIT_EMAIL = 'vamsimohanyacham@gmail.com'  // Replace with your email address
//     }

//     stages {
//         stage('Checkout SCM') {
//             steps {
//                 echo 'Checkout SCM'
//                 checkout scm
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 echo 'Installing npm dependencies...'
//                 bat 'npm install'  // Install npm dependencies
//             }
//         }

//         stage('Build') {
//             steps {
//                 echo 'Building the project...'

//                 script {
//                     def buildLogsDir = "${env.WORKSPACE}\\${BUILD_DIR}"
//                     if (!fileExists(buildLogsDir)) {
//                         echo "Creating directory: ${buildLogsDir}"
//                         bat "mkdir \"${buildLogsDir}\""
//                     }
//                 }

//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     def currentDate = new Date().format('yyyy-MM-dd HH:mm:ss')
//                     echo "Starting build at: ${currentDate}"
//                     bat "echo 'Starting build at: ${currentDate}' > \"${logFile}\""
//                     bat "npm run build >> \"${logFile}\" 2>&1"
//                     echo "Build log written to: ${logFile}"
//                 }
//             }
//         }

//         stage('Run Error Prediction') {
//             steps {
//                 echo 'Running error prediction...'

//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     def predictionFile = "${env.WORKSPACE}\\${BUILD_DIR}\\prediction_${env.BUILD_ID}.json"

//                     echo "Log file: ${logFile}"
//                     echo "Prediction result file: ${predictionFile}"

//                     // Ensure Python is available
//                     bat "\"C:\\Users\\MTL1020\\AppData\\Local\\Programs\\Python\\Python39\\python.exe\" --version"  // Check Python version

//                     // Run error prediction
//                     bat "\"C:\\Users\\MTL1020\\AppData\\Local\\Programs\\Python\\Python39\\python.exe\" scripts\\error_prediction.py --build_duration ${env.BUILD_DURATION} --dependency_changes ${env.DEPENDENCY_CHANGES} --failed_previous_builds ${env.FAILED_PREVIOUS_BUILDS} --prediction_file \"${predictionFile}\""

//                     // Display the contents of the prediction file
//                     bat "type \"${predictionFile}\""
//                 }
//             }
//         }

//         stage('Post Build Actions') {
//             steps {
//                 echo 'Build Status: SUCCESS'
//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     echo "Log file contents:"
//                     bat "type \"${logFile}\""
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             // Append build data to the CSV after each build
//             echo "Appending build data to CSV file..."
//             script {
//                 // Verify if the script exists in the correct directory
//                 def appendCsvCommand = """
//                     echo "Workspace path: ${env.WORKSPACE}"
//                     echo "Checking if append_to_csv.py exists..."
//                     dir "${env.WORKSPACE}\\scripts\\append_to_csv.py"  // Use correct syntax for Windows path
//                     if exist "${env.WORKSPACE}\\scripts\\append_to_csv.py" (
//                         echo "Running Python script to append to CSV..."
//                         \"${env.PYTHON_PATH}python.exe\" "${env.WORKSPACE}\\scripts\\append_to_csv.py" ${env.BUILD_DURATION} ${env.DEPENDENCY_CHANGES} ${env.FAILED_PREVIOUS_BUILDS} "${env.CSV_FILE}"
//                     ) else (
//                         echo "Error: append_to_csv.py not found!"
//                     )
//                 """
//                 bat appendCsvCommand
//             }

//             // Commit and push the changes to GitHub after appending to CSV
//             echo "Committing and pushing changes to GitHub..."
//             script {
//                 def gitCommitMessage = "Updated build log after build #${env.BUILD_ID}"
                
//                 // Configure Git
//                 bat """
//                     git config user.name "${env.GIT_USER}"
//                     git config user.email "${env.GIT_EMAIL}"
//                 """

//                 // Add, commit, and push the changes
//                 bat """
//                     git add "${env.CSV_FILE}"
//                     git commit -m "${gitCommitMessage}"
//                     git push origin HEAD:main  // Push to the main branch (modify if necessary)
//                 """
//             }
//         }
//     }
// }



// pipeline {
//     agent any

//     environment {
//         BUILD_DIR = 'build_log\\build_logs'  // Use double-backslashes for Windows path
//         PYTHON_PATH = 'C:\\Users\\MTL1020\\AppData\\Local\\Programs\\Python\\Python39\\'  // Path to Python installation
//         BUILD_DURATION = '300'  // Placeholder for build duration (in seconds)
//         DEPENDENCY_CHANGES = '0'  // 0 represents 'false'
//         FAILED_PREVIOUS_BUILDS = '0'  // Placeholder for number of failed previous builds
//     }

//     stages {
//         stage('Checkout SCM') {
//             steps {
//                 echo 'Checkout SCM'
//                 checkout scm
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 echo 'Installing npm dependencies...'
//                 bat 'npm install'  // Install npm dependencies
//             }
//         }

//         stage('Build') {
//             steps {
//                 echo 'Building the project...'

//                 script {
//                     def buildLogsDir = "${env.WORKSPACE}\\${BUILD_DIR}"
//                     if (!fileExists(buildLogsDir)) {
//                         echo "Creating directory: ${buildLogsDir}"
//                         bat "mkdir \"${buildLogsDir}\""
//                     }
//                 }

//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     def currentDate = new Date().format('yyyy-MM-dd HH:mm:ss')
//                     echo "Starting build at: ${currentDate}"
//                     bat "echo 'Starting build at: ${currentDate}' > \"${logFile}\""
//                     bat "npm run build >> \"${logFile}\" 2>&1"
//                     echo "Build log written to: ${logFile}"
//                 }
//             }
//         }

//         stage('Run Error Prediction') {
//             steps {
//                 echo 'Running error prediction...'

//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     def predictionFile = "${env.WORKSPACE}\\${BUILD_DIR}\\prediction_${env.BUILD_ID}.json"

//                     echo "Log file: ${logFile}"
//                     echo "Prediction result file: ${predictionFile}"

//                     // Ensure Python is available
//                     bat "\"C:\\Users\\MTL1020\\AppData\\Local\\Programs\\Python\\Python39\\python.exe\" --version"  // Check Python version

//                     // Run error prediction without --log_file argument
//                     bat "\"C:\\Users\\MTL1020\\AppData\\Local\\Programs\\Python\\Python39\\python.exe\" scripts\\error_prediction.py --build_duration ${env.BUILD_DURATION} --dependency_changes ${env.DEPENDENCY_CHANGES} --failed_previous_builds ${env.FAILED_PREVIOUS_BUILDS} --prediction_file \"${predictionFile}\""

//                     // Display the contents of the prediction file
//                     bat "type \"${predictionFile}\""
//                 }
//             }
//         }

//         stage('Post Build Actions') {
//             steps {
//                 echo 'Build Status: SUCCESS'
//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     echo "Log file contents:"
//                     bat "type \"${logFile}\""
//                 }
//             }
//         }
//     }
// }

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





// pipeline {
//     agent any
    
//     environment {
//         BUILD_DIR = 'build_log\\build_logs'  // Use double-backslashes for Windows path
//     }

//     stages {
//         stage('Checkout SCM') {
//             steps {
//                 echo 'Checkout SCM'
//                 checkout scm
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 echo 'Installing dependencies...'
//                 bat 'npm install'
//             }
//         }

//         stage('Build') {
//             steps {
//                 echo 'Building the project...'

//                 // Ensure the build_log\\build_logs directory exists
//                 script {
//                     def buildLogsDir = "${env.WORKSPACE}\\${BUILD_DIR}"
//                     // Check if the directory exists; if not, create it
//                     if (!fileExists(buildLogsDir)) {
//                         echo "Creating directory: ${buildLogsDir}"
//                         bat "mkdir \"${buildLogsDir}\""
//                     }
//                 }

//                 script {
//                     // Define the log file path using the BUILD_ID
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     echo "Path to log file: ${logFile}"

//                     // Get the current date/time (using Groovy to capture date)
//                     def currentDate = new Date().format('yyyy-MM-dd HH:mm:ss')
//                     echo "Current date: ${currentDate}"

//                     // Write an initial entry into the log file to confirm writing
//                     bat "echo 'Starting build at: ${currentDate}' > \"${logFile}\""

//                     // Run the build command and append the output to the log file
//                     bat "npm run build >> \"${logFile}\" 2>&1"

//                     // Confirm the log file is written
//                     echo "Log file written at: ${logFile}"
//                 }
//             }
//         }

//         stage('Run Error Prediction') {
//             steps {
//                 echo 'Running error prediction...'

//                 script {
//                     // Assuming the error prediction script is available and ready to be run.
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     def predictionFile = "${env.WORKSPACE}\\${BUILD_DIR}\\prediction_${env.BUILD_ID}.json"

//                     echo "Log file: ${logFile}"
//                     echo "Prediction result file: ${predictionFile}"

//                     // Run the prediction script and save the result in a JSON file
//                     bat "python predict_errors.py --log_file \"${logFile}\" --prediction_file \"${predictionFile}\""
                    
//                     // Optional: Display the prediction result
//                     bat "type \"${predictionFile}\""
//                 }
//             }
//         }

//         stage('Post Build Actions') {
//             steps {
//                 echo 'Build Status: SUCCESS'

//                 // Optionally, print the log contents for debugging purposes
//                 script {
//                     def logFile = "${env.WORKSPACE}\\${BUILD_DIR}\\build_${env.BUILD_ID}.log"
//                     echo "Log file contents:"
//                     bat "type \"${logFile}\""
//                 }
//             }
//         }
//     }
// }
