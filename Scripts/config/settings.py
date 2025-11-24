"""Configuration constants and settings."""

# Available workloads
AVAILABLE_WORKLOADS = [
    "Steel_Nomad", 
    "Timespy", 
    "Timespy_Extreme", 
    "Firestrike", 
    "Firestrike_Extreme",
    "Wildlife", 
    "Wildlife_Extreme", 
    "PortRoyal", 
    "Speedway", 
    "XeSS",
    "Superposition", 
    "Heaven", 
    "Valley", 
    "Computer_Vision", 
    "ImageGeneration", 
    "TextGeneration"
]

# Duration per loop for each workload (in minutes)
DURATION_PER_LOOP = {
    "Timespy": 3,
    "Timespy_Extreme": 3,
    "Firestrike": 2,
    "Firestrike_Extreme": 2,
    "Wildlife": 1,
    "Wildlife_Extreme": 1,
    "Portroyal": 2,
    "Superposition": 1,
    "Heaven": 4,
    "Valley": 3
}

# File paths
SOURCE_3DMDEF = r"C:\Users\gta\Desktop\GFX-API-Script\Scripts\3dmdef"
SOURCE_HEAVEN = r"C:\Users\gta\Desktop\GFX-API-Script\Scripts\Heaven"
SOURCE_VALLEY = r"C:\Users\gta\Desktop\GFX-API-Script\Scripts\Valley"
DESTINATION_3DMDEF = r"C:\Program Files\UL\3DMark"
SUPERPOSITION_FOLDER = r"C:\Unigine\Superposition Benchmark 1.1 Advanced\bin"
THREEDMARK_FOLDER = r"C:\Program Files\UL\3DMark"
ULPROCYON_FOLDER = r"C:\Program Files\UL\Procyon"
HEAVEN_RUN_FOLDER = r"C:\Unigine\Heaven Benchmark 4.0 Advanced\automation"
HEAVEN_INIT_FOLDER = r"C:\Unigine\Heaven Benchmark 4.0 Advanced\automation\heaven_automation"
VALLEY_RUN_FOLDER = r"C:\Unigine\Valley Benchmark 1.0 Advanced\automation"
VALLEY_INIT_FOLDER = r"C:\Unigine\Valley Benchmark 1.0 Advanced\automation\valley_automation"
DGMONITOR_BAT = r"C:\Users\gta\Desktop\GFX-API-Script\Scripts\DGmonitor.bat"
DEPENDENCY_INSTALLATION = r"C:\Users\gta\Desktop\GFX-API-Script\Scripts\Installation.bat"

# Files to copy
THREEDMARK_FILES = [
    "custom_firestrike_OnlyGT.3dmdef",
    "custom_portroyal_OnlyGT.3dmdef",
    "custom_timespy_OnlyGT.3dmdef",
    "custom_wildlife_OnlyGT.3dmdef",
    "custom_firestrike_extreme_OnlyGT.3dmdef",
    "custom_timespy_extreme_OnlyGT.3dmdef",
    "custom_wildlife_extreme_OnlyGT.3dmdef",
    "custom_speedway_OnlyGT.3dmdef",
    "custom_steel_nomad_OnlyGT.3dmdef",
    "custom_XeSS_OnlyGT.3dmdef"
]

HEAVEN_FILES = {
    "__init__.py": HEAVEN_INIT_FOLDER,
    "heavenSingleAutomationRun.py": HEAVEN_RUN_FOLDER
}

VALLEY_FILES = {
    "__init__.py": VALLEY_INIT_FOLDER,
    "valleySingleAutomationRun.py": VALLEY_RUN_FOLDER
}

# GUI Options
HEAVEN_VALLEY_API_OPTIONS = ["OpenGL", "DX9", "DX11"]
SUPERPOSITION_API_OPTIONS = ["OpenGL", "DirectX"]
SUPERPOSITION_TEXTURE_OPTIONS = ["low", "medium", "high"]
HEAVEN_VALLEY_AA_OPTIONS = ["0", "2", "4", "8"]
FULLSCREEN_OPTIONS = ["0", "1"]
RESOLUTION_OPTIONS = ["1920x1080", "2560x1440", "3840x2160"]
HEAVEN_VALLEY_QUALITY_OPTIONS = ["low", "medium", "high", "ultra"]
HEAVEN_TESSELLATION_OPTIONS = ["Disabled", "Modereate", "Normal", "Extreme"]
SUPERPOSITION_QUALITY_OPTIONS = ["low", "medium", "high", "extreme", "4k_optimized", "8k_optimized"]
SUPERPOSITION_DEPTH_OF_FIELD_OPTIONS = ["0", "1"]
SUPERPOSITION_MOTION_BLUR_OPTIONS = ["0", "1"]