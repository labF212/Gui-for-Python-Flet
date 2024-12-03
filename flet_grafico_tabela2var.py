import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt
import random
import asyncio
from datetime import datetime

# Configuração inicial
num_amostras = 100
max_valores_tabela = 10  # Número máximo de valores na tabela estilizada
recolher_dados = True
num_amostra = 0  # Contador para o número de amostras

# Função para gerar dados aleatórios
def gerar_dados():
    temperatura = random.uniform(20, 25)
    humidade = random.uniform(20, 80)
    return temperatura, humidade

# Inicializar listas de dados
tempos = list(range(num_amostras))
temperaturas = [0] * num_amostras
humidades = [0] * num_amostras

async def main(page: ft.Page):
    global recolher_dados, num_amostra, temperaturas, humidades

    page.title = "Gráfico e Tabela de Dados"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Configuração do gráfico
    fig, ax = plt.subplots()
    ax.set_xlim(0, num_amostras - 1)
    ax.set_ylim(0, 110)
    ax.set_title("Temperatura e Humidade em Tempo Real\n")
    ax.set_xlabel("Tempo (amostras)")
    ax.set_ylabel("Valor")

    linha_temperatura, = ax.plot(tempos, temperaturas, label="Temperatura (°C)", color='red')
    linha_humidade, = ax.plot(tempos, humidades, label="Humidade (%)", color='blue')
    ax.grid(axis='y', color='lightgrey', linestyle='--', linewidth=0.7)
    ax.set_yticks(range(0, 101, 10))
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.0), ncol=2)

    chart = MatplotlibChart(fig, expand=True)

    # Tabela estilizada
    tabela_estilizada = ft.DataTable(
        # Estilo da tabela
        bgcolor="yellow",
        border=ft.border.all(2, "red"),
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
        border_radius=10,
        heading_row_color="#d95f0e",  # Cor da primeira linha
        heading_text_style=ft.TextStyle(color="white", weight="bold"),
        # Dados da tabela
        columns=[
            ft.DataColumn(ft.Text("Hora", color="black")),
            ft.DataColumn(ft.Text("Temperatura (°C)", color="black")),
            ft.DataColumn(ft.Text("Humidade (%)", color="black")),
        ],
        rows=[],
    )

    # Função para adicionar uma linha com cores alternadas
    def adicionar_linha(hora, temperatura, humidade, indice):
        # Define a cor com base no índice da linha
        cor_linha = "#fec44f" if indice % 2 == 0 else "#fff7bc"
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(hora, color="black")),  # Texto preto
                ft.DataCell(ft.Text(f"{temperatura:.2f}°C", color="black")),  # Texto preto
                ft.DataCell(ft.Text(f"{humidade:.2f}%", color="black")),  # Texto preto
            ],
            color=cor_linha  # Passa a cor como string hexadecimal
        )

    # Função para atualizar gráfico e tabela
    async def atualizar_dados():
        global temperaturas, humidades, recolher_dados, num_amostra

        while True:
            if recolher_dados:
                num_amostra += 1
                nova_temp, nova_hum = gerar_dados()
                temperaturas.pop(0)
                humidades.pop(0)
                temperaturas.append(nova_temp)
                humidades.append(nova_hum)

                # Atualiza o gráfico
                linha_temperatura.set_ydata(temperaturas)
                linha_humidade.set_ydata(humidades)
                chart.update()

                # Atualiza a tabela estilizada
                agora = datetime.now()
                hora_atual = agora.strftime("%H:%M:%S")

                tabela_estilizada.rows.insert(
                    0,
                    adicionar_linha(hora_atual, nova_temp, nova_hum, len(tabela_estilizada.rows))
                )

                # Limita o número de linhas na tabela estilizada
                if len(tabela_estilizada.rows) > max_valores_tabela:
                    tabela_estilizada.rows.pop()

                # Reaplica as cores corretamente
                for i, row in enumerate(tabela_estilizada.rows):
                    row.color = "#fec44f" if i % 2 == 0 else "#fff7bc"

                # Atualiza a tabela na página
                await page.update_async()

            # Aguardar 1 segundo entre as atualizações
            await asyncio.sleep(1)

    # Botão para alternar recolha
    def alternar_recolha(e):
        global recolher_dados
        recolher_dados = not recolher_dados
        botao_parar_iniciar.text = "Iniciar" if not recolher_dados else "Parar"
        botao_parar_iniciar.update()

    # Botão para sair
    def sair_app(e):
        page.window.close()

    # Botões
    botao_parar_iniciar = ft.ElevatedButton(
        text="Parar",
        on_click=alternar_recolha,
        tooltip="Clique para iniciar ou parar a recolha de dados."
    )
    botao_sair = ft.ElevatedButton(
        text="Sair",
        on_click=sair_app,
        tooltip="Clique para sair da aplicação."
    )

    # Layout principal: Gráfico e tabela lado a lado
    conteudo_principal = ft.Row(
        [
            ft.Column(
                [
                    ft.Text("Medição de Temperatura e Humidade", weight="BOLD", size=20, text_align="CENTER"),
                    ft.Container(chart, expand=True, height=400),
                ],
                expand=1,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Column(
                [
                    ft.Text("Tabela de Dados", weight="BOLD", size=18, text_align="CENTER"),
                    tabela_estilizada,
                ],
                expand=0,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    botoes = ft.Container(
        ft.Row(
            [botao_parar_iniciar, botao_sair],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        padding=10,
        border_radius=8,
    )

    page.add(
        ft.Column(
            [conteudo_principal, botoes],
            expand=True,
            spacing=20,
        )
    )

    asyncio.create_task(atualizar_dados())

ft.app(main)
