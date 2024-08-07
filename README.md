# READ ME

## Contributors

[Henrique Sousa (Self)](https://github.com/henriquecscode)

[Mateus Silva](https://github.com/lessthelonely)

[Melissa Silva](https://github.com/melisilva)

## The Game

*Lines of Action* is a 1v1 board game in which players take turns in moving one of their pieces at a time - the catch? They can only move as many spaces as the *line of action* allows: if we move horizontally, then the number of pieces in the line determines exactly how many places we can move. Same happens vertically and diagonally.

Players can capture the opponent's pieces with an exact movement to a piece's position; they can also skip over their own pieces, but never an opponent's. The end goal? Connecting all pieces: as long as all pieces can be reached from which ever piece we start in a group, the pieces are connected.

This also means that capturing can make it easier for the opponent to connect their pieces - less pieces to move makes it easier to connect them all. Only one piece left? That's an instant win.

## How To Run The Game

The game was programmed in Python, thus it requires Python to run. We recommend the most recent version, which you can find in the following link: https://www.python.org/downloads/.

After this, opening a terminal in the source directory (where all files are present) and running the command *python ./main.py* is enough.

### The Menu

When one initially runs the game, they'll be greeted with a menu. It works through text input and there are contextual clues to help understand how to run the game. Every time the game is run, the player's settings will need to be setup: is it a human player or a computer? Does the player wish for a custom name?

In case of PC players, you'll have to provide a difficulty for it: we provide 4 levels of difficulty. These actually determine the heuristic used for the AI to chose its moves, and a description of them is provided, should a player be interested. There's also a way more approachable description which should let you know if you're playing casually or sweating the game out against a mighty opponent.

We hope the reader enjoys the game!
