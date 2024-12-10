import flet as ft
    
def main(page: ft.Page):
    btn1 = ft.OutlinedButton(
        text='Botão terciario',
        icon = ft.icons.ZOOM_IN,
        icon_color=ft.colors.TEAL,
        tooltip='Clique aqui',
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
        url='https://programadoraventureiro.com',
        on_click=lambda _: print('fui')
        
        
    )
    
       
   
    
    page.add(btn1)
    
ft.app(target=main)