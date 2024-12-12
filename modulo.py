import flet as ft
    
def main(page: ft.Page):
    page.title = 'modulo.py'
    page.update()

ft.app(target=main, assets_dir='assets')