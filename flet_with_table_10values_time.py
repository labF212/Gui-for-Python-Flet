import random
import asyncio
import flet as ft
import datetime

async def main(page: ft.Page):
    # Set page title
    page.title = "Medição de Temperatura e Humidade"
    
    
    
    # Center the page horizontally
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create title text widget
    txt = ft.Text(value="Medição de Temperatura e Humidade", text_align="CENTER", weight="BOLD")

    # Create DataTable widget with temperature, humidity, and timestamp columns
    table = ft.DataTable(
        #table style
        bgcolor="yellow",
        border=ft.border.all(2,"blue"),
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
        border_radius=10,
        heading_row_color=ft.colors.BLACK12,
        #table data
        columns=[
            ft.DataColumn(ft.Text("Data")),
            ft.DataColumn(ft.Text("Hora")),
            ft.DataColumn(ft.Text("Temperatura")),
            ft.DataColumn(ft.Text("Humidade")),
        ],
        rows=[],
    )

    # Add widgets to page
    await page.add_async(txt)
    await page.add_async(table)

    async def update_values():
        while True:
            # Get the current date and time
            now = datetime.datetime.now()
            data_atual = now.strftime("%d/%m/%Y ")
            hora_atual = now.strftime(" %H:%M:%S")
            
            # Generate random temperature and humidity values
            temperature = random.randint(0, 50)
            humidity = random.randint(20, 80)

            # Add a new row to the table with the new values
            table.rows.insert(
                0,
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(data_atual)),
                        ft.DataCell(ft.Text(hora_atual)),
                        ft.DataCell(ft.Text(f"{temperature}°C")),
                        ft.DataCell(ft.Text(f"{humidity}%")),
                    ]
                ),
            )

            # Only keep the last 10 rows
            if len(table.rows) > 10:
                table.rows.pop()

            # Update the page with the new values
            await page.update_async()

            # Sleep for 1 second
            await asyncio.sleep(1)

    # Start updating the values
    asyncio.create_task(update_values())

ft.app(main)