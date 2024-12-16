import flet as ft 

def main(page: ft.Page):
    # page.scroll=True
    page.scroll = ft.ScrollMode.AUTO
    
    def handle_dismiss(e):
        lv.controls.remove(e.control),
        lv.update()
        
    lv =ft.ListView(
        controls=[
            
            ft.Dismissible(
                content=ft.Text(value=f'Item {i}', size=40),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.AMBER, content=ft.Text(value='Arquivar')),
                secondary_background=ft.Container(bgcolor=ft.colors.RED, content=ft.Text(value='Excluir')),
                on_dismiss= handle_dismiss,
                on_update=lambda _: print('Atualizado'),
                on_resize=lambda _: print('Redimencionado')
            ) for i in range(30)
        ]
    )


    page.add(lv)
if __name__ == '__main__':
    ft.app(target=main)