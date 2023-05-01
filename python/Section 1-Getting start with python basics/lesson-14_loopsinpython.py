list_numbers=[2,3,4,2,4,2,5,2,8,9,1]
for items in list_numbers:
    print(items)
    
# output:
# 2
# 3
# 4
# 2
# 4
# 2
# 5
# 2
# 8
# 9
# 1

user_info={'firstname':'sri','lastname':'ram','job':'junior test engineer'}
for i in user_info:
    print(i)
    
#ouput:the above code only provide the keys in the dictionary
# firstname
# lastname
# job

# if yoy want only the keys on the dictionary the below code works

user_info={'firstname':'sri','lastname':'ram','job':'junior test engineer'}
for i in user_info.keys():
    print(i)
    
# output   
# firstname
# lastname
# job

# if yoy want only the values on the dictionary the below code works

user_info={'firstname':'sri','lastname':'ram','job':'junior test engineer'}
for i in user_info.values():
    print(i)

# output
# sri
# ram
# junior test engineer