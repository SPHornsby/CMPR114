# Sean Hornsby-Caban
# 2/13/2023
# Week2 Class Exercises - Conditionals Part 2

# Challenge Exercise #1

# def validate(input, min, max):
#     if input < min or input > max:
#         print('That number is not possible.')
#         exit()
#     else:
#         return input

# pick = validate(int(input('pick a number from 0 to 36\n')), 0, 36)

# if pick == 0:
#     print('The pocket is Green')
# elif (pick > 0 and pick <= 10) or (pick > 18 and pick <= 28):
#     if pick % 2 == 0:
#         print('The pocket is Black')
#     else:
#         print('The pocket is Red')
# else:
#     if pick % 2 != 0:
#         print('The pocket is Black')
#     else:
#         print('The pocket is Red')

# Challenge Exercise #2
weight = float(input('How much does your package weigh (in pounds)?\n'))

# set default rate (for 2 pounds or under)
# then set rate based on weight
rate = 1.5
# 
if weight > 10:
    rate = 4.75
elif weight <= 10 and weight > 6:
    rate = 4.00
elif weight <=6 and weight > 2:
    rate = 3.00
# format to display like currency
shipping = f"{weight * rate:.2f}"
print('Your shipping costs are: $', shipping, sep='')