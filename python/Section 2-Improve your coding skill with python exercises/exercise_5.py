# TODO find the factorial of a number

def factorial_number(factnum):
    factorial=1
    if factnum<0:
        print("negative number")
        #output
        # enter the number: -1
        # negative number
    elif factnum==0:
        print("factorial of zero is always 1")
        #output
        # enter the number: 0
        # factorial of zero is always 1
    else:
        for i in range(1,factnum+1):
            factorial=factorial*i
        print("The factorial of {} is {}".format(factnum,factorial))
        #output
        # enter the number: 5
        # The factorial of 5 is 120

factnum=int(input("enter the number: "))
factorial_number(factnum)
