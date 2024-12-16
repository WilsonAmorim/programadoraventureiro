import flet as ft

def Home(page: ft.Page):
    return ft.Container(
        bgcolor='cyan',
        height=300,
        alignment=ft.alignment.center,
            content=ft.Column([
                ft.Text('Home', size=40),
                ft.ElevatedButton("Ir para o Login", on_click=lambda _: page.go('/login'))
            ]
        )
        
    )