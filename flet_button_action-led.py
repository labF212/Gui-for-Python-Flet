import flet as ft

def main(page: ft.Page):
    page.title = "Controlo de Relé"
    page.theme_mode = ft.ThemeMode.DARK

    # Função para o botão "Ligar Relé"
    def ligar_rele(e):
        led_icon.color = "green"  # Define o LED para verde
        page.update()

    # Função para o botão "Desligar Relé"
    def desligar_rele(e):
        led_icon.color = "red"  # Define o LED para vermelho
        page.update()

    # Título
    title = ft.Text("Controlo de Relé", size=24, weight="bold")

    # Ícone do LED maior e rótulo
    led_icon = ft.Icon(name=ft.icons.CIRCLE, color="red", size=60)  # LED com tamanho maior
    led_label = ft.Text("Relé 1", size=14, color="black")  # Cor do texto alterada para preto

    # LED e label em uma coluna centralizada dentro do contêiner amarelo
    led_container = ft.Container(
        content=ft.Column(
            [led_icon, led_label],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza o LED e o texto horizontalmente
        ),
        padding=10,
        bgcolor="yellow",
        border_radius=8,
        width=100,
        alignment=ft.alignment.center
    )

    # Botões de controle do relé
    ligar_button = ft.ElevatedButton(
        "Ligar Relé",
        on_click=ligar_rele,
        icon=ft.icons.POWER,
        icon_color="green600",
        tooltip="Liga o relé"
    )

    desligar_button = ft.ElevatedButton(
        "Desligar Relé",
        on_click=desligar_rele,
        icon=ft.icons.POWER_OFF,
        icon_color="red600",
        tooltip="Desliga o relé"
    )

    # Coloca os botões e o contêiner do LED em uma linha
    control_row = ft.Row(
        [ligar_button, desligar_button, led_container],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Adiciona os elementos à página
    page.add(title, control_row)

ft.app(target=main)
