
# FlightCommander

FlightCommander is a lightweight Windows utility that automatically applies
Logitech Extreme 3D Pro joystick mappings to any aircraft module in DCS World.

## Features
* Detects Logitech Extreme 3D Pro joystick
* Lists all aircraft profiles shipped in `profiles/`
* Copies the corresponding `.diff.lua` file to your DCS `Saved Games` input folder
* Persists your DCS path selection
* One‑click mapping

## Usage
1. Unzip the package.
2. Double‑click `FlightCommander.exe` (or run `python main.py` if you have Python).
3. Select your joystick and aircraft, browse to your `Saved Games\DCS\Config\Input`
   if it is not auto‑detected, then hit **Apply Mapping**.

## Building your own EXE
```bash
pip install -r requirements.txt
pyinstaller --onefile main.py
```

## Adding Profiles
Add more `.diff.lua` files here:

```
profiles/<AircraftName>/Logitech_Extreme_3D_Pro.diff.lua
```
You can export your own bindings from DCS and drop them in that location.

Enjoy and fly safe!
