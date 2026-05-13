# GhostType

A lightweight native Windows overlay that lights up keys on a virtual keyboard as you type — globally, across every application. Built to help developers learn touch typing without interrupting their actual work.

---

## What it does

- Sits transparently on top of every app — LeetCode, VS Code, Chrome, anything
- Highlights the key you just pressed in real time
- Never steals focus — your keystrokes always go to the active app
- Remembers its position and visibility between sessions
- Supports all 4 keyboard form factors

---

## Why it exists

Typing tutors like Monkeytype make you stop working to practice. This HUD lets you learn while you actually code. Your muscle memory builds on real code, real variable names, real symbols — not fake sentences.

---

## Supported keyboard form factors

| Form Factor | Keys | Description |
|---|---|---|
| Full Size (100%) | 104 | Has numpad + full navigation cluster |
| Tenkeyless (TKL) | 87 | No numpad, keeps navigation cluster |
| 75% | 84 | Compressed, navigation keys squeezed |
| 60% | 61 | Core keys only, no function row or numpad |

---

## Installation (for users)

Download `TypingHUD-setup.msi` from the [Releases](../../releases) page and run it. No Python required.

---

## Running from source (for developers)

**Requirements:** Python 3.10 or higher, Windows

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/typing-hud.git
cd typing-hud

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python main.py
```

---

## Usage

- The HUD appears in the bottom right corner of your screen on first launch
- **Drag** the top bar to reposition it anywhere
- **Click ×** to hide the HUD (app keeps running in background)
- **Right-click the system tray icon** to show/hide, change opacity, switch form factor, or quit

---

## Project structure

```
typing-hud/
├── main.py                  # Entry point — 3 lines
├── hud/
│   ├── layout.py            # All keyboard layouts and key mappings (pure data)
│   ├── listener.py          # Global keyboard hook via pynput
│   └── window.py            # tkinter overlay, drawing, lighting, drag
├── utils/
│   └── settings.py          # Load/save settings to AppData
├── assets/
│   └── icon.ico             # System tray and taskbar icon
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Building the installer

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Build the exe
pyinstaller --onefile --windowed --icon=assets/icon.ico main.py

# 3. The exe is in dist/main.exe
# 4. Use WiX Toolset or Inno Setup to wrap it into an MSI/installer
```

---

## Settings

Stored automatically at `%APPDATA%\TypingHUD\settings.json`

```json
{
  "visible": true,
  "opacity": 0.82,
  "form_factor": "tkl",
  "position_x": 940,
  "position_y": 820
}
```

---

## Roadmap

- [ ] System tray icon with show/hide toggle
- [ ] Per-session key heatmap
- [ ] Symbol weakness detection
- [ ] Global hotkey to toggle visibility
- [ ] Launch at Windows startup option
- [ ] Layout switching (QWERTY / AZERTY / QWERTZ / Dvorak)
- [ ] MSI installer via WiX Toolset

---

## Tech stack

| Tool | Purpose |
|---|---|
| Python | Language |
| pynput | Global keyboard hook |
| tkinter | Overlay window |
| pystray | System tray icon |
| PyInstaller | Package to .exe |
| WiX Toolset | Build .msi installer |

---

## Platform

Windows only. macOS and Linux support planned for a future version.

---

## License

MIT
