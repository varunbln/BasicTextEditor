import tkinter as tk
from utils import io_utils


class EditorWindow:
    root = tk.Tk("Basic Text Editor")

    navbar = tk.Menu(root, background="#485092")
    file_menu = tk.Menu(navbar, tearoff=0)
    edit_menu = tk.Menu(navbar, tearoff=0)
    about_menu = tk.Menu(navbar, tearoff=0)

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
        self.root.config(menu=self.navbar)
        self.populate_file_options()
        self.populate_edit_options()
        self.populate_about_options()

    def init_scrollbar(self):
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.text.yview)

    def configure_textbox(self):
        self.text.configure(font=("Ariel", 14), bg="#21044D", fg="white", insertbackground="#e7e6f1")
        self.text.pack(fill=tk.BOTH, expand=True)

    def populate_file_options(self):
        self.file_menu.add_command(label="New", command=lambda: io_utils.new_and_save(self))
        self.file_menu.add_command(label="Open", command=lambda: io_utils.open_file(self))
        self.file_menu.add_command(label="Save", command=lambda: io_utils.save(self))

        self.file_menu.entryconfig(0, background="#6b72ae", font=("Ariel", 12))
        self.file_menu.entryconfig(1, background="#6b72ae", font=("Ariel", 12))
        self.file_menu.entryconfig(2, background="#6b72ae", font=("Ariel", 12))

        self.navbar.add_cascade(label="File", menu=self.file_menu)

    def populate_edit_options(self):
        self.edit_menu.add_command(label="Find", command=lambda: io_utils.save(self))
        self.edit_menu.add_command(label="Replace", command=lambda: io_utils.save(self))
        self.edit_menu.add_command(label="Rename", command=lambda: io_utils.save(self))

        self.edit_menu.entryconfig(0, background="#6b72ae", font=("Ariel", 12))
        self.edit_menu.entryconfig(1, background="#6b72ae", font=("Ariel", 12))
        self.edit_menu.entryconfig(2, background="#6b72ae", font=("Ariel", 12))

        self.navbar.add_cascade(label="Edit", menu=self.edit_menu)

    def populate_about_options(self):
        self.about_menu.add_command(label="About", command=lambda: io_utils.save(self))
        self.about_menu.add_command(label="Help", command=lambda: io_utils.save(self))

        self.about_menu.entryconfig(0, background="#6b72ae", font=("Ariel", 12))
        self.about_menu.entryconfig(1, background="#6b72ae", font=("Ariel", 12))

        self.navbar.add_cascade(label="About", menu=self.about_menu)