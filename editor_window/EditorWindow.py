import tkinter as tk
from utils import io_utils


class EditorWindow:
    root = tk.Tk("Basic Text Editor")
    text = tk.Text(root)
    button = tk.Button(root, text="Save")
    file_name = None

    def __init__(self):
        self.root.wm_title("Basic Text Editor")
        self.populate()
        self.register_shortcuts()
        self.root.mainloop()

    def populate(self):
        self.text.grid()
        self.button.configure(text="Save", command=lambda: io_utils.save(self))
        self.button.grid()

    def register_shortcuts(self):
        self.root.bind('<Control-s>', (lambda event: io_utils.save(self)))
