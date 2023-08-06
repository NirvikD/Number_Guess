'''Write a program that generates a random number and asks the user
 to guess what the number is. If the user's guess is higher than the random number,
 the program should display "Too high, try again.
 " If the user's guess is lower than the random number, the program should display "Too low, try again."
  The program should use a loop that repeats until the user correctly guesses the random number.
  Program should count and display number of tries to win the game. '''
import random
import art
c = random.randint(1,100)
def guess(lives,c):

    print(f"You have {lives} lives")
    while lives!=0:
        guess = int(input("Guess the number: "))
        lives-=1
        if guess==c:
            print(f"you guessed it right. The number was {c}")
            break
        elif (c-5)<guess<(c+5):
            print("You are very close")
            print(f"You have {lives} lives left.")
        elif (c-10)<guess<(c+10):
            print("You are close")
            print(f"You have {lives} lives left.")
        elif (c-20)<guess<(c+20):
            print("Your guess is little bit far")
            print(f"You have {lives} left")
        elif c-20<guess:
            print("Too high")
            print(f"You have {lives} left")
        elif c>guess+20:
            print("too low")
            print(f"You have {lives} left")
    if lives==0:
        print("Sorry You loose ")
        print(f"The number was {c}")
print(art.logo)
print("I have selected a number between 1 and 100. "
      "Can you guess what is it ?")
while True:
    print("Enter the level you want to choose\n"
          "1.Easy\n"
          "2.Medium\n"
          "3.Hard\n")
    ch = int(input("Enter your choice: "))
    if ch== 1:
        lives = 10

        guess(lives,c)
    elif ch==2:
        lives= 7
        guess(lives,c)
    elif ch==3:
        lives = 5
        guess(lives,c)
    else:
        print("Enter correct input")
    print("Do you want to continue?\n"
      "1.Yes\n"
      "2.No\n")
    d = int(input("Enter your choice: "))
    if d==2:
        break

























