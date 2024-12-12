import flet as ft
    
def main(page: ft.Page):
    btn1 = ft.OutlinedButton(
        text='Botão terciario',
        icon = 'Editar',
        icon_color=ft.colors.TEAL,
        tooltip='Clique aqui',
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
        url='https://programadoraventureiro.com',
        on_click=lambda _: print('fui')
        
        
    ),
    # btn2 = ft.OutlinedButton(icon="edit", icon_color="blue", title="Editar Perfil")
    page.add(btn1)
    
ft.app(target=main)