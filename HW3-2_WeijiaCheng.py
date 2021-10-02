# start

# write a program that gets an average score of four tests
# named score level
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# get test score from user
grade1 = float(input('What is the first test score? '))
grade2 = float(input('What is the second test score? '))
grade3 = float(input('What is the third test score? '))
grade4 = float(input('What is the forth test score? '))
average = (grade1+grade2+grade3+grade4)/4
print('the average score is:', average)

# determine the score level
if average >= A_SCORE:
    print('Your grade is A.')
elif average >= B_SCORE:
    print('Your grade is B.')
elif average >= C_SCORE:
    print('Your grade is C.')
elif average >= D_SCORE:
    print('Your grade is D.')
else:
    print('Your grade is F.')

# end
