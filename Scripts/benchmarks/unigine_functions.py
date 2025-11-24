"""Unigine Heaven and Valley benchmark functions."""

import os
import subprocess
from config.settings import HEAVEN_RUN_FOLDER, VALLEY_RUN_FOLDER
from utils.dgmonitor_utils import start_dgmonitor, stop_dgmonitor
from utils.duration_utils import parse_duration_and_check
import timeLogging
import logManagement

def run_heaven_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration, settings):
    """Run Heaven benchmark with logging and duration checking."""
    os.chdir(HEAVEN_RUN_FOLDER)
    
    dgmonitor_window = None
    if include_logging:
        dgmonitor_window = start_dgmonitor(benchmark_name)
    
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    benchmark_command = (
        f'py heavenSingleAutomationRun.py '
        f'--api {settings["api"].get()} '
        f'--fullscreen {settings["fullscreen"].get()} '
        f'--aa {settings["aa"].get()} '
        f'--width {settings["width"].get()} '
        f'--height {settings["height"].get()} '
        f'--quality {settings["quality"].get()} '
        f'--tessellation {settings["tessellation"].get()} '
    )

    print("\nStarting Unigine Heaven benchmark")

    while True:
        process = subprocess.run(benchmark_command, shell=True)
        if parse_duration_and_check(test_duration):
            break
        else:
            print("Rerunning the benchmark to meet the target duration...")

    timeLogging.stop_test()

    if process.returncode == 0 and include_logging == 0:
        logManagement.move_heaven_logs(expected_folder_name)
    elif process.returncode == 0 and include_logging == 1:
        stop_dgmonitor(benchmark_name, dgmonitor_window)
        logManagement.move_dgmonitor_logs(expected_folder_name)
        logManagement.move_heaven_logs(expected_folder_name)
    else:
        print("Heaven execution failed.")

    return process.returncode

def run_valley_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration, settings):
    """Run Valley benchmark with logging and duration checking."""
    os.chdir(VALLEY_RUN_FOLDER)
    
    dgmonitor_window = None
    if include_logging:
        dgmonitor_window = start_dgmonitor(benchmark_name)
    
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    benchmark_command = (
        f'py valleySingleAutomationRun.py '
        f'--api {settings["api"].get()} '
        f'--fullscreen {settings["fullscreen"].get()} '
        f'--aa {settings["aa"].get()} '
        f'--width {settings["width"].get()} '
        f'--height {settings["height"].get()} '
        f'--quality {settings["quality"].get()} '
    )

    print("\nStarting Unigine Valley benchmark")

    while True:
        process = subprocess.run(benchmark_command, shell=True)
        if parse_duration_and_check(test_duration):
            break
        else:
            print("Rerunning the benchmark to meet the target duration...")

    timeLogging.stop_test()

    if process.returncode == 0 and include_logging == 0:
        logManagement.move_valley_logs(expected_folder_name)
    elif process.returncode == 0 and include_logging == 1:
        stop_dgmonitor(benchmark_name, dgmonitor_window)
        logManagement.move_dgmonitor_logs(expected_folder_name)
        logManagement.move_valley_logs(expected_folder_name)
    else:
        print("Valley execution failed.")

    return process.returncode