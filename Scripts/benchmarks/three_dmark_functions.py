"""3DMark benchmark functions."""

import os
import subprocess
from config.settings import THREEDMARK_FOLDER
from utils.dgmonitor_utils import start_dgmonitor, stop_dgmonitor
from utils.duration_utils import run_with_duration_check
import timeLogging
import logManagement

def run_single_3dmark_iteration(benchmark_name, expected_folder_name, loop_count=1):
    """Run a single iteration of 3DMark benchmark."""
    definition_file = f'C:\\Program Files\\UL\\3DMark\\custom_{benchmark_name}_OnlyGT.3dmdef'
    log_file = f'C:\\Users\\gta\\Desktop\\GFX-API-Script\\{expected_folder_name}\\Benchmark Logs\\{benchmark_name}.log'
    loop_param = f'--loop="{loop_count}"'
    benchmark_command = f'3DMarkCmd.exe --definition="{definition_file}" --log="{log_file}" {loop_param}'
    
    process = subprocess.Popen(benchmark_command, shell=True)
    return_code = process.wait()
    return return_code

def run_threedmark_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration):
    """Run 3DMark benchmark with logging and duration checking."""
    os.chdir(THREEDMARK_FOLDER)
    
    dgmonitor_window = None
    if include_logging:
        dgmonitor_window = start_dgmonitor(benchmark_name)
    
    timeLogging.set_log_path(f"{benchmark_name}_duration.log", expected_folder_name)
    timeLogging.start_test()

    # Run benchmark with duration checking
    return_code = run_with_duration_check(
        run_single_3dmark_iteration, 
        test_duration, 
        benchmark_name, 
        expected_folder_name
    )
    
    timeLogging.stop_test()
    
    if include_logging and dgmonitor_window:
        stop_dgmonitor(benchmark_name, dgmonitor_window)
        logManagement.move_dgmonitor_logs(expected_folder_name)
    
    if return_code != 0:
        print(f"{benchmark_name} execution failed.")
    
    return return_code