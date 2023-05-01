# TODO create your simple calculator

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

print('select the operation:')
print('1: addition')
print('2: subraction')
print('3: multiplication')
print('4: division')
 
while True:
    choice=input("enter choice(1/2/3/4)")
    if choice in ('1','2','3','4'):
            num1=float(input("enter the first number: "))
            num2=float(input("enter the second number: "))
            if choice =='1':
                print(num1,"+",num2,"=",addition(num1,num2))
            elif choice =='2':
                print(num1,"-",num2,"=",subtraction(num1,num2))
            elif choice =='3':
                print(num1,"*",num2,"=",multiplication(num1,num2))
            elif choice =='4':
                print(num1,"/",num2,"=",division(num1,num2))
        

        
