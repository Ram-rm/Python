# program that act like a login system

attempt=0
attempts=2

def login(username,password):
    user=input("Enter the username : ").lower() # it is the build in function that change the upper case value to lower case
    passs=input("Enter the password : ")
    if user == username and passs == password:
        return True
    return False
while True:
    if  login("sriram","sri123"):
        print('login successfully')
        break
    attempt+=1
    if attempt>=attempts:
        print('login failed')
        break
    print("either the username or password or incorrect please try again later")
        
    