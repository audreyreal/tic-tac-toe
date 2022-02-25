import random
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
        [sg.Text("Game in progress!", key="-STATUS-")],
    ]

    return sg.Window(
        "Tic-Tac-Toe",
        layout=layout,
        use_default_focus=False,
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
    while (event := window.read()[0]) is not None:
        if window[event].get_text() == "":
            column, row = event_map[event]
            write_value = "X" if turn % 2 == 0 else "O"
            turn += 1
            window[event].update(write_value)
            board[column][row] = write_value
            if turn == 9:
                window["-STATUS-"].update("Draw!")
            window["-STATUS-"].update(check_winner(board))


def check_winner(board: list) -> str or None:  # actually works now lets go
    # check horizontally
    for row in board:
        if "" not in row and row[0] == row[1] == row[2]:
            return f"{row[0]} is the winner!"
    # check vertically
    transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
    for column in transposed_board:
        if "" not in column and column[0] == column[1] == column[2]:
            return f"{column[0]} is the winner!"
    # check diagonally
    descending_diagonals = [board[x][x] for x in range(3)]
    ascending_diagonals = [board[0][2], board[1][1], board[2][0]]
    if "" not in descending_diagonals and len(set(descending_diagonals)) == 1:
        return f"{descending_diagonals[1]} is the winner!"
    if "" not in ascending_diagonals and len(set(ascending_diagonals)) == 1:
        return f"{ascending_diagonals[1]} is the winner!"


if __name__ == "__main__":
    main()
