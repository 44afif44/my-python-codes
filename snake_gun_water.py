import random
def gamew(player,computer):
    if player==computer:
        return "It's a tie!"
    elif(computer=="snake"and player=="water"):
            return ("you lose! Snake drinks water")
    elif(computer=="water"and player=="snake"):
            return ("you win! Snake drinks water")
    elif(player=="gun" and computer=="water"):
          return ("you lose! Gun sinks in water")
    elif (player=="water" and  computer=="gun"):
          return ("you win! Gun sinks in water")
    elif(player=="snake" and computer=="gun"):
          return ("you lose! Gun shoots snake")
    elif(player=="gun"and computer=="snake"):
          return ("you win! Gun shoots snake")

list=["snake","water","gun"]
computer=random.choice(list)
player=input("Enter your choice (snake, water, gun): ").lower()
print("computer stupid have chosen",computer)
print(gamew(player,computer))
    
    