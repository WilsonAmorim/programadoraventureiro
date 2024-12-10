import flet as ft
    
def main(page: ft.Page):
    page.padding= ft.padding.only(top=100)
    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(text='1', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='2', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ft.ElevatedButton(text='3', bgcolor=ft.colors.RED, color=ft.colors.WHITE),
        ],
        alignment= ft.MainAxisAlignment.START,
        spacing=20,
        #wrap=True,
        run_spacing=10,
        vertical_alignment= ft.CrossAxisAlignment.START,
       # expand=True,
    )
    row2 = ft.Row(
        controls=[
        
            ft.Image(height=200, src='https://blog.geekhunter.com.br/wp-content/uploads/2022/02/linguagem-python-1024x579-1.jpg'),
            ft.Image(height=200, src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUr1v8UqdbRDoPNVXoCO-mwfQrtElVdTnaPzNwyXuTGngPnB8rqgEV9s3pqB1X9P1GYGc&usqp=CAU'),
            ft.Image(height=200, src='https://blog.geekhunter.com.br/wp-content/uploads/2022/02/linguagem-python-1024x579-1.jpg'),
            ft.Image(height=200, src='https://blog.geekhunter.com.br/wp-content/uploads/2022/02/linguagem-python-1024x579-1.jpg'),
            ft.Image(height=200, src='https://blog.geekhunter.com.br/wp-content/uploads/2022/02/linguagem-python-1024x579-1.jpg'),
           
        ],
        scroll=ft.ScrollMode.AUTO,
    )
    page.add(row1, row2)
    
ft.app(target=main)