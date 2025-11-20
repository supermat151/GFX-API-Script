'''
GFX Long Duration Automation Script
Created by: matthew.lim@intel.com

Version 2.0 - Added more benchmarks including speedway and steel nomad
Version 2.1 - Added Unigine Heaven and Valley into benchmark

Version 2.2 - Added run.bat script to save console output of program
Version 2.3 - Added XeSS workload
Version 2.4 - Added setting choices for Superposition, Heaven, Valley
Version 2.5 - Added UL procyon vision, image and LLM
'''

import os, shutil, subprocess, time, timeLogging, logManagement, Driver_IFWI_Info, sys, logging
import tkinter as tk
from tkinter import messagebox



# ==================================================================================
# 
#                                Functions Located Here
# 
# ==================================================================================


#---------------Opening DGDiag and running DGmonitor with bat script-----------------------
def runDGMonitorWindow(benchmark_name):
    DGmonitor_bat = r"C:\Users\gta\Desktop\GFX API Script\Scripts\DGmonitor.bat"
    subprocess.Popen(['cmd', '/c', DGmonitor_bat, benchmark_name], creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(2)
    DGmonitor_title= "cmd.exe"

    #Get window list name for DGmonitor cmd window
    windows = pyautogui.getWindowsWithTitle(DGmonitor_title)
    return windows

#-----------------------------Closing DGMonitor window ------------------------------
def closeDGmontior(benchmarkName, getDGMontiorWindow):
    print(f"{benchmarkName} execution completed.")
    DGMonitorFocus = getDGMontiorWindow[0]
    DGMonitorFocus.activate()
    print("Stopping DGMontior Logging")
    time.sleep(3)
    pyautogui.hotkey('alt','f4')
    print("DGMonitor Logging has stopped")
    print("\n")
    time.sleep(2)

#-------------------Running all benchmarks------------------------
def runBenchmarks(benchmark_name, loop, includeLogging, expected_folder_name, test_duration):

    #Condition to run if workload has Superposition
    if "Superposition" in benchmark_name:
        os.chdir(Superposition_folder)

        if includeLogging == 1:
            getDGMontiorWindow = runDGMonitorWindow(benchmark_name)
        
        timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
        timeLogging.start_test()

        superpositionLog_CSV = f'C:\\Users\\gta\\Desktop\\GFX API Script\\{expected_folder_name}\\Benchmark Logs\\superposition_report.csv'
        superpositionLog_TXT = f'C:\\Users\\gta\\Desktop\\GFX API Script\\{expected_folder_name}\\Benchmark Logs\\superposition_results.txt'
        benchmark_command_superposition = (
            f'superposition_cli.exe '
            f'-api {superposition_settings["api"].get()} '
            f'-textures {superposition_settings["textures"].get()} ' 
            f'-fullscreen {superposition_settings["fullscreen"].get()} ' 
            f'-resolution {superposition_settings["resolution"].get()} ' 
            f'-sound 0 ' 
            f'-mode_duration {loop["superposition"]} ' 
            f'-quality {superposition_settings["quality"].get()} ' 
            f'-dof {superposition_settings["dof"].get()} '
            f'-motion_blur {superposition_settings["motion_blur"].get()} ' 
            f'-log_csv "{superpositionLog_CSV}" '
            f'-log_txt "{superpositionLog_TXT}"'
        )
        benchmark_process_superposition = subprocess.run(benchmark_command_superposition, shell=True)

        if benchmark_process_superposition.returncode == 0 and includeLogging == 0:
            timeLogging.stop_test()
            pass
        elif benchmark_process_superposition.returncode == 0 and includeLogging == 1:
            timeLogging.stop_test()
            closeDGmontior(benchmark_name, getDGMontiorWindow)
            logManagement.move_dgmonitor_logs(expected_folder_name)

        else:
            timeLogging.stop_test()
            print("Superposition execution failed.")


    #Condition to run if workload has Heaven
    elif "Heaven" in benchmark_name:
        os.chdir(Heaven_runFolder)
        benchmark_command_Heaven = (
            f'py heavenSingleAutomationRun.py '
            f'--api {Heaven_settings["api"].get()} '
            f'--fullscreen {Heaven_settings["fullscreen"].get()} '
            f'--aa {Heaven_settings["aa"].get()} '
            f'--width {Heaven_settings["width"].get()} '
            f'--height {Heaven_settings["height"].get()} '
            f'--quality {Heaven_settings["quality"].get()} '
            f'--tessellation {Heaven_settings["tessellation"].get()} '
        )

        if includeLogging == 1:
            getDGMontiorWindow = runDGMonitorWindow(benchmark_name)
        
        timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
        timeLogging.start_test()

        print("\n")
        print("Starting Unigine Heaven benchmark")

        while True:
            benchmark_process_Heaven = subprocess.run(benchmark_command_Heaven, shell=True)
            if parse_duration_and_check(test_duration):
                break
            else:
                print("Rerunning the benchmark to meet the target duration...")

        timeLogging.stop_test()  # Ensure logging is stopped after the process completes


        if benchmark_process_Heaven.returncode == 0 and includeLogging == 0:
            timeLogging.stop_test()
            logManagement.move_heaven_logs(expected_folder_name)
            pass
        elif benchmark_process_Heaven.returncode == 0 and includeLogging == 1:
            timeLogging.stop_test()
            closeDGmontior(benchmark_name, getDGMontiorWindow)
            logManagement.move_dgmonitor_logs(expected_folder_name)
            logManagement.move_heaven_logs(expected_folder_name)

        else:
            timeLogging.stop_test()
            print("Heaven execution failed.")

    #Condition to run if workload has Valley
    elif "Valley" in benchmark_name:
        os.chdir(Valley_runFolder)
        benchmark_command_Valley = (
            f'py valleySingleAutomationRun.py '
            f'--api {Valley_settings["api"].get()} '
            f'--fullscreen {Valley_settings["fullscreen"].get()} '
            f'--aa {Valley_settings["aa"].get()} '
            f'--width {Valley_settings["width"].get()} '
            f'--height {Valley_settings["height"].get()} '
            f'--quality {Valley_settings["quality"].get()} '
        )

        if includeLogging == 1:
            getDGMontiorWindow = runDGMonitorWindow(benchmark_name)
        
        timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
        timeLogging.start_test()

        print("\n")
        print("Starting Unigine Valley benchmark")

        while True:
            benchmark_process_Valley = subprocess.run(benchmark_command_Valley, shell=True)
            if parse_duration_and_check(test_duration):
                break
            else:
                print("Rerunning the benchmark to meet the target duration...")

        timeLogging.stop_test()  # Ensure logging is stopped after the process completes


        if benchmark_process_Valley.returncode == 0 and includeLogging == 0:
            timeLogging.stop_test()
            logManagement.move_valley_logs(expected_folder_name)
            pass
        elif benchmark_process_Valley.returncode == 0 and includeLogging == 1:
            timeLogging.stop_test()
            closeDGmontior(benchmark_name, getDGMontiorWindow)
            logManagement.move_dgmonitor_logs(expected_folder_name)
            logManagement.move_valley_logs(expected_folder_name)

        else:
            timeLogging.stop_test()
            print("Valley execution failed.")

    elif any(keyword in benchmark_name for keyword in ["Computer_Vision", "ImageGeneration", "TextGeneration"]):
        os.chdir(ULProcyon_folder)
        loopCount = 1

        if includeLogging == 1:
            getDGMontiorWindow = runDGMonitorWindow(benchmark_name)
            
        return_code = manage_benchmark_ULProcyon(benchmark_name, loopCount, expected_folder_name, test_duration)
        
        if return_code == 0 and includeLogging == 0:
            timeLogging.stop_test()
            pass
        elif return_code == 0 and includeLogging == 1:
            timeLogging.stop_test()
            closeDGmontior(benchmark_name, getDGMontiorWindow)
            logManagement.move_dgmonitor_logs(expected_folder_name)
        else:
            timeLogging.stop_test()
            print(f"{benchmark_name} execution failed.")

        
    
    #Condition to run if detects 3dmark workloads
    else:

        os.chdir(ThreeDMark_folder)
        
        loopCount = 1

        if includeLogging == 1:
            getDGMontiorWindow = runDGMonitorWindow(benchmark_name)
            
        return_code = manage_benchmark_3DMark(benchmark_name, loopCount, expected_folder_name, test_duration)
        
        if return_code == 0 and includeLogging == 0:
            timeLogging.stop_test()
            pass
        elif return_code == 0 and includeLogging == 1:
            timeLogging.stop_test()
            closeDGmontior(benchmark_name, getDGMontiorWindow)
            logManagement.move_dgmonitor_logs(expected_folder_name)
        else:
            timeLogging.stop_test()
            print(f"{benchmark_name} execution failed.")

#-------------------Running the specific 3Dmark benchmark-----------------------
def run3DMarkBenchmark(benchmark_name, loop_count, expected_folder_name):
    """Run the 3DMark benchmark without controlling the logging."""
    definition_file = f'C:\\Program Files\\UL\\3DMark\\custom_{benchmark_name}_OnlyGT.3dmdef'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX API Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'3DMarkCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    runBenchmarkProcess = subprocess.Popen(benchmark_command, shell=True)
    return_code = runBenchmarkProcess.wait()
    return return_code

#-------------------Running the UL Procyon Computer Vision benchmark-----------------------
def runComputerVision(benchmark_name, loop_count, expected_folder_name):
    """Run the 3DMark benchmark without controlling the logging."""
    definition_file = f'C:\\Program Files\\UL\\Procyon\\ai_computer_vision_openvino.def'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX API Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'ProcyonCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    runBenchmarkProcess = subprocess.Popen(benchmark_command, shell=True)
    return_code = runBenchmarkProcess.wait()
    return return_code

#-------------------Running the UL Procyon Image Generation benchmark-----------------------
def runImageGeneration(benchmark_name, loop_count, expected_folder_name, percision):
    """Run the 3DMark benchmark without controlling the logging."""
    definition_file = f'C:\\Program Files\\UL\\Procyon\\ai_imagegeneration_sd{percision}_openvino.def'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX API Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'ProcyonCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    runBenchmarkProcess = subprocess.Popen(benchmark_command, shell=True)
    return_code = runBenchmarkProcess.wait()
    return return_code

#-------------------Running the UL Procyon Text Generation benchmark-----------------------
def runTextGeneration(benchmark_name, loop_count, expected_folder_name):
    """Run the 3DMark benchmark without controlling the logging."""
    definition_file = f'C:\\Program Files\\UL\\Procyon\\ai_textgeneration_all.def'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX API Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'ProcyonCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    runBenchmarkProcess = subprocess.Popen(benchmark_command, shell=True)
    return_code = runBenchmarkProcess.wait()
    return return_code

#------------------ Running 3Dmark benchmark in a loop-------------------
def manage_benchmark_ULProcyon(benchmark_name, loop_count, expected_folder_name, target_duration_minutes):
    """Manage the benchmark process and logging."""
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    if benchmark_name=="Computer_Vision":
        while True:
            return_code = runComputerVision(benchmark_name, loop_count, expected_folder_name)
            if parse_duration_and_check(target_duration_minutes):
                break
            else:
                print("Rerunning the benchmark to meet the target duration...")
        timeLogging.stop_test()  # Ensure logging is stopped after the process completes
        return return_code
    
    elif benchmark_name=="ImageGeneration":
        percision_value  = ['15fp16', '15int8', 'xlfp16']
        while True:
            for value in percision_value:
                return_code = runImageGeneration(benchmark_name, loop_count, expected_folder_name, value)
                if parse_duration_and_check(target_duration_minutes):
                    timeLogging.stop_test()  # Ensure logging is stopped after the process completes
                    return return_code 
                else:
                    print("Rerunning the benchmark to meet the target duration...")

                
            
    else:
        while True:
           return_code = runTextGeneration(benchmark_name, loop_count, expected_folder_name)
           if parse_duration_and_check(target_duration_minutes):
               break
           else:
               print("Rerunning the benchmark to meet the target duration...")
        timeLogging.stop_test()  # Ensure logging is stopped after the process completes
        return return_code


#------------------ Running 3Dmark benchmark in a loop-------------------
def manage_benchmark_3DMark(benchmark_name, loop_count, expected_folder_name, target_duration_minutes):
    """Manage the benchmark process and logging."""
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    while True:
        return_code = run3DMarkBenchmark(benchmark_name, loop_count, expected_folder_name)
        if parse_duration_and_check(target_duration_minutes):
            break
        else:
            print("Rerunning the benchmark to meet the target duration...")

    timeLogging.stop_test()  # Ensure logging is stopped after the process completes
    return return_code

#------------------Checking if the time logging meets the target duration-----------------
def parse_duration_and_check(target_duration_minutes):
    """Parse the logged duration and check if it meets the target duration."""
    with open(timeLogging.log_path, 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            logged_duration = last_line.strip().split(": ")[-1]
            
            # Split the duration into components
            parts = logged_duration.split(", ")
            if len(parts) == 2:  # Format "1 day(s), HH:MM:SS"
                days_part, time_part = parts
                days = int(days_part.split()[0])  # Extract the number of days
                hours, minutes, seconds = map(int, time_part.split(':'))
            else:  # Format "HH:MM:SS" without days
                days = 0
                hours, minutes, seconds = map(int, parts[0].split(':'))
            
            # Calculate total minutes from days, hours, minutes, and seconds
            total_minutes = days * 1440 + hours * 60 + minutes + seconds / 60

            if total_minutes >= target_duration_minutes:
                print(f"Target duration of {target_duration_minutes} minutes reached or exceeded with {total_minutes:.2f} minutes.")
                return True
            else:
                print(f"Elapsed time {total_minutes:.2f} minutes is less than target {target_duration_minutes} minutes.")
                return False
    return False

#-------------------Creating New Folder For Board Test ------------------------
def create_info_folder(boardnumber, script_path, timestamp):
    
    # Get driver and firmware information
    Driver_version = Driver_IFWI_Info.get_Driver_Version()
    IFWI_version = Driver_IFWI_Info.get_IFWI_Version()
    
    # Create folder name based on the provided format
    folder_name = f"Board{boardnumber}_Driver{Driver_version}_IFWI{IFWI_version}_%s"%timestamp
    
    # Define the path for the new folder (adjust the base path as needed)
    full_path = os.path.join(script_path, folder_name)
    #print(full_path)
    
    # Create the directory
    try:
        os.makedirs(full_path)
        print(f"Folder created successfully: {full_path}")
    except OSError as error:
        print(f"Error creating folder: {error}")







# ==================================================================================
# 
#                                Code starts here
# 
# ==================================================================================

#--------------------Install dependencies if not installed------------------------
try:
    import psutil # type: ignore
    print("psutil is already installed")
    import pyautogui # type: ignore
    print("pyautogui is already installed")
except ImportError:
    print("Necessary dependencies are not installed. Installing...")
    dependencyInstallation = r"C:\Users\gta\Desktop\GFX API Script\Scripts\Installation.bat"
    dependencyInstallationProcess = subprocess.Popen(['cmd', '/c', dependencyInstallation], creationflags=subprocess.CREATE_NEW_CONSOLE)
    dependencyInstallationProcess.wait()
    print("Necessary dependencies have been successfully installed.")
    time.sleep(3)

#--------------------Close Original Process if found-------------------------
pyautoguiInstallationProcess = pyautogui.getWindowsWithTitle("py.exe")

if pyautoguiInstallationProcess:
    pyAutoguiInstallationProcessFocus = pyautoguiInstallationProcess[0]
    pyAutoguiInstallationProcessFocus.activate()
    time.sleep(1)
    pyautogui.hotkey('alt','f4')

#------------------Source and destination directories----------------------
source_3dmdef = r"C:\Users\gta\Desktop\GFX API Script\Scripts\3dmdef"
source_heaven = r"C:\Users\gta\Desktop\GFX API Script\Scripts\Heaven"
source_valley = r"C:\Users\gta\Desktop\GFX API Script\Scripts\Valley"
destination_3dmdef = r"C:\Program Files\UL\3DMark"
Superposition_folder = r"C:\Unigine\Superposition Benchmark 1.1 Advanced\bin"  
ThreeDMark_folder = r"C:\Program Files\UL\3DMark"
ULProcyon_folder = r"C:\Program Files\UL\Procyon"
Heaven_runFolder = r"C:\Unigine\Heaven Benchmark 4.0 Advanced\automation"
Heaven_initFolder = r"C:\Unigine\Heaven Benchmark 4.0 Advanced\automation\heaven_automation"
Valley_runFolder = r"C:\Unigine\Valley Benchmark 1.0 Advanced\automation"
Valley_initFolder = r"C:\Unigine\Valley Benchmark 1.0 Advanced\automation\valley_automation"

#-------------------Copying 3DMark 3dmdef files over--------------------
if not os.path.exists(destination_3dmdef):
    print("Destination directory does not exist")
    exit()

#List of files to be copied
files = [
    "custom_firestrike_OnlyGT.3dmdef",
    "custom_portroyal_OnlyGT.3dmdef",
    "custom_timespy_OnlyGT.3dmdef",
    "custom_wildlife_OnlyGT.3dmdef",
    "custom_firestrike_extreme_OnlyGT.3dmdef",
    "custom_timespy_extreme_OnlyGT.3dmdef",
    "custom_wildlife_extreme_OnlyGT.3dmdef", 
    "custom_speedway_OnlyGT.3dmdef",
    "custom_steel_nomad_OnlyGT.3dmdef",
    "custom_XeSS_OnlyGT.3dmdef"
]

# Loop through files
for file in files:
    source_file = os.path.join(source_3dmdef, file)
    destination_file = os.path.join(destination_3dmdef, file)
    
    # Check if file already exists in the destination directory
    if os.path.exists(destination_file):
        print(f"{file} already exists in the destination directory")
    else:
        print(f"{file} does not exist in the destination directory, copying now...")
        shutil.copy(source_file, destination_3dmdef)

print("Copy operation completed.")
print("\n")



#-------------------Copying Heaven Python files over--------------------
if not os.path.exists(Heaven_runFolder):
    print("Heaven run folder directory does not exist")
    exit()
elif not os.path.exists(Heaven_initFolder):
    print("Heaven init folder directory does not exist")
    exit()

#List of files to be copied
file_and_destination = {
    "__init__.py": Heaven_initFolder, 
    "heavenSingleAutomationRun.py": Heaven_runFolder
}
# Loop through files
for file, destination in file_and_destination.items():
    source_file = os.path.join(source_heaven, file)
    destination_file = os.path.join(destination, file)
    
    # Copy the files over
    shutil.copy2(source_file, destination_file)
    print(f"{file} has been copied to {destination}")

print("Copy operation completed.")
print("\n")


#-------------------Copying Valley Python files over--------------------
if not os.path.exists(Valley_runFolder):
    print("Valley run folder directory does not exist")
    exit()
elif not os.path.exists(Valley_initFolder):
    print("Valley init folder directory does not exist")
    exit()

#List of files to be copied
file_and_destination = {
    "__init__.py": Valley_initFolder, 
    "valleySingleAutomationRun.py": Valley_runFolder
}
# Loop through files
for file, destination in file_and_destination.items():
    source_file = os.path.join(source_valley, file)
    destination_file = os.path.join(destination, file)
    
    # Copy the files over
    shutil.copy2(source_file, destination_file)
    print(f"{file} has been copied to {destination}")

print("Copy operation completed.")
print("\n")




#-------------------Choosing list of workloads to be ran------------------------------
# List of available workloads
availableWorkloads = ["Steel_Nomad",
                      "Timespy",
                      "Timespy_Extreme", 
                      "Firestrike", 
                      "Firestrike_Extreme", 
                      "Wildlife", 
                      "Wildlife_Extreme", 
                      "PortRoyal", 
                      "Speedway", 
                      "XeSS",
                      "Superposition", 
                      "Heaven", 
                      "Valley",
                      "Computer_Vision",
                      "ImageGeneration",
                      "TextGeneration"
                    ]


#--------------------Defining duration per loop for each workload----------------------
durationPerLoop = {
    "Timespy": 3,
    "Timespy_Extreme": 3,
    "Firestrike": 2,
    "Firestrike_Extreme": 2,
    "Wildlife": 1,
    "Wildlife_Extreme": 1,
    "Portroyal": 2,
    "Superposition": 1,
    "Heaven": 4,
    "Valley": 3
}

#------------------GUI for User Input----------------------
def submit():
    
    #Grabs the name of all the selected workloads
    selected_workloads = [workload for workload, var in workload_vars.items() if var.get()]
    
    #Grab the test duration time in minutes
    test_duration = duration_entry.get()

    #Grabs the boolean value of whether logging is included or not
    include_logging = logging_var.get()

    #Get the board number
    board_number=boardNumber.get()

    if not selected_workloads:
        messagebox.showerror("Error", "Please select at least one workload.")
        return

    if not test_duration.isdigit() or int(test_duration) <= 0:
        messagebox.showerror("Error", "Please enter a valid test duration in minutes.")
        return

    #Grabs whole number for test duration
    test_duration = int(test_duration)

    #Grabs the number of loops per workload based on test_duration
    loops_per_workload = {}
    for workload, duration in durationPerLoop.items():
        lowerCaseWorkload = workload.lower()
        loops_per_workload[lowerCaseWorkload] = test_duration // duration

    # Close the GUI window
    root.destroy()  

    #Get current working script directory
    os.chdir(r"C:\Users\gta\Desktop\GFX API Script")
    script_path = os.getcwd()

    #Get current time 
    timestamp = time.strftime("%Y-%m-%d_%I-%M-%S-%p", time.localtime())

    #Creates current test folder
    create_info_folder(board_number, script_path, timestamp)

    #Create new folder for keeping benchmark logs if it doesn't exist
    Driver_version = Driver_IFWI_Info.get_Driver_Version()
    IFWI_version = Driver_IFWI_Info.get_IFWI_Version()
    
    expected_folder_name = f"Board{board_number}_Driver{Driver_version}_IFWI{IFWI_version}_%s"%timestamp
    
    # Specify the directory where you want to save the file
    target_directory = r"C:\Users\gta\Desktop\GFX API Script"

    # Ensure the directory exists, create if it does not
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Full path for the file
    file_path = os.path.join(target_directory, "folder_name.txt")

    # Write the expected folder name to the file   
    with open(file_path, "w") as file:
        file.write(expected_folder_name)

    print(f"The file has been written to: {file_path}")

    #Create Benchmark Folder in the expected folder path
    logManagement.create_benchmark_logs_folder(board_number, Driver_version, IFWI_version, timestamp)

    #Run the benchmarks that were selected
    try:
        for benchmarkName in selected_workloads:
            runBenchmarks(benchmarkName, loops_per_workload, include_logging, expected_folder_name, test_duration)
    except Exception as e:
        print(f"Caught an exception: {e}")


#-----------------------Initialize the main window-----------------------------

def update_workload_settings_visibility():
    if workload_vars["Superposition"].get():
        superposition_settings_frame.pack(pady=10, padx=10, fill=tk.X)
    else:
        superposition_settings_frame.pack_forget()

    if workload_vars["Heaven"].get():
        heaven_settings_frame.pack(pady=10, padx=10, fill=tk.X)
    else:
        heaven_settings_frame.pack_forget()

    if workload_vars["Valley"].get():
        valley_settings_frame.pack(pady=10, padx=10, fill=tk.X)
    else:
        valley_settings_frame.pack_forget()

    # Update the window size to fit the content
    root.update_idletasks()
    new_width = root.winfo_reqwidth()
    new_height = root.winfo_reqheight()
    root.geometry(f"{new_width}x{new_height}")

def update_resolution(settings, *args):
    resolution = settings["resolution"].get()
    width, height = resolution.split('x')
    superposition_settings["width"].set(width)
    superposition_settings["height"].set(height)
    Heaven_settings["width"].set(width)
    Heaven_settings["height"].set(height)

root = tk.Tk()
root.title("GFX Benchmark Automation")

# Allow the root window to resize based on its content
#root.pack_propagate(True)

# Workload selection with checkboxes
workload_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
workload_frame.pack(pady=10, padx=10, fill=tk.X)
tk.Label(workload_frame, text="Select Workloads to Run:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

workload_vars = {}
for i, workload in enumerate(availableWorkloads):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(workload_frame, text=workload, variable=var, command=update_workload_settings_visibility)
    chk.grid(row=(i % 4) + 1, column=i // 4, sticky=tk.W)
    workload_vars[workload] = var

# Test duration input
tk.Label(root, text="Enter Test Duration (in minutes):").pack(pady=(20, 10))
duration_entry = tk.Entry(root)
duration_entry.pack(pady=10)

# Board Number input
tk.Label(root, text="Enter Your Board Number:").pack(pady=(20, 10))
boardNumber = tk.Entry(root)
boardNumber.pack(pady=10)

# Include logging option
logging_var = tk.IntVar(value=1)  # Set default value to 1 (enabled)
tk.Checkbutton(root, text="Include DGmonitor Logging", variable=logging_var).pack(pady=20)


# Define options for each setting
HeavenValley_api_options = ["OpenGL", "DX9", "DX11"]
superposition_api_options = ["OpenGL", "DirectX"]
superposition_texture_options = ["low", "medium", "high"]
HeavenValley_aa_options = ["0", "2", "4", "8"]
fullscreen_options = ["0", "1"]
resolution_options = ["1920x1080", "2560x1440", "3840x2160"]
superposition_sound_options  = ["0", "1"]
HeavenValley_quality_options = ["low", "medium", "high", "ultra"]
Heaven_tessellation_options = ["Disabled", "Modereate", "Normal", "Extreme"]
superposition_quality_options = ["low", "medium", "high", "extreme", "4k_optimized",  "8k_optimized"]
superposition_depthOfField_options = ["0", "1"]
superposition_motionBlur_options = ["0", "1"]

#--------------------------------------Superposition settings-------------------------------------------

# Unigine Superposition settings input
superposition_settings_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
superposition_settings_frame.pack(pady=10, padx=10, fill=tk.X)
tk.Label(superposition_settings_frame, text="Unigine Superposition Settings:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

superposition_settings  = {
    "api": tk.StringVar(value="OpenGL"),
    "textures": tk.StringVar(value="high"),
    "fullscreen": tk.StringVar(value="1"),
    "resolution": tk.StringVar(value="3840x2160"),
    "sound": tk.StringVar(value="0"),
    "width": tk.StringVar(value="3840"),
    "height": tk.StringVar(value="2160"),
    "quality": tk.StringVar(value="extreme"),
    "dof": tk.StringVar(value="1"),
    "motion_blur": tk.StringVar(value="1")
}

# Create OptionMenu widgets for Unigine Superposition
tk.Label(superposition_settings_frame, text="API:").grid(row=1, column=0, sticky=tk.W)
tk.OptionMenu(superposition_settings_frame, superposition_settings["api"], *superposition_api_options).grid(row=1, column=1, sticky=tk.W)

tk.Label(superposition_settings_frame, text="Textures:").grid(row=2, column=0, sticky=tk.W)
tk.OptionMenu(superposition_settings_frame, superposition_settings["textures"], *superposition_texture_options).grid(row=2, column=1, sticky=tk.W)

tk.Label(superposition_settings_frame, text="Fullscreen:").grid(row=3, column=0, sticky=tk.W)
tk.OptionMenu(superposition_settings_frame, superposition_settings["fullscreen"], *fullscreen_options).grid(row=3, column=1, sticky=tk.W)

tk.Label(superposition_settings_frame, text="Resolution:").grid(row=4, column=0, sticky=tk.W)
resolution_menu = tk.OptionMenu(superposition_settings_frame, superposition_settings["resolution"], *resolution_options)
resolution_menu.grid(row=4, column=1, sticky=tk.W)
superposition_settings["resolution"].trace("w", lambda *args: update_resolution(superposition_settings))

tk.Label(superposition_settings_frame, text="Quality:").grid(row=5, column=0, sticky=tk.W)
tk.OptionMenu(superposition_settings_frame, superposition_settings["quality"], *superposition_quality_options).grid(row=5, column=1, sticky=tk.W)

tk.Label(superposition_settings_frame, text="Depth of Field:").grid(row=6, column=0, sticky=tk.W)
tk.OptionMenu(superposition_settings_frame, superposition_settings["dof"], *superposition_depthOfField_options).grid(row=6, column=1, sticky=tk.W)

tk.Label(superposition_settings_frame, text="Motion Blur:").grid(row=7, column=0, sticky=tk.W)
tk.OptionMenu(superposition_settings_frame, superposition_settings["motion_blur"], *superposition_motionBlur_options).grid(row=7, column=1, sticky=tk.W)


#--------------------------------------Heaven settings-------------------------------------------

# Unigine Superposition settings input
heaven_settings_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
heaven_settings_frame.pack(pady=10, padx=10, fill=tk.X)
tk.Label(heaven_settings_frame, text="Unigine Heaven Settings:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

Heaven_settings  = {
    "api": tk.StringVar(value="OpenGL"),
    "fullscreen": tk.StringVar(value="1"),
    "aa": tk.StringVar(value="8"),
    "resolution": tk.StringVar(value="3840x2160"),
    "width": tk.StringVar(value="3840"),
    "height": tk.StringVar(value="2160"),
    "quality": tk.StringVar(value="ultra"),
    "tessellation": tk.StringVar(value="extreme"),
}

# Create OptionMenu widgets for Unigine Heaven
tk.Label(heaven_settings_frame, text="API:").grid(row=1, column=0, sticky=tk.W)
tk.OptionMenu(heaven_settings_frame, Heaven_settings["api"], *HeavenValley_api_options).grid(row=1, column=1, sticky=tk.W)

tk.Label(heaven_settings_frame, text="Fullscreen:").grid(row=2, column=0, sticky=tk.W)
tk.OptionMenu(heaven_settings_frame, Heaven_settings["fullscreen"], *fullscreen_options).grid(row=2, column=1, sticky=tk.W)

tk.Label(heaven_settings_frame, text="AA:").grid(row=3, column=0, sticky=tk.W)
tk.OptionMenu(heaven_settings_frame, Heaven_settings["aa"], *HeavenValley_aa_options).grid(row=3, column=1, sticky=tk.W)

tk.Label(heaven_settings_frame, text="Resolution:").grid(row=4, column=0, sticky=tk.W)
resolution_menu = tk.OptionMenu(heaven_settings_frame, Heaven_settings["resolution"], *resolution_options)
resolution_menu.grid(row=4, column=1, sticky=tk.W)
Heaven_settings["resolution"].trace("w", lambda *args: update_resolution(Heaven_settings))

tk.Label(heaven_settings_frame, text="Quality:").grid(row=5, column=0, sticky=tk.W)
tk.OptionMenu(heaven_settings_frame, Heaven_settings["quality"], *HeavenValley_quality_options).grid(row=5, column=1, sticky=tk.W)

tk.Label(heaven_settings_frame, text="Tessellation:").grid(row=6, column=0, sticky=tk.W)
tk.OptionMenu(heaven_settings_frame, Heaven_settings["tessellation"], *Heaven_tessellation_options).grid(row=6, column=1, sticky=tk.W)

#--------------------------------------Valley settings-------------------------------------------

# Unigine Superposition settings input
valley_settings_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
valley_settings_frame.pack(pady=10, padx=10, fill=tk.X)
tk.Label(valley_settings_frame, text="Unigine Valley Settings:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

Valley_settings  = {
    "api": tk.StringVar(value="OpenGL"),
    "fullscreen": tk.StringVar(value="1"),
    "aa": tk.StringVar(value="8"),
    "resolution": tk.StringVar(value="3840x2160"),
    "width": tk.StringVar(value="3840"),
    "height": tk.StringVar(value="2160"),
    "quality": tk.StringVar(value="ultra"),
}

# Create OptionMenu widgets for Unigine Valley
tk.Label(valley_settings_frame, text="API:").grid(row=1, column=0, sticky=tk.W)
tk.OptionMenu(valley_settings_frame, Valley_settings["api"], *HeavenValley_api_options).grid(row=1, column=1, sticky=tk.W)

tk.Label(valley_settings_frame, text="Fullscreen:").grid(row=2, column=0, sticky=tk.W)
tk.OptionMenu(valley_settings_frame, Valley_settings["fullscreen"], *fullscreen_options).grid(row=2, column=1, sticky=tk.W)

tk.Label(valley_settings_frame, text="AA:").grid(row=3, column=0, sticky=tk.W)
tk.OptionMenu(valley_settings_frame, Valley_settings["aa"], *HeavenValley_aa_options).grid(row=3, column=1, sticky=tk.W)

tk.Label(valley_settings_frame, text="Resolution:").grid(row=4, column=0, sticky=tk.W)
resolution_menu = tk.OptionMenu(valley_settings_frame, Valley_settings["resolution"], *resolution_options)
resolution_menu.grid(row=4, column=1, sticky=tk.W)
Valley_settings["resolution"].trace("w", lambda *args: update_resolution(Valley_settings))

tk.Label(valley_settings_frame, text="Quality:").grid(row=5, column=0, sticky=tk.W)
tk.OptionMenu(valley_settings_frame, Valley_settings["quality"], *HeavenValley_quality_options).grid(row=5, column=1, sticky=tk.W)

# Submit button
tk.Button(root, text="Submit", command=submit).pack(pady=5)

update_workload_settings_visibility()

# Start the GUI event loop
root.mainloop()
