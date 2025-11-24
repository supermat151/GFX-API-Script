"""GUI functions for user input."""

import tkinter as tk
from tkinter import messagebox
from config.settings import (AVAILABLE_WORKLOADS, HEAVEN_VALLEY_API_OPTIONS, SUPERPOSITION_API_OPTIONS,
                           SUPERPOSITION_TEXTURE_OPTIONS, HEAVEN_VALLEY_AA_OPTIONS, FULLSCREEN_OPTIONS,
                           RESOLUTION_OPTIONS, HEAVEN_VALLEY_QUALITY_OPTIONS, HEAVEN_TESSELLATION_OPTIONS,
                           SUPERPOSITION_QUALITY_OPTIONS, SUPERPOSITION_DEPTH_OF_FIELD_OPTIONS,
                           SUPERPOSITION_MOTION_BLUR_OPTIONS)

def create_workload_selection(root, update_callback):
    """Create workload selection checkboxes."""
    workload_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    workload_frame.pack(pady=10, padx=10, fill=tk.X)
    tk.Label(workload_frame, text="Select Workloads to Run:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

    workload_vars = {}
    for i, workload in enumerate(AVAILABLE_WORKLOADS):
        var = tk.BooleanVar()
        chk = tk.Checkbutton(workload_frame, text=workload, variable=var, command=update_callback)
        chk.grid(row=(i % 4) + 1, column=i // 4, sticky=tk.W)
        workload_vars[workload] = var
    
    return workload_vars

def create_superposition_settings(root):
    """Create Superposition settings frame."""
    frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    tk.Label(frame, text="Unigine Superposition Settings:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

    settings = {
        "api": tk.StringVar(value="OpenGL"),
        "textures": tk.StringVar(value="high"),
        "fullscreen": tk.StringVar(value="1"),
        "resolution": tk.StringVar(value="3840x2160"),
        "quality": tk.StringVar(value="extreme"),
        "dof": tk.StringVar(value="1"),
        "motion_blur": tk.StringVar(value="1")
    }

    # Create the option menus
    tk.Label(frame, text="API:").grid(row=1, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["api"], *SUPERPOSITION_API_OPTIONS).grid(row=1, column=1, sticky=tk.W)

    tk.Label(frame, text="Textures:").grid(row=2, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["textures"], *SUPERPOSITION_TEXTURE_OPTIONS).grid(row=2, column=1, sticky=tk.W)

    tk.Label(frame, text="Fullscreen:").grid(row=3, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["fullscreen"], *FULLSCREEN_OPTIONS).grid(row=3, column=1, sticky=tk.W)

    tk.Label(frame, text="Resolution:").grid(row=4, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["resolution"], *RESOLUTION_OPTIONS).grid(row=4, column=1, sticky=tk.W)

    tk.Label(frame, text="Quality:").grid(row=5, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["quality"], *SUPERPOSITION_QUALITY_OPTIONS).grid(row=5, column=1, sticky=tk.W)

    tk.Label(frame, text="Depth of Field:").grid(row=6, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["dof"], *SUPERPOSITION_DEPTH_OF_FIELD_OPTIONS).grid(row=6, column=1, sticky=tk.W)

    tk.Label(frame, text="Motion Blur:").grid(row=7, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["motion_blur"], *SUPERPOSITION_MOTION_BLUR_OPTIONS).grid(row=7, column=1, sticky=tk.W)

    return frame, settings

def create_heaven_settings(root):
    """Create Heaven settings frame."""
    frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    tk.Label(frame, text="Unigine Heaven Settings:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

    settings = {
        "api": tk.StringVar(value="OpenGL"),
        "fullscreen": tk.StringVar(value="1"),
        "aa": tk.StringVar(value="8"),
        "resolution": tk.StringVar(value="3840x2160"),
        "width": tk.StringVar(value="3840"),
        "height": tk.StringVar(value="2160"),
        "quality": tk.StringVar(value="ultra"),
        "tessellation": tk.StringVar(value="extreme"),
    }

    tk.Label(frame, text="API:").grid(row=1, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["api"], *HEAVEN_VALLEY_API_OPTIONS).grid(row=1, column=1, sticky=tk.W)

    tk.Label(frame, text="Fullscreen:").grid(row=2, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["fullscreen"], *FULLSCREEN_OPTIONS).grid(row=2, column=1, sticky=tk.W)

    tk.Label(frame, text="AA:").grid(row=3, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["aa"], *HEAVEN_VALLEY_AA_OPTIONS).grid(row=3, column=1, sticky=tk.W)

    tk.Label(frame, text="Resolution:").grid(row=4, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["resolution"], *RESOLUTION_OPTIONS).grid(row=4, column=1, sticky=tk.W)

    tk.Label(frame, text="Quality:").grid(row=5, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["quality"], *HEAVEN_VALLEY_QUALITY_OPTIONS).grid(row=5, column=1, sticky=tk.W)

    tk.Label(frame, text="Tessellation:").grid(row=6, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["tessellation"], *HEAVEN_TESSELLATION_OPTIONS).grid(row=6, column=1, sticky=tk.W)

    return frame, settings

def create_valley_settings(root):
    """Create Valley settings frame."""
    frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
    tk.Label(frame, text="Unigine Valley Settings:").grid(row=0, column=0, columnspan=2, sticky=tk.W)

    settings = {
        "api": tk.StringVar(value="OpenGL"),
        "fullscreen": tk.StringVar(value="1"),
        "aa": tk.StringVar(value="8"),
        "resolution": tk.StringVar(value="3840x2160"),
        "width": tk.StringVar(value="3840"),
        "height": tk.StringVar(value="2160"),
        "quality": tk.StringVar(value="ultra"),
    }

    tk.Label(frame, text="API:").grid(row=1, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["api"], *HEAVEN_VALLEY_API_OPTIONS).grid(row=1, column=1, sticky=tk.W)

    tk.Label(frame, text="Fullscreen:").grid(row=2, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["fullscreen"], *FULLSCREEN_OPTIONS).grid(row=2, column=1, sticky=tk.W)

    tk.Label(frame, text="AA:").grid(row=3, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["aa"], *HEAVEN_VALLEY_AA_OPTIONS).grid(row=3, column=1, sticky=tk.W)

    tk.Label(frame, text="Resolution:").grid(row=4, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["resolution"], *RESOLUTION_OPTIONS).grid(row=4, column=1, sticky=tk.W)

    tk.Label(frame, text="Quality:").grid(row=5, column=0, sticky=tk.W)
    tk.OptionMenu(frame, settings["quality"], *HEAVEN_VALLEY_QUALITY_OPTIONS).grid(row=5, column=1, sticky=tk.W)

    return frame, settings

def run_gui():
    """Run the main GUI and return user selections."""
    root = tk.Tk()
    root.title("GFX Benchmark Automation")
    
    result = None
    
    # Variables to store settings
    superposition_settings = None
    heaven_settings = None
    valley_settings = None
    
    def update_workload_settings_visibility():
        """Show/hide settings frames based on selected workloads."""
        if workload_vars["Superposition"].get():
            superposition_frame.pack(pady=10, padx=10, fill=tk.X)
        else:
            superposition_frame.pack_forget()

        if workload_vars["Heaven"].get():
            heaven_frame.pack(pady=10, padx=10, fill=tk.X)
        else:
            heaven_frame.pack_forget()

        if workload_vars["Valley"].get():
            valley_frame.pack(pady=10, padx=10, fill=tk.X)
        else:
            valley_frame.pack_forget()

        # Update the window size to fit the content
        root.update_idletasks()
    
    def submit():
        """Handle form submission."""
        nonlocal result
        selected_workloads = [workload for workload, var in workload_vars.items() if var.get()]
        test_duration = duration_entry.get()
        include_logging = logging_var.get()
        board_num = board_number.get()

        if not selected_workloads:
            messagebox.showerror("Error", "Please select at least one workload.")
            return

        if not test_duration.isdigit() or int(test_duration) <= 0:
            messagebox.showerror("Error", "Please enter a valid test duration in minutes.")
            return

        if not board_num:
            messagebox.showerror("Error", "Please enter a board number.")
            return

        test_duration = int(test_duration)
        
        # Package all the settings
        all_settings = {
            'superposition': superposition_settings,
            'heaven': heaven_settings,
            'valley': valley_settings
        }
        
        result = (selected_workloads, test_duration, include_logging, board_num, all_settings)
        root.destroy()
    
    # Create workload selection
    workload_vars = create_workload_selection(root, update_workload_settings_visibility)
    
    # Test duration input
    tk.Label(root, text="Enter Test Duration (in minutes):").pack(pady=(20, 10))
    duration_entry = tk.Entry(root)
    duration_entry.pack(pady=10)

    # Board Number input
    tk.Label(root, text="Enter Your Board Number:").pack(pady=(20, 10))
    board_number = tk.Entry(root)
    board_number.pack(pady=10)

    # Include logging option
    logging_var = tk.IntVar(value=1)
    tk.Checkbutton(root, text="Include DGmonitor Logging", variable=logging_var).pack(pady=20)

    # Settings frames (initially hidden)
    superposition_frame, superposition_settings = create_superposition_settings(root)
    heaven_frame, heaven_settings = create_heaven_settings(root)
    valley_frame, valley_settings = create_valley_settings(root)

    # Submit button
    tk.Button(root, text="Submit", command=submit).pack(pady=20)

    # Initial visibility update
    update_workload_settings_visibility()

    # Start the GUI
    root.mainloop()
    return result