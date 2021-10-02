# The following is used as a global constant the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    A = show_pay_contrib(gross_pay)
    B = show_bonus_contrib(bonus)
    show_total_contrib(A,B)
    
    
# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.
def show_pay_contrib(gross):
    contrib_pay = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $', 
          format(contrib_pay, ',.2f'), 
          sep='')
    return contrib_pay
    
# The show_bonus_contrib function accepts the
# bonus amount as an argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
    contrib_bonus = bonus * CONTRIBUTION_RATE
    print('Contribution for bonuses: $', 
          format(contrib_bonus, ',.2f'), 
          sep='')
    return contrib_bonus

# The total_contribution function calculate
# the company’s total contribution for each employee. 
def show_total_contrib(A,B):
    contrib_total = A + B
    print('Total contribution: $',
          format(contrib_total, ',.2f'),
          sep='')

# Call the main function.
main()
