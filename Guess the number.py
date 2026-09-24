Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import random as r
def GuessNo():
    count=0
    print("WELCOME TO GUESS THE NUMBER")
    p=input("DO YOU WANT TO PLAY:YES / NO")
    if p.lower()=="yes":
        print("LET'S PLAY")
        num=r.randint(1,100)
        print("GUESS MY NUMBER BETWEEN 1 TO 100")
        print()
        while True:
            count=count+1
            guess=int(input("Enter Your Guess"))
            print()
            if guess > num:
                print("HIGH")
                print("Try something Lower")
                print()
            elif guess < num:
                print("LOW")
                print("Try something Higher")
                print()
            elif guess == num:
...                 print("CONGRATULATIONS! YOU GUESSED THE CORRECT NUMBER!")
...                 print("You have Guessed The number in",count,"Tries")
...                 print()
...                 GuessNo()
...                 break
...     elif p.lower()=="no":
...         print("BYE BYE COME PLAY LATER!")
...     else:
...         print("Invalid Choice")
...         print(" Please enter YES or NO")
...         GuessNo()
