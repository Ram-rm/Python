input1=894
print(input1)

#output=894

# below is an error code

# input2="hello"
# int_num=int(input2)
# result=input1+int_num
# print(result)

#output

#  result=input1+input2
#            ~~~~~~^~~~~~~
# TypeError: unsupported operand type(s) for +: 
# 'int' and 'str'

# because we can't able to concat the integer and string value

# otuput

# input2=int("hello")
#            ^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'hello'


# The error in the above code is when we try to convert the 
# [input2=int("hello")] python consider the input2 value as a string
# your can't add or concate a string and int value in python
# in the below code i have changed the [input2] value as "22"

input2="22"
int_num=int(input2)
result=input1+int_num
print(result)

#output=916

# if you need to concate the integer and string value 
# change the typecate intger to string then add the value