'''
The computer secretly chooses a number, and the user has to guess it.
Hint: the number is odd or even.
Hint: Two or three digits
'''
import random
import time

print("Lets Start the number guessig game !")

time.sleep(2)

print("\nHere are the rules: \n\t1. Guess the number between 10, 1000."
    "\n\t2. You will get two hints \n\t3. I can provide the direction to guess the number \n\t4. You only have 7 chances")

time.sleep(2)

print("Press 1 to start the game\nPress 2 to End the game")

x=int(input("Whats your choice?: "))

if x==1:
    print("\nI will generate a number for you now")
    fnumber=random.randint(10,1000)
    z=int(input("\nDo you want hints? Press 9 for Yes: "))
    if z==9:
        hint1=int(fnumber%2)
        if hint1==1:
            print("\nHint 1: The number is Odd")
        else:
            print("\nHint 1: The number is Even")
        if fnumber >=100 and fnumber<1000:
            print("\nHint 2: The number is 3 digit number")
        elif fnumber<100 and fnumber>=10:
            print("\nHint 2: The number is 2 digit number")
    elif z!=9:
        print("\nYour choice, Proceed with no hints")
    for i in range(1,8):  
        my_guess=int(input("\nWhats your guess?: "))
        ratio1=my_guess/fnumber
        ratio2=fnumber/my_guess
        if ratio1>=2:
            print("Your guess is too High")
        elif ratio1>=1.2 and ratio1<2:
            print("Your guess is high but not too close")          
        elif ratio1>1 and ratio1<1.2:
            print("Your guess is too close but still on higher side")
        elif ratio1<1 and ratio1>=0.9:
            print("Your guess is too close but still on lower side")          
        elif ratio1<0.9 and ratio1>=0.6:
            print("Your guess is low but not too close")
        elif ratio1<0.6:
            print("Your guess is too low")          
        elif fnumber==my_guess:
            print("Thats the correct number")
            break
    print(f"You lose the number was {fnumber}")
elif x==2: 
    print("The game ends here")
else:
    print("Please press the correct choice")

    
