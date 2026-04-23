import flet as ft

class LoginView:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        # 1. Título de la pantalla
        titulo = ft.Text(
            value="Iniciar Sesión", 
            size=30, 
            color=ft.Colors.BLUE_900, 
            weight=ft.FontWeight.BOLD
        )
        
        # 2. Campos de texto para usuario y contraseña
        input_usuario = ft.TextField(
            label="Nombre de Usuario", 
            border_color=ft.Colors.BLUE_400, 
            prefix_icon=ft.Icons.PERSON_OUTLINE,
        )
        
        input_password = ft.TextField(
            label="Contraseña", 
            border_color=ft.Colors.BLUE_400, 
            prefix_icon=ft.Icons.LOCK_OUTLINE,
            password=True, # Oculta el texto
            can_reveal_password=True # Agrega el ícono del "ojito" para ver la contraseña
        )
        
        # 3. Botones de acción
        boton_ingresar = ft.ElevatedButton(
            "Ingresar", 
            bgcolor=ft.Colors.CYAN_700, 
            color=ft.Colors.WHITE,
            width=200
        )
        
        boton_registro = ft.TextButton(
            "¿No tienes cuenta? Regístrate aquí",
            icon=ft.Icons.ARROW_FORWARD,
            icon_color=ft.Colors.BLUE_600,
            on_click=lambda e: self.page.go("/register")
        )

        # 4. Agrupamos todo en una columna centrada
        columna_login = ft.Column(
            controls=[
                titulo,
                ft.Container(height=20), # Usamos un Container vacío como espaciador
                input_usuario,
                input_password,
                ft.Container(height=20),
                boton_ingresar,
                boton_registro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=320 # Le damos un ancho máximo para que se vea bien en celular o PC
        )
        
        return columna_login