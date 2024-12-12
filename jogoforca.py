import flet as ft
import random
import string

def letter_to_guess(letter):
    return ft.Container(
                bgcolor=ft.colors.AMBER_500,
                height=50,
                width=50,
                border_radius=ft.border_radius.all(5),
                content=ft.Text(
                    value=letter, 
                    color=ft.colors.WHITE,
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                ),
            )

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.BROWN_600

    available_words = ['python','flet','programador','aventureiro']
    choiced = random.choice(available_words).upper()

    def validate_letter(e):
        for pos, letter in enumerate(choiced):
            if e.control.content.value == letter:
                word.controls[pos] = letter_to_guess(letter=letter)
                word.data +=1
                word.update()

            if word.data == len(choiced):
               
                page.overlay.append(
                    ft.AlertDialog(title=ft.Text(value='Você Ganhou! ;)'), open=True))
                page.update()

        if e.control.content.value not in choiced:
            victim.data += 1

            if victim.data > 7:
                page.dialog = ft.AlertDialog(
                    title=ft.Text('Você perdeu! :('),
                    open=True
                )
                page.update()

            errors = victim.data
            victim.src = f'images/forca/hangman_{errors}.png'
            victim.update()

        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()

    victim = ft.Image(
        data=0,
        src = 'images/forca/hangman_0.png',
        repeat= ft.ImageRepeat.NO_REPEAT,
        height=300,
    )


    word = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        data=0,
        wrap=True,
        controls=[letter_to_guess('_') for letter in choiced]
    )

    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word,
            ]
        )
    )

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6},
        image_src= 'images/forca/keyboard.png',
        image_repeat= ft.ImageRepeat.NO_REPEAT,
        image_fit= ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    # bgcolor=ft.colors.AMBER,
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter, 
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
                    ),
                    on_click=validate_letter,
                )
                for letter in string.ascii_uppercase
            ],
        )
    )

    scene = ft.Image(col=12, src = 'images/forca/scene.png')

    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')