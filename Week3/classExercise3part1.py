from validate import validate
# Challenge Exercise #1: create a program with a while loop, that will ask the user to enter 4 sets of temps under 102.5
# and then get the sum and average of the four temps when the user enter a temp over 102.5
# Data set test: enter 60, 70, 80 and 90
MAX_TEMP = 102.5

def four_temps():
    i = 1
    temp_sum = 0
    print('Enter the temperatures for 4 days. I will give you the sum and average.')
    while i <= 4:
        i_temp = float(input('Enter the temperature for day: ' + str(i) + '\n'))
        validate(i_temp, max=MAX_TEMP), 
        temp_sum += i_temp
        i += 1
    print('The sum of the temps is', str(temp_sum), 'and the average temp is', str(temp_sum/4))


# four_temps()

# Challenge Exercise #2: create a program with a while loop, that will ask the user to enter the sales with commission four times, 
# and on the 4th, time will sum the sales and commission.

def four_commissions():
    i = 1
    sales_sum = 0
    commission_sum = 0
    print('Enter sales and commission rates for 4 sales. I will give you the sum of sales and the sum of commissions.')
    while i <= 4:
        i_sales = float(input('Enter the sales for sale: ' + str(i) + '\n'))
        i_commission = float(input('Enter the commission rate for sale: ' + str(i) + '\n'))
        sales_sum += i_sales
        commission_sum += (i_sales * i_commission)
        i += 1
    print('The sum of the sales is', str(sales_sum), '\nThe sum of commissions is', str(commission_sum))

def main():
    MAX_CHOICE = 2
    print('********************************')
    print('*    Class Exercise 3 Pt 1     *')
    print('*------------------------------*')
    print('*  1) Four Temps (Exercise #1) *')
    print('*  2) Four Sales (Exercise #2) *')
    print('********************************')
    print('********************************')

    choice = int(input('Which function do you want to run?'))
    if choice < 0 or choice > MAX_CHOICE:
        exit()
    elif choice == 1:
        four_temps()
        exit()
    elif choice == 2:
        four_commissions()
        exit()

main()
