from datetime import datetime
import threading
import time
import os

# Initialize the event flag
test_finished = threading.Event()

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to 'GFX API Script'
base_dir = os.path.dirname(script_dir)

# Default log file path in the 'GFX API Script' directory
log_path = os.path.join(base_dir, "Duration.log")

def set_log_path(filename, expected_folder_name):
    """Sets the log file path within 'Testing Duration' folder inside the expected folder and ensures the file exists."""
    global log_path

    # Construct the path to the expected folder
    expected_folder_path = os.path.join(base_dir, expected_folder_name)

    # Check if the expected folder exists
    if os.path.exists(expected_folder_path):
        # Adjust the path to include "Testing Duration" directory within the
        #  expected folder
        log_path = os.path.join(expected_folder_path, "Testing Duration", filename)

        # Ensure the "Testing Duration" directory exists, create it if not
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        # Create the log file if it doesn't exist
        if not os.path.exists(log_path):
            with open(log_path, 'w') as f:
                # Create an empty log file
                f.write("")
            print(f"Log file created: {log_path}")
            print("\n")
        else:
            print(f"Log file already exists: {log_path}")
    else:
        print(f"Expected folder does not exist: {expected_folder_path}")


def log_duration(start_time, end_time=None):
    """Log the current duration or final duration to the log file with days, hours (not exceeding 24), minutes, and seconds."""
    if end_time:
        duration = end_time - start_time
    else:
        duration = datetime.now() - start_time
    
    # Calculate total seconds in the duration
    total_seconds = int(duration.total_seconds())
    
    # Calculate days, hours, minutes, and seconds
    days = total_seconds // (3600 * 24)
    hours = (total_seconds % (3600 * 24)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    # Create a formatted duration string
    if days > 0:
        formatted_duration = f"{days} day(s), {hours}:{minutes:02d}:{seconds:02d}"
    else:
        formatted_duration = f"{hours}:{minutes:02d}:{seconds:02d}"
    
    # Write the formatted duration to the log file
    with open(log_path, "w") as f:
        f.write(f"Duration: {formatted_duration}\n")

def update_log_periodically(start_time, interval=1):
    """Periodically update the log file with the current test duration."""
    while not test_finished.is_set():
        log_duration(start_time)
        time.sleep(interval)
    # Log final duration
    log_duration(start_time, datetime.now())

def start_test():
    """Starts the test and begins periodic logging."""
    global start_time, updater_thread
    test_finished.clear()  # Reset the event flag in case of reuse
    start_time = datetime.now()
    
    # Fixed interval set to 1 second
    interval = 1
    
    # Start the thread that will periodically update the log
    updater_thread = threading.Thread(target=update_log_periodically, args=(start_time, interval))
    updater_thread.start()
    
def stop_test():
    """Stops the test and logs the final duration."""
    # Indicate test completion and wait for the updater thread to finish
    test_finished.set()
    updater_thread.join()
    
    # Log final duration
    log_duration(start_time, datetime.now())