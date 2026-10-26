#define function
def welcome():
    print("Welcome to the Community Shout-Out Wall")
    print("71 people. One wall. Every voice matters")
#step 2 call it
welcome()
#writing the functions name with () RUNS the code inside

#call it again. Same recipe. Runs again
welcome()
welcome()


def shout_out (name, message):
    post="SHOUT-OUT: " + name + "-" + message
    return post

#CALL the function with diffrent arguments
first_post = shout_out ("Amara" + " ")