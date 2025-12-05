import art, game_data
from random import choice
# TODO - introduce Logo
print(art.logo)
score = 0
winner = ""
comperision = []
cont_game = True

def selection(comperision):
    # TODO - generate random comparison & compare 
    comperision.append(choice(game_data.data))
    if len(comperision) == 2:
        if comperision[0]["follower_count"] > comperision[1]["follower_count"]:
            winner = "A"
        elif comperision[0]["follower_count"] < comperision[1]["follower_count"]:
            winner = "B"
        return winner

def user_input(comperision):
    # TODO - Ask user for tip
    print(f"Compare A: {comperision[0]["name"]}, a {comperision[0]["description"]}, from {comperision[0]["country"]}.")
    print(art.vs)
    print(f"Against B: {comperision[1]["name"]}, a {comperision[1]["description"]}, from {comperision[1]["country"]}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    return guess

# TODO - Main game logic
while cont_game:
    # TODO - clear comperision list if game is in continueation and add new compare
    if len(comperision) != 0:
        comperision.reverse()
        comperision.pop()
        winner = selection(comperision)
    # TODO - Initiate comperision list
    else:
        for i in range(1,3):
            winner = selection(comperision)
    # TODO call in user
    guess = user_input(comperision)
    # TODO - Infrom user on outcome
    if winner == guess:
        score += 1
        print(f"\nYou are right. Current score: {score}")
    else:
        print(f"Sorry, that is wrong. Final score: {score}")
        cont_game = False