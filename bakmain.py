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

        profile_source = os.path.join(profiles_folder, selected_aircraft, "Logitech_Extreme_3D_Pro.diff.lua")

        # Where to copy the profile (you might adjust the destination path later)
        saved_games_path = os.path.expanduser("~/Saved Games/DCS/Config/Input")

        if not os.path.exists(saved_games_path):
            os.makedirs(saved_games_path)

        target_folder = os.path.join(saved_games_path, selected_aircraft, "joystick")
        os.makedirs(target_folder, exist_ok=True)

        profile_target = os.path.join(target_folder, "Logitech_Extreme_3D_Pro.diff.lua")

        try:
            shutil.copyfile(profile_source, profile_target)
            sg.popup_ok(f"Mapping applied successfully to {selected_aircraft}!")
        except Exception as e:
            sg.popup_error(f"Failed to apply mapping:\n{e}")

window.close()
