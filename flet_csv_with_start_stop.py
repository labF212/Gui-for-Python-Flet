import random
import asyncio
import flet as ft
import csv

async def main(page: ft.Page):
    page.title = "Gravação de dados para ficheiro"    
    # Create title text widget
    txt_title = ft.Text(value="Medição de Temperatura e Humidade", text_align="CENTER", weight="BOLD")
    
    async def start_clicked(e):
        
        # Re-enable the stop button
        await enable_stop_button()
        
        print("start")
        temperature = random.randint(0, 50)
        humidity = random.randint(20, 80)
        txt_temperature.value = f"Temperatura: {temperature}°C"
        txt_humidity.value = f"Humidade: {humidity}%"
        #The csv file will be on HOME folder
        with open('flet.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Temperature', 'Humidity']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                writer.writeheader()

        # Keep track of the number of records written
        record_count = 0
        
        while True:
            if stop_button.disabled:
                break
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
                record_count += 1

            # Break out of the loop if we've written 100 records
            if record_count >= 100:
                break
        
            # Update the page with the new values
            await page.update_async()
        
            # Sleep for 1 second
            await asyncio.sleep(1)
      
    async def stop_clicked(e):
        
        # Disable the stop button
        stop_button.disabled = True

        # Read the contents of the CSV file
        with open('flet.csv', mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = [row for row in reader]

        # Delete the oldest rows if there are more than 100 rows
        if len(rows) > 100:
            rows = rows[-100:]
        
        # Write the remaining rows back to the CSV file
        with open('flet.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['Temperature', 'Humidity'])
            writer.writeheader()
            writer.writerows(rows)
              
        await page.update_async()
        
    async def enable_stop_button():
        stop_button.disabled = False
        await page.update_async()
          
    # Create widget
    txt_temperature = ft.Text(value="Temperatura: --°C")  
    txt_humidity = ft.Text(value="Humidade: --%")
    start_button = ft.ElevatedButton("Save", on_click=start_clicked,tooltip="Guarda os dados",icon=ft.Icons.SAVE,icon_color="green600")
    stop_button = ft.ElevatedButton("Stop", on_click=stop_clicked,tooltip="Para a gravação",icon=ft.Icons.STOP,icon_color="pink600")
    button_row = ft.Row([start_button, stop_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    
    # Add widgets to page
    await page.add_async(txt_title)
    await page.add_async(txt_temperature)
    await page.add_async(txt_humidity)
    await page.add_async(button_row)

    # Update widgets with initial values
    temperature = random.randint(0, 50)
    humidity = random.randint(20, 80)
    txt_temperature.value = f"Temperatura: {temperature}°C"
    txt_humidity.value = f"Humidade: {humidity}%"

       
    async def update_values():

        while True:
            # Center the page horizontally
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            
            # Generate random temperature and humidity values
            temperature = random.randint(0, 50)
            humidity = random.randint(20, 80)

            # Update the text widgets
            txt_temperature.value = f"Temperatura: {temperature}°C"
            txt_humidity.value = f"Humidade: {humidity}%"

            # Update the page with the new values
            await page.update_async()

            # Sleep for 1 second
            await asyncio.sleep(1)

    # Start updating the values
    asyncio.create_task(update_values())

ft.app(main)