import os, shutil, datetime

def create_benchmark_logs_folder(board_number, DriverVersion, IFWIVersion, time):
    """Create a new folder named 'Benchmark Logs' at the specified location."""
    # Construct the full path for the new folder
    location = r"C:\Users\gta\Desktop\GFX-API-Script"
    
    # Construct the expected folder name
    expected_folder_name = f"Board{board_number}_Driver{DriverVersion}_IFWI{IFWIVersion}_%s"%time
    
    # Search for the matching folder
    for folder in os.listdir(location):
        if folder == expected_folder_name:
            # Construct the full path for the new "Benchmark Logs" folder
            benchmark_logs_path = os.path.join(location, folder, "Benchmark Logs")
            
            # Check if the "Benchmark Logs" folder already exists
            if not os.path.exists(benchmark_logs_path):
                # Create the "Benchmark Logs" folder
                os.makedirs(benchmark_logs_path)
                print(f"Folder created: {benchmark_logs_path}")
                return
            else:
                print(f"Folder already exists: {benchmark_logs_path}")
                return
    
    # If no matching folder is found
    print(f"No matching folder found for {expected_folder_name}")

def move_dgmonitor_logs(expected_folder_name):

    #Set the folder location
    script_location = r"C:\Users\gta\Desktop\GFX-API-Script"
    DGmonitor_log_location = r"C:\Program Files\Intel Corporation\DGDiagTool_internal"

    # Ensure the dgdiag folder exists
    if not os.path.exists(DGmonitor_log_location):
        print(f"Source folder does not exist: {DGmonitor_log_location}")
        return
    
     # List all files in the source folder
    files = [os.path.join(DGmonitor_log_location, file) for file in os.listdir(DGmonitor_log_location) if os.path.isfile(os.path.join(DGmonitor_log_location, file))]
    
    # Sort files by date modified (most recent first)
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    # Check if there are any files to process
    if not files:
        print("No files found in the source folder.")
        return
    
    # Most recent file
    most_recent_file = files[0]
    
    # Search for the matching folder
    for folder in os.listdir(script_location):
        if folder == expected_folder_name:
            # Construct the full path for the new "DGMonitor Logs" folder
            DGmonitor_logs_path = os.path.join(script_location, folder, "DGMonitor Logs")
            
            # Check if the "DGMonitor Logs" folder already exists
            if not os.path.exists(DGmonitor_logs_path):
                # Create the "DGMonitor Logs" folder
                os.makedirs(DGmonitor_logs_path)
                print(f"Folder created: {DGmonitor_logs_path}")
            else:
                print(f"Folder already exists: {DGmonitor_logs_path}")
            
            # Move the most recent file to the newly created "DGMonitor Logs" folder
            shutil.move(most_recent_file, DGmonitor_logs_path)
            print(f"Moved {most_recent_file} to {DGmonitor_logs_path}")
            return
    
    # If no matching folder is found
    print(f"No matching folder found for {expected_folder_name}")

def move_heaven_logs(expected_folder_name):

    #Set the folder location
    script_location = r"C:\Users\gta\Desktop\GFX-API-Script"
    Heaven_log_location = r"C:\Users\gta\Heaven\reports"

    # Ensure the dgdiag folder exists
    if not os.path.exists(Heaven_log_location):
        print(f"Source folder does not exist: {Heaven_log_location}")
        return
    
     # List all files in the source folder
    files = [os.path.join(Heaven_log_location, file) for file in os.listdir(Heaven_log_location) if os.path.isfile(os.path.join(Heaven_log_location, file))]
    
    # Sort files by date modified (most recent first)
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    # Check if there are any files to process
    if not files:
        print("No files found in the source folder.")
        return
    
    # Most recent file
    most_recent_file = files[0]
    
    # Search for the matching folder
    for folder in os.listdir(script_location):
        if folder == expected_folder_name:
            # Construct the full path for the new "Benchmark Logs" folder
            Heaven_logs_path = os.path.join(script_location, folder, "Benchmark Logs")
            
            # Check if the "Benchmark Logs" folder already exists
            if not os.path.exists(Heaven_logs_path):
                # Create the "Benchmark Logs" folder
                os.makedirs(Heaven_logs_path)
                print(f"Folder created: {Heaven_logs_path}")
            else:
                print(f"Folder already exists: {Heaven_logs_path}")
            
            # Move the most recent file to the newly created "Benchmark Logs" folder
            shutil.move(most_recent_file, Heaven_logs_path)
            print(f"Moved {most_recent_file} to {Heaven_logs_path}")
            return
    
    # If no matching folder is found
    print(f"No matching folder found for {expected_folder_name}")

def move_valley_logs(expected_folder_name):

    #Set the folder location
    script_location = r"C:\Users\gta\Desktop\GFX-API-Script"
    Valley_log_location = r"C:\Users\gta\Valley\reports"

    # Ensure the dgdiag folder exists
    if not os.path.exists(Valley_log_location):
        print(f"Source folder does not exist: {Valley_log_location}")
        return
    
     # List all files in the source folder
    files = [os.path.join(Valley_log_location, file) for file in os.listdir(Valley_log_location) if os.path.isfile(os.path.join(Valley_log_location, file))]
    
    # Sort files by date modified (most recent first)
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    # Check if there are any files to process
    if not files:
        print("No files found in the source folder.")
        return
    
    # Most recent file
    most_recent_file = files[0]
    
    # Search for the matching folder
    for folder in os.listdir(script_location):
        if folder == expected_folder_name:
            # Construct the full path for the new "Benchmark Logs" folder
            Valley_logs_path = os.path.join(script_location, folder, "Benchmark Logs")
            
            # Check if the "Benchmark Logs" folder already exists
            if not os.path.exists(Valley_logs_path):
                # Create the "Benchmark Logs" folder
                os.makedirs(Valley_logs_path)
                print(f"Folder created: {Valley_logs_path}")
            else:
                print(f"Folder already exists: {Valley_logs_path}")
            
            # Move the most recent file to the newly created "Benchmark Logs" folder
            shutil.move(most_recent_file, Valley_logs_path)
            print(f"Moved {most_recent_file} to {Valley_logs_path}")
            return
    
    # If no matching folder is found
    print(f"No matching folder found for {expected_folder_name}")

def move_output_file(expected_folder_name):
    # Define the source path of the output.txt file
    source_path = r"C:\Users\gta\Desktop\GFX-API-Script\output.txt"
    
    # Check if the source file exists
    if not os.path.exists(source_path):
        print("The file output.txt does not exist in the specified directory.")
        return
    
    # Define the destination path where the output.txt file will be moved
    destination_path = os.path.join(r"C:\Users\gta\Desktop\GFX-API-Script", expected_folder_name, "output.txt")
    
    # Create the destination directory if it does not exist
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Move the file
    shutil.move(source_path, destination_path)
    print(f"Output file moved successfully to {destination_path}")