# Create a program that will ask the user to enter the Sales then multiply 
# the salary with commission, and finally add the results to the salary.
# See table below: Use the If statement. The more sales are sold the more commission is given.

def calculate_commission_with_salary():
    # initialize the commission rates and salary to zero
    commission_rate = 0.0
    salary = 0.0
    # Get user input for sales amount
    sales = float(input('Enter the amount of sales: '))
    # Set actual commission rate and salary based on sales
    if sales >= 50000 and sales < 70000:
        commission_rate, salary = 0.1, 70000
    elif sales >= 70000 and sales < 90000:
        commission_rate, salary = 0.2, 80000
    elif sales >= 90000 and sales <=100000:
        commission_rate, salary = 0.3, 90000
    # multiply the salary with commission and add the results to the salary
    total_compensation = '{:0,.2f}'.format(salary + (salary*commission_rate))
    print(f'The salary with commission is {total_compensation}')
calculate_commission_with_salary()