"""Output logging utility to capture console output and save to file."""

import sys
import os
from datetime import datetime

# Global variables to store original streams and log file
original_stdout = None
log_file = None
output_folder = None

def write_to_both(text):
    """Write text to both console and log file."""
    global original_stdout, log_file
    original_stdout.write(text)
    if log_file:
        log_file.write(text)

def flush_both():
    """Flush both console and log file."""
    global original_stdout, log_file
    original_stdout.flush()
    if log_file:
        log_file.flush()

def setup_logging(folder_path):
    """Setup logging to capture output to both console and file."""
    global original_stdout, log_file, output_folder
    
    # Store original stdout
    original_stdout = sys.stdout
    output_folder = folder_path
    
    # Ensure the output folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create log file path
    log_file_path = os.path.join(folder_path, "output.txt")
    log_file = open(log_file_path, 'w', encoding='utf-8')
    
    # Write header to log file
    log_file.write(f"GFX Automation Script Output\n")
    log_file.write(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 50 + "\n\n")
    log_file.flush()
    
    # Create a simple object with our functions
    class SimpleOutput:
        def write(self, text):
            write_to_both(text)
        def flush(self):
            flush_both()
    
    # Replace stdout with our simple output
    sys.stdout = SimpleOutput()

def cleanup_logging():
    """Restore original stdout and close log file."""
    global original_stdout, log_file
    
    if log_file:
        log_file.write(f"\n\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.close()
        log_file = None
    
    # Restore original stdout
    if original_stdout:
        sys.stdout = original_stdout

def print_and_log(message):
    """Helper function to print a message (will be captured by logging)."""
    print(message)