# All keyboard layouts and form factors live here
# No logic — pure data only

# ── Form Factors ──────────────────────────────────────────────────────────────

FULL_SIZE = {
    "name": "Full Size (100%)",
    "rows": [
        ["Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","PrtSc","ScrLk","Pause"],
        ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace","Insert","Home","PgUp","NumLk","/","*","-"],
        ["Tab","q","w","e","r","t","y","u","i","o","p","[","]","\\","Delete","End","PgDn","7","8","9","+"],
        ["Caps","a","s","d","f","g","h","j","k","l",";","'","Enter","4","5","6"],
        ["Shift","z","x","c","v","b","n","m",",",".","/","Shift","Up","1","2","3","Enter"],
        ["Ctrl","Win","Alt","Space","Alt","Fn","Menu","Ctrl","Left","Down","Right","0","."],
    ],
}

TKL = {
    "name": "Tenkeyless (TKL)",
    "rows": [
        ["Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","PrtSc","ScrLk","Pause"],
        ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace","Insert","Home","PgUp"],
        ["Tab","q","w","e","r","t","y","u","i","o","p","[","]","\\","Delete","End","PgDn"],
        ["Caps","a","s","d","f","g","h","j","k","l",";","'","Enter"],
        ["Shift","z","x","c","v","b","n","m",",",".","/","Shift","Up"],
        ["Ctrl","Win","Alt","Space","Alt","Fn","Ctrl","Left","Down","Right"],
    ],
}

SEVENTY_FIVE = {
    "name": "75%",
    "rows": [
        ["Esc","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","Del"],
        ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace","PgUp"],
        ["Tab","q","w","e","r","t","y","u","i","o","p","[","]","\\","PgDn"],
        ["Caps","a","s","d","f","g","h","j","k","l",";","'","Enter","Home"],
        ["Shift","z","x","c","v","b","n","m",",",".","/","Shift","Up","End"],
        ["Ctrl","Win","Alt","Space","Alt","Fn","Left","Down","Right"],
    ],
}

SIXTY = {
    "name": "60%",
    "rows": [
        ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace"],
        ["Tab","q","w","e","r","t","y","u","i","o","p","[","]","\\"],
        ["Caps","a","s","d","f","g","h","j","k","l",";","'","Enter"],
        ["Shift","z","x","c","v","b","n","m",",",".","/","Shift"],
        ["Ctrl","Win","Alt","Space","Alt","Fn","Ctrl"],
    ],
}

FORM_FACTORS = {
    "full":   FULL_SIZE,
    "tkl":    TKL,
    "75":     SEVENTY_FIVE,
    "60":     SIXTY,
}

# ── Key width multipliers ─────────────────────────────────────────────────────

WIDE_KEYS = {
    "Backspace": 2.0, "Tab": 1.5, "Caps": 1.75, "Enter": 2.25,
    "Shift": 2.25, "Ctrl": 1.5, "Alt": 1.5, "Win": 1.5,
    "Space": 6.0, "Fn": 1.5, "Menu": 1.5,
    "PrtSc": 1.5, "ScrLk": 1.5, "Pause": 1.5,
    "NumLk": 1.5,
}

# ── pynput → layout label mapping ────────────────────────────────────────────
# Import pynput.keyboard.Key and map each special key to the label in your rows

SPECIAL_KEY_MAP = {
    "backspace":  "Backspace",
    "tab":        "Tab",
    "caps_lock":  "Caps",
    "enter":      "Enter",
    "shift":      "Shift",
    "shift_r":    "Shift",
    "ctrl_l":     "Ctrl",
    "ctrl_r":     "Ctrl",
    "alt_l":      "Alt",
    "alt_r":      "Alt",
    "cmd":        "Win",
    "cmd_r":      "Win",
    "space":      "Space",
    "esc":        "Esc",
    "f1": "F1",  "f2": "F2",  "f3": "F3",  "f4": "F4",
    "f5": "F5",  "f6": "F6",  "f7": "F7",  "f8": "F8",
    "f9": "F9",  "f10": "F10","f11": "F11","f12": "F12",
    "insert":     "Insert",
    "home":       "Home",
    "page_up":    "PgUp",
    "page_down":  "PgDn",
    "delete":     "Delete",
    "end":        "End",
    "up":         "Up",
    "down":       "Down",
    "left":       "Left",
    "right":      "Right",
    "num_lock":   "NumLk",
    "print_screen": "PrtSc",
    "scroll_lock":  "ScrLk",
    "pause":        "Pause",
}
