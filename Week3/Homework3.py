# Distance traveled

def distance_traveled():
    speed = int(input('What is the speed of the vehicle in MPH? '))
    time = int(input('How many hours has it traveled? '))
    print('  Hour       Distance Traveled')
    print('------------------------------')
    for hour in range(time):
        print(f'   {hour+1}             {speed*(hour+1)}')


# distance_traveled()

# Average Rainfall
def average_rainfall():
    MONTHS_PER_YEAR = 12
    years = int(input('How many years do you wish to calculate for? '))
    total_rainfall = 0
    for year in range(years):
        for month in range(MONTHS_PER_YEAR):
            rainfall = float(input(f'How many inches of rain fell in month {month +1} of year {year +1}? '))
            total_rainfall += rainfall
    print(f'There are {years*MONTHS_PER_YEAR} months in this calculation.')
    print(f'The total rainfall was {total_rainfall} inches.')
    print(f'The average rainfall per month was {total_rainfall/(years*MONTHS_PER_YEAR)} inches.')

# average_rainfall()

# Sum of Numbers
def sum_of_numbers():
    numbers = []
    keep_going = 'y'
    print('Enter a series of whole numbers to be summed, one at a time. To stop, enter a negative number.')
    while keep_going == 'y':
        number = int(input('Enter your number: '))
        if number < 0:
            keep_going = 'n'
        else:
            numbers.append(number)
    print(f'The sum of the numbers entered is: {sum(numbers)}')

sum_of_numbers()