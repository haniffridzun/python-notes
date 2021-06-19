# this is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('i am thinking of a number between 1 and 20')

# ask the player to guess 6 times
for guessesTaken in range(1, 7):    # loop to guess 6 times
    print('take a guess')
    guess = int(input())            # take user input into var guess

    if guess < secretNumber:        # check if guess num is lower 
        print('your guess is too low')
    elif guess > secretNumber:      # check if guess num is higher
        print('your guess is too high')
    else:                           # break loop if guess is correct or loop end
        break

if guess == secretNumber:   # guess correct in 6 attempts
    print('good job! you guessed my number in ' + str(guessesTaken) + ' guesses')
else:                       # guess wrong after 6 attempts
    print('nope. the number i was thinking of was ' + str(secretNumber))
