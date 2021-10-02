
#asks the user to enter the total square feet in a tract of land
totalsquare=float(input("what is the total square feet in a tract of land? "))
#calculates the number of acres in the tract
#divide the amount entered by 43,560 to get the number of acres
acresnumber=totalsquare/43560
print(totalsquare,'acre of land is equivalent to', acresnumber,'square feet.')
