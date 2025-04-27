
import os, json, shutil, sys
from pathlib import Path
import PySimpleGUI as sg

APP_NAME = "FlightCommander"
DEFAULT_PROFILES_DIR = Path(__file__).parent / "profiles"
CONFIG_FILE = Path.home() / ".flightcommander.json"

def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except Exception:
            pass
    return {"dcs_path": str(Path.home() / "Saved Games" / "DCS" / "Config" / "Input")}

def save_config(cfg):
    try:
        CONFIG_FILE.write_text(json.dumps(cfg))
    except Exception as e:
        sg.popup_error(f"Failed to save config: {e}")

def detect_joysticks():
    # minimal placeholder – you can extend with pywinusb later
    # We'll just return Logitech for demo
    return ["Logitech Extreme 3D Pro"]

def list_aircraft():
    return sorted([p.name for p in DEFAULT_PROFILES_DIR.iterdir() if p.is_dir()])

def apply_mapping(dcs_path, aircraft, joystick):
    src = DEFAULT_PROFILES_DIR / aircraft / f"{joystick.replace(' ','_')}.diff.lua"
    if not src.exists():
        sg.popup_error(f"Profile not found: {src}")
        return False
    dest_dir = Path(dcs_path) / aircraft / "joystick"
    dest_dir.mkdir(parents=True, exist_ok=True)
    # We don't know device GUID; copy with generic name
    dest = dest_dir / f"{joystick.replace(' ','_')}.diff.lua"
    shutil.copy(src, dest)
    return True

def main():
    cfg = load_config()
    joysticks = detect_joysticks()
    aircraft_list = list_aircraft()

    layout = [
        [sg.Text("Joystick:"), sg.Combo(joysticks, key="-JOY-", default_value=joysticks[0] if joysticks else "", size=(30,1))],
        [sg.Text("Aircraft:"), sg.Listbox(values=aircraft_list, key="-AC-", size=(30,6), select_mode="single")],
        [sg.Text("DCS Saved Games Input path:"), sg.InputText(cfg["dcs_path"], key="-PATH-", size=(50,1)), sg.FolderBrowse()],
        [sg.Button("Apply Mapping"), sg.Button("Exit")],
        [sg.StatusBar("", size=(60,1), key="-STATUS-")]
    ]

    window = sg.Window(f"{APP_NAME}", layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "Apply Mapping":
            joy = values["-JOY-"]
            ac_selected = values["-AC-"]
            if not joy:
                window["-STATUS-"].update("No joystick selected!")
                continue
            if not ac_selected:
                window["-STATUS-"].update("No aircraft selected!")
                continue
            ac = ac_selected[0]
            dcs_path = values["-PATH-"].strip()
            if not dcs_path:
                window["-STATUS-"].update("DCS path not set!")
                continue
            ok = apply_mapping(dcs_path, ac, joy)
            if ok:
                window["-STATUS-"].update(f"Mapped {joy} -> {ac}")
            else:
                window["-STATUS-"].update("Failed!")

    cfg["dcs_path"] = values["-PATH-"]
    save_config(cfg)
    window.close()

if __name__ == "__main__":
    main()
