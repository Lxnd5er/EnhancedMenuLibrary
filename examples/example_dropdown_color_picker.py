import tkinter as tk
from enhanced_menu_library import EnhancedMenuLibrary

def on_dropdown_change(value):
    print(f"Dropdown selection: {value}")

def on_color_pick(color):
    print(f"Selected color: {color}")

def main():
    theme = {
        'Background': '#ffffff',
        'ElementColor': '#3f51b5',
        'TextColor': '#000000'
    }

    app = EnhancedMenuLibrary(title="Dropdown and Color Picker Example", theme=theme)
    tab = app.new_tab("Options Tab")
    section = tab.new_section("Options Section", 0)
    section.new_dropdown("Choose Option", ["Option 1", "Option 2", "Option 3"], on_dropdown_change)
    section.new_color_picker("Pick a Color", "#ff0000", on_color_pick)
    app.run()

if __name__ == "__main__":
    main()
