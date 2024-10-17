import flet as ft

def main(page: ft.Page):
    page.title = "Manual and Automatic Slider"

    slider1_value = 0
    slider2_value = 0

    pwm_label1 = ft.Text("None", key="tes")
    pwm_label2 = ft.Text("None")

    def update_pwm_values():
        value_slider1 = int(slider1_value * 2.55)
        value_slider2 = int(slider2_value * 2.55)
        pwm_label1.value = f"{value_slider1} PWD"
        pwm_label2.value = f"{value_slider2} PWD"

    def manual_mode(e):
        slider1.visible = True
        slider2.visible = True
        update_pwm_values()

    def automatic_mode(e):
        slider1.visible = False
        slider2.visible = False

        # Implement the automatic control logic here

        def animate_fade():
            for i in range(256):
                ft.wait(0.05)
                pwm_label1.value = str(i)
                pwm_label2.value = str(255 - i)
                page.update()

            for i in range(255, -1, -1):
                ft.wait(0.05)
                pwm_label1.value = str(255 - i)
                pwm_label2.value = str(i)
                page.update()

        animate_fade()

    manual_radio = ft.Radio(value="Manual", label="Manual", on_click=manual_mode)
    automatic_radio = ft.Radio(value="Automatic", label="Automatic", on_click=automatic_mode)

    exit_button = ft.FilledButton("Exit", icon="exit", on_click=ft.close)

    slider1 = ft.Slider(value=slider1_value, min=0, max=100, on_change=lambda v: setattr(page, "slider1_value", v))
    slider2 = ft.Slider(value=slider2_value, min=0, max=100, on_change=lambda v: setattr(page, "slider2_value", v))

    page.add(
        ft.Column(
            [
                ft.Row(ft.Text("LED in pin 6"), pwm_label1),
                ft.Row(slider1),
                ft.Row(ft.Text("LED in pin 5"), pwm_label2),
                ft.Row(slider2),
                ft.Row(ft.Column([manual_radio, automatic_radio])),
                ft.Row(exit_button),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
