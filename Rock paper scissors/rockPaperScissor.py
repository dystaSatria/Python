from random import randint


print ("Rock paper scissors game")
print ("R for Rock \nS for Scissor\nP for Paper")
bot = ["B","G", "K"]

computer = bot[(randint(0,2))]
player = False

while player == False:
    player = (input("masukkan pilihan anda :\n"))
    if player == computer:
        print ("Tie.Draw")

    elif player == "B":
        if computer == "G":
            print ("You are Win")
        else:
            print ("You are lose")

    elif player == "K":
        if computer == "B":
            print ("You are Win")
        else:
            print ("You are Lose")

    elif player == "G":
        if computer == "K":
            print ("You are win")
        else:
            print ("You are lose")

    else:
        print ("Your input is wrong. Remember just input B or G Or K")


    player = False
    computer =bot[randint(0,2)]






