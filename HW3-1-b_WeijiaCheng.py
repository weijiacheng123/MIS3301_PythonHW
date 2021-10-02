
# Start
# check for the health condition and the salary
health_condition = input("Are you health? ")
salary = float(input("What is your salary? "))

# meeting both criteria, ask willing to pay the premium of $500 to buy the insurance or not
if health_condition == "Yes" or health_condition == "yes":
    if salary >= 60000:
        print("You are meeting the criteria, congratulation!")
        willing_to_pay = input("Do you willing to pay the premium of $500 to buy the insurance? ")

# answer is yes, then display “congratulation for the wise choice”
        if willing_to_pay == "Yes" or willing_to_pay == "yes":
            print("congratulation for the wise choice!")

# answer is no, ask the person for the maximum amount he or she is willing to pay
        else:
            max_amount = input("what is the maximum amount you willing to pay? ")
            print("Thank you for your participation！")

    else:
        print("Sorry, you meet the standard health condition, but not meeting the standard salary.")    

# if not meeting any of these criteria, ask the person for the maximum amount he or she is willing to pay
else:
    if salary >= 60000:
        print("Sorry, you meet the standard salary, but not meet the standard health condition.")     
    else:
        print("Sorry, you are not meeting the standard health condition and standard salary.")
        

# End
