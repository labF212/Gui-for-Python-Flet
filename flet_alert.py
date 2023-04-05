import flet as ft

def main(page: ft.Page):
    page.title = "Como utilizar botões Elevated buttons"
    page.theme_mode = ft.ThemeMode.DARK

    def open_alert():
        icon=ft.icons.REPORT_PROBLEM,
        icon_color="red600"
        
        dialog1= ft.AlertDialog(
            title=ft.Text("Caixa de texto vazia"),
            content=ft.Text("Introduza dados na caixa primeiro"),
            actions=[ft.TextButton("OK", on_click=lambda e: close_dlg1(dialog1))],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.dialog = dialog1
        dialog1.open = True
        page.update()

    def save_clicked(e):
        if not i.value:
            print("vazio")
            open_alert()
            return
        t.value = i.value
        page.add(t)  # add the Text widget to the page
        page.update()

    def clear_clicked(e):
        i.value = ""
        t.value = ""
        page.add(t)  # add the Text widget to the page
        page.update()

    def help_clicked(e):
        dialog = ft.AlertDialog(
            title=ft.Text(value="Como usar", text_align="CENTER", weight="BOLD"),
            content=ft.Row([
                ft.Icon(name=ft.icons.QUESTION_MARK_OUTLINED, color=ft.colors.PINK,size=60),
                ft.Column([
                    ft.Text("Coloque algo na caixa de texto."),
                    ft.Text("Grave o que escreveu no botão gravar."),
                    ft.Text("Apague o que escreveu com o botão Apagar.")
                ],tight=True),
            ]),
            actions=[ft.TextButton("OK", expand="True",on_click=lambda e: close_dlg(dialog))],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            
            on_dismiss=lambda e: print("Dialog dismissed!"),
        )
        page.dialog = dialog
        dialog.open = True
        page.update()


    def close_dlg1(dialog1):
        dialog1.open = False
        page.update()


    def close_dlg(dialog):
        dialog.open = False
        page.update()

    # put elements on the page
    title_page = ft.Text("Botões e Input Box")
    i = ft.TextField()
    save_button = ft.ElevatedButton(
        "Guardar",
        tooltip="Guarda o que está na caixa de texto",
        icon=ft.icons.SAVE,
        icon_color="green600"
    )
    clear_button = ft.ElevatedButton(
        "Apagar",
        tooltip="Apaga conteúdo da caixa de texto",
        icon=ft.icons.DELETE_FOREVER_ROUNDED,
        icon_color="pink600"
    )
    help_button = ft.ElevatedButton(
        "Ajuda",
        tooltip="Mostra ajuda do programa",
        icon=ft.icons.HELP,
        icon_color="blue600"
    )
    t = ft.Text()

    save_button.on_click = save_clicked
    clear_button.on_click = clear_clicked
    help_button.on_click = help_clicked

    button_row = ft.Row(
        [save_button, clear_button, help_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    page.add(
        ft.Row([title_page], alignment=ft.MainAxisAlignment.CENTER),
        i,
        button_row,
        t
    )

ft.app(target=main)