pl1 = input("Please enter rock, paper or scissors: ")
pl2 = input("Please enter rock, paper or scissors: ")

if pl1 == "rock" and pl2 == "scissors" or pl1 == "scissors" and pl2 == "paper" or pl1 == "paper" and pl2 == "rock" :
    print("Player 1 wins")
elif pl2 == "rock" and pl1 == "scissors" or pl2 == "scissors" and pl1 == "paper" or pl2 == "paper" and pl1 == "rock" :
    print("Player 2 wins")
else:
    print("incorect input")