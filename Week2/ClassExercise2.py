# Sean Hornsby-Caban
# 2/13/2023
# Week2 Class Exercises - Conditionals

# Challenge Exercise #1: 

# Ask for user to enter three tests scores, average the scores, and then tell the user the average and the letter grade.
# test1 = float(input('Enter test score 1\n'))
# test2 = float(input('Enter test score 2\n'))
# test3 = float(input('Enter test score 3\n'))
# average_score = (test1 + test2 + test3)/3

# if average_score > 100:
#     print('the average cannot be over 100, try again.')
# else:
#     print('the average score is', round(average_score))
#     if average_score >= 90:
#         print('letter grade A', round(average_score))
#     elif average_score >= 80 and average_score < 90:
#         print('letter grade B', round(average_score))
#     elif average_score >= 70 and average_score < 80:
#         print('letter grade C', round(average_score))
#     elif average_score >= 60 and average_score < 70:
#         print('letter grade D', round(average_score))
#     else:
#         print('letter grade F', round(average_score))

# Challenge Exercise #2

# temperature = float(input('What is the temperature?\n'))
# if temperature < 40:
#     print('A little cold, isn\'t it?')
# else:
#     print('Nice weather we\'re having.')

# Challenge Exercise #3

# sales = float(input('Enter amount of sales\n'))
# if sales > 50000:
#     bonus = 500.0
#     print('You have surpassed your sales goal and earned a bonus of $', bonus, sep='')

# Challenge Exercise #4
# Ask user to input number from 1 to 10 and translate it into roman numeral

# number = int(input('Enter a number from 1-10\n'))
# if number < 1 or number > 10:
#     print('That number is not from 1 to 10.')
# else:
#     if number == 1:
#         print('I')
#     if number == 2:
#         print('II')
#     if number == 3:
#         print('III')
#     if number == 4:
#         print('IV')
#     if number == 5:
#         print('V')
#     if number == 6:
#         print('VI')
#     if number == 7:
#         print('VII')
#     if number == 8:
#         print('VIII')
#     if number == 9:
#         print('IX')
#     if number == 10:
#         print('X')

# Challenge Exercise 5

def validate_score(score, min, max):
    if score < min or score > max:
        print('That score is not possible.')
        exit()
    else:
        return score
test1 = validate_score(float(input('Enter test 1 score\n')), 0, 25)
test2 = validate_score(float(input('Enter test 2 score\n')), 0, 25)
exam = validate_score(float(input('Enter main exam score\n')), 0, 50)

grade = 'Fail'
total_score = test1 + test2 + exam
if exam >= 25:
    if total_score > 80:
        grade = 'Distinction'
        print('Your total points are:',total_score, 'and your grade is:', grade)
    elif total_score > 60:
        grade = 'Credit'
        print('Your total points are:',total_score, 'and your grade is:', grade)
    else:
        grade = 'Pass'
        print('Your total points are:',total_score, 'and your grade is:', grade)
else:
    print('Your total points are:',total_score, 'and your grade is:', grade)

