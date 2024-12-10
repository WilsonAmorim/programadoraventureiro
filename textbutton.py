import flet as ft

def main(page: ft.Page):
    btn = ft.TextButton(
        text="Editar",
        icon=ft.icons.EDIT,
        icon_color=ft.colors.WHITE,
        url='https://programadoraventureiro.com',
    )
    page.add(btn)
    
ft.app(target=main)