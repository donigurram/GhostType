# Global keyboard listener — knows nothing about tkinter
# Communicates with the window only through the on_press/on_release callbacks

import threading
from pynput import keyboard
from hud.layout import SPECIAL_KEY_MAP


class KeyListener:
    def __init__(self, on_press, on_release):
        self._on_press_cb = on_press
        self._on_release_cb = on_release
        self._thread = None

    def start(self):
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _run(self):
        with keyboard.Listener(
            on_press=self._handle_press,
            on_release=self._handle_release,
            suppress=False,  # NEVER suppress — keys still go to every app
        ) as listener:
            listener.join()

    def _resolve(self, key):
        # Special key (Enter, Shift, F1, etc.)
        try:
            name = key.name  # pynput Key enum name
            return SPECIAL_KEY_MAP.get(name)
        except AttributeError:
            pass
        # Regular character key
        try:
            if key.char:
                return key.char.lower()
        except AttributeError:
            pass
        return None

    def _handle_press(self, key):
        label = self._resolve(key)
        if label:
            self._on_press_cb(label)

    def _handle_release(self, key):
        label = self._resolve(key)
        if label:
            self._on_release_cb(label)
