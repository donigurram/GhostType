# Saves and loads user settings from AppData/Roaming/TypingHUD/settings.json

import json
import os
from pathlib import Path

DEFAULTS = {
    "visible":     True,
    "opacity":     0.82,
    "form_factor": "tkl",
    "position_x":  100,
    "position_y":  100,
}


def _settings_path() -> Path:
    appdata = os.getenv("APPDATA") or Path.home()
    folder  = Path(appdata) / "TypingHUD"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "settings.json"


def load_settings() -> dict:
    path = _settings_path()
    if not path.exists():
        return DEFAULTS.copy()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Fill in any missing keys with defaults
        return {**DEFAULTS, **data}
    except (json.JSONDecodeError, OSError):
        return DEFAULTS.copy()


def save_settings(data: dict):
    path = _settings_path()
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError:
        pass
