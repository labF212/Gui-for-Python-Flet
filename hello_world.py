import flet as ft

def main(page: ft.Page):
    # Set page title
    page.title = "Hello, World!"
    
    # Create title text widget
    txt = ft.Text(value="Hello, World in Flet - A GUI por Python",text_align="CENTER",weight="BOLD")
    txt.alignment = ft.MainAxisAlignment.CENTER
    
    page.controls.append(txt)
    page.update()

ft.app(target=main)