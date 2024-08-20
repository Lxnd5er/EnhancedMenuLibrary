import tkinter as tk
from enhanced_menu_library import EnhancedMenuLibrary

def on_button_click():
    print("Button clicked!")

def main():
    theme = {
        'Background': '#ffffff',
        'ElementColor': '#000000',
        'TextColor': '#000000'
    }

    app = EnhancedMenuLibrary(title="Simple Button Example", theme=theme)
    tab = app.new_tab("Button Tab")
    section = tab.new_section("Button Section", 0)
    section.new_button("Click Me", on_button_click)
    app.run()

if __name__ == "__main__":
    main()
