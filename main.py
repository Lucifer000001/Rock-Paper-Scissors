import random
def gamewin(comp_turn,player):
    if comp_turn == player:
        return None
    elif comp_turn=='r':
            if player=='s':
                return False
            elif player=='p':
                return True
    elif comp_turn=='p':
            if player=='r':
                return False
            elif player=='s':
                return True
    elif comp_turn=='s':
            if player=='p':
                return False
            elif player=='r':
                return True


print("Computer's Turn: Rock(r) Paper(p) Scissor(s)")
rand_1=random.randint(1,3)
if rand_1==1:
    comp_turn='r'
if rand_1==2:
    comp_turn='p'
if rand_1==3:
    comp_turn='s'

player=input("Your Turn: Rock(r) Paper(p) Scissor(s)")

stat=gamewin(comp_turn,player)
print(f"Comp's Input is {comp_turn}")
print(f"Your Input is {player}")
if stat == None:
    print("The game is a tie")
elif stat:
    print("You won")
else:
    print("You Loose")

