import flet as ft
    
def main(page: ft.Page):
    container = ft.Container(
        # height=100,
        # width=200,
        image_src='images/logoPrimeiroe.jpg',
        expand=True,
        # margin=ft.margin.only(top=100, left=10, right=30, bottom=100),
        margin=ft.margin.all(30),
        # border=ft.border.all(width=10, color=ft.Colors.RED),
        # border=ft.border.only(
        #     top=ft.BorderSide(width=15, color=ft.colors.PINK),
        #     left=ft.BorderSide(width=15, color=ft.colors.ORANGE),
        #     right=ft.BorderSide(width=10, color=ft.colors.GREEN),
        #     bottom=ft.BorderSide(width=30, color=ft.colors.YELLOW),
        #     ),
        # border=ft.border.symmetric(
        #     vertical= ft.BorderSide(width=15, color=ft.colors.PINK),
        #     horizontal= ft.BorderSide(width=5, color=ft.colors.AMBER),
        # ),
        # border_radius=ft.border_radius.horizontal(left=10, right=40),
        # border_radius=ft.border_radius.vertical(top=40, bottom=100),
        border_radius=ft.border_radius.all(30),
        # border_radius=ft.border_radius.only(
        #     top_left=10, 
        #     top_right=50,
        #     bottom_left=100,
        #     bottom_right=10),

        content=ft.Row(
            controls=[
                ft.ElevatedButton(text='Texto 1'),
                ft.ElevatedButton(text='Texto 2'),
                ft.ElevatedButton(text='Texto 3'),
                ft.ElevatedButton(text='Texto 4'),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.top_center,
        padding=ft.padding.all(20),
        shape=ft.BoxShape.RECTANGLE,

        bgcolor=ft.colors.BLUE,
        
    )
   
    page.add(container)
    
ft.app(target=main, assets_dir='assets')