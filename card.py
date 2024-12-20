import flet as ft 

def main(page: ft.Page):
    card = ft.Card(
        content=ft.Column(
            controls=[
                ft.Text(value='Título do Card', style=ft.TextThemeStyle.HEADLINE_LARGE),
                ft.Divider(
                    height=10,
                    thickness=3,
                    color=ft.colors.YELLOW,
                ),
                ft.Text(value='Conteúdo do card', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.Divider(),
                ft.FilledButton(text='Salvar'),
            ],
        ),
        color=ft.colors.GREEN_900,
        elevation=8,
        margin=ft.margin.all(30),
        shadow_color=ft.colors.GREEN,
    )
    ft.Divider()
    page.add(card)
if __name__ == '__main__':
    ft.app(target=main)