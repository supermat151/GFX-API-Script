"""UL Procyon benchmark functions."""

import os
import subprocess
import pyautogui
from config.settings import ULPROCYON_FOLDER
from utils.dgmonitor_utils import start_dgmonitor, stop_dgmonitor
from utils.duration_utils import parse_duration_and_check
import timeLogging
import logManagement

def run_computer_vision(benchmark_name, loop_count, expected_folder_name):
    """Run the UL Procyon Computer Vision benchmark."""
    definition_file = f'C:\\Program Files\\UL\\Procyon\\ai_computer_vision_openvino.def'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX-API-Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'ProcyonCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    process = subprocess.Popen(benchmark_command, shell=True)
    return_code = process.wait()
    return return_code

def run_image_generation(benchmark_name, loop_count, expected_folder_name, precision):
    """Run the UL Procyon Image Generation benchmark."""
    definition_file = f'C:\\Program Files\\UL\\Procyon\\ai_imagegeneration_sd{precision}_openvino.def'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX-API-Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'ProcyonCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    process = subprocess.Popen(benchmark_command, shell=True)
    return_code = process.wait()
    return return_code

def run_text_generation(benchmark_name, loop_count, expected_folder_name):
    """Run the UL Procyon Text Generation benchmark."""
    definition_file = f'C:\\Program Files\\UL\\Procyon\\ai_textgeneration_all.def'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX-API-Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'ProcyonCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    process = subprocess.Popen(benchmark_command, shell=True)
    return_code = process.wait()
    return return_code

def manage_ul_procyon_benchmark(benchmark_name, loop_count, expected_folder_name, target_duration_minutes):
    """Manage the UL Procyon benchmark process and logging."""
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    if benchmark_name == "Computer_Vision":
        while True:
            return_code = run_computer_vision(benchmark_name, loop_count, expected_folder_name)
            if parse_duration_and_check(target_duration_minutes):
                break
            else:
                print("Rerunning the benchmark to meet the target duration...")
        timeLogging.stop_test()
        return return_code
    
    elif benchmark_name == "ImageGeneration":
        precision_values = ['15fp16', '15int8', 'xlfp16']
        while True:
            for value in precision_values:
                return_code = run_image_generation(benchmark_name, loop_count, expected_folder_name, value)
                if parse_duration_and_check(target_duration_minutes):
                    timeLogging.stop_test()
                    return return_code 
                else:
                    print("Rerunning the benchmark to meet the target duration...")
    
    else:  # TextGeneration
        while True:
            return_code = run_text_generation(benchmark_name, loop_count, expected_folder_name)
            if parse_duration_and_check(target_duration_minutes):
                break
            else:
                print("Rerunning the benchmark to meet the target duration...")
        timeLogging.stop_test()
        return return_code

def run_ul_procyon_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration):
    """Run UL Procyon benchmark with logging and duration checking."""
    # Store original failsafe setting and disable it for UL Procyon
    original_failsafe = pyautogui.FAILSAFE
    pyautogui.FAILSAFE = False
    print(f"PyAutoGUI failsafe disabled for {benchmark_name} benchmark")
    
    try:
        os.chdir(ULPROCYON_FOLDER)
        loop_count = 1

        dgmonitor_window = None
        if include_logging:
            dgmonitor_window = start_dgmonitor(benchmark_name)
            
        return_code = manage_ul_procyon_benchmark(benchmark_name, loop_count, expected_folder_name, test_duration)
        
        if return_code == 0 and include_logging == 0:
            pass
        elif return_code == 0 and include_logging == 1:
            stop_dgmonitor(benchmark_name, dgmonitor_window)
            logManagement.move_dgmonitor_logs(expected_folder_name)
        else:
            print(f"{benchmark_name} execution failed.")

        return return_code
    
    finally:
        # Always restore the original failsafe setting
        pyautogui.FAILSAFE = original_failsafe
        print(f"PyAutoGUI failsafe restored after {benchmark_name} benchmark")