"""Superposition benchmark functions."""

import os
import subprocess
from config.settings import SUPERPOSITION_FOLDER
from utils.dgmonitor_utils import start_dgmonitor, stop_dgmonitor
import timeLogging
import logManagement

def run_superposition_benchmark(benchmark_name, loops_per_workload, include_logging, expected_folder_name, test_duration, settings):
    """Run Superposition benchmark with logging and duration checking."""
    os.chdir(SUPERPOSITION_FOLDER)
    
    dgmonitor_window = None
    if include_logging:
        dgmonitor_window = start_dgmonitor(benchmark_name)
    
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    superposition_log_csv = f'C:\\Users\\gta\\Desktop\\GFX-API-Script\\{expected_folder_name}\\Benchmark Logs\\superposition_report.csv'
    superposition_log_txt = f'C:\\Users\\gta\\Desktop\\GFX-API-Script\\{expected_folder_name}\\Benchmark Logs\\superposition_results.txt'
    
    benchmark_command = (
        f'superposition_cli.exe '
        f'-api {settings["api"].get()} '
        f'-textures {settings["textures"].get()} '
        f'-fullscreen {settings["fullscreen"].get()} '
        f'-resolution {settings["resolution"].get()} '
        f'-sound 0 '
        f'-mode_duration {loops_per_workload["superposition"]} '
        f'-quality {settings["quality"].get()} '
        f'-dof {settings["dof"].get()} '
        f'-motion_blur {settings["motion_blur"].get()} '
        f'-log_csv "{superposition_log_csv}" '
        f'-log_txt "{superposition_log_txt}"'
    )
    
    process = subprocess.run(benchmark_command, shell=True)
    
    timeLogging.stop_test()
    
    if process.returncode == 0 and include_logging == 0:
        pass
    elif process.returncode == 0 and include_logging == 1:
        stop_dgmonitor(benchmark_name, dgmonitor_window)
        logManagement.move_dgmonitor_logs(expected_folder_name)
    else:
        print("Superposition execution failed.")
    
    return process.returncode