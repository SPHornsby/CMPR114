# Create a program that will ask the user to enter the Sales, and then display the commission

def calculate_commission():
    sales = float(input('Enter the amount of sales: '))
    commission_rate = 0.0
    if sales >= 50000 and sales <= 60000:
        commission_rate = 0.1
    elif sales >= 70000 and sales <= 80000:
        commission_rate = 0.2
    elif sales >= 90000 and sales <=100000:
        commission_rate = 0.3
    commission = '{:0,.2f}'.format(sales * commission_rate)
    print(f'The commission rate is {commission_rate} and the commission earned is: {commission}')
calculate_commission()