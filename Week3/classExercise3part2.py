# This program calculates the sum and average
# of a series of numbers entered by the user.

MAX = 5 # Maximum number of numbers

# Initialize an accumulator variable
total = 0.0

# Explain to the user
print('This program calculates the sum and average of')
print(f'{MAX} numbers you will enter.')

# Get the numbers and accumulate them
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total += number

# Display sum and average
print(f'The total is {total} and the average is {total/MAX}')