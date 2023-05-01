# TODO check if the number is odd or even

def even_or_odd(number):
    if number%2==0:#% this symbole will check the remider is equal to zero
        print("{} is even".format(number))
        #output
        #Enter the number:2
        #2 is even
    else:
        print("{} is odd".format(number))
        #output
        #Enter the number:3
        #3 is odd


number=int(input("Enter the number:"))
even_or_odd(number)

