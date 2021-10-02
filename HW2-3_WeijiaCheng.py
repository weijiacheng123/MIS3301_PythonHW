#ask total amount of sales
totalsales=float(input("what is the total amount of sales? "))
#calculate the sales tax paid and total amount of payment
salestax=0.07*totalsales
totalpayment=totalsales+salestax
#display the total of the sale, the amount of sales tax, and the total payment
print("total of the sales is ",totalsales)
print("the amount of sales tax is ",salestax)
print("the total payment is ",totalpayment)
