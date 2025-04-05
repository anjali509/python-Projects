import random
def game():
    p1=input("choose Rock, Paper or Scissor : ")
    p2=random.choice(['paper','rock','scissor'])
    print(f"Player 2 choose '{p2}' ")
    if p1=='rock' and p2=='scissor':
        print("player 1 wins")
    elif p1=='paper' and p2=='rock':
        print("Player 1 wins")
    elif p1=="scissor" and p2=="paper":
        print("Player 1 wins")
    elif p1==p2:
        print("Tie...")
    else:
        print("Player 2 wins")

game()