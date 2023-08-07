import flet as ft
import time

def main(page: ft.Page):
    page.title = "Manual and Automatic Slider"

    slider1_value = 0
    slider2_value = 0
    
    
    def slider_changed(e):
        nonlocal slider1_value, slider2_value
        if e.control == slider1:
            slider1_value = int(e.control.value)
            pwm_label2.value = f"{slider1_value} PWD"
        elif e.control == slider2:
            slider2_value = int(e.control.value)
            pwm_label4.value = f"{slider2_value} PWD"
        page.update()
        
    def radiogroup_changed(value):  # Receive the selected value directly
        
        if value == "manual":  # Access the selected value directly
            slider1.visible = True
            slider2.visible = True
            pwm_label1.visible = True
            pwm_label2.visible = True
            print("manual")
            
        else:
            slider1.visible = False
            slider2.visible = False
            pwm_label1.visible = True
            pwm_label2.visible = True
            print("automatic")
            
            
            #Fading up and down...
            for i in range(255):
                time.sleep(.05)
                pwm_label2.value = f"{i} PWD"
                pwm_label4.value = f"{255-i} PWD"
                page.update()
                
            for i in range(255):
                time.sleep(.05)
                pwm_label2.value = f"{255-i} PWD"
                pwm_label4.value = f"{i} PWD"
                page.update()
            
    def exit_app(_):
        page.window_destroy()

    pwm_label1 = ft.Text("LED in pin 6")
    pwm_label2 = ft.Text(expand=True, text_align=ft.TextAlign.END)

    row1 = ft.Row([
        pwm_label1,
        pwm_label2
    ])

    pwm_label3 = ft.Text("LED in pin 5")
    pwm_label4 = ft.Text(expand=True, text_align=ft.TextAlign.END)

    slider1 = ft.Slider(value=0, min=0, max=254, on_change=slider_changed)

    row2 = ft.Row([
        pwm_label3,
        pwm_label4
    ])

    slider2 = ft.Slider(value=0, min=0, max=254, on_change=slider_changed)
    
    button_exit = ft.ElevatedButton("Exit", icon=ft.icons.EXIT_TO_APP, on_click=exit_app)
    button_center = ft.Row([button_exit], alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    cg = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="manual", label="Manual"),  
            ft.Radio(value="auto", label="Automatic"),
        ]),
        on_change=radiogroup_changed
    )

    row3 = ft.Row([
        ft.Text("Work mode:"),
        cg 
    ])
    
    page.add(
        row1,
        slider1,
        row2,
        slider2,
        row3,
        button_center
    )

    # Set initial value of the radio group to "manual"
    cg.value = "manual"
    radiogroup_changed(cg.value)  # Call the radiogroup_changed function to show the sliders accordingly

ft.app(target=main)
