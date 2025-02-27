import csv
import sys

def append_to_csv(build_duration, dependency_changes, failed_previous_builds, csv_file_path):
    try:
        # Open the CSV file in append mode
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Writing data to the CSV file
            writer.writerow([build_duration, dependency_changes, failed_previous_builds])
            print(f"Successfully appended data to {csv_file_path}")
    except Exception as e:
        print(f"Error appending to CSV: {e}")

if __name__ == "__main__":
    # Capture arguments passed from Jenkins
    build_duration = sys.argv[1]
    dependency_changes = sys.argv[2]
    failed_previous_builds = sys.argv[3]
    csv_file_path = sys.argv[4]

    append_to_csv(build_duration, dependency_changes, failed_previous_builds, csv_file_path)
