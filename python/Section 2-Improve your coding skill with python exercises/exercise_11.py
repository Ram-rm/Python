# TODO make a simple guess number program

import random

random_num=random.randint(0,10)

while True:
    user_num=int(input("Enter the number: "))

    if user_num==random_num:
        print("congratulations your guess the correct number")
        break
    else:
        print("Sorry, pls guess the number again!")
    
#output:
# Enter the number: 1
# Sorry, pls guess the number again!
# Enter the number: 2
# Sorry, pls guess the number again!
# Enter the number: 3
# congratulations your guess the correct number
# PS C:\Users\sriram\Desktop\pythonautomation>