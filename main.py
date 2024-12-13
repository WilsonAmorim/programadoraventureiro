import flet as ft
import flet_fastapi

app = flet_fastapi.FastAPI()

async def root_main(page: ft.Page):
    await page.add_async(ft.Text('Página Inicial'))

async def sub_main(page: ft.Page):
    await page.add_async(ft.Text('Página segundari'))

app.mount(path='/sub-app', app=flet_fastapi.app(root_main))
app.mount(path='/', app=flet_fastapi.app(root_main))

