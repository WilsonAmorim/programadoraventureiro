import flet as ft 

def main(page: ft.Page):
    page.scroll=ft.ScrollMode.AUTO
    lv = ft.ListView(
       controls=[ft.Text(f'Item {i}') for i in range(50)],
       first_item_prototype=False,
       horizontal=False,
       item_extent=40,
       padding=ft.padding.all(100),
       spacing=10,
       divider_thickness=1,
    )

    page.add(lv)
if __name__ == '__main__':
    ft.app(target=main)