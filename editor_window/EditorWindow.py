import tkinter as tk
from utils import io_utils


class EditorWindow:
    root = tk.Tk("Basic Text Editor")
    button_frame = tk.Frame(root, background="#485092")
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
        self.button_frame.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(self.button_frame, height=2, width=10, text="Save", bg="#9095bd", command=lambda: io_utils.save(self)).grid(row=0, column=0)
        tk.Button(self.button_frame, height=2, width=10, text="Find", bg="#9095bd").grid(row=0, column=1)

    def init_scrollbar(self):
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.text.yview)

    def configure_textbox(self):
        self.text.configure(font=("Ariel", 14), bg="#21044D", fg="white", insertbackground="#e7e6f1")
        self.text.pack(fill=tk.BOTH, expand=True)
