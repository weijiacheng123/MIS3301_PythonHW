# This program calculates and displays the county and state sales tax on a purchase.

# Main function should ask the user for the purchase amount
# then should calculate StateTax, County Tax

def main():
    purchase = float(input('What is the purchase amount? '))
    state_tax = purchase * 0.05
    county_tax = purchase * 0.025
    Showsale(purchase, state_tax, county_tax)


# calculate total tax as state tax + county tax
# and total sale as purchase + total tax.

# this function should display the values of all of the 5 values
# purchase, state tax, county tax, total tax and total sale

def Showsale(purchase, state_tax, county_tax):
    total_tax = state_tax + county_tax
    total_sale = purchase + total_tax
    print('The purchase amount is $', purchase," the state tax is $",state_tax," the county tax is $",
          county_tax,"\n","the total tax is $",total_tax," and the total sale is $",total_sale, 
              sep='')

    
# Call the main function.
main()
