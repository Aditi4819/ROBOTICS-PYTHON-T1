import random
randomNumber = random.randrange(1000,9999)
print("I am Thinking of a number between 1000 and 9999 and you have 10 tries to guess it")
guess= False
c=0
while guess is False and c<10:
    userChoice = int(input("Guess?"))
    if userChoice < 1000 :
        print("Wrong choice!!! Choose a 4-digit number")
        continue
    elif userChoice>9999 :
        print("Wrong choice!!! Choose a 4-digit number")
        continue
    c+=1
    if userChoice == randomNumber:
        guess = True
        print("R")
    elif userChoice == randomNumber:
        guess = True
        choice_str = str(userChoice)
        for i , val in enumerate(str(randomNumber)):
            if choice_str[i] != val:
                print("A")
    elif userChoice != randomNumber:
        print("W")
    if c == 10:
        print("You are running out of tries!!! Try again...")
