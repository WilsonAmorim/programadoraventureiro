import flet as ft

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.PINK,
        ),

        tabs_theme=ft.TextTheme(
            title_large=ft.TextStyle(size=50, weight=ft.FontWeight.W_900),
        )
    )

    page.add(
        ft.Container(
            height=100,
            width=200,
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(value='Título',style=ft.TextThemeStyle.TITLE_LARGE),
                    ft.ElevatedButton(text='Botão', color=ft.colors.AMBER),
                ],
            ),
            bgcolor=ft.colors.PRIMARY,
            expand=True,
        ),

    )

ft.app(target=main, assets_dir='assets')