import flet as ft
def abrir_menu(e):
    print('aqui')

def main(page: ft.Page):
    btn = ft.TextButton(
        text="Editar",
        icon=ft.icons.EDIT,
        icon_color=ft.colors.WHITE,
        url='https://programadoraventureiro.com',
    )
    btn1 = ft.TextButton("Abrir Menu", on_click=abrir_menu)
    page.add(btn,btn1)
    
ft.app(target=main)