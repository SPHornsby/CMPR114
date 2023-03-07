# Using the for loop, create a program that will sum the numbers 1 – 10.

NUMBERS = [1,2,3,4,5,6,7,8,9,10]

def sum_with_for_loop(list_of_numbers):
    acc = 0
    for number in list_of_numbers:
        acc += number
    return acc
    
print(f'This sum of the numbers: {NUMBERS} is: {sum_with_for_loop(NUMBERS)}')