import flet as ft


def main(page: ft.Page):
    
    def change_route(e):
        match e.control.selected_index:
            case 0:
                page.go('/')
            case 1:
                page.go('/loja')
            case 2:
                page.go('/app')
        # if e.control.selected_index == 0:
        #     page.go('/')
        # elif e.control.selected_index == 1:
        #     page.go('/loja')
        # elif e.control.selected_index == 2:
        #     page.go('/app')

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route='/',
                appbar=ft.AppBar(
                    title=ft.Text('Meu APP'),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                
                scroll=ft.ScrollMode.AUTO,
                auto_scroll=False,
                bgcolor=ft.colors.BLACK,
                drawer=ft.NavigationDrawer(
                    controls=[
                        ft.NavigationDrawerDestination(
                            label='Home',
                            icon=ft.icons.HOME,
                        ),
                        ft.NavigationDrawerDestination(
                            label='Loja',
                            icon=ft.icons.STORE,
                        ),
                        ft.NavigationDrawerDestination(
                            label='App',
                            icon=ft.icons.PHONE_ANDROID,
                        ),
                    ],
                    on_change=change_route
                ),
                end_drawer=ft.NavigationDrawer(
                    controls=[
                        ft.NavigationDrawerDestination(label='Configuraçãos'),
                        ft.NavigationDrawerDestination(label='Dados da conta'),
                        ft.NavigationDrawerDestination(label='Sair'),
                    ]
                ),
                floating_action_button=ft.FloatingActionButton(icon=ft.icons.ADD),
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.START,
                padding=ft.padding.all(20),
            ),
        )
        if page.route == '/loja':
            page.views.append(
                ft.View(
                    route='/loja',
                    appbar=ft.AppBar(
                        title=ft.Text('Mina Loja'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                    fullscreen_dialog=True,
                ),
            )
        if page.route == '/app':
            page.views.append(
                ft.View(
                    route='/app',
                    appbar=ft.AppBar(
                        title=ft.Text('App'),
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    ),
                ),
            )
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change=route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)