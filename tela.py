import flet as ft

def main(page: ft.Page):
    container = ft.Container(
        height=100,
        width=900,
        #image_src='images/logoPrimeiroe.jpg',
        #expand=True,
        margin=ft.margin.all(10),
        #border=ft.border.all(width=10, color=ft.colors.RED),
        # border=ft.border.only(
        #     top=ft.BorderSide(width=1, color=ft.colors.PINK),
        #     left=ft.BorderSide(width=1, color=ft.colors.PINK),
        #     right=ft.BorderSide(width=1, color=ft.colors.PINK),
        #     bottom=ft.BorderSide(width=1, color=ft.colors.PINK),
        # ),
        # border=ft.border.symmetric(
        #     vertical=ft.BorderSide(width=12, color=ft.colors.PINK),
        #     horizontal=ft.BorderSide(width=5, color=ft.colors.AMBER)
        # ),
        border_radius=ft.border_radius.all(100),
        # border_radius=ft.border_radius.only(
        #     top_left=10,
        #     top_right=50,
        #     bottom_left=100,
        #     bottom_right=10,
        # ),

        content=ft.Row(
             
            controls=[
                ft.ElevatedButton(text='Texto 1'),
                ft.ElevatedButton(text='Texto 2'),
                ft.ElevatedButton(text='Texto 3'),
                ft.ElevatedButton(text='Texto 4'),
            ],
        ),
        alignment=ft.alignment.center,
        # padding=ft.padding.all(40),
        padding=ft.padding.symmetric(horizontal=20),
        bgcolor=ft.colors.WHITE,
        shape=ft.BoxShape.RECTANGLE,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.BLUE_GREY_100, ft.colors.BLUE_50],
        ),
        shadow=ft.BoxShadow(
            spread_radius=10,
            blur_radius=10,
            color=ft.colors.BLUE_50,
            blur_style=ft.ShadowBlurStyle.OUTER,
            offset=ft.Offset(x=0, y=0),
        ),
    )

    page.add(container)

ft.app(target=main, assets_dir='assets')