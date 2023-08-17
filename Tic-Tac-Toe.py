def sum(a, b, c):
    return a + b + c

def print_board(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else " ")
    one = 'X' if xState[1] else ('O' if zState[1] else " ")
    two = 'X' if xState[2] else ('O' if zState[2] else " ")
    three = 'X' if xState[3] else ('O' if zState[3] else " ")
    four = 'X' if xState[4] else ('O' if zState[4] else " ")
    five = 'X' if xState[5] else ('O' if zState[5] else " ")
    six = 'X' if xState[6] else ('O' if zState[6] else " ")
    seven = 'X' if xState[7] else ('O' if zState[7] else " ")
    eight = 'X' if xState[8] else ('O' if zState[8] else " ")
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def check_win(x_state, z_state):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum(z_state[win[0]], z_state[win[1]], z_state[win[2]]) == 3:
            print("O Won the match")
            return 0
    return -1

if __name__ == "__main__":
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        print_board(x_state, z_state)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            x_state[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            z_state[value] = 1
        win_status = check_win(x_state, z_state)
        if win_status != -1:
            print("Match over")
            break
        turn = 1 - turn
