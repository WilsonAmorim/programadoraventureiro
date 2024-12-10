import flet as ft
    
def main(page: ft.Page):
    # Aspect Radio
    # 9:16      -> 0.56
    # 2:3       -> 0.66
    # 1:1       -> 1.0
    # 16:9      -> 1.77

    grid = ft.GridView(
        controls=[
            ft.Image(src=f'https://picsum.photos/250/300?{num}', fit='cover') for num in range(20)],
            runs_count=3,
            padding=20,
            spacing=20,
            run_spacing=20,
            # max_extent=100,
            auto_scroll=True,
            aspect_ratio=1.77,

    )
   
    page.add(grid)
    
ft.app(target=main,  assets_dir='assets')