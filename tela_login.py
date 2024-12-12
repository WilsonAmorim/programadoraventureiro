import os
import flet as ft
import mysql.connector
from dotenv import load_dotenv
import hashlib

# Para carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Função para conectar ao MySQL
def create_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )

# Função principal do sistema
def main(page: ft.Page):
    page.title = 'Tela de login'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.padding = 0

    # Função para levar pra tela de login
    def btn_logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    # Função para levar pra tela de registrar
    def btn_registrar(e):
        page.remove(login)
        page.add(register)
        page.update()

    # Função para logar o usuario no sistema
    def logar_usuario(e):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM adiministrador WHERE email = %s", (email_field,))
            user = cursor.fetchone()
            if user:
                hashed_password = hashlib.sha256(senha_field.encode()).hexdigest()
                if hashed_password == user[3]:  # Comparação com o hash armazenado
                    return user
                else:
                    return None  # Senha incorreta
            else:
                return None  # Usuário não encontrado
        except mysql.connector.Error as err:
            ft.AlertDialog(f'Não foi possível realizar o login. {err}')
        finally:
            cursor.close()
            conn.close()
    
    # Função para cadastrar o usuário
    def cadastrar_usuario(e):
        if senha_field != confirmar_senha_field:
            ft.AlertDialog('As senhas não coincidem. Por favor, verifique.')
            return
        
        # Para criptografar a senha
        hashed_password = hashlib.sha256(senha_field.encode()).hexdigest()
        
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO adiministrador (usuario, telefone, email, senha) VALUES (%s, %s, %s, %s)",
                           (usuario_field, telefone_field, email_field, hashed_password))
            conn.commit()
            ft.AlertDialog('Usuário registrado com sucesso!', 'Cadastro realizado!')
        except mysql.connector.Error as err:
            ft.AlertDialog(f'Erro ao cadastrar usuário. {err}')
        finally:
            cursor.close()
            conn.close()
    
    login = ft.Column([
        ft.Container(
            bgcolor='#111418',
            width=page.window.width - 10,
            height=page.window.height - 60,
            border_radius=10,
            content=ft.Column([
                ft.Container(
                    bgcolor='#181a21',
                    width=400,
                    height=320,
                    border_radius=10,
                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            content=ft.Column([
                                ft.Text(
                                    value='Faça seu login',
                                    color='#c3c7cf',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            email_field:=ft.TextField(
                                hint_text='Digite o seu email',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                keyboard_type=ft.KeyboardType.EMAIL,
                                text_vertical_align=1,
                                cursor_color=ft.colors.BLUE,
                            ),

                            senha_field:=ft.TextField(
                                hint_text='Digite a sua senha',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                password=True,
                                can_reveal_password=True,
                                text_vertical_align=1
                            ),

                            ft.ElevatedButton(
                                text='Entrar',
                                bgcolor='#0B0F26',
                                on_hover=ft.colors.GREEN_100,
                                color='#c3c7cf',
                                width=300,
                                height=40,
                                on_click=logar_usuario
                            ),

                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text='Criar nova conta',
                                    on_click=btn_registrar),
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing=10),

                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])

    register = ft.Column([
        ft.Container(
            bgcolor='#111418',
            width=page.window.width - 10,
            height=page.window.height - 60,
            border_radius=10,
            content=ft.Column([
                ft.Container(
                    bgcolor='#181a21',
                    width=400,
                    height=450,
                    border_radius=10,
                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            content=ft.Column([
                                ft.Text(
                                    value='Nova conta',
                                    color='#c3c7cf',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            usuario_field:=ft.TextField(
                                hint_text='Seu nome',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                keyboard_type=ft.KeyboardType.NAME,
                                text_vertical_align=1,
                                cursor_color=ft.colors.BLUE,
                            ),

                            telefone_field:=ft.TextField(
                                hint_text='Digite o seu telefone',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PHONE,
                                keyboard_type=ft.KeyboardType.EMAIL,
                                text_vertical_align=1,
                                cursor_color=ft.colors.BLUE,
                            ),

                            email_field:=ft.TextField(
                                hint_text='Digite o seu email',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.ALTERNATE_EMAIL,
                                keyboard_type=ft.KeyboardType.EMAIL,
                                text_vertical_align=1,
                                cursor_color=ft.colors.BLUE,
                            ),

                            senha_field:=ft.TextField(
                                hint_text='Digite a sua senha',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                password=True,
                                can_reveal_password=True,
                                text_vertical_align=1
                            ),

                            confirmar_senha_field:=ft.TextField(
                                hint_text='Digite a sua senha novamente',
                                color=ft.colors.WHITE,
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                password=True,
                                can_reveal_password=True,
                                text_vertical_align=1
                            ),

                            ft.ElevatedButton(
                                text='Criar conta',
                                bgcolor='#0B0F26',
                                on_hover=ft.colors.GREEN_100,
                                color='#c3c7cf',
                                width=300,
                                height=40,
                                on_click=cadastrar_usuario
                            ),

                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text='Já tenho uma conta',
                                    on_click=btn_logar),
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing=8),

                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])

    def resize_controls(e):
        login.controls[0].width = page.window.width - 10
        login.controls[0].height = page.window.height - 60

        register.controls[0].width = page.window.width - 10
        register.controls[0].height = page.window.height - 60
    
        page.update()

    page.on_resized.subscribe(resize_controls)
    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)