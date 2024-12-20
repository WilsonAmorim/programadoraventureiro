import flet as ft
import os

def main(page: ft.Page):
  
   page.bgcolor = ft.colors ="#BFFDDA"

   page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
   page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND

   page.padding = 20
   page.spacing = 10
   page.title = 'PPE - PRIMEIRO EMPREGO'
   # aplicativo fica em primeiro plano
   # page.window.always_on_top = True
   # esconder a barra de titulo
   page.window.title_bar_hidden = False
   # some com os butões de minimizar maximinizar e fechar
   page.window.frameless = False
   # inicia na tela cheia
   page.window.full_screen = False
   # definir a largura do aplicativo
   page.window.height = 300
   # define a Altura maxima do aplicativo
   page.window.max_height = 900
   # defini a Altura minima
   page.window.min_height = 200
   # defina a largura
   page.window.width = 600
   # define a largura maxima
   page.window.max_width = 900
   # defina a lagura minima
   page.window.min_width = 200
   #desativa o rediemncionamento da tela
   page.window.resizable = True
   # defina a localização de app na tela
   page.window.top = 100
   page.window.left = 100
   # permitir que o usario mova a tela
   page.window.movable = False
   # usuario não fecha a tela
   page.window.prevent_close = False
   # barra de progreço
   page.window.progress_bar = 0.5

   # informa a plataforma
   print(page.platform)

   #

  # def page_resize(e):
     #print('Tamanho: ', page.window.width, page.window.height)

  # page.on_resize = page_resize


   def window_event(e):
      match e.data:
         case 'moved':
            print('Moveu a pagiona')
         case 'resized':
            print('Redimencionou a página')
         case 'minimized':
            print('Minimizou')
         case _:
            print('outra ação')

   page.window.on_event = window_event

   page.add(
      ft.Text(value='Olá Mundo'),
      ft.Container(ft.Text(value='Oi Mundinho', color='#FFFFFF'), bgcolor='black')
      
   )
   
   page.update()
   
   
ft.app(target=main)


