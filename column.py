import flet as ft
    
def main(page: ft.Page):
    col1 = ft.Column(
        controls=[
            ft.ElevatedButton(text='1', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.RED, color=ft.colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.AMBER, color=ft.colors.WHITE),

            ft.ElevatedButton(text='1', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        # spacing=20,
        wrap=True,
        run_spacing=50,
        horizontal_alignment=ft.CrossAxisAlignment.END,
    )
    # page.add(col1)
    page.add(
        ft.Container(col1, bgcolor=ft.colors.AMBER_100, expand=True),
        ft.Container(col1, bgcolor=ft.colors.BLACK, expand=True))
    
ft.app(target=main, assets_dir='assets')