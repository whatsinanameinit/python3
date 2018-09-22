from random import choice
#random choice from rock paper scissor
random_choice= choice(['rock','paper','scissor'])
print(random_choice + "\n")
#take user input
player1=input("Choose among the following \n rock \n paper \n scissor \n")
print(player1)
player2=input("\nChoose among the following \n rock \n paper \n scissor\n")
print(player2)

#if else blocks for who won
if player1 and player2:
    if player1 == player2:
        print("Its a tie")
    elif player1 == "rock" and player2 == "paper":
        print("Player2 won the game")
    elif player1 == "rock" and player2 == "scissor":
        print("Player1 won the game")
    elif player1 == "paper" and player2 == "rock":
        print("Player1 won the game")
    elif player1 == "paper" and player2 == "scissor":
        print("Player2 won the game")
    elif player1 == "scissor" and player2 == "rock":
        print("Player2 won the game")
    elif player1 == "scissor" and player2 == "paper":
        print("Player1 won the game")
else:
    print("enter choice please")
