import tkinter as tk
from enhanced_menu_library import EnhancedMenuLibrary

def on_textbox_submit():
    text = textbox.get()
    print(f"Textbox input: {text}")

def main():
    theme = {
        'Background': '#e0e0e0',
        'ElementColor': '#4caf50',
        'TextColor': '#000000'
    }

    app = EnhancedMenuLibrary(title="Textbox and Button Example", theme=theme)
    tab = app.new_tab("Textbox Tab")
    section = tab.new_section("Textbox Section", 0)
    global textbox
    textbox = section.new_textbox()
    section.new_button("Submit Text", on_textbox_submit)
    app.run()

if __name__ == "__main__":
    main()
