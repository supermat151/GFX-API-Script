"""Duration checking utility functions."""

import timeLogging

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
                days = int(days_part.split()[0])
                hours, minutes, seconds = map(int, time_part.split(':'))
            else:  # Format "HH:MM:SS" without days
                days = 0
                hours, minutes, seconds = map(int, parts[0].split(':'))
            
            # Calculate total minutes
            total_minutes = days * 1440 + hours * 60 + minutes + seconds / 60

            if total_minutes >= target_duration_minutes:
                print(f"Target duration of {target_duration_minutes} minutes reached or exceeded with {total_minutes:.2f} minutes.")
                return True
            else:
                print(f"Elapsed time {total_minutes:.2f} minutes is less than target {target_duration_minutes} minutes.")
                return False
    return False

def run_with_duration_check(benchmark_function, target_duration_minutes, *args, **kwargs):
    """Run benchmark function repeatedly until target duration is met."""
    while True:
        return_code = benchmark_function(*args, **kwargs)
        if parse_duration_and_check(target_duration_minutes):
            break
        else:
            print("Rerunning the benchmark to meet the target duration...")
    return return_code