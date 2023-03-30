import random
import asyncio
import flet as ft
import csv

async def main(page: ft.Page):
    # Create title text widget
    txt_title = ft.Text(value="Medição de Temperatura e Humidade", text_align="CENTER", weight="BOLD")
        
    # Create temperature text widget
    txt_temperature = ft.Text(value="Temperatura: --°C")

    # Create humidity text widget
    txt_humidity = ft.Text(value="Humidade: --%")

    # Add widgets to page
    await page.add_async(txt_title)
    await page.add_async(txt_temperature)
    await page.add_async(txt_humidity)

    # Update widgets with initial values
    temperature = random.randint(0, 50)
    humidity = random.randint(20, 80)
    txt_temperature.value = f"Temperatura: {temperature}°C"
    txt_humidity.value = f"Humidade: {humidity}%"

    async def update_values():
        #The csv file will be on HOME folder
        with open('flet.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Temperature', 'Humidity']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

        while True:
            # Center the page horizontally
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            
            # Generate random temperature and humidity values
            temperature = random.randint(0, 50)
            humidity = random.randint(20, 80)

            # Update the text widgets
            txt_temperature.value = f"Temperatura: {temperature}°C"
            txt_humidity.value = f"Humidade: {humidity}%"

            # Open the CSV file for appending and write the data
            with open('flet.csv', mode='a', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'Temperature': temperature, 'Humidity': humidity})

            # Limit the number of rows to 100
            with open('flet.csv', mode='r', newline='') as csv_file:
                num_lines = sum(1 for line in csv_file) - 1  # subtract 1 for the header row
                if num_lines >= 100:
                    # Delete the oldest row
                    with open('flet.csv', mode='r', newline='') as csv_file:
                        reader = csv.DictReader(csv_file)
                        rows = [row for row in reader]
                        del rows[0]
                    # Write the remaining rows to the file
                    with open('flet.csv', mode='w', newline='') as csv_file:
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(rows)

            # Update the page with the new values
            await page.update_async()

            # Sleep for 1 second
            await asyncio.sleep(1)

    # Start updating the values
    asyncio.create_task(update_values())

ft.app(main)