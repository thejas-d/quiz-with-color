import colorama
from colorama import Fore

print(Fore.YELLOW+"\n Wellcome to Offline Quiz!")
playing = input(Fore.WHITE+"\n Do you want to play?"+Fore.YELLOW)
if playing.lower() != "yes":
    quit()

print("\n Okay! Let's play :)")   
score = 0 

answer = input(Fore.GREEN +"\n  1. What does CPU stands for ?\nAns:" +Fore.WHITE)
if answer.lower() == "central processing unit":
    print('Correct'+ '\U0001f600')
    score += 1
else:
    print("Incorrect!"+ '\U0001f641')

answer = input(Fore.GREEN +"\n 2. What does RAM stands for ?\nAns:"+Fore.WHITE)
if answer.lower() == "random access memory":
    print('Correct'+ '\U0001f600')
    score += 1
else:
    print("Incorrect!"+ '\U0001f641')    

answer = input(Fore.GREEN +"\n 3. What does PSU stands for ?\nAns:"+Fore.WHITE)
if answer.lower() == "power supply":
    print('Correct'+ '\U0001f600')
    score += 1
else:
    print("Incorrect!"+ '\U0001f641')   

answer = input(Fore.GREEN +"\n 4. What does GPU stands for ?\nAns:"+Fore.WHITE)
if answer.lower() == "graphics processing unit":
    print('Correct'+ '\U0001f600')
    score += 1
else:
    print("Incorrect!"+ '\U0001f641')   

print(Fore.RED +"\n (You got "+ str(score) +" Questions Right)")
print(Fore.WHITE +" You got "+ str((score/4)*100) +"% winning ratio.")
