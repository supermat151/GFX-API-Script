"""Output logging utility to capture console output and save to file."""

import sys
import os
from datetime import datetime

# Global variables to store original streams and log file
original_stdout = None
original_stderr = None
log_file = None
output_folder = None

def setup_logging(folder_path):
    """Setup logging to capture output to both console and file."""
    global original_stdout, original_stderr, log_file, output_folder
    
    # Store original streams
    original_stdout = sys.stdout
    original_stderr = sys.stderr
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
    
    # Replace stdout with our custom write function
    sys.stdout.write = write_to_both
    sys.stdout.flush = flush_both

def write_to_both(text):
    """Write text to both console and log file."""
    global original_stdout, log_file
    
    # Write to original console
    original_stdout.write(text)
    original_stdout.flush()
    
    # Write to log file if it exists
    if log_file:
        log_file.write(text)
        log_file.flush()

def flush_both():
    """Flush both console and log file."""
    global original_stdout, log_file
    
    original_stdout.flush()
    if log_file:
        log_file.flush()

def cleanup_logging():
    """Restore original stdout/stderr and close log file."""
    global original_stdout, original_stderr, log_file
    
    if log_file:
        log_file.write(f"\n\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.close()
        log_file = None
    
    # Restore original stdout and stderr
    if original_stdout:
        sys.stdout = original_stdout
    if original_stderr:
        sys.stderr = original_stderr

def print_and_log(message):
    """Helper function to print a message (will be captured by logging)."""
    print(message)