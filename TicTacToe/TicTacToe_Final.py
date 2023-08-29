#Importing from the os library, which is used to interact with the operating system.
import os
 
#Function responsible for printing the game board in the form of a 3x3 grid.      
def printGrid(grid):
    for row in grid:
        print(' | '.join(row))
        print('-' * 9)
        
#Function that checks if the cell in position (x,y), in case it does not fill it.
def play(grid, x, y, symbol):
    if grid[x][y] == ' ':
        grid[x][y] = symbol
        return True
    else:
        return False

#Function that checks if the current player (represented by the symbol) has won the game.Contains functions that check the cells in lines, columns and diagonals
def checkWin(grid, symbol):
    def check_row():
            for row in grid:
                if all(cell == symbol for cell in row):
                    return True
    def check_column():
        for col in range(3):
            if all(grid[row][col] == symbol for row in range (3)):
                return True
    def check_diagonals():
        if all(grid[i][i] == symbol for i in range(3)) or all(grid[i][2 - i] == symbol for i in range(3)):
            return True

    return check_row() or check_column() or check_diagonals()

names=[]

#Function that requests the names of two players that cannot contain a newline or a colon. Returns valid names in a list.
def receive_validate_names(names):
    for i in range(2):
        while True:
            name = input(f"Type the {i+1} name: ")
            
            if len(name) > 40:
                print("Error type1")
            elif '\n' in name or ':' in name:
                print("Error type2")
            else:
                names.append(name)
                break
                
    return names

#Atribui os símbolos 'X' e 'O' aos jogadores na ordem em que os nomes foram fornecidos.
def assign_symbols(players):
    symbols = ['X', 'O']
    player_symbols = {players[0]: symbols[0], players[1]: symbols[1]}
    return player_symbols

#Main function, calls all other methods, is the brain of the operation. Saves the scores in the file "scores1.txt".

def main():
    grid = [[' ' for _ in range(3)] for _ in range(3)]

    

    players = receive_validate_names(names)
    player_symbols = assign_symbols(players)

    scores = {}

    if os.path.exists("scores1.txt"):
        with open("scores1.txt", "r") as Raid:
            for line in Raid:
                name, score = line.strip().split(":")
                scores[name] = int(score)

    current_player = players[0]

    while True:
        printGrid(grid)

        while True:
            x = int(input(f"{current_player}, enter the row where you want to place {player_symbols[current_player]} (0-2): "))
            y = int(input(f"{current_player}, enter the column where you want to place {player_symbols[current_player]} (0-2): "))
            if play(grid, x, y, player_symbols[current_player]):
                break
            else:
                print("Invalid position! Try again.")

        if checkWin(grid, player_symbols[current_player]):
            printGrid(grid)
            print(f"Congratulations, {current_player}! You won!")
            scores[current_player] = scores.get(current_player, 0) + 2
            scores[players[1 - players.index(current_player)]] = scores.get(players[1 - players.index(current_player)], 0)
            break

        if all(cell != ' ' for row in grid for cell in row):
            printGrid(grid)
            print("It's a draw!")
            scores[players[0]] = scores.get(players[0], 0) + 1
            scores[players[1]] = scores.get(players[1], 0) + 1
            break

        current_player = players[1 - players.index(current_player)]

    with open("scores1.txt", "w") as f:
        for name, score in scores.items():
            f.write(f"{name}:{score}\n")

#Run the program, first checking that it is running as the main function and not as an imported module. At the end it asks the user if he wants to continue playing.
if __name__ == "__main__":
    while True:
        main()
        answer = input("Do you want to play again? (Y/N): ").upper()
        if answer != 'Y':
            break
