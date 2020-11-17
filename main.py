#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import os

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_vars()
        self.init_widgets()
        self.init_events()

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def init_vars(self):
        pass

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(False, False)
        self.title('File Browser Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Window Events / Keyboard Shorcuts
    #-------------------------------------------
    def init_events(self):
        self.listbox.bind('<Double-Button>', self.evt_open_file)
        self.entry.bind('<Return>', lambda x: self.evt_search_files('.png', self.filepath.get()))

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.fieldset = ttk.LabelFrame(self.frame, text='Search File Path')
        self.fieldset.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.filepath = tk.StringVar()
        self.entry = ttk.Entry(self.fieldset, width=100, textvariable=self.filepath)
        self.entry.pack(side=tk.TOP, fill=tk.X, expand=True, padx=5, pady=5)
        self.entry.focus()

        button = ttk.Button(self.fieldset, text='Clear', command=self.ins_clear)
        button.pack(side=tk.RIGHT, padx=(0, 5), pady=(0, 5))

        button = ttk.Button(self.fieldset, text='Search', command=lambda: self.evt_search_files('.png', self.filepath.get()))
        button.pack(side=tk.RIGHT, padx=(0, 5), pady=(0, 5))

        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    # INSTANCE ---------------------------------
    def ins_clear(self):
        self.listbox.delete(0, tk.END)

    # EVENTS -----------------------------------
    def evt_search_files(self, extension='.txt', folder='C:/'):
        """Insert all files in the listbox."""
        container = []
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    container.append(os.path.join(r, file))

        for file in container:
            self.listbox.insert(0, file)

    def evt_open_file(self, event=None):
        os.startfile(self.listbox.get(self.listbox.curselection()[0]))


#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()