game = "yes"
while (game=="yes" or game=="YES"):

    print("\t\t\t Transformer age of cybertron")
    print("\n")
    print("\t the teams are ")
    print("\t 1 ==> Autobots ")
    print("\t 2 ==> Decepticons ")
    team = int(input("select your team"))

    if (team == 1):
        print("you choose Autobots")

    else:
        print("you choose Decepticons")

    print("3==> Optimus Prime The leader of autobots ")
    print("4==> Megatron The leader of decepticons")
    print("5==> Bumblebee The warrior in the team of autobots")
    print("6==> Lockdown The decepticon but now he is a bounty hunter")
    tran=int(input("select your transformer for fight"))
    tran2=int(input("select your Opponent transformer for fight"))
    if (tran==3):
        print("you chosen Optimus Prime")
    elif (tran==4):
        print("you chosen Megatron")
    elif (tran==5):
        print("you chosen Bumblebee")
    elif (tran==6):
        print("you chosen Lockdown")
    else:
        print("you didn't choose any")

    if (tran==3 and tran2==4):
        print("Optimus Prime Vs Megatron")
        print("\t\t\t\t OPTIMUS PRIME WINS ")
    elif (tran==4 and tran2==5):
        print("Megatron Vs Bumblebee")
        print("\t\t\t\t BUMBLEBEE WINS ")
    elif (tran==3 and tran2==6):
        print("Optimus Prime Vs Lockdown")
        print("\t\t\t\t OPTIMUS PRIME WINS BY SLICING UP LOCKDOWN BODY INTO TWO HALVES")
    elif (tran==4 and tran2==6):
        print("Megatron Vs Lockdown")
        print("\t\t\t\t MEGATRON WIN")
    elif (tran==6 and tran2==5 ):
        print("Lockdown Vs Bumblebee")
        print("\t\t\t\t BUMBLEBEE WINS")
    elif (tran==3 and tran2==5):
        print("Optimus Prime Vs Bumblebee")
        print("\t\t\t\t OPTIMUS PRIME WINS")
    elif (tran==4 and tran2==3):
        print("Megatron Vs Optimus Prime")
        print("\t\t\t\t OPTIMUS PRIME WINS")
    elif (tran==6 and tran2==3):
        print("Lockdown Vs Optimus Prime")
        print("\t\t\t\t OPTIMUS PRIME WINS")
    elif (tran==5 and tran2==3):
        print("Bumblebee Vs Optimus Prime")
        print("\t\t\t\t OPTIMUS PRIME WINS")
    else:
        print("\t\t\t\t LOCKDOWN WINS")
    game=input("do you want to exit from this game if yes then press no if you want to continue press yes")





