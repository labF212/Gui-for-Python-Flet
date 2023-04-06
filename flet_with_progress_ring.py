import random
import asyncio
import flet as ft

async def main(page: ft.Page):
    # Set page title
    page.title = "Medição de Temperatura e Humidade"

    # Create title text widget
    txt = ft.Text(value="Medição de Temperatura e Humidade", text_align="CENTER", weight="BOLD")

    #Create progress Ring Temperatura
    txt_temp=ft.Text(value="Temperatura")
    pr_temp_value = ft.Text(value="0°C", size=20)
    pr_temp_container = ft.Container(
        content=[pr_temp_value],
        width=25,
        height=25,
        border_radius=50,
        margin=5,
        bgcolor="white",
        ink=True,
    )
    pr_temp = ft.ProgressRing(
        width=50,
        height=50,
        stroke_width=10,
        color="red",
        value=[pr_temp_container, txt_temp],
    )

    #Create progress Ring Humidade
    txt_hum=ft.Text(value="Humidade")
    pr_hum_value = ft.Text(value="0%", size=20)
    pr_hum_container = ft.Container(
        content=[pr_hum_value],
        width=25,
        height=25,
        border_radius=50,
        margin=5,
        bgcolor="white",
        ink=True,
    )
    pr_hum = ft.ProgressRing(
        width=50,
        height=50,
        stroke_width=10,
        color="blue",
        value=[pr_hum_container, txt_hum],
    )

    #Create Table
    table1 = ft.DataTable(
        columns=[
            ft.DataColumn(pr_temp),
            ft.DataColumn(pr_hum),
        ],
        rows=[],
    )

    # Create DataTable widget with temperature and humidity columns
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Temperatura")),
            ft.DataColumn(ft.Text("Humidade")),
        ],
        rows=[],
    )

    # Add widgets to page
    await page.add_async(txt)
    await page.add_async(pr_temp_value)  # Add pr_temp_value widget
    await page.add_async(pr_hum_value)   # Add pr_hum_value widget
    await page.add_async(table1)
    await page.add_async(table)

    # List to store last 10 temperature and humidity values
    values = []

    async def update_values():
        nonlocal values
        i = 0
        while True:
            # Generate random temperature and humidity values
            temperature = random.randint(0, 50)
            humidity = random.randint(20, 80)

            # Add new value to the list
            values.append((temperature, humidity))

            # Keep only the last 10 values
            values = values[-5:]

            # Update the table with the last 10 values
            rows = []
            for temp, hum in values:
                row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"{temp}°C")),
                        ft.DataCell(ft.Text(f"{hum}%")),
                    ],
                )
                rows.append(row)
            table.rows = rows

            # Update the page with the new values
            await page.update_async()

            #Update progress ring values
            pr_temp_value.value = f"{temperature}°C"
            pr_hum_value.value = f"{humidity}%"
            pr_temp.value = temperature * 0.01
            pr_hum.value = humidity * 0.01

            # Sleep for 1 second
            await asyncio.sleep(1)

    # Start updating the values
    asyncio.create_task(update_values())

ft.app(main)
