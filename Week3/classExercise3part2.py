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
# sum_avg()
# This program will take user input, multiply it by 10 and continue looping until that product is greater than or equal to 100
def product_over_100():
    product = 0
    while product < 100:
        product = 10 * int(input('Enter a number: '))
        print(f'Product is {product}')
    print('You have escaped the loop!')
# product_over_100()   

def five_days_of_bugs():
    DAYS = 5
    total = 0

    # Explain to the user
    print('This program calculates the total number of bugs')
    print(f'collected over {DAYS} days.')

    # Get the numbers and accumulate them
    for counter in range(DAYS):
        number = int(input(f'How many bugs were collected on day {counter +1}? '))
        total += number 
    print(f'{total} bugs were collected.')
# five_days_of_bugs()

def calories_burned():
    intervals = [10,15,20,25,30]
    rate = 4.2
    for interval in intervals:
        print(f'Total calories burned after {interval} minutes is {interval*rate}')
# calories_burned()

def lap_times():
    slowest_lap = 0
    fastest_lap = 10000
    total_time = 0
    laps = int(input('How many laps did you go today?'))
    for lap in range(laps):
        lap_time = int(input(f'How many minutes did lap {lap+1} take? '))
        total_time += lap_time
        if lap_time < fastest_lap:
            fastest_lap = lap_time
        if lap_time > slowest_lap:
            slowest_lap = lap_time
    print(f'Your slowest lap time was {slowest_lap} minutes.')
    print(f'Your fastest lap time was {fastest_lap} minutes.')
    print(f'Your average lap time was {total_time/laps} minutes.')

lap_times()

