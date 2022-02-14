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
        [sg.Text("Game in progress!", key="-STATUS-")]
    ]
    return sg.Window(
        "Tic-Tac-Toe",
        layout=layout,
        use_default_focus=False,
        auto_size_buttons=False,
    )


def main() -> None:
    window = gui()
    turn = 0
    board = [["" for _ in range(3)] for _ in range(3)]
    event_map = {
        "-1-": [0]
    }
    while (event := window.read()[0]) != None:
        if window[event].get_text() == "":
            if turn % 2 == 0:
                window[event].update("X")
            else:
                window[event].update("O")
            
            turn += 1
            check_if_won(window)


def check_if_won(window) -> bool: # TODO
    pass


if __name__ == "__main__":
    main()
