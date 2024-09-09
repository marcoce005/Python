import random


def display_board():
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for e in board:
        print("|       " * 3 + "|")
        print("|   {}   |   {}   |   {}   |".format(e[0], e[1], e[2]))
        print("|       " * 3 + "|")
        print("+-------+-------+-------+")


def enter_move():
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while 1:
        try:
            m = int(input("Enter your move:\t"))
            if type(board[m // 3][m % 3]) is int:
                board[m // 3][m % 3] = "O"
                return
            else:
                print("This cell is full!!!")
        except KeyboardInterrupt:
            global end
            end = False
            return
        except:
            print("ERROR! Wrong move")


def make_list_of_free_fields():
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return [e for r in board for e in r if type(e) is int]


def exit_game(s):
    global end
    end = False
    print("The winner is........\n{} player".format(s))


def victory_for(sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if str(board[i][0]) + str(board[i][1]) + str(board[i][2]) == sign * 3:
            exit_game(sign)

    for j in range(3):
        if str(board[0][j]) + str(board[1][j]) + str(board[2][j]) == sign * 3:
            exit_game(sign)

    if (
        str(board[0][0]) + str(board[1][1]) + str(board[2][2]) == sign * 3
        or str(board[0][2]) + str(board[1][1]) + str(board[2][0]) == sign * 3
    ):
        exit_game(sign)


def draw_move():
    # The function draws the computer's move and updates the board.
    l = make_list_of_free_fields()
    if len(l) == 1:
        board[l[0] // 3][l[0] % 3] = "X"
        global end
        end = False
        return
    else:
        ran = random.choice(l)
        board[ran // 3][ran % 3] = "X"
        return


end = True
board = [[i for i in range(j * 3, j * 3 + 3)] for j in range(0, 3)]
board[1][1] = "X"

display_board()
while end:
    enter_move()
    display_board()
    victory_for("O")
    if not end:
        break
    draw_move()
    display_board()
    victory_for("X")
    if not end:
        break
