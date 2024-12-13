import flet as ft
    
def main(page: ft.Page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    bn1 = ft.Banner(
        actions=[
            ft.TextButton(text='Cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_banner),
            ft.ElevatedButton(text='Tentar novamente', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE), on_click=close_banner),
        ],
        content=ft.Text(value='Ops, parece que não conseguimos processar a sua solicitação no momento'),
        content_padding=ft.padding.all(0),
        leading=ft.Icon(name=ft.icons.WARNING_AMBER),
        force_actions_below=True,
        bgcolor=ft.colors.BLACK,
    
    )
    bn1.l
    page.banner = bn1
    bn1.open = True
    page.update()

if __name__ == '__main__':
   ft.app(target=main, assets_dir='assets')