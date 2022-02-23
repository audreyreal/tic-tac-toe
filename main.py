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
        "-1-": (0, 0),
        "-2-": (0, 1),
        "-3-": (0, 2),
        "-4-": (1, 0),
        "-5-": (1, 1),
        "-6-": (1, 2),
        "-7-": (2, 0),
        "-8-": (2, 1),
        "-9-": (2, 2),
    }
    while (event := window.read()[0]) != None:
        if window[event].get_text() == "":
            column, row = event_map[event]
            write_value = "X" if turn % 2 == 0 else "O"
            turn += 1
            window[event].update(write_value)
            board[column][row] = write_value
            window["-STATUS-"].update(check_winner(board))
        


def check_winner(board: list) -> str: # doesn't work yet lol
    # check horizontally
    for row in board:
        if row[0] == row[1] == row[2]:
            return "X is the winner!" if row[0] == "X" else "O is the winner!"
    # check vertically
    columns_board = [["" for _ in range(3)] for _ in range(3)]

if __name__ == "__main__":
    main()
