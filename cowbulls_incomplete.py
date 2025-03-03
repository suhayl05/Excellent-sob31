import random

def compare_numbers(number, user_guess): # (Mohammed suhayl, M01033117) compare_numbers() is defined but does not contain logic for counting cows and bulls.
    cows = 0  # (Mohammed suhayl, M01033117) defining variable
    bulls = 0  # (Mohammed suhayl, M01033117) defining variable

    for i in range(len(number)):
        if user_guess[i] == number[i]:  #(Mohammed suhayl, M01033117) if statement added for loop
            bulls += 1
        elif user_guess[i] in number:  # (Mohammed suhayl, M01033117) else statement added
            cows += 1

    return cows, bulls  # (Mohammed suhayl, M01033117) Return a tuple

playing = True
number = str(random.randint(1000, 9999)) # (Mohammed suhayl, M01033117) changed 0 to 1000
guesses = 0

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") # (Mohammed suhayl, M01033117) changed raw input to input
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")