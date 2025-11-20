"""
GFX Long Duration Automation Script
Created by: matthew.lim@intel.com

Version 2.5 - Modularized code structure (function-based)
"""

import os
import time
from setup.setup_functions import setup_dependencies, setup_all_files
from benchmarks.benchmark_runner import run_selected_benchmarks
from utils.file_utils import create_info_folder, save_folder_name_to_file
import timeLogging
import logManagement
import Driver_IFWI_Info

def main():
    """Main function that runs the entire program."""
    print("GFX Long Duration Automation Script")
    print("Version 2.5 - Modularized Structure")
    print("=" * 50)
    
    # Setup dependencies and files
    print("Setting up dependencies and files...")
    setup_dependencies()
    setup_all_files()
    
    # TODO: Run GUI and get user selections
    # For now, we'll use some test values
    print("\nGUI not implemented yet - using test values")
    selected_workloads = ["Timespy"]  # Test with one 3DMark benchmark
    test_duration = 10  # 10 minutes for testing
    include_logging = 1  # Enable logging
    board_number = "001"  # Test board number
    
    if selected_workloads:
        # Setup folder structure
        os.chdir(r"C:\Users\gta\Desktop\GFX API Script")
        script_path = os.getcwd()
        timestamp = time.strftime("%Y-%m-%d_%I-%M-%S-%p", time.localtime())
        
        create_info_folder(board_number, script_path, timestamp)
        
        # Create benchmark logs folder
        Driver_version = Driver_IFWI_Info.get_Driver_Version()
        IFWI_version = Driver_IFWI_Info.get_IFWI_Version()
        expected_folder_name = f"Board{board_number}_Driver{Driver_version}_IFWI{IFWI_version}_{timestamp}"
        
        save_folder_name_to_file(expected_folder_name)
        logManagement.create_benchmark_logs_folder(board_number, Driver_version, IFWI_version, timestamp)
        
        # Run benchmarks
        print("Starting benchmark execution...")
        try:
            run_selected_benchmarks(selected_workloads, test_duration, include_logging, expected_folder_name)
            print("All benchmarks completed successfully!")
        except Exception as e:
            print(f"Caught an exception: {e}")
    else:
        print("No workloads selected.")

if __name__ == "__main__":
    main()