import subprocess, os

def get_Driver_Version():
    try:
        # Command to execute DGDiagTool.exe with parameters
        command = r'"C:/Program Files/Intel Corporation/DGDiagTool_Internal/DGDiagTool.exe" -SYSINFO.UTIL.DGDriverinfo'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            # Normalize the output by stripping leading/trailing whitespaces
            output = result.stdout.strip()
            
            # Split the output to process lines
            lines = output.splitlines()
            
            # Initialize variables to store the required information
            driver_version = None
            result_status = None
            
            # Iterate over lines to find the required information
            for line in lines:
                if "Result" in line:
                    result_status = line.split(':')[1].strip()
                    # Check if the result is "PASS" or "FAIL"
                    if result_status == "PASS":
                        # Continue to find the Driver Version
                        for line in lines:
                            if "Driver Version" in line:
                                driver_version = line.split(':')[1].strip()
                                # Extract the desired part of the version
                                parts = driver_version.split('.')
                                if len(parts) >= 3:
                                    # Combine the third and fourth parts
                                    final_version = parts[2] + parts[3]
                                    return final_version
                    else:
                        return "FAIL"
            
            # If no result status found, return unexpected format
            return "Unexpected output format"
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return str(e)
    

def get_IFWI_Version():
    try:
        # Command to execute DGDiagTool.exe with parameters
        command = r'"C:/Program Files/Intel Corporation/DGDiagTool_Internal/DGDiagTool.exe" -SYSINFO.UTIL.FirmwareInfo'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            # Normalize the output by stripping leading/trailing whitespaces
            output = result.stdout.strip()
            
            # Split the output to process lines
            lines = output.splitlines()
            
            # Initialize variables to store the required information
            gfx_ip_version = None
            result_status = None
            
            # Iterate over lines to find the required information
            for line in lines:
                if "Result" in line:
                    result_status = line.split(':')[1].strip()
                    # Check if the result is "PASS" or "FAIL"
                    if result_status == "PASS":
                        # Continue to find the GFX IP Version
                        for line in lines:
                            if "GFX IP Version" in line:
                                gfx_ip_version = line.split(':')[1].strip()
                                return gfx_ip_version
                    else:
                        return "FAIL"
            
            # If no result status found, return unexpected format
            return "Unexpected output format"
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return str(e)