import PySimpleGUI as sg


def gui() -> sg.Window:
    sg.theme("Reddit")
    sg.set_options(
        suppress_raise_key_errors=False,
        suppress_error_popups=False,
        suppress_key_guessing=False,
    )

    layout = [
        [sg.Button("", key="-1-"), sg.Button("", key="-2-"), sg.Button("", key="-3-")],
        [sg.Button("", key="-4-"), sg.Button("", key="-5-"), sg.Button("", key="-6-")],
        [sg.Button("", key="-7-"), sg.Button("", key="-8-"), sg.Button("", key="-9-")],
    ]
    return sg.Window("Tic-Tac-Toe", layout=layout, use_default_focus=False, auto_size_buttons=False)


def main() -> None:
    try:
        window = gui()
        while True:
            event = window.read()[0]
            match event:
                case None:
                    break
                case default:
                    window[event].update("X")
    except Exception as e:
        sg.popup_error(e)

def is_filled(window) -> bool:
    pass

if __name__ == "__main__":
    main()
