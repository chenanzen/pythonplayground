import random

# roll 2 dice, return the sum
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def find_winner(player1, player2, player1_roll, player2_roll):
    if player1_roll > player2_roll:
        print(f"{player1} wins!")
    elif player2_roll > player1_roll:
        print(f"{player2} wins!")
    else:
        print("It's a tie!")

player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

player1_roll = roll_dice()
player2_roll = roll_dice()

print(f"{player1} rolled {player1_roll}")
print(f"{player2} rolled {player2_roll}")
find_winner(player1, player2, player1_roll, player2_roll)