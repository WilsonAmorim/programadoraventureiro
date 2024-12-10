import flet as ft

    
def main(page: ft.Page):
    btn1 = ft.FilledTonalButton(text='Botão segundario')
    
    page.add(
             ft.FilledTonalButton(text='Botão segundario'),
             ft.FilledTonalButton(text='Botão segundario', disabled=True),
             ft.FilledTonalButton(text='Botão segundario', icon=ft.icons.ADD),
             ft.FilledTonalButton(text='Botão segundario', icon=ft.icons.ADD, icon_color=ft.colors.GREEN),
             ft.FilledTonalButton(text='Botão segundario', tooltip='Ação não permitida', disabled=True),
             ft.FilledTonalButton(text='Botão segundario', style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))),
             )
    
ft.app(target=main)