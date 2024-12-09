import flet as ft

def main(page: ft.Page):
    icon1 = ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK)
    icon2 = ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.GREEN_400, size=30)
    icon3 = ft.Icon(name='settings', color='#C1C1C1', size=100, tooltip='Configuração')
    icon4 = ft.Icon(name=ft.icons.EDIT_SHARP)

    page.add(icon1, icon2, icon3, icon4)

ft.app(target=main, assets_dir='assets')