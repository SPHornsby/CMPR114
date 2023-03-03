# This program will ask the user to enter 20 numbers
# and store them as a list.
# It will then display the highest and lowest numbers,
# the sum of the numbers, and the average of the numbers.
# Set the number of numbers to get
NUMBER_OF_NUMBERS = 20
# The get_numbers function gets a series of numbers
# from the user and stores them in a list.
# A reference list is returned
def get_numbers():
    # Initialize an empty list
    numbers = []
    for i in range(NUMBER_OF_NUMBERS):
        number = int(input('Enter a number: '))
        numbers.append(number)
    return numbers

def get_lowest(number_list):
    number_list.sort()
    return number_list[0]

def get_highest(number_list):
    number_list.sort(reverse=True)
    return number_list[0]

def get_total(number_list):
    return sum(number_list)

def get_average(sum):
    return sum/NUMBER_OF_NUMBERS

def main():
    number_list = get_numbers()
    lowest = get_lowest(number_list)
    highest = get_highest(number_list)
    total = get_total(number_list)
    average = get_average(total)
    print(f'lowest = {lowest},highest = {highest},total = {total},average = {average}')

if __name__ == '__main__':
    main()