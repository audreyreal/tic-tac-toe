import PySimpleGUI as sg

def gui() -> sg.Window:
    sg.theme("Reddit")
    sg.set_options(
        suppress_raise_key_errors=False,
        suppress_error_popups=False,
        suppress_key_guessing=False,
    )
    layout = [
        [],
        [],
        [],
    ]
    return sg.Window("Tic-Tac-Toe")