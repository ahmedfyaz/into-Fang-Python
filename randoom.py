import random #imported random for the random number 

start = input("Enter 'y' to start ").lower()
if(start!='y'):
    quit()#used builtin python function to quit if the user enter anything other than 'y'
    
print("Game started")


randnum = random.randint(1,10) #set the range of the number from 1 to 10

while(True): #started an infinte loop
    guess = int(input("you have to Guess number between 1 to 10 "))

    if(guess==randnum):
        print("congrats you guessed right")
        break #if the person guessed right the loop will end
    elif(guess>randnum):
        print("number is low try again")
    else:
        print("number is high try again")
