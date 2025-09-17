import random
def game():
    print("the game has started")
    score=random.randint(1,62)
    with open("file.txt","r") as f:
        highscore=f.read()
        if highscore!="":
            highscore=int(highscore)
        else:
            highscore=0
    print("your score is ",score)
    if score>highscore:
        with open("file.txt","w") as f:
            f.write(str(score)) 
    return score,highscore
    #  doitai return hoyai high score beat hoolei only updare hobe  
game()         
