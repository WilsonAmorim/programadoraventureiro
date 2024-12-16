import flet as ft 

def main(page: ft.Page):
   
    tl1 = ft.ListTile(
       title=ft.Text(value='Título do peimeiro'),
       subtitle=ft.Text(value='Subtítulo do primeiro'),
       leading=ft.Icon(name=ft.icons.ADB, color=ft.colors.GREEN),
       trailing=ft.PopupMenuButton(
           items=[
               ft.PopupMenuItem(text='Item 1'),
               ft.PopupMenuItem(text='Item 2'),
           ]
       ),
       content_padding=ft.padding.all(20),
       selected=True,
       on_click=lambda _: print('clicado'),
       url='https:/programadoraventureiro.com',
    )
    
    tl2 = ft.ListTile(
       title=ft.Text(value='Título do peimeiro'),
       leading=ft.Icon(name=ft.icons.ADB, color=ft.colors.GREEN),
       trailing=ft.Switch(),
       toggle_inputs=True,
    )

    page.add(tl1, tl2)
if __name__ == '__main__':
    ft.app(target=main)