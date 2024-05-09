def printBoard(xstate, zstate):
    zero = "X" if xstate[0] else ("O" if zstate[0] else 0)
    one = "X" if xstate[1] else ("O" if zstate[1] else 1)
    two = "X" if xstate[2] else ("O" if zstate[2] else 2)
    three = "X" if xstate[3] else ("O" if zstate[3] else 3)
    four = "X" if xstate[4] else ("O" if zstate[4] else 4)
    five = "X" if xstate[5] else ("O" if zstate[5] else 5)
    six = "X" if xstate[6] else ("O" if zstate[6] else 6)
    seven = "X" if xstate[7] else ("O" if zstate[7] else 7)
    eight = "X" if xstate[8] else ("O" if zstate[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")


def CheckWin(xstate, zstate):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for win in wins:
        if xstate[win[0]] + xstate[win[1]] + xstate[win[2]] == 3:
            print(f"X won the match")
            return 1

        if zstate[win[0]] + zstate[win[1]] + zstate[win[2]] == 3:
            print(f"O won the match")
            return 1

    return -1


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's chance")
            value = int(input("Please Enter the Position on the Board : "))
            xState[value] = 1
        else:
            print("O's chance")
            value = int(input("Please Enter the Position on the Board : "))
            zState[value] = 1

        turn = 0 if turn == 1 else (1 if turn == 0 else 0)
        
        if CheckWin(xState, zState) != -1:
            printBoard(xState, zState)
            print("--Game Drawed--")
            break
        