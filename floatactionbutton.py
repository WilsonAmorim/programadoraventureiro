import flet as ft


def main(page: ft.Page):
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.DELETE,
        bgcolor=ft.colors.AMBER,
        mini=True,
        on_click=lambda _: print('Fui')
    )
    
    
    page.update()
    # page.add(
    #     ft.Container(
    #         content=ft.FloatingActionButton(text='BOtão'),
    #         bgcolor=ft.colors.RED,
    #         expand=True,
    #         alignment=ft.Alignment(x=1, y=-1)
    #     )
    # )
    
ft.app(target=main)
