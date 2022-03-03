"""Multiplayer Tic Tac Toe Program

Returns:
    None: None
"""
import random
import PySimpleGUI as sg


def gui() -> sg.Window:
    """Define the main gui

    Returns:
        sg.Window: The tic tac toe GUI with layout
    """
    sg.theme("Reddit")

    def button(key: int) -> sg.Button:
        return sg.Button("", key=f"-{key}-", size=(3, 1))

    layout = [
        [button(1), button(2), button(3)],
        [button(4), button(5), button(6)],
        [button(7), button(8), button(9)],
        [sg.Text("Game in progress!", key="-STATUS-")],
    ]

    return sg.Window(
        "Tic-Tac-Toe",
        layout=layout,
        use_default_focus=False,
        
    )


def main() -> None:
    """Main function

    Returns:
        None: None
    """
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
    """Checks for winner of a tic tac toe board

    Args:
        board (list): Current tic tac toe board

    Returns:
        str or None: None if noone has won, str if someone has
    """
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


def normal_ai(board: list) -> list:
    """Beatable tic tac toe AI

    Args:
        board (list): Current tic tac toe board composition

    Returns:
        list: Tic tac toe board with another square filled out by the AI
    """
    computer_choice = random.choice(board)
    if computer_choice != "":
        return 


if __name__ == "__main__":
    main()
