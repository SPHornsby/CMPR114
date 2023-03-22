
def salary() -> None:
    salary_file = open('salary.txt', 'w')
    salary_amt = float(input('enter the salary '))
    salary_file.write(str(salary_amt))

def sales() -> None:
    """Asks user to input a number of days
    and then the sales amount for each day."""
    num_days = int(input("enter the days of sales "))
    sales_file = open('sales.txt','w')

    for count in range(1, num_days+1):
        sales = float(input('enter the sales for day # ' + str(count) + ': '))
        sales_file.write(str(sales) + '\n')
    sales_file.close()
    print('sales recorded')

def ReadSales() -> float:
    sales_file = open('sales.txt','r')
    line = sales_file.readline()
    total_sales = 0
    while line != '':
        amount = float(line)
        total_sales += amount
        print('Sales:',format(amount, '.2f'))
        line = sales_file.readline()

    sales_file.close()
    return total_sales

def ReadSalary() -> float:
    salary_file = open('salary.txt')
    return salary_file.readline()

def display_salary(salary) -> None:
    print(f'Salary with bonus is {salary}')
    
def main() -> None:
    salary()
    sales()
    total_sales = ReadSales()
    salary_amt = ReadSalary()
    if total_sales > 1000:
        salary_amt = float(salary_amt)
        salary_amt *= 1.1
    display_salary(salary_amt)

if __name__ == '__main__':
    main()