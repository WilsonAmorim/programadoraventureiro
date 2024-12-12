import flet as ft
    
def main(page: ft.Page):
    btn1 = ft.IconButton(
        icon=ft.DELETE_FOREVER_ROUNDED,
        icon_color=ft.colors.PINK,
        icon_size=30,
        tooltip='Deletar ação',
    )
    
    def play_pause(e):
        e.control.selected = not e.control.selected
        e.control.update()
        
    btn2 = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE,
        selected_icon=ft.icons.PAUSE_CIRCLE,
        selected=False,
        icon_size=150,
        on_click=play_pause,
        style=ft.ButtonStyle(
            color={
            ft.MaterialState.SELECTED: ft.colors.BLUE,
            ft.MaterialState.DEFAULT: ft.colors.RED,
        })
    )
    
    page.add(btn1, btn2)
    
ft.app(target=main)
