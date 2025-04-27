import PySimpleGUI as sg
import os
import shutil
import sys

APP_NAME = "FlightCommander"
APP_VERSION = "1.0.0"

# Helper for PyInstaller runtime
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller .exe"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Path where profiles are stored
profiles_folder = resource_path('profiles')

# Mapping FlightCommander profile names → real DCS Saved Games folder names
aircraft_name_mapping = {
    "F-16C_50": "F-16C_Viper",
    "FA-18C_hornet": "FA-18C_hornet",
    "A-10C_2": "A-10C_2",
    "TF-51D": "TF-51D",
    # Add more mappings as needed!
}

# List available aircraft profiles
def list_aircraft():
    aircraft = []
    for folder in os.listdir(profiles_folder):
        folder_path = os.path.join(profiles_folder, folder)
        if os.path.isdir(folder_path):
            aircraft.append(folder)
    return sorted(aircraft)

# GUI Layout
layout = [
    [sg.Text(f"FlightCommander {APP_VERSION}", font=("Any", 16))],
    [sg.Text("Select aircraft:"), sg.Combo(list_aircraft(), key='aircraft')],
    [sg.Button('Apply Mapping'), sg.Button('Exit')]
]

# Main window
window = sg.Window(APP_NAME, layout)

# Main event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == 'Apply Mapping':
        selected_aircraft = values['aircraft']
        if not selected_aircraft:
            sg.popup_error("Please select an aircraft!")
            continue

        # Map to real DCS folder name if needed
        dcs_aircraft_folder = aircraft_name_mapping.get(selected_aircraft, selected_aircraft)

        profile_source = os.path.join(profiles_folder, selected_aircraft, "Logitech_Extreme_3D_Pro.diff.lua")

        # Support both DCS Stable and DCS OpenBeta
        saved_games_path = os.path.expanduser("~/Saved Games/DCS/Config/Input")
        if not os.path.exists(saved_games_path):
            saved_games_path = os.path.expanduser("~/Saved Games/DCS.openbeta/Config/Input")

        if not os.path.exists(saved_games_path):
            sg.popup_error("Cannot find DCS Input folder! Is DCS installed?")
            continue

        target_folder = os.path.join(saved_games_path, dcs_aircraft_folder, "joystick")
        os.makedirs(target_folder, exist_ok=True)

        profile_target = os.path.join(target_folder, "Logitech_Extreme_3D_Pro.diff.lua")

        try:
            shutil.copyfile(profile_source, profile_target)
            sg.popup_ok(f"Mapping applied successfully to {dcs_aircraft_folder}!")
        except Exception as e:
            sg.popup_error(f"Failed to apply mapping:\n{e}")

window.close()
