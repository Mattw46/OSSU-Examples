"""
ESTIMATED TIME TO COMPLETE: 15 minutes

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 
(not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
"""

print("Please think of a number between 0 and 100! ")

high = 100
low = 0
guess = 50
answer = 'x'

while(answer != 'c'):
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == 'c':
        break
    elif answer == 'l':
        low = guess
        guess = low + ((high - low) // 2)
    elif answer == 'h':
        high = guess
        guess = low + ((high - low) // 2)
    else:
        print("Sorry, I did not understand your input.")
        
print("Game over. Your secret number was: " + str(guess))