import random
import asyncio
import flet as ft

async def main(page: ft.Page):
    # Set page title
    page.title = "Medição de Temperatura e Humidade"

    # Create title text widget
    txt = ft.Text(value="Medição de Temperatura e Humidade", text_align="CENTER", weight="BOLD")

    # Create DataTable widget with temperature and humidity columns
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Temperatura")),
            ft.DataColumn(ft.Text("Humidade")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("--°C")),
                    ft.DataCell(ft.Text("--%")),
                ],
            ),
        ],
    )

    # Add widgets to page
    await page.add_async(txt)
    await page.add_async(table)

    async def update_values():
        while True:
            # Generate random temperature and humidity values
            temperature = random.randint(0, 50)
            humidity = random.randint(20, 80)

            # Update the table with the new values
            table.rows[0].cells[0].content.value = f"{temperature}°C"
            table.rows[0].cells[1].content.value = f"{humidity}%"

            # Update the page with the new values
            await page.update_async()

            # Sleep for 1 second
            await asyncio.sleep(1)

    # Start updating the values
    asyncio.create_task(update_values())

ft.app(main)