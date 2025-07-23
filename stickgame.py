import random

# Greet the user
user_name = input("Enter your name: ")  # input username 
print(f"Hello, {user_name}! Welcome to the Stick Pulling Game!")

# Error handling for number of sticks
try:
    sticks_num = int(input("Enter the number of sticks: "))
except ValueError:
    print("that's not a number! (¬_¬)")
    exit(1)

print(f"There are {sticks_num} sticks in the game.")

# Computer's move logic: try to lose on purpose (leave a multiple of 3 for the player)
def computer_pull(sticks_left):
    # Always try to leave a multiple of 3 for the player
    if sticks_left <= 1:
        return 1
    elif (sticks_left - 1) % 3 == 0:
        return 1
    elif (sticks_left - 2) % 3 == 0 and sticks_left >= 2:
        return 2
    else:
        return 1 if sticks_left >= 1 else 0  # fallback

# Main game logic
def stick_pulling_game(sticks):
    n = 0
    while sticks > 0:
        # Player turn
        try:
            player_pull = int(input("how many would you pull? "))
        except ValueError:
            print("that's not a number! (¬_¬)")
            print("-----------------------------------------------------------------------")
            continue

        if player_pull > 2:
            print("your greed sicken me. (¬_¬)")
            print("-----------------------------------------------------------------------")
            continue
        elif player_pull < 1:
            print("coward. (≖⩊≖)")
            print("-----------------------------------------------------------------------")
            continue

        sticks -= player_pull
        n += 1

        if sticks <= 0:
            print("u pulled the last stick. loser (˵¬ᴗ¬˵)")
            print(f"you pulled {n} times.")
            print("....")
            print("how to win this game?")
            print("well... idk, we have to wait for ajarn to teach us.")
            break
        else:
            print(f"{sticks} sticks remain.")
            print("-----------------------------------------------------------------------")

        # Computer turn
        comp_pull = computer_pull(sticks)
        print(f"The computer pulls {comp_pull} stick(s).")
        sticks -= comp_pull

        if sticks <= 0:
            print("The computer pulled the last stick.")
            print("YOU WIN!! ᕙ(`▽´)ᕗ")
            print(f"Total player turns: {n}")
            print("Computer: 'Nooo... I have been outwitted by a human??!! (☉_☉)'")
            print("Computer: '...Recalibrating pride circuits... (╯°□°）╯︵ ┻━┻'")
            break
        else:
            print(f"{sticks} sticks remain.")
            print("-----------------------------------------------------------------------")

# Start the game
stick_pulling_game(sticks_num)
