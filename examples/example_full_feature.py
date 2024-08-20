import tkinter as tk
from enhanced_menu_library import EnhancedMenuLibrary

def on_button_click():
    print("Button clicked!")

def on_toggle_change(value):
    print(f"Toggle is {'on' if value else 'off'}")

def on_slider_change(value):
    print(f"Slider value: {value}")

def on_textbox_submit():
    text = textbox.get()
    print(f"Textbox input: {text}")

def on_keybind():
    print("Keybind 'a' pressed!")

def on_dropdown_change(value):
    print(f"Dropdown selection: {value}")

def on_color_pick(color):
    print(f"Selected color: {color}")

def main():
    theme = {
        'Background': '#ffffff',
        'ElementColor': '#2196f3',
        'TextColor': '#000000'
    }

    app = EnhancedMenuLibrary(title="Full Feature Example", theme=theme)
    tab = app.new_tab("All Controls")
    section = tab.new_section("Full Section", 0)
    section.new_button("Click Me", on_button_click)
    section.new_toggle("Toggle Me", on_toggle_change)
    section.new_slider("Slide Me", 100, 0, on_slider_change)
    global textbox
    textbox = section.new_textbox()
    section.new_button("Submit Text", on_textbox_submit)
    section.new_keybind("a", on_keybind)
    section.new_dropdown("Choose Option", ["Option 1", "Option 2", "Option 3"], on_dropdown_change)
    section.new_color_picker("Pick a Color", "#00ff00", on_color_pick)
    app.run()

if __name__ == "__main__":
    main()
