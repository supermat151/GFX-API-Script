"""Main benchmark runner functions."""

from config.settings import DURATION_PER_LOOP
from benchmarks.three_dmark_functions import run_threedmark_benchmark
from benchmarks.superposition_functions import run_superposition_benchmark
from benchmarks.unigine_functions import run_heaven_benchmark, run_valley_benchmark
from benchmarks.ul_procyon_functions import run_ul_procyon_benchmark

def calculate_loops_per_workload(test_duration):
    """Calculate number of loops per workload based on test duration."""
    loops_per_workload = {}
    for workload, duration in DURATION_PER_LOOP.items():
        lower_case_workload = workload.lower()
        loops_per_workload[lower_case_workload] = test_duration // duration
    return loops_per_workload

def run_single_benchmark(benchmark_name, test_duration, include_logging, expected_folder_name, all_settings):
    """Run a single benchmark based on its name."""
    print(f"\nStarting {benchmark_name} benchmark...")
    
    loops_per_workload = calculate_loops_per_workload(test_duration)
    
    if "Superposition" in benchmark_name:
        superposition_settings = all_settings.get('superposition', {})
        run_superposition_benchmark(benchmark_name, loops_per_workload, include_logging, 
                                  expected_folder_name, test_duration, superposition_settings)
        
    elif "Heaven" in benchmark_name:
        heaven_settings = all_settings.get('heaven', {})
        run_heaven_benchmark(benchmark_name, include_logging, expected_folder_name, 
                           test_duration, heaven_settings)
        
    elif "Valley" in benchmark_name:
        valley_settings = all_settings.get('valley', {})
        run_valley_benchmark(benchmark_name, include_logging, expected_folder_name, 
                           test_duration, valley_settings)
        
    elif any(keyword in benchmark_name for keyword in ["Computer_Vision", "ImageGeneration", "TextGeneration"]):
        run_ul_procyon_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration)
        
    else:
        # 3DMark benchmarks
        run_threedmark_benchmark(benchmark_name, include_logging, expected_folder_name, test_duration)
    
    print(f"{benchmark_name} benchmark completed.\n")

def run_selected_benchmarks(selected_workloads, test_duration, include_logging, expected_folder_name, all_settings=None):
    """Run all selected benchmarks."""
    if all_settings is None:
        all_settings = {}
    
    for benchmark_name in selected_workloads:
        try:
            run_single_benchmark(benchmark_name, test_duration, include_logging, 
                               expected_folder_name, all_settings)
        except Exception as e:
            print(f"Error running {benchmark_name}: {e}")
            continue