import flet as ft 

def main(page: ft.Page):
    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f'Selecionado a linha de índice {e.control.data}')
        page.update()
        
    dt = ft.DataTable(
       columns=[
           ft.DataColumn(label=ft.Text('Editar', color=ft.colors.BLACK)),
           ft.DataColumn(label=ft.Text('Nome', color=ft.colors.BLACK)),
           ft.DataColumn(label=ft.Text('Login', color=ft.colors.BLACK), tooltip='Login do Usuário na Plataforma'),
           ft.DataColumn(
               label=ft.Text('Idade'),
               numeric=True,
               on_sort=lambda e: print(f'{e.column_index}, {e.ascending}')
           )
       ], 
       rows=[
            ft.DataRow(
               cells=[
                   ft.DataCell(
                       content=ft.Text('', color=ft.colors.BLACK),
                       show_edit_icon=True,
                       on_tap=lambda _: print('Célula clicada'),
                    
                   ),
                   ft.DataCell(
                       content=ft.Text('Maria', color=ft.colors.BLACK),
                   ),
                   ft.DataCell(
                       content=ft.Text('mary99', color=ft.colors.BLACK)
                   ),
                   ft.DataCell(
                       content=ft.Text('14', color=ft.colors.BLACK)
                   ),
               ],
               on_select_changed=toggle_select,
               data = 0,
            ),
            ft.DataRow(
                cells=[
                   ft.DataCell(
                       content=ft.Text('', color=ft.colors.BLACK),
                       show_edit_icon=True,
                       on_tap=lambda _: print('Célula clicada'),
                   ),
                   ft.DataCell(
                       content=ft.Text('Luiz', color=ft.colors.BLACK),
                   ),
                   ft.DataCell(
                       content=ft.Text('luz99', color=ft.colors.BLACK)
                   ),
                   ft.DataCell(
                       content=ft.Text('21', color=ft.colors.BLACK)
                   ),  
                ],
               on_select_changed=toggle_select,
               data = 1,
           ),
            ft.DataRow(
                cells=[
                   ft.DataCell(
                       content=ft.Text('', color=ft.colors.BLACK),
                       show_edit_icon=True,
                       on_tap=lambda _: print('Célula clicada'),
                   ),
                   ft.DataCell(
                       content=ft.Text('Pedro', color=ft.colors.BLACK),
                   ),
                   ft.DataCell(
                       content=ft.Text('ped99', color=ft.colors.BLACK)
                   ),
                   ft.DataCell(
                       content=ft.Text('24', color=ft.colors.BLACK)
                   ),  
                ],
               on_select_changed=toggle_select,
               data = 4,
           )
        ],
       show_checkbox_column=True,
       bgcolor=ft.colors.WHITE,
       border=ft.border.all(width=1, color=ft.colors.BLACK),
       border_radius=ft.border_radius.all(5),
       column_spacing=50,
       data_row_min_height=10,
       data_row_max_height=30,
       data_text_style=ft.TextStyle(italic=True),
    #    divider_thickness=5,
       gradient=ft.LinearGradient(
           begin=ft.alignment.center_left,
           end=ft.alignment.center_right,
           colors=[ft.colors.TEAL, ft.colors.CYAN],
       ),
       data_row_color={
           ft.MaterialState.SELECTED: ft.colors.RED,
           ft.MaterialState.DEFAULT: ft.colors.GREEN_700,
       },
    #    heading_row_color=ft.colors.BLACK,
        heading_row_height=50,
        heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        horizontal_lines=ft.BorderSide(width=5, color=ft.colors.AMBER),
        vertical_lines=ft.BorderSide(width=5, color=ft.colors.AMBER),
        horizontal_margin=50,
        show_bottom_border=False,
        sort_column_index=3,
        sort_ascending=True,
    )
    
    
    page.add(dt)
if __name__ == '__main__':
    ft.app(target=main)