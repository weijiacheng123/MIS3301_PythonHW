# Start
# Ask initial balance, number of withdrawals, and amount of each withdrawals


print("What is your initial balance? ")
balance = float(input())
print("What is your number of withdrawals? ")
withdraw_num = int(input())
totalwithdraw = 0
i = 0

# if withdraw more than his account: "Your current balance is not sufficient. Try another amount."
# then allow him enter a new withdrawal amount

for i in range (withdraw_num):
    print("How much you want to withdraw? ")
    amount_withdraw = float(input())
    #totalwithdraw += amount_withdraw
    while amount_withdraw > balance:
        print("Your current balance is not sufficient. Try another amount which smaller than $", balance, sep=' ')
        print("How much you want to withdraw? ")
        amount_withdraw = float(input())
        
    balance -= amount_withdraw   
    i += 1
    totalwithdraw += amount_withdraw
    print("The current balance is $", balance, "total withdrawal is $", totalwithdraw , sep=' ')

# End

#totalwithdraw = 0
#for num in range (1, withdraw_num+1):
    #print("How much you want to withdraw? ")
    #amount = float(input())
    #balance -= amount
    #totalwithdraw += amount
#print("The current balance is $", balance, "total withdrawal is $", totalwithdraw , "and initial balance was $300", sep=' ')
