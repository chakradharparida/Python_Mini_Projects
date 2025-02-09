'''
1 for snake 
-1 for water
0 for gun
'''

import random
computer = random.choice([-1,1,0])
YouChoose = input("Choose 's' for Snake, 'w' for Water, 'g' for Gun :")
YouDict = {"s":1,"w":-1,"g":0}
ReverseDict = {1:"Snake",-1:"Water",0:"Gun"}

You = YouDict[YouChoose]
print(f"You Choose: {ReverseDict[You]}")
print(f"Computer Choose: {ReverseDict[computer]}")
if (computer == You):
    print("It's Draw !")
else:
    '''if((computer-You)==-1 or (computer-You)==2):
        print("You Win")
    else:
        print("You Lose")'''
    if(computer == -1 and You == 1):
        print("You Win !")
    elif(computer == 0 and You == -1):
        print("You Lose !")
    elif(computer == 1 and You == 0):
        print("You Win !")
    elif(computer == 1 and You == -1):
        print("You Lose !")
    elif(computer == 0 and You == -1):
        print("You Win !")
    elif(computer == 0 and You == 1):
        print("You Lose !")
    else:
        print("Something What's Wrong !")