# TODO create a quiz app
score=0
print("welcome to my python quiz app!")
playing=input("do you want to play my quiz ? yes/no: ")


if playing.lower() == "no":
    print("Thanks for your response")

#output
# welcome to my python quiz app!
# do you want to play my quiz ? yes/no: no
# Thanks for your response

elif playing.lower() == "yes":
    print("let's play!")

    answer_one=input("What is HTML stand for? ")
    if answer_one== "hyper test markup language":
        print("correct!")
        score+=1   
    else:
        print("incorrect!")
        
    answer_two=input("What is 4+4? ")
    if answer_two == "8":
        print("correct!")
        score+=1
    else:
        print("incorrect!")
        
    answer_three=input("What is 4-4? ")
    if answer_three == "0":
        print("correct!")
        score+=1
    else:
        print("incorrect!")

    print("you got {} questions correct!".format(score))
    print("you got {}".format((score/3)*100))


#output
# welcome to my python quiz app!
# do you want to play my quiz ? yes/no: yes
# let's play!
# What is HTML stand for? hyper text markup laungage
# incorrect!
# What is 4+4? 8
# correct!
# What is 4-4? 0
# correct!
# you got 2 questions correct!
# you got 66.66666666666666
