# TODO challenge number 1, add two number

# ask the user to enter first number:
# save it in a variable called num1
# ask the user to enter second number:
# save it in a variable called num2
# create a variable called sum
# assign the sum of num1 and num2 in sum variable
# print the sum

num1=input("Enter first number:")
num2=input("Enter second number:")
sum=int(num1)+int(num2)
print(sum)

# Why i user int("__") i am typecasting the string to integer


# What will be the output if i didn't typecast
# Enter first number:2
# Enter second number:1
# 3

# output:
# Enter first number:2
# Enter second number:1
# 21


#type() = Build in function is used to show type of the variable ie. string or integer or float

print(type(num1))
print(type(num2))
print(type(sum))

# output:

# <class 'str'>
# <class 'str'>
# <class 'int'>
