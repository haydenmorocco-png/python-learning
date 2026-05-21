import random
def diffculty_select():
    difficulty = input("Choose difficulty — easy / medium / hard: ")
    print("I've picked a number between 1 and 100.")
    if difficulty.lower() == "hard":
        guesses = 5
        return guesses
    elif difficulty.lower() == "medium":
        guesses = 7
        return guesses
    elif difficulty.lower() == "easy":
        guesses = 10
        return guesses
    else:
        print("Try again")
        return diffculty_select()



def play_again():
    again = input("Do you want to play again (yes/no): ")
    if again.lower() == "no":
        playing = False
        return playing
    elif again.lower() == "yes":
        playing = True
        return playing
    else:
        print("Error, try again.")
        return play_again()



print("=================================")
print("     NUMBER GUESSING GAME")
print("=================================")
wins = 0
losses = 0
playing = True
while playing:
    print(f"Score: {wins} wins, {losses} losses")
    guesses = diffculty_select()
    print(f"You have {guesses} guesses. Good luck!")
    number = random.randint(1,100)
    i = 1
    while i <= guesses:
        user_input = input(f"Guess {i}/{guesses}: ")
        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess == number:
                print(f"Correct! The number was {number}.")
                print(f"You got it in {i} guess(es)!")
                i = guesses + 1
        elif guess > 100 or guess < 1:
             print("Range error, try again")
        elif guess < number:
             print("Too low.")
             i += 1
        elif guess > number:
             print("Too high.")
             i += 1
        else:
             print("Error, try again.")
    if guess != number:
         print(f"Sorry you lost, the number was {number}.")
         losses += 1
    else:
         wins += 1
    playing = play_again()
print(f"Final score: {wins} win(s), {losses} loss(es). See you next time!")