# TODO challenge number 5, largest among three number

firstnumber=float(input("Enter the first number:"))
secondnumber=float(input("Enter the second number:"))
thirdnumber=float(input("Enter the third numver:"))

if firstnumber > secondnumber and thirdnumber:
    print("first number {} is greater than second  {} and third numbers {}" .format(firstnumber,secondnumber,thirdnumber))
#output:
# Enter the first number:2
# Enter the second number:1
# Enter the third numver:1 
# first number 2 is greater than second  1 and third numbers 1

elif secondnumber > firstnumber and thirdnumber:
    print("second number {} is greater than first  {} and third numbers {}" .format(secondnumber,firstnumber,thirdnumber))
#output:
# Enter the first number:2
# Enter the second number:3
# Enter the third numver:2
# second number 3 is greater than first 2 and third numbers 2

elif thirdnumber > firstnumber and secondnumber:
    print("third number {} is greater than first {} and second numbers {}" .format(thirdnumber,firstnumber,secondnumber))
#output
# Enter the first number:1
# Enter the second number:1
# Enter the third numver:2
# third number 2 is greater than first 1 and second numbers 1

elif firstnumber==secondnumber==thirdnumber:
    print("The give number are equal")
# output:
# Enter the first number:1
# Enter the second number:1
# Enter the third numver:1
# The give number are equal

       