import random
import asyncio
import flet as ft

import random
import asyncio
import flet as ft

async def main(page: ft.Page):
    # Create temperature text widget
    txt_temperature = ft.Text(value="Temperatura: --°C")

    # Create humidity text widget
    txt_humidity = ft.Text(value="Humidade: --%")

    # Add widgets to page
    await page.add_async(txt_temperature)
    await page.add_async(txt_humidity)

    # Update widgets with initial values
    temperature = random.randint(0, 50)
    humidity = random.randint(20, 80)
    txt_temperature.value = f"Temperatura: {temperature}°C"
    txt_humidity.value = f"Humidade: {humidity}%"

    async def update_values():
        while True:
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