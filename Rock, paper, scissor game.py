import random
Options= ["Rock", "Paper", "Scissors"]
Player_choice = input ("Choose between Rock, Paper and Scissors")
Device_choice = random.choice (Options)
print ("Your_choice - ", Player_choice)
print ("Device's_choice - ", Device_choice)
if (Player_choice == Device_choice):
    print("Tie")
elif (Player_choice == "Paper" and Device_choice == "Rock"):
    print ("You won")
elif (Player_choice == "Rock" and Device_choice == "Scissors"):
    print ("You won")
elif (Player_choice == "Scissors" and Device_choice == "Paper"):
    print ("You won") 
else:
    print ("Device won")
    print ("Thank you for playing, visit again.")