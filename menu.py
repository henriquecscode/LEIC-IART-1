
#https://ozzmaker.com/add-colour-to-text-in-python/


from algo import Minimax, heuristic_1, heuristic_2, heuristic_3, heuristic_4
from players import Player, AI


def menu() :
    print('\033[6;35;40m WELCOME TO PYTHON LINES OF ACTION\n')
    print('\033[1;35;40m HERE ARE THE OPTIONS:\n')
    print('\n')
    print('\033[1;32;40m 1 - HUMAN VS. HUMAN')
    print('\033[1;32;40m 2 - HUMAN VS. PC')
    print('\033[1;32;40m 3 - PC VS. HUMAN')
    print('\033[1;32;40m 4 - PC VS. PC')

    op = input()
    player1 = getPlayer(1)
    player2 = getPlayer(2)
    
    return player1, player2

def getPlayer(number) :
    println('\033[1;35;40m IF YOU WISH TO PLAY AS YOURSELF, INPUT 0')
    println('\033[1;35;40m IF YOU WISH TO BE A PC, INPUT 1.')
    println()
    println(f'PLAYER {number}: ')
    option = getOption('Type of player', 0, 1)
    if option == 0:
        name = input("What is your player name")
        return Player(name)
    elif option == 1:
        algo = getOption('Choose your poison: \n1 - Number of Playable Pieces\n2 - Number of Groups of Pieces\n3 - Number of Plays that Result in a Capture\n4 - Footprint Maximizer', 1, 4)
        if algo == 1:
            heuristic = heuristic_1
        elif algo == 2:
            heuristic = heuristic_2
        elif algo == 3:
            heuristic = heuristic_3
        elif algo == 4:
            heuristic = heuristic_4

        depth = getOption('Choose your depth (1-4):', 1, 4)
        
        algorithm = Minimax(depth, heuristic)
        personalized_name = getOption("Do you want a personalized name?", 0, 1)
        if personalized_name:
            name = input("What is the name")
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