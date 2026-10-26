print("This is the grade calculator, its made to get your grades back quicker. Just enter the points you got and the max points and it comes out to you!")
print("")

try:
    quizpoints=input("Enter your points for the test / quiz:  ")
    quizmaxpoints=input("Enter max points for the test / quiz:  ")
    decgrade = int(quizpoints) / int(quizmaxpoints)

    grade = ( (decgrade) * 100)
    print("Your grade is "+ str(grade) + "%.")

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
while true:
    try: 
        if grade >= 0:
            break 
        print("Dumbass Try again")