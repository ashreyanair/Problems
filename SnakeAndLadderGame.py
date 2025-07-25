import random
snakes = {22: 6, 45: 30, 96: 64}
ladders = {7: 24, 21: 77, 42: 90, 40: 60}
positions = {1: 0, 2: 0}
def roll_die():
    return random.randint(1, 6)
def move(player):
    die = roll_die()
    print(f"Dice no: {die}")

    new_pos = positions[player] + die

    if new_pos > 100:
        new_pos = positions[player]
    else:
        if new_pos in ladders:
            print("Ladder climbed!")
            new_pos = ladders[new_pos]
        elif new_pos in snakes:
            print("Caught by snake!")
            new_pos = snakes[new_pos]
    positions[player] = new_pos

def play_game():
    while True:
        try:
            player = int(input("Enter the player no : "))
            if player not in [1, 2]:
                print("Invalid player number. Enter either 1 or 2: 1")
                continue
            move(player)
            print(f"player 1: {positions[1]}")
            print(f"player 2: {positions[2]}")
            print("-" * 30)
            if positions[player] == 100:
                print(f" Player {player} wins!")
                break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
play_game()