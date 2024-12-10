import flet as ft
 # Breakpoint       Dimension
 # xs               <576px
 # sm               >=576px
 # md               >=768px
 # lg               >=992px
 # xl               >=1200px
 # xxl              >=1400px

def main(page: ft.Page):
   rrow1 = ft.ResponsiveRow(
    columns=12,
     controls=[
       ft.ElevatedButton(
        col={'sm': 4, 'md': 3, 'lg': 2, 'xl': 1},
         text='1',
         bgcolor=ft.colors.AMBER,
         color=ft.colors.BLACK,
       ),
       ft.ElevatedButton(
         col=4,
         text='2',
         bgcolor=ft.colors.AMBER,
         color=ft.colors.BLACK,
       ),
       ft.ElevatedButton(
         col={'sm': 4, 'md': 3},
         text='3',
         bgcolor=ft.colors.AMBER,
         color=ft.colors.BLACK,
       ),
       
     ]
   )
   page.add(rrow1)
    
ft.app(target=main)