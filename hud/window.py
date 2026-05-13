# All tkinter logic lives here
# Talks to listener only through callbacks — never imports pynput directly

import tkinter as tk
from hud.layout import FORM_FACTORS, WIDE_KEYS
from hud.listener import KeyListener
from utils.settings import load_settings, save_settings

KEY_W   = 38
KEY_H   = 36
GAP     = 4
PAD     = 12
RADIUS  = 5

BG          = "#0d0f16"
KEY_IDLE    = "#1c2030"
KEY_BORDER  = "#2e3448"
KEY_LIT     = "#1a5cff"
KEY_LIT_BDR = "#5aacff"
TEXT_IDLE   = "#8a90a8"
TEXT_LIT    = "#ffffff"


class TypingHUD:
    def __init__(self):
        self.settings  = load_settings()
        self.visible   = self.settings.get("visible", True)
        self.opacity   = self.settings.get("opacity", 0.82)
        self.form      = self.settings.get("form_factor", "tkl")

        self.root = tk.Tk()
        self.root.title("Typing HUD")
        self.root.configure(bg=BG)
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", self.opacity)

        self._key_items = {}   # label → (canvas, rect_id, text_id)
        self._lit       = None
        self._drag_x    = 0
        self._drag_y    = 0

        self._build_ui()
        self._restore_position()
        if not self.visible:
            self.root.withdraw()

        self._listener = KeyListener(
            on_press=lambda label: self.root.after(0, self._light, label),
            on_release=lambda label: self.root.after(250, self._unlight, label),
        )
        self._listener.start()
        self.root.protocol("WM_DELETE_WINDOW", self._quit)
        self.root.mainloop()

    # ── build ──────────────────────────────────────────────────────────────────

    def _build_ui(self):
        layout = FORM_FACTORS[self.form]
        outer  = tk.Frame(self.root, bg=BG, padx=PAD, pady=PAD)
        outer.pack()

        # drag bar
        bar = tk.Frame(outer, bg=BG)
        bar.pack(fill="x", pady=(0, 8))
        tk.Label(bar, text="● ● ●", bg=BG, fg="#3a4060", font=("Courier", 9)).pack(side="left")
        close_btn = tk.Label(bar, text="×", bg=BG, fg="#555e7a",
                             font=("Courier", 13, "bold"), cursor="hand2")
        close_btn.pack(side="right")
        close_btn.bind("<Button-1>", lambda e: self._hide())
        close_btn.bind("<Enter>",    lambda e: close_btn.config(fg="#ff5f57"))
        close_btn.bind("<Leave>",    lambda e: close_btn.config(fg="#555e7a"))

        for widget in [bar] + bar.winfo_children():
            widget.bind("<ButtonPress-1>",   self._drag_start)
            widget.bind("<B1-Motion>",       self._drag_move)

        # keyboard rows
        self._key_items = {}
        for row in layout["rows"]:
            row_frame = tk.Frame(outer, bg=BG)
            row_frame.pack(pady=(0, GAP))
            for label in row:
                mult = WIDE_KEYS.get(label, 1.0)
                w    = int(KEY_W * mult)
                c    = tk.Canvas(row_frame, width=w, height=KEY_H,
                                 bg=BG, highlightthickness=0)
                c.pack(side="left", padx=(0, GAP))
                r = self._rrect(c, 0, 0, w, KEY_H, RADIUS, KEY_IDLE, KEY_BORDER)
                t = c.create_text(w // 2, KEY_H // 2, text=label,
                                  fill=TEXT_IDLE, font=("Courier", 8))
                # Multiple rows can have same label (two Shifts) — store list
                self._key_items.setdefault(label, []).append((c, r, t))

    def _rrect(self, canvas, x1, y1, x2, y2, r, fill, outline):
        pts = [x1+r,y1, x2-r,y1, x2,y1, x2,y1+r,
               x2,y2-r, x2,y2, x2-r,y2, x1+r,y2,
               x1,y2, x1,y2-r, x1,y1+r, x1,y1]
        return canvas.create_polygon(pts, smooth=True, fill=fill,
                                     outline=outline, width=1)

    # ── lighting ───────────────────────────────────────────────────────────────

    def _light(self, label):
        if self._lit and self._lit in self._key_items:
            for c, r, t in self._key_items[self._lit]:
                c.itemconfig(r, fill=KEY_IDLE, outline=KEY_BORDER)
                c.itemconfig(t, fill=TEXT_IDLE)
        if label in self._key_items:
            for c, r, t in self._key_items[label]:
                c.itemconfig(r, fill=KEY_LIT, outline=KEY_LIT_BDR)
                c.itemconfig(t, fill=TEXT_LIT)
        self._lit = label

    def _unlight(self, label):
        if label in self._key_items:
            for c, r, t in self._key_items[label]:
                c.itemconfig(r, fill=KEY_IDLE, outline=KEY_BORDER)
                c.itemconfig(t, fill=TEXT_IDLE)
        if self._lit == label:
            self._lit = None

    # ── visibility ─────────────────────────────────────────────────────────────

    def _hide(self):
        self.visible = False
        self.root.withdraw()
        self._save()

    def show(self):
        self.visible = True
        self.root.deiconify()
        self._save()

    # ── drag ───────────────────────────────────────────────────────────────────

    def _drag_start(self, e):
        self._drag_x = e.x_root - self.root.winfo_x()
        self._drag_y = e.y_root - self.root.winfo_y()

    def _drag_move(self, e):
        self.root.geometry(f"+{e.x_root - self._drag_x}+{e.y_root - self._drag_y}")

    # ── settings ───────────────────────────────────────────────────────────────

    def _restore_position(self):
        self.root.update_idletasks()
        x = self.settings.get("position_x", 100)
        y = self.settings.get("position_y", 100)
        self.root.geometry(f"+{x}+{y}")

    def _save(self):
        save_settings({
            "visible":     self.visible,
            "opacity":     self.opacity,
            "form_factor": self.form,
            "position_x":  self.root.winfo_x(),
            "position_y":  self.root.winfo_y(),
        })

    def _quit(self):
        self._save()
        self.root.destroy()
