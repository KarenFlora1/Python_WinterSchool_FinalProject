# Python_WinterSchool_FinalProject
### TicTacToe game using python
This repository contains a simple implementation of Tic-Tac-Toe in Python. The game is designed to be played by two players alternately on the same terminal. Below is an overview of how the game works:

###### Board and Moves:
The board is represented by a 3x3 matrix.
Players enter their moves by indicating the row and column where they wish to place their symbol ('X' or 'O').

###### Win and Draw:
The game checks on each move if a player has won or if the game is a draw.
A win occurs when a player has three matching symbols in a row, column or diagonal.
The game is a draw when all the cells on the board are filled, but neither player wins.

###### Scores:
Each player's scores are maintained and updated throughout the game.
Scores are stored in a file called "scores1.txt".
The file is read at game start to load previous scores and updated at the end of each game.

###### Execution:
The game starts from the tic_tac_toe.py file.
Players enter their names and alternate turns until the game ends.
After each game, players are given the option to play again.

###### Requirements:
This game requires Python 3.x to run in the terminal.

###### Instructions for use:
Clone this repository to your local machine.
Open a terminal in the repository folder and run the python tic_tac_toe.py command.
Follow the instructions on the terminal to enter names and play.

###### Customizations:
You can customize the appearance of the board and game messages in code.
Feel free to add new features like a GUI or different game modes.

Disclaimer: This is a simple project for learning and fun purposes. If you want to build a more advanced implementation, consider adding exception handling, more robust input validation, and other improvements (such as using the Pygame programming library). 

###### Hope You Enjoy It!
