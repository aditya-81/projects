board = ["-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-"]  # our game board
game_still_on = True
winner = None
current_player = "X"


# Functionssss
def start():
    rules()
    display_board()  # initial borad
    while game_still_on:
        give_turn(current_player)  # handle a turn
        check_for_game_winner()  # Check for winner or tie
        change_player()  # opponents turn.
    if winner == "X" or winner == "O":
        print(f"{winner} Won Congratulations")
    elif winner == None:
        print("It is a tie. Nice Game")


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4] + " | " + board[
        5] + "       1 |  2 |  3 |  4 |  5 |  6")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | " + board[9] + " | " + board[10] + " | " + board[
        11] + "       7 |  8 |  9 | 10 | 11 | 12")
    print(board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] + " | " + board[16] + " | " + board[
        17] + "      13 | 14 | 15 | 16 | 17 | 18")
    print(board[18] + " | " + board[19] + " | " + board[20] + " | " + board[21] + " | " + board[22] + " | " + board[
        23] + "      19 | 20 | 21 | 22 | 23 | 24")
    print(board[24] + " | " + board[25] + " | " + board[26] + " | " + board[27] + " | " + board[28] + " | " + board[
        29] + "      25 | 26 | 27 | 28 | 29 | 30")
    print("\n")


def give_turn(player):
    print(player + "'s turn.")
    position = input("Choose a number from 1-30: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                               "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]:
            position = input("Choose a number from 1-30: ")
        while int(position) in range(25) and board[int(position) + 5] == "-":
            print("Rule violation try again")
            position = input("Choose a number from 1-30: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Position Blocked. Try Again.")

    board[position] = current_player
    display_board()


def check_for_game_winner():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner
    row_winner = check_rows()
    coloumn_winner = check_coloumns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_on
    row11 = board[0] == board[1] == board[2] == board[3] != "-"
    row12 = board[1] == board[2] == board[3] == board[4] != "-"
    row13 = board[2] == board[3] == board[4] == board[5] != "-"
    row21 = board[6] == board[7] == board[8] == board[9] != "-"
    row22 = board[7] == board[8] == board[9] == board[10] != "-"
    row23 = board[8] == board[9] == board[10] == board[11] != "-"
    row31 = board[12] == board[13] == board[14] == board[15] != "-"
    row32 = board[13] == board[14] == board[15] == board[16] != "-"
    row33 = board[14] == board[15] == board[16] == board[17] != "-"
    row41 = board[18] == board[19] == board[20] == board[21] != "-"
    row42 = board[19] == board[20] == board[21] == board[22] != "-"
    row43 = board[20] == board[21] == board[22] == board[23] != "-"
    row51 = board[24] == board[25] == board[26] == board[27] != "-"
    row52 = board[25] == board[26] == board[27] == board[28] != "-"
    row53 = board[26] == board[27] == board[28] == board[29] != "-"
    if row11 or row12 or row13 or row21 or row22 or row23 or row31 or row32 or row33 or row41 or row42 or row43 or row51 or row52 or row53:
        game_still_on = False
        if row11:
            return board[0]
        elif row12:
            return board[1]
        elif row13:
            return board[2]
        elif row21:
            return board[6]
        elif row22:
            return board[7]
        elif row23:
            return board[8]
        elif row31:
            return board[12]
        elif row32:
            return board[13]
        elif row33:
            return board[14]
        elif row41:
            return board[18]
        elif row42:
            return board[19]
        elif row43:
            return board[20]
        elif row51:
            return board[24]
        elif row52:
            return board[25]
        elif row53:
            return board[26]
        else:
            return None


def check_coloumns():
    global game_still_on
    col11 = board[0] == board[6] == board[12] == board[18] != "-"
    col12 = board[6] == board[12] == board[18] == board[24] != "-"
    col21 = board[1] == board[7] == board[13] == board[19] != "-"
    col22 = board[7] == board[13] == board[19] == board[25] != "-"
    col31 = board[2] == board[8] == board[14] == board[20] != "-"
    col32 = board[8] == board[14] == board[20] == board[26] != "-"
    col41 = board[3] == board[9] == board[15] == board[21] != "-"
    col42 = board[9] == board[15] == board[21] == board[27] != "-"
    col51 = board[4] == board[10] == board[16] == board[22] != "-"
    col52 = board[10] == board[16] == board[22] == board[28] != "-"
    col61 = board[5] == board[11] == board[17] == board[23] != "-"
    col62 = board[11] == board[17] == board[23] == board[29] != "-"
    if col11 or col12 or col21 or col22 or col31 or col32 or col41 or col42 or col51 or col52 or col61 or col62:
        game_still_on = False
        if col11:
            return board[0]
        elif col12:
            return board[6]
        elif col21:
            return board[1]
        elif col22:
            return board[7]
        elif col31:
            return board[2]
        elif col32:
            return board[8]
        elif col41:
            return board[3]
        elif col42:
            return board[9]
        elif col51:
            return board[4]
        elif col52:
            return board[10]
        elif col61:
            return board[5]
        elif col62:
            return board[11]
        else:
            return None


def check_diagonals():
    global game_still_on
    diag11 = board[0] == board[7] == board[14] == board[21] != "-"
    diag12 = board[1] == board[8] == board[15] == board[22] != "-"
    diag13 = board[2] == board[9] == board[16] == board[23] != "-"
    diag21 = board[6] == board[13] == board[20] == board[27] != "-"
    diag22 = board[7] == board[14] == board[21] == board[28] != "-"
    diag23 = board[8] == board[15] == board[22] == board[29] != "-"
    diag31 = board[5] == board[10] == board[15] == board[20] != "-"
    diag32 = board[4] == board[9] == board[14] == board[19] != "-"
    diag33 = board[3] == board[8] == board[13] == board[18] != "-"
    diag41 = board[11] == board[16] == board[21] == board[26] != "-"
    diag42 = board[10] == board[15] == board[20] == board[25] != "-"
    diag43 = board[9] == board[14] == board[19] == board[24] != "-"
    if diag11 or diag12 or diag13 or diag21 or diag22 or diag23 or diag31 or diag32 or diag33 or diag41 or diag42 or diag43:
        game_still_on = False
        if diag11:
            return board[0]
        elif diag12:
            return board[1]
        elif diag13:
            return board[2]
        elif diag21:
            return board[6]
        elif diag22:
            return board[7]
        elif diag23:
            return board[8]
        elif diag31:
            return board[5]
        elif diag32:
            return board[4]
        elif diag33:
            return board[3]
        elif diag41:
            return board[11]
        elif diag42:
            return board[10]
        elif diag43:
            return board[9]
        else:
            return None


def check_for_tie():
    global game_still_on
    if "-" not in board:
        game_still_on = False
        return True
    else:
        return False


def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def rules():
    print("Rules are as follows:-\n ")
    print("It Is A 2-Player Game.\n")
    print("The bottom row must contain a peice to stack another peice over it.\n")
    print(
        "The game is similar to Tic Tac Toe. The difference being you have to 4 continouos peices and also following rule 1\n")
    print(
        "The game ends if either of the player has stacked 4 peices continuously either vertically/horizontally or diagonally\nENJOY")


start()
