import tkinter as tk
from enhanced_menu_library import EnhancedMenuLibrary

def on_toggle_change(value):
    print(f"Toggle is {'on' if value else 'off'}")

def on_slider_change(value):
    print(f"Slider value: {value}")

def main():
    theme = {
        'Background': '#f0f0f0',
        'ElementColor': '#009688',
        'TextColor': '#000000'
    }

    app = EnhancedMenuLibrary(title="Toggle and Slider Example", theme=theme)
    tab = app.new_tab("Controls Tab")
    section = tab.new_section("Controls Section", 0)
    section.new_toggle("Toggle Me", on_toggle_change)
    section.new_slider("Adjust Me", 100, 0, on_slider_change)
    app.run()

if __name__ == "__main__":
    main()
