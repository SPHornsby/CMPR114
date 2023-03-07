# Create a program that will ask the user to enter the first 
# and last name, with age, and output the results.
# Be sure to use your criteria for the input.
# Expected outcomes is: Jason Sim, 45

def print_bio():
    first_name = str(input('Enter your first name: '))
    last_name = str(input('Enter your last name: '))
    age = str(input('Enter your age: '))
    print(f'{first_name} {last_name}, {age}')
print_bio()