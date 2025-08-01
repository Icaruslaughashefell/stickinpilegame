import random

# Greet the user
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to the Stick Pulling Game!")

# Error handling for number of sticks
try:
    sticks_num = int(input("Enter the number of sticks: "))
    if sticks_num < 1:
        print("you can't play with no stick. ಠ_ಠ")
        exit(1)
except ValueError:
    print("that's not a number! (¬_¬)")
    exit(1)

# Error handling for max sticks per turn
try:
    max_pull = int(input("What's the MAX number of sticks you can pull per turn? "))
    if max_pull < 1:
        print("you have to pull *at least* one stick, drama queen. 🙄")
        exit(1)
except ValueError:
    print("are you okay? that wasn’t a number either. (눈_눈)")
    exit(1)

print(f"There are {sticks_num} sticks in the game.")
print(f"You can pull 1 to {max_pull} sticks per turn.")
print("-----------------------------------------------------------------------")

# Smart AI strategy: try to win if possible, else random
def computer_pull(sticks_left):
    target = max_pull + 1
    # If AI can win right now, take the last stick(s)
    if sticks_left <= max_pull:
        return sticks_left

    # Ideal move: leave a multiple of (max_pull + 1) to the player
    for i in range(1, max_pull + 1):
        if (sticks_left - i) % target == 0:
            return i

    # If there's no winning move, pick random just to spice it up
    return random.randint(1, max_pull)

# Main game logic
def stick_pulling_game(sticks):
    n = 0
    while sticks > 0:
        # Player turn
        try:
            player_pull = int(input("How many would you pull? "))
        except ValueError:
            print("that’s not a number! ಠ益ಠ")
            print("-----------------------------------------------------------------------")
            continue

        if player_pull > max_pull:
            print(f"your greed sicken me. you can only pull up to {max_pull} stick(s). (¬_¬)")
            print("-----------------------------------------------------------------------")
            continue
        elif player_pull < 1:
            print("coward. at least take 1 stick. (≖⩊≖)")
            print("-----------------------------------------------------------------------")
            continue
        elif player_pull > sticks:
            print(f"there aren't that many sticks left, genius. only {sticks} remain. (눈_눈)")
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
