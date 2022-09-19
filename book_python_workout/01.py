import random


def want_to_play_another() -> bool:
    answer = input("Quit the game: [y]/n: ")
    if answer.lower().startswith("n"):
        return False
    return True


still_playing = True

print("***** GUES THE NUMBER GAME *****")
while still_playing:
    number = random.randint(0, 100)
    while True:
        player_guesed = int(input("Please select number between 0 and 100: "))
        if player_guesed == number:
            print("Just right.")
            break
        elif player_guesed > number:
            print("Too high.")
        else:
            print("Too low.")

    still_playing = want_to_play_another()

print("Good bye!")
