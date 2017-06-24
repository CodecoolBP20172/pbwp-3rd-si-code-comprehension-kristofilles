"""Its a bot what randomly choose a number between 1 and 20, and the user need to guess within 6 round what
number was choosen by the bot."""

import random #import the random module

guessesTaken = 0 #assign 0 to guessesTaken variable

print('Hello! What is your name?') #print out this sentence
myName = input() #assign a user input to myName variable

number = random.randint(1, 20) #assign a randomly choosen integer(between 1 and 20) to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #printing out this sentence with the given name

while guessesTaken < 6: #loop while the guessesTaken variable is less then  6
    print('Take a guess.') #print out this sentence
    guess = input() #assign a user input to guess variable
    guess = int(guess) #making type conversion changing the value of the guess variable to integer from string

    guessesTaken += 1 #increasing the  value of the guessesTaken by 1

    if guess < number: #doing something if guess value is lower than number value
        print('Your guess is too low.') #if its true print out this sentence

    if guess > number: #doing something if the guess value is higher than the number value
        print('Your guess is too high.') #if its true print out this sentence

    if guess == number: #doing something if the guess value is equal with the number value
        break #if its true the loop is immediately stop

if guess == number: #doing something if the guess value is equal with  the number value
    guessesTaken = str(guessesTaken) #making type conversion changing the value of the guessesTaken variable to string from integer
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') #print out how many try needed to the user to guess out

if guess != number: #doing something if guess value is not equal with number value
    number = str(number) #making type conversion changing the value of the number variable to string from integer
    print('Nope. The number I was thinking of was ' + number) #print out the randomly choosen number
