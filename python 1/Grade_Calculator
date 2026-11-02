print("This is the grade calculator, its made to get your grades back quicker. Just enter the points you got and the max points and it comes out to you!")
print("")
#just a nice message at the start

try:
    quizpoints=input("Enter your points for the test / quiz:  ")
    quizmaxpoints=input("Enter max points for the test / quiz:  ")
    #get the named variables in
    decgrade = int(quizpoints) / int(quizmaxpoints)
#devide them to make it close to a grade
    grade = ( (decgrade) * 100)
    print("Your grade is "+ str(grade) + "%.")
#make it a real name
    if grade > 70: 
        print("Good One!")
    elif grade < 70: 
        print("Failed that one.")
    elif grade < 6: 
        print("HOW\nJUST HOW")
    elif grade < 1: 
        print("Are doing this on PURPOSE")
except ValueError: 
    print("Thats not a number. Try and reset")
    #Funny Messages