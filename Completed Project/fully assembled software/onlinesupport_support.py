

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global spinbox1
    spinbox1 = tk.StringVar()
    global spinbox2
    spinbox2 = tk.StringVar()
    global spinbox3
    spinbox3 = tk.StringVar()
    global spinbox4
    spinbox4 = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import modificationmainpage
    modificationmainpage.vp_start_gui()




