"""
GFX Long Duration Automation Script
Created by: matthew.lim@intel.com

Version 2.5 - Modularized code structure (function-based)
"""

import os
import time
from setup.setup_functions import setup_dependencies, setup_all_files
from gui.gui_functions import run_gui
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
    
    # Run GUI and get user selections
    print("\nLaunching GUI for user input...")
    gui_result = run_gui()
    
    if gui_result:
        selected_workloads, test_duration, include_logging, board_number, all_settings = gui_result
        
        print(f"\nUser selections:")
        print(f"Selected workloads: {selected_workloads}")
        print(f"Test duration: {test_duration} minutes")
        print(f"Include logging: {'Yes' if include_logging else 'No'}")
        print(f"Board number: {board_number}")
        
        # Setup folder structure
        os.chdir(r"C:\Users\gta\Desktop\GFX-API-Script")
        script_path = os.getcwd()
        timestamp = time.strftime("%Y-%m-%d_%I-%M-%S-%p", time.localtime())
        
        create_info_folder(board_number, script_path, timestamp)
        
        # Create benchmark logs folder
        Driver_version = Driver_IFWI_Info.get_Driver_Version()
        IFWI_version = Driver_IFWI_Info.get_IFWI_Version()
        expected_folder_name = f"Board{board_number}_Driver{Driver_version}_IFWI{IFWI_version}_{timestamp}"
        
        save_folder_name_to_file(expected_folder_name)
        logManagement.create_benchmark_logs_folder(board_number, Driver_version, IFWI_version, timestamp)
        
        # Run benchmarks with settings
        print("\nStarting benchmark execution...")
        try:
            run_selected_benchmarks(selected_workloads, test_duration, include_logging, 
                                  expected_folder_name, all_settings)
            print("All benchmarks completed successfully!")
        except Exception as e:
            print(f"Caught an exception: {e}")
    else:
        print("No selections made or GUI was cancelled.")

if __name__ == "__main__":
    main()