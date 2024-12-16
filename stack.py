import flet as ft 

def main(page: ft.Page):
    st = ft.Stack(
        controls=[
            ft.Container(
                image_src='https://files.tecnoblog.net/wp-content/uploads/2022/11/logotipo-linguagem-python.jpg',
                image_fit=ft.ImageFit.COVER,
            ),
            ft. Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_left,
                    colors=[ft.colors.TEAL, ft.colors.CYAN],
                ),
                opacity=0.5,
            ),
            ft.Text(value='Texto sobreposto', style=ft.TextThemeStyle.HEADLINE_LARGE),
            ft.Column(
                # top=0,
                left=100,
                right=100,
                bottom=100,
                controls=[
                    ft.Text(value='Curso de Flet', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value='Aprenda', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text='Saiba mas'),
                ],
            ),
        ],
        aspect_ratio=1.0
        # expand=True,
    )

    page.add(st)
if __name__ == '__main__':
    ft.app(target=main)