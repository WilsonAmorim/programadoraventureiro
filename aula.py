import flet as ft

def main(page: ft.Page):
  
   page.bgcolor = ft.colors.AMBER_100

   page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
   page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND

   page.padding = 20
   page.spacing = 10
   page.title = 'PPE - PRIMEIRO EMPREGO'
   page.window_always_on_top = True
   page.window_title_bar_hidden = False
   page.window_frameless = False
   page.window_full_screen = False
   page.window_height = 300
   page.window_max_height = 900
   page.window_min_height = 200
   page.window_width = 600
   page.window_max_height = 800
   page.window_min_width = 200
   page.window_resizable = False


   page.add(
      ft.Text(value='Olá Mundo'),
      ft.Container(ft.Text(value='Oi Mundinho', color='#FFFFFF'), bgcolor='black')
      
   )
   
   page.update()
   
   
ft.app(target=main)


