import tkinter as tk
from utils import io_utils


class EditorWindow:
    root = tk.Tk("Basic Text Editor")
    buttonframe = tk.Frame(root)
    scrollbar = tk.Scrollbar(root)
    text = tk.Text(root, yscrollcommand=scrollbar.set)
    file_name = None

    def __init__(self):
        self.root.wm_title("Basic Text Editor")
        self.populate()
        self.register_shortcuts()
        self.root.mainloop()

    def populate(self):
        self.populate_navbar()
        self.init_scrollbar()
        self.configure_textbox()

    def register_shortcuts(self):
        self.root.bind('<Control-s>', (lambda event: io_utils.save(self)))

    def populate_navbar(self):
        self.buttonframe.pack(side=tk.TOP, fill=tk.Y)
        tk.Button(self.buttonframe, height=2, width=10, text="Save", command=lambda: io_utils.save(self)).grid(row=0, column=0)
        tk.Button(self.buttonframe, height=2, width=10, text="Find").grid(row=0, column=1)

    def init_scrollbar(self):
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.text.yview)

    def configure_textbox(self):
        self.text.configure(font=("Ariel", 14))
        self.text.pack(fill=tk.BOTH, expand=True)
