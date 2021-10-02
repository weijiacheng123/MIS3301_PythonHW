
# Start
# check for the health condition and the salary
health_condition = input("Are you health? ")
salary = float(input("What is your salary? "))

# meeting both criteria, congratulated the person
if health_condition == "Yes" or health_condition == "yes":
    if salary >= 60000:
        print("You are meeting the criteria, congratulation!")
    else:
        print("Sorry, you meet the standard health condition, but not meeting the standard salary.")    

# if not meeting any of these criteria, displayed the reason
else:
    if salary >= 60000:
        print("Sorry, you meet the standard salary, but not meet the standard health condition.")
    else:
        print("Sorry, you are not meeting the standard health condition and standard salary.")

# End
