import flet as ft
    
def main(page: ft.Page):
    page.theme = ft.Theme(color_scheme_seed="green")

    page.update()
    # page.add()
    
ft.app(target=main, assets_dir='assets')