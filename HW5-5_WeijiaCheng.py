# main function should display the instruction of the quiz
# and call other functions
import random
def main():
    value1, value2 = random_values()
    display_problem(value1,value2)
    display_answer(value1,value2)

# Define a function and name it random_values as your second function
# generates two random numbers
# and displays the values to the user
# then return the values to be used in other functions
def random_values():
    value1 = random.randint(0,999)
    value2 = random.randint(0,999)
    print('you get two numbers', value1,"and",value2)
    return value1, value2

# Define a function and name it display_problem as your third function
# gets the two random numbers from random_values 
# insert the values in the formula just to show it to the user
# Display the formula to the user
def display_problem(a,b):
    print("what is the answer to ("+str(a)+"*"+str(b)+") - min ("+str(a)+","+str(b)+")")


# Define a function and name it display_answer as your fourth function
# gets the two random numbers from random_values and 
# Calculates the correct answer
# asks the user to calculate the result of the displayed formula
def display_answer(a,b):
    x = a*b - min(a,b)
    ask = int(input("What is the answer:"))

    if x == ask:
        print("your answer is correct!")
    else:
        print("your answer is not correct!")
        print("the correct answer is",x)

main()


