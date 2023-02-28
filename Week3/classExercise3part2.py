# This program calculates the sum and average
# of a series of numbers entered by the user.
def sum_avg():
    MAX = 5 # Maximum number of numbers

    # Initialize an accumulator variable
    total = 0.0

    # Explain to the user
    print('This program calculates the sum and average of')
    print(f'the {MAX} numbers you will enter.')

    # Get the numbers and accumulate them
    for counter in range(MAX):
        number = int(input('Enter a number: '))
        total += number

    # Display sum and average
    print(f'The total is {total} and the average is {total/MAX}')

# This program will take user input, multiply it by 10 and continue looping until that product is greater than or equal to 100
def product_over_100():
    product = 0
    while product < 100:
        product = 10 * int(input('Enter a number: '))
        print(f'Product is {product}')
    print('You have escaped the loop!')
# product_over_100()   

