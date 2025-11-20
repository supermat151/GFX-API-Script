"""Main benchmark runner functions."""

from config.settings import DURATION_PER_LOOP
from benchmarks.three_dmark_functions import run_threedmark_benchmark

def calculate_loops_per_workload(test_duration):
    """Calculate number of loops per workload based on test duration."""
    loops_per_workload = {}
    for workload, duration in DURATION_PER_LOOP.items():
        lower_case_workload = workload.lower()
        loops_per_workload[lower_case_workload] = test_duration // duration
    return loops_per_workload

def run_single_benchmark(benchmark_name, test_duration, include_logging, expected_folder_name):
    """Run a single benchmark based on its name."""
    print(f"\nStarting {benchmark_name} benchmark...")
    
    if "Superposition" in benchmark_name:
        # TODO: Will add this function later
        print(f"Superposition benchmark not implemented yet")
        
    elif "Heaven" in benchmark_name:
        # TODO: Will add this function later
        print(f"Heaven benchmark not implemented yet")
        
    elif "Valley" in benchmark_name:
        # TODO: Will add this function later
        print(f"Valley benchmark not implemented yet")
        
    elif any(keyword in benchmark_name for keyword in ["Computer_Vision", "ImageGeneration", "TextGeneration"]):
        # TODO: Will add this function later
        print(f"UL Procyon benchmark not implemented yet")
        
    else:
        # 3DMark benchmarks
        run_threedmark_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration)
    
    print(f"{benchmark_name} benchmark completed.\n")

def run_selected_benchmarks(selected_workloads, test_duration, include_logging, expected_folder_name):
    """Run all selected benchmarks."""
    loops_per_workload = calculate_loops_per_workload(test_duration)
    
    for benchmark_name in selected_workloads:
        try:
            run_single_benchmark(benchmark_name, test_duration, include_logging, expected_folder_name)
        except Exception as e:
            print(f"Error running {benchmark_name}: {e}")
            continue