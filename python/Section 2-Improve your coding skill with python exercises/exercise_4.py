# TODO check prime number within an interval

def interval_prime_number(lower,upper):
    for num in range(lower,upper+1):
        if num >1:
            for i in range(2,num):
                if num%i==0:
                    print(num,"it is not a prime number")
                    print(i,"times",num//i,"is",num)
                    break
            else:
                print(num,'it is an prime number')
        else:
            print(num,"it is not a prime number")


lower=int(input("enter the lower number: "))
upper=int(input("enter the upper number: "))

interval_prime_number(lower,upper)