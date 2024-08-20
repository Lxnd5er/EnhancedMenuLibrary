import tkinter as tk
from tkinter import colorchooser

class EnhancedMenuLibrary:
    def __init__(self, title, theme):
        self.root = tk.Tk()
        self.root.title(title)
        self.theme = theme
        self.root.configure(bg=theme['Background'])
        self.widgets = {}

        self.content_frame = tk.Frame(self.root, bg=self.theme['Background'])
        self.content_frame.pack(fill='both', expand=True)

        self.root.update_idletasks()
        self.root.minsize(self.content_frame.winfo_reqwidth(), self.content_frame.winfo_reqheight())
        self.root.resizable(True, True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def new_tab(self, name):
        frame = tk.Frame(self.content_frame, bg=self.theme['Background'])
        frame.pack(fill='both', expand=True)
        self.widgets[name] = frame
        return Tab(frame, self)

    def run(self):
        self.root.update_idletasks()
        self.root.geometry(f"{self.content_frame.winfo_reqwidth()}x{self.content_frame.winfo_reqheight()}")
        self.root.mainloop()

    def on_close(self):
        self.root.destroy()

    def set_theme(self, theme):
        self.theme = theme
        self.root.configure(bg=theme['Background'])
        self.content_frame.configure(bg=theme['Background'])

class Tab:
    def __init__(self, frame, library):
        self.frame = frame
        self.library = library

    def new_section(self, name, column):
        section_frame = tk.LabelFrame(self.frame, text=name, bg=self.library.theme['Background'])
        section_frame.grid(row=column // 2, column=column % 2, padx=10, pady=10, sticky='nsew')
        return Section(section_frame, self.library)

class Section:
    def __init__(self, frame, library):
        self.frame = frame
        self.library = library
        self.current_row = 0

    def new_button(self, text, command):
        button = tk.Button(self.frame, text=text, command=command, bg=self.library.theme['ElementColor'], fg=self.library.theme['TextColor'])
        button.grid(row=self.current_row, column=0, padx=5, pady=5, sticky='ew')
        self.current_row += 1
        return button

    def new_toggle(self, text, command):
        self.toggle_var = tk.BooleanVar()
        toggle_button = tk.Checkbutton(self.frame, text=text, variable=self.toggle_var, onvalue=True, offvalue=False, command=lambda: command(self.toggle_var.get()), bg=self.library.theme['ElementColor'], fg=self.library.theme['TextColor'], selectcolor=self.library.theme['ElementColor'])
        toggle_button.grid(row=self.current_row, column=0, padx=5, pady=5, sticky='ew')
        toggle_button.config(highlightthickness=0, relief='flat')
        self.current_row += 1
        return toggle_button

    def new_slider(self, text, max_val, min_val, command):
        slider = tk.Scale(self.frame, from_=min_val, to=max_val, orient='horizontal', bg=self.library.theme['ElementColor'], fg=self.library.theme['TextColor'], command=lambda val: command(float(val)))
        slider.grid(row=self.current_row, column=0, padx=5, pady=5, sticky='ew')
        self.current_row += 1
        return slider

    def new_textbox(self):
        textbox = tk.Entry(self.frame, bg=self.library.theme['ElementColor'], fg=self.library.theme['TextColor'])
        textbox.grid(row=self.current_row, column=0, padx=5, pady=5, sticky='ew')
        self.current_row += 1
        return textbox

    def new_keybind(self, key, command):
        self.frame.bind(f'<KeyPress-{key}>', lambda event: command())
        return None

    def new_dropdown(self, text, options, command):
        self.dropdown_var = tk.StringVar(self.frame)
        self.dropdown_var.set(options[0])
        dropdown_menu = tk.OptionMenu(self.frame, self.dropdown_var, *options, command=command)
        dropdown_menu.config(bg=self.library.theme['ElementColor'], fg=self.library.theme['TextColor'])
        dropdown_menu.grid(row=self.current_row, column=0, padx=5, pady=5, sticky='ew')
        self.current_row += 1
        return dropdown_menu

    def new_color_picker(self, text, default_color, command):
        def choose_color():
            color = colorchooser.askcolor(initialcolor=default_color)[1]
            if color:
                command(color)
        color_picker_button = tk.Button(self.frame, text=text, command=choose_color, bg=self.library.theme['ElementColor'], fg=self.library.theme['TextColor'])
        color_picker_button.grid(row=self.current_row, column=0, padx=5, pady=5, sticky='ew')
        self.current_row += 1
        return color_picker_button

    def update_dropdown(self, dropdown, new_options):
        menu = dropdown['menu']
        menu.delete(0, 'end')
        for option in new_options:
            menu.add_command(label=option, command=tk._setit(self.dropdown_var, option))
        self.dropdown_var.set(new_options[0])
        return dropdown