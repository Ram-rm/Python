# TODO create multiplication for a number

def multiplication(number):
    for i in range(1,11):
        print('{} * {} = {}'.format(number,i,number*i))
    
number=int(input("enter the number: "))
multiplication(number)

# output:
# enter the number: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50