import random
def board(l):
    turn = 2
    for i in range(100):
        l.insert(i, i + 1)
    for j in range(99,-1,-10):
        if(turn % 2 == 0):
            print(l[j], "|", l[j-1], "|", l[j-2], "|", l[j-3], "|", l[j-4], "|", l[j-5], "|", l[j-6], "|", l[j-7], "|", l[j-8], "|", l[j-9])
            turn-=1
            print("------------------------------------------------")   
        else:  
            print(l[j-9], "|", l[j-8], "|", l[j-7], "|", l[j-6], "|", l[j-5], "|", l[j-4], "|", l[j-3], "|", l[j-2], "|", l[j-1], "|", l[j])
            print("------------------------------------------------")
            turn+=1

def snakesAndLadders():
    print("SNAKES")
    print("33-5\n54-34\n63-16\n93-74\n97-61\n")
    print("LADDERS")
    print("2-38\n8-31\n21-42\n46-84\n51-67\n71-91\n80-99")

def fall(x):
    if(x == 33):
        x = 5
    if(x == 54):
        x = 34
    if(x == 63):
        x = 16
    if(x == 93):
        x = 74
    if(x == 97):
        x = 61
    return x
        
def climb(x):
    if(x == 2):
        x = 38
    if(x == 8):
        x = 31
    if(x == 21):
        x = 42
    if(x == 46):
        x = 84
    if(x == 51):
        x = 67
    if(x == 71):
        x = 91
    if(x == 80):
        x = 99
    return x

def acceptUser(chance_1, chance_2):
    player1 = input("Enter the player 1's name: ")
    player2 = input("Enter the player 2's name: ")
    who = int(input("Tell me! Who'll play first(1 or 2)? "))
    dice = [1,2,3,4,5,6]
    while(chance_1 <= 100 and chance_2 <= 100):
        if(who == 1):
            roll_1 = int(input("{0} Roll 1 using dice: ".format(player1)))
            if(roll_1==1):
                x = random.choice(dice)
                chance_1 += x
                print(chance_1, "Before climbing")
                chance_1 = climb(chance_1)
                print("{0} is at position {1}".format(player1,chance_1))
                chance_1 = fall(chance_1)
                print("After fall\n{0} is at position {1}".format(player1,chance_1))
                who += 1
                print("\n")
            else:
                print("roll the dice for 1! Then only you can PROCEED!")
                who += 1
                print("\n")
        else:
            roll_2 = int(input("{0} Roll 1 using dice: ".format(player2)))
            if(roll_2 == 1):
                y = random.choice(dice)
                chance_2 += y
                print(y, "Before climbing")
                chance_2 = climb(chance_2)
                print("{0} is at position {1}".format(player2,chance_2))
                chance_2 = fall(chance_2)
                print("After fall\n{0} is at position {1}".format(player2,chance_2))
                who -= 1
                print("\n")
            else:
                print("roll the dice for 1! Then only you can PROCEED!")
                who -= 1
                print("\n")
    else:
        if(chance_1 > chance_2):
            print("Congratulations!!! {0} is the WINNER".format(player1))
        else:
            print("Congratulations!!! {0} is the WINNER".format(player2))
            
l = []
board(l)
snakesAndLadders()
acceptUser(1, 1)
