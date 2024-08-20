# EnhancedMenuLibrary

A Python library for creating enhanced Tkinter menus and widgets.

## Installation

To install the library, you can download the repository and use it directly in your project.

## Usage

Here's a basic example of how to use the library:

```python
import tkinter as tk
from enhanced_menu_library import EnhancedMenuLibrary

def on_button_click():
    print("Button clicked!")

def main():
    theme = {
        'Background': '#2b2b2b',
        'ElementColor': '#3c3f41',
        'TextColor': '#ffffff'
    }

    app = EnhancedMenuLibrary(title="Full Feature Demo", theme=theme)

    tab1 = app.new_tab("Controls Demo")
    section1 = tab1.new_section("Text Elements", 0)
    section1.new_button("Click Me", on_button_click)

    app.run()

if __name__ == "__main__":
    main()
