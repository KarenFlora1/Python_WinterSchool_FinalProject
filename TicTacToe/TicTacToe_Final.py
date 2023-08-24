import os

def printGrid(grid):
    for row in grid:
        print(' | '.join(row))
        print('-' * 9)

def play(grid, x, y, symbol):
    if grid[x][y] == ' ':
        grid[x][y] = symbol
        return True
    else:
        return False

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
#testar se realmente valida
def receive_validate_names(names):
        for i in range (2):
            while True:
                names.append(input(f"Type the {i+1} name: "))
                if (len(names[i])>40):
                    print("Error type1")
                elif '\n' in names[i] or ':' in names[i]:
                    print("Error type2")
                else:
                    break
        return names


def assign_symbols(players):
    symbols = ['X', 'O']
    player_symbols = {players[0]: symbols[0], players[1]: symbols[1]}
    return player_symbols

def main():
    grid = [[' ' for _ in range(3)] for _ in range(3)]

    

    players = receive_validate_names(names)
    player_symbols = assign_symbols(players)

    scores = {}

    if os.path.exists("scores1.txt"):
        with open("scores1.txt", "r") as f:
            for line in f:
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

if __name__ == "__main__":
    while True:
        main()
        answer = input("Do you want to play again? (Y/N): ").upper()
        if answer != 'Y':
            break