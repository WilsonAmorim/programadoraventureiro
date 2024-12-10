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
   page.window_frameless = True
   page.window_full_screen = False
   page.window_height = 300
   page.window_max_height = 900
   page.window_min_height = 200
   page.window_width = 600
   page.window_max_height = 800
   page.window_min_width = 200
   page.window_resizable = True
   
   page.window_top = 100
   page.window_left = 100
   page.window_movable = True
   page.window_prevent_close = False
   page.window_progress_bar = 1
   
   print(page.platform)
   def page_resize(e):
      print('Tamanho: ', page.window_width, page.window_height)
      
   def window_event(e):
      match e.data:
         
   
   page.on_resize = page_resize

   page.add(
      ft.Text(value='Olá Mundo'),
      ft.Container(ft.Text(value='Oi Mundinho', color='#FFFFFF'), bgcolor='black')
      
   )
   
   page.update()
   
   
ft.app(target=main)


