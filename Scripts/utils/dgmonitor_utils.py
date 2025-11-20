"""DGMonitor utility functions."""

import subprocess
import time
import pyautogui
from config.settings import DGMONITOR_BAT

def start_dgmonitor(benchmark_name):
    """Start DGMonitor logging and return window handle."""
    subprocess.Popen(['cmd', '/c', DGMONITOR_BAT, benchmark_name], 
                    creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(2)
    windows = pyautogui.getWindowsWithTitle("cmd.exe")
    return windows

def stop_dgmonitor(benchmark_name, dgmonitor_window):
    """Stop DGMonitor logging."""
    print(f"{benchmark_name} execution completed.")
    if dgmonitor_window:
        dgmonitor_focus = dgmonitor_window[0]
        dgmonitor_focus.activate()
        print("Stopping DGMonitor Logging")
        time.sleep(3)
        pyautogui.hotkey('alt', 'f4')
        print("DGMonitor Logging has stopped")
        print("\n")
        time.sleep(2)