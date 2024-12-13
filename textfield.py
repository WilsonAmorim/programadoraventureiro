import flet as ft

def main(page: ft.Page):
    tf = ft.TextField(
        label='E-mail',
        label_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        text_align=ft.TextAlign.RIGHT,
        text_size=20,
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        value='',
        badge=ft.colors.BLACK45,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.colors.WHITE,
        border_radius=ft.border_radius.all(0),
        border_width=2,
        capitalization=ft.TextCapitalization.WORDS,

        color=ft.colors.AMBER,
        content_padding=ft.padding.all(20),
        counter_text='Texto',
        counter_style=ft.TextStyle(size=40, italic=True),
        
        cursor_height=50,
        cursor_radius=10,
        cursor_width=5,
        dense=True,

        # error_text='valor inválido'

        helper_text='Seu melohor',

        hint_text='eu@mail.com',

        icon=ft.icons.EMAIL,

        # input_filter=ft.InputFilter(
        #     allow=False,
        #     regex_string=r"[0-9]",
        #     replacement_string='',
        # )

        # input_filter=ft.NumbersOnlyInputFilter(),
        # input_filter=ft.TextOnlyInputFilter(),

        # keyboard_type=ft.KeyboardType.NUMBER,
        max_length=50,
        max_lines=5,
        min_lines=2,
        multiline=True,
        password=True,
        can_reveal_password=True,
        
        prefix_text='https://',
        suffix_text='.com',

        # read_only=True,
        on_change=lambda x: print(x.data)

    )

    page.add(tf)

ft.app(target=main)