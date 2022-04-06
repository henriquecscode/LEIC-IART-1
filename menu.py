
#https://ozzmaker.com/add-colour-to-text-in-python/


from algo import Minimax, heuristic_1, heuristic_2, heuristic_3, heuristic_4
from players import Player, AI, outcolors

def menu() :
    print(outcolors.HEADING + '██╗░░░░░██╗███╗░░██╗███████╗░██████╗  ░█████╗░███████╗  ░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗\n██║░░░░░██║████╗░██║██╔════╝██╔════╝  ██╔══██╗██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║\n██║░░░░░██║██╔██╗██║█████╗░░╚█████╗░  ██║░░██║█████╗░░  ███████║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║\n██║░░░░░██║██║╚████║██╔══╝░░░╚═══██╗  ██║░░██║██╔══╝░░  ██╔══██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║\n███████╗██║██║░╚███║███████╗██████╔╝  ╚█████╔╝██║░░░░░  ██║░░██║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║\n╚══════╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░  ░╚════╝░╚═╝░░░░░  ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝')
    print(outcolors.MENU_TEXT + 'THESE ARE THE POSSIBLE MODES, FOR YOUR REFERENCE:')
    print(outcolors.NORMAL + '1 - HUMAN VS. HUMAN')
    print(outcolors.NORMAL + '2 - HUMAN VS. PC')
    print(outcolors.NORMAL + '3 - PC VS. HUMAN')
    print(outcolors.NORMAL + '4 - PC VS. PC')

    player1 = getPlayer(1)
    player2 = getPlayer(2)

    return player1, player2

def getPlayer(number) :
    print(outcolors.NORMAL + '\nIF YOU WISH TO PLAY AS YOURSELF, INPUT 0')
    println(outcolors.NORMAL + 'IF YOU WISH TO BE A PC, INPUT 1.')
    print(outcolors.HEADING + 'PLAYER ' + str(number) + ': ')
    option = getOption(outcolors.INPUT_TEXT + 'Player type? ' + outcolors.NORMAL, 0, 1)
    if option == 0:
        name = input(outcolors.INPUT_TEXT + 'What is your player name? ' + outcolors.NORMAL)
        return Player(name)
    elif option == 1:
        algo = getOption(outcolors.INPUT_TEXT + '\nChoose your poison: \n' + outcolors.NORMAL + '1 - Number of Playable Pieces\n2 - Number of Groups of Pieces\n3 - Number of Plays that Result in a Capture\n4 - Footprint Maximizer\n\n' + outcolors.INPUT_TEXT + 'Your option: ' + outcolors.NORMAL, 1, 4)
        if algo == 1:
            heuristic = heuristic_1
        elif algo == 2:
            heuristic = heuristic_2
        elif algo == 3:
            heuristic = heuristic_3
        elif algo == 4:
            heuristic = heuristic_4
        depth = getOption(outcolors.INPUT_TEXT + 'Input the desired depth (1-4): ' + outcolors.NORMAL, 1, 4)
        
        algorithm = Minimax(depth, heuristic)
        personalized_name = getOption(outcolors.INPUT_TEXT + 'Do you want a personalized name? ' + outcolors.NORMAL, 0, 1)
        if personalized_name:
            name = input(outcolors.INPUT_TEXT + 'Input your desired name: ' + outcolors.NORMAL)
        else:
            name = None

        is_maximizer = 1 if number == 1 else -1 # If it is the first player then it is the maximizer

        return AI(algorithm, is_maximizer, name)
        
def getOption(prompt, lower, higher):
    while True:
        move = input(prompt)
        if move.isdigit():
            move = int(move)
            if lower <= move <= higher:
                return move

def println(str = '') :
    print(str + '\n')