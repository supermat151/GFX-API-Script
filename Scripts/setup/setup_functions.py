"""Setup and initialization functions."""

import os
import subprocess
import time
import pyautogui
from config.settings import DEPENDENCY_INSTALLATION
from utils.file_utils import copy_3dmark_files, copy_heaven_files, copy_valley_files

def setup_dependencies():
    """Install necessary dependencies if not already installed."""
    try:
        import psutil
        print("psutil is already installed")
        import pyautogui
        print("pyautogui is already installed")
    except ImportError:
        print("Necessary dependencies are not installed. Installing...")
        process = subprocess.Popen(['cmd', '/c', DEPENDENCY_INSTALLATION], 
                                 creationflags=subprocess.CREATE_NEW_CONSOLE)
        process.wait()
        print("Necessary dependencies have been successfully installed.")
        time.sleep(3)

    # Close installation process window if found
    installation_windows = pyautogui.getWindowsWithTitle("py.exe")
    if installation_windows:
        installation_focus = installation_windows[0]
        installation_focus.activate()
        time.sleep(1)
        pyautogui.hotkey('alt', 'f4')

def setup_all_files():
    """Setup all necessary files."""
    print("Setting up 3DMark files...")
    copy_3dmark_files()
    print("3DMark copy operation completed.\n")

    print("Setting up Heaven files...")
    copy_heaven_files()
    print("Heaven copy operation completed.\n")

    print("Setting up Valley files...")
    copy_valley_files()
    print("Valley copy operation completed.\n")