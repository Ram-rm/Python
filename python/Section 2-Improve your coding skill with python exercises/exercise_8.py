# TODO generting fibonacci sequence

nterm=int(input("How many term: "))
n1,n2=0,1
count=0 

if nterm<=0:
    print("please enter a positive number: ")
elif nterm ==1:
    print("Fibonacci sequence upto",nterm,':')
    print(n1)
    #output
    # How many term: 1
    # Fibonacci sequence upto 1 :
    # 0
else:
    print("fibonacci sequence:")
    while count<nterm:
        print(n1)
        nth=n1 + n2
        n1=n2
        n2=nth
        count+=1
    #output
    # 0
    # 1
    # 1
    # 2
    # 3
    
