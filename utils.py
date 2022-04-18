class outcolors :
    HEADING = '\033[38;5;135m'
    INPUT_TEXT = '\u001b[38;5;183m'
    MENU_TEXT = '\033[38;5;135m'
    NORMAL = '\u001b[37m'
    COORDINATES = '\033[38;5;135m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'

def _print_board(board):
    def _print_line(line):
        for i in range(0, 8):
            if (line[i] == 1):
                print(outcolors.RED, end="")
            elif (line[i] == 2):
                print(outcolors.BLUE, end="")
            else:
                print(outcolors.NORMAL, end="")
            
            print(" " + str(line[i]), end="")
    
    print(outcolors.COORDINATES + "  0 1 2 3 4 5 6 7")
    for i in range(0, 8):
        print(outcolors.COORDINATES + str(i) + outcolors.NORMAL, end="")
        _print_line(board[i])
        print()
    print()
