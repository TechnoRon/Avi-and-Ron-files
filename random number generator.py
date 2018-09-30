import random
computer = random.randint(1,10)
numberchosen = random.randint(1,10)
print("Welcome to the number game!")
print("The game is simple - both you and the computer choose a number, and whoever is closer to the designated number wins!")
person = int(input("Choose a random number from 1 to 10 inclusively. "))
if abs(numberchosen - person)< abs(numberchosen - computer):
    print("You win")
elif abs(numberchosen - person)> abs(numberchosen - computer):
    print("You lose")
numberchoseninfo = "The number was " + str(numberchosen)
computernumberinfo = "The computer chose " + str(computer)
print(numberchoseninfo)
print(computernumberinfo)
