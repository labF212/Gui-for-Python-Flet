import flet as ft

def main(page: ft.Page):
    page.title = "Controlo de Relés"
    page.theme_mode = ft.ThemeMode.DARK

    # Funções para os botões "Ligar Relé" e "Desligar Relé" para cada relé
    def ligar_rele(led_icon):
        led_icon.color = "green"  # Define o LED para verde
        page.update()

    def desligar_rele(led_icon):
        led_icon.color = "red"  # Define o LED para vermelho
        page.update()

    # Título
    title = ft.Text("Controlo de Relés", size=24, weight="bold")

    # Função auxiliar para criar um conjunto de botões e LED para cada relé
    def create_rele_controls(rele_number):
        # LED ícone e rótulo
        led_icon = ft.Icon(name=ft.Icons.CIRCLE, color="red", size=60)
        led_label = ft.Text(f"Relé {rele_number}", size=14, color="black")

        # Contêiner amarelo para o LED e o rótulo
        led_container = ft.Container(
            content=ft.Column(
                [led_icon, led_label],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10,
            bgcolor="yellow",
            border_radius=8,
            width=120,
            height=100,
            alignment=ft.alignment.center
        )

        # Botões para ligar e desligar o relé
        ligar_button = ft.ElevatedButton(
            f"Ligar Relé {rele_number}",
            on_click=lambda e: ligar_rele(led_icon),
            icon=ft.Icons.POWER,
            icon_color="green600",
            tooltip=f"Liga o Relé {rele_number}"
        )

        desligar_button = ft.ElevatedButton(
            f"Desligar Relé {rele_number}",
            on_click=lambda e: desligar_rele(led_icon),
            icon=ft.Icons.POWER_OFF,
            icon_color="red600",
            tooltip=f"Desliga o Relé {rele_number}"
        )

        # Contêiner para os botões, com largura aumentada para 350
        buttons_container = ft.Container(
            content=ft.Row(
                [ligar_button, desligar_button],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            padding=10,
            bgcolor="yellow",
            border_radius=8,
            width=350,  # Largura aumentada para acomodar os botões
            height=100,
            alignment=ft.alignment.center
        )

        # Retorna uma linha com os botões e o LED do relé
        return ft.Row(
            [buttons_container, led_container],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

    # Adiciona o título, as labels e as linhas de controle para cada relé à página
    page.add(
        title,
        # Labels "Entradas" e "Saídas" centralizadas acima dos contêineres
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Entradas", size=18, weight="bold", text_align=ft.TextAlign.CENTER),
                    alignment=ft.alignment.center,
                    width=350  # Largura alinhada com o contêiner de botões
                ),
                ft.Container(
                    content=ft.Text("Saídas", size=18, weight="bold", text_align=ft.TextAlign.CENTER),
                    alignment=ft.alignment.center,
                    width=120  # Largura alinhada com o contêiner de LED
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        ),
        create_rele_controls(1),
        create_rele_controls(2),
        create_rele_controls(3),
        create_rele_controls(4)
    )

ft.app(target=main)
