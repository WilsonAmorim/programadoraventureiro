import flet as ft

def main(page: ft.Page):
    def restart_app(e):
        page.controls.clear()  # Limpa todos os controles da página
        setup_app()            # Reconfigura os controles da interface
        page.update()          # Atualiza a página

    def setup_app():
        page.add(
            ft.Text("Bem-vindo ao aplicativo!"),
            ft.ElevatedButton("Reiniciar", on_click=restart_app)
        )

    setup_app()

ft.app(target=main)