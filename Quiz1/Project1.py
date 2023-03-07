# Create a program that will ask the user to enter the gross salary (input $80,000.00) as the test data, 
# and then add 10% to the gross salary. Format the output with dollar signs, comma, and periods as shown below.
# Expected outcomes is $88,000.00

def salary_plus():
    salary = float(input('Please enter a salary: '))
    raised_salary = salary * 1.1
    formatted_salary = '{:0,.2f}'.format(raised_salary)
    print(f'The salary with a 10% raise is {formatted_salary}')

salary_plus()