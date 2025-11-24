"""File operation utility functions."""

import os
import shutil
from config.settings import (SOURCE_3DMDEF, SOURCE_HEAVEN, SOURCE_VALLEY, 
                           DESTINATION_3DMDEF, HEAVEN_RUN_FOLDER, HEAVEN_INIT_FOLDER,
                           VALLEY_RUN_FOLDER, VALLEY_INIT_FOLDER, THREEDMARK_FILES,
                           HEAVEN_FILES, VALLEY_FILES)
import Driver_IFWI_Info

def create_info_folder(board_number, script_path, timestamp):
    """Create folder for board test information."""
    # Get driver and firmware information
    driver_version = Driver_IFWI_Info.get_Driver_Version()
    ifwi_version = Driver_IFWI_Info.get_IFWI_Version()
    
    # Create folder name
    folder_name = f"Board{board_number}_Driver{driver_version}_IFWI{ifwi_version}_{timestamp}"
    
    # Create the directory
    full_path = os.path.join(script_path, folder_name)
    try:
        os.makedirs(full_path)
        print(f"Folder created successfully: {full_path}")
    except OSError as error:
        print(f"Error creating folder: {error}")

def save_folder_name_to_file(expected_folder_name):
    """Save the expected folder name to a text file."""
    target_directory = r"C:\Users\gta\Desktop\GFX-API-Script"
    
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    file_path = os.path.join(target_directory, "folder_name.txt")
    
    with open(file_path, "w") as file:
        file.write(expected_folder_name)

    print(f"The file has been written to: {file_path}")

def copy_3dmark_files():
    """Copy 3DMark definition files."""
    if not os.path.exists(DESTINATION_3DMDEF):
        print("Destination directory does not exist")
        return

    for file in THREEDMARK_FILES:
        source_file = os.path.join(SOURCE_3DMDEF, file)
        destination_file = os.path.join(DESTINATION_3DMDEF, file)
        
        if os.path.exists(destination_file):
            print(f"{file} already exists in the destination directory")
        else:
            print(f"{file} does not exist in the destination directory, copying now...")
            shutil.copy(source_file, DESTINATION_3DMDEF)

def copy_heaven_files():
    """Copy Heaven automation files."""
    if not os.path.exists(HEAVEN_RUN_FOLDER) or not os.path.exists(HEAVEN_INIT_FOLDER):
        print("Heaven folder directories do not exist")
        return

    for file, destination in HEAVEN_FILES.items():
        source_file = os.path.join(SOURCE_HEAVEN, file)
        destination_file = os.path.join(destination, file)
        shutil.copy2(source_file, destination_file)
        print(f"{file} has been copied to {destination}")

def copy_valley_files():
    """Copy Valley automation files."""
    if not os.path.exists(VALLEY_RUN_FOLDER) or not os.path.exists(VALLEY_INIT_FOLDER):
        print("Valley folder directories do not exist")
        return

    for file, destination in VALLEY_FILES.items():
        source_file = os.path.join(SOURCE_VALLEY, file)
        destination_file = os.path.join(destination, file)
        shutil.copy2(source_file, destination_file)
        print(f"{file} has been copied to {destination}")