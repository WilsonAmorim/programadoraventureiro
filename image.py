import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        src = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9EPE_D5yjSlVUi0QW_KqFc93OelK8hJJLI8jotfpIj7knaohht4DADbmaSDeWQQ7lZfQ&usqp=CAU',
        #border_radius=ft.border_radius.only(top_left=10, top_right=20, bottom_left=40, bottom_right=0),
        border_radius=ft.border_radius.all(20),
        height=100,
        width=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.REPEAT_Y,
    )

    img2 = ft.Image(
        src = 'images/logoPrimeiroe.jpg',
        border_radius=ft.border_radius.all(20),
        height=100,
        width=400,
        tooltip='Logo do Projeto Primeiro Emprego',
        src_base64=''
    )


    page.add(img, img2)

ft.app(target=main, assets_dir='assets')