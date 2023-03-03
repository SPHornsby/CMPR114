# The get_scores function gets a series of test
# scores from the user and stores them in a list.
# A reference list is returned.
def get_scores():
    # Create an empty list.
    test_scores = []

    # Create a variable to control the loop.
    again = 'y'

    # Get the scores from the user
    # and add them to the list.
    while again =='y':
        # Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        # Want to do this again?
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()
    
    # Return the list.
    return test_scores

# The get_total function accepts a list as an
# argument and returns the total of the values
# in the list.

def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total += num
    
    # Return the total.
    return total

def output_to_console(output):
    print(output)

def store_to_file(contents):
    fh = open('total_score','w')
    fh.write(contents)
    fh.close()

def main():
    total = get_total(get_scores())
    formatted_total = f'The total score is {str(total)}'
    store_to_file(formatted_total)
    output_to_console(formatted_total)

if __name__ == '__main__':
    main()