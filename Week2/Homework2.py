# Sean Hornsby-Caban
# 2/13/2023
# Week2 Homework

from validate import validate
# Quarter of the year
# month = validate (int(input('Enter the number of the month\n')), 1, 12)
# if month < 4:
#     print('That month is in the first quarter.')
# elif month < 7:
#     print('That month is in the second quarter.')
# elif month < 10:
#     print('That month is in the third quarter.')
# else:
#     print('That month is in the fourth quarter.')

# Hot Dog Cookout Calculator
# import math
# HOT_DOG_PACKAGE = 10
# HOT_DOG_BUN_PACKAGE = 8
# number_of_people = int(input('How many people are coming?\n'))
# dogs_per_person = int(input('How many hotdogs will each person be alloted?\n'))
# hot_dogs_necessary = number_of_people * dogs_per_person
# dog_packages_necessary = math.ceil(hot_dogs_necessary/HOT_DOG_PACKAGE)
# bun_packages_necessary = math.ceil(hot_dogs_necessary/HOT_DOG_BUN_PACKAGE)
# left_over_dogs = HOT_DOG_PACKAGE - (hot_dogs_necessary%HOT_DOG_PACKAGE)
# left_over_buns = HOT_DOG_BUN_PACKAGE - (hot_dogs_necessary%HOT_DOG_BUN_PACKAGE)
# print('That is',hot_dogs_necessary,'hot dogs!')
# print('You will need to buy',dog_packages_necessary,'packages of hot dogs.')
# print('You will need to buy',bun_packages_necessary,'packages of hot dog buns.')
# print('You will have',left_over_dogs,'hot dogs left over.')
# print('You will have',left_over_buns,'buns left over.')

# Software Sales

quantity = int(input('How many copies of the software do you want to purchase?\n'))
discount_rate = 0.0
cost = 99.0
if quantity > 9 and quantity < 20:
    discount_rate = 0.1
elif quantity >= 20 and quantity < 50:
    discount_rate = 0.2
elif quantity >= 50 and quantity < 100:
    discount_rate = 0.3
elif quantity >= 100:
    discount_rate = 0.4

discounted_cost = quantity * cost * (1 - discount_rate)
print(discounted_cost)

