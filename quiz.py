print("Wellcome to Guessing Game")

playing = input("Enter yes to play ").lower() #  used lower() function to convert strint to lower case

if (playing != 'yes'):
    quit() #used builtin python function to quit if the user enter anything other than 'yes'

score = 0
print("Let's Play")

answer = input("What does Cpu stands for ? ").lower().strip() #  used strip() function to cancel white spaces

if (answer=='central processing unit'):
    print("Congrats! you guessed right")
    score+=1 #  incremented score by every right answer 
else:
    print("You guessed wrong")

answer = input("Who is father of computer? ").lower().strip()

if (answer=='charles babbage'):
    print("Congrats! you guessed right")
    score+=1

else:
    print("you guess wrong")

answer = input("Ram stands for?").lower().strip()

if(answer=='random access memory'):
    print("Congrats! you guessed right")
    score+=1
else:
    print("you guessed wrong")

answer = input("what is brain of computer ? ").lower().strip()

if(answer=='cpu' or 'central processing unit'):
    print("Congrats you guessed right")
    score+=1
else:
    print("you guessed right")

if(score==4):
    print("Bravo yiu scored 4 out of 4")
elif(score==3):
    print("you scored 3")
elif(score==2):
    print("you score 2")
elif(score==1):
    print("you scored 1")
else:
    print("loser")
