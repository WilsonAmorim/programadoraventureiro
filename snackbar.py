import flet as ft

def main(page: ft.Page):
    page.snack_bar = ft.SnackBar(
        content=ft.Text(value='Não foi possivel process'),
        bgcolor=ft.colors.RED_100,
        show_close_icon=True,
        close_icon_color=ft.colors.RED,
        padding=ft.padding.all(10),
        duration=4000,
    )

    page.snack_bar.open=True
    page.update()


if __name__ == '__main__':
    ft.app(target=main)