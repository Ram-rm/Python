# TODO check if a number is prime

# what is prime number?

# a prime number is a positive integer which is
# greater than 1

# prime number has no positive integer other than 1
# and by it self

# 2 is a prime number which means 
# two can divisable by itself not by other positive 
# intergers other than 1

def prime_number(number):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                print(number,"it is not a prime number")
                print(i,"times",number//i,"is",number) #//= is gives the quotient
                #output
                # Enter the number: 4
                # 4 it is not a prime number
                # 2 times 2 is 4
                break
        else:
            print(number,"it is a prime number")
            #output
            # Enter the number: 2
            # 2 it is a prime number
    else:
        print(number,"it is not a prime number")  
        #output
        # Enter the number: 1
        # 1 it is not a prime number 
        
number=int(input("Enter the number: "))
prime_number(number)





# def pm(n):
#     n=int(n)
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("it is not a prime number")
#         else:
#             print("it is a prime number")
#     else:
#         print("it is not a prime number")

# n=input("num")
# pm(n)