import flet as ft

def main(page: ft.Page):
    page.fonts = {
        'Kanit': 'https://raw.githubusercontent.com/google/fonts/master/ofl/Kanit-Bold.ttf',
        'Super Arena': 'fonts/Super Arena.ttf'

    }

  
    te1 = ft.Text(
        value='Ola, seja bem vindo',
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        font_family= 'Super Arena',
        italic=True,
        max_lines=2,
       #overflow= ft.TextOverflow.ELLIPSIS,
       #no_wrap=True,
       selectable=True,
       #size= 10,
       text_align=ft.TextAlign.CENTER,
       weight=ft.FontWeight.W_200,
    )

    link_style = ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)
    te2 = ft.Text(
        spans = [
                 ft.TextSpan(text='Texto com link ', style=link_style, url='https://programadoraventureiro.com'),
                 ft.TextSpan(text='Copntinuação do texto.. '),
                 ft.TextSpan(text='Texto em destaque!!! ', style=link_style),
             ]
    )

    page.add(te1, te2)
    page.update()
ft.app(target=main, assets_dir='assets')