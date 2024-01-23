import random
import math

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

min_count = math.log(upper_range-lower_range+1,2)
chances = round(min_count)

x = random.randint(lower_range, upper_range)

print("You have only %d chances to guess the number"%chances)

count = 0
while(count<chances):
    number = int(input("Guess the number:"))
    count+=1
    if(number == x):
        print("Congratulations! You have guessed the number with %d guesses"%count)
        break
    elif(number > x):
        print("No! You guessed too high!")
    else:
        print("No! You guessed too low!")
    
    
if count>=chances:
    print("Oops! You have crossed the limit\nThe number is %d\nBetter Luck Next time!"%x)
