import random 

print("Welcome to rock paper siccors")

choice = input("press y or 'Y' to begin ").lower()

if (choice!='y'):
    quit() #quit if user haven't entered the correct choice

print("Game Started")

print("Use r for Rock ")
print("Use p for Paper")
print("Use s for siccors")
while True:
    randum = random.randint(1,3)
    if randum ==1 :
        randum = 'r'
    elif randum ==2 :
        randum = 'p'
    else: # If not 1 or 2, it must be 3
        randum = 's'
    
    guess = input("rock paper siccors ")

    if(guess==randum):
        print(f'Tied')
        print(f'you entered {guess}')
        print(f'computer enteres {randum}')        
        inp = input("enter y to start agin ").lower()
        if(inp!='y'):
            quit()

    elif(guess=='r'and randum == 'p'): # Rock loses to Paper
        print(f'you entered {guess}')
        print(f'computer enteres {randum}')
        print("computer won")
        inp = input("enter y to start agin ").lower()
        if(inp!='y'):
            quit()

    elif(guess=='r'and randum == 's'): # Rock beats Scissors
        print("you won")
        print(f'you entered {guess}')
        print(f'computer enteres {randum}')
        inp = input("enter y to start agin ").lower()
        if(inp!='y'):
            quit()

    else: # This covers Paper beating Rock and Scissors beating Paper
        print("you won")
        print(f'you entered {guess}')
        print(f'computer enteres {randum}')
        inp = input("enter y to start agin ").lower()
        if(inp!='y'):
            quit()
