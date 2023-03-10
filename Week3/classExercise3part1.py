# from validate import validate
# Challenge Exercise #1: create a program with a while loop, that will ask the user to enter 4 sets of temps under 102.5
# and then get the sum and average of the four temps when the user enter a temp over 102.5
# Data set test: enter 60, 70, 80 and 90
MAX_TEMP = 102.5

def four_temps():
    keep_going = 'y'
    temps = []
    print('Enter the temperatures for 4 days. I will give you the sum and average.')
    while keep_going == 'y':
        i_temp = float(input('Enter the temperature for day: ' + str(len(temps) + 1) + '\n'))
        if i_temp > MAX_TEMP:
            keep_going = 'n'
        else:
            temps.append(i_temp)
        if len(temps) > 4:
            temps.pop(0)
    # print('The sum of the temps is', str(temp_sum), 'and the average temp is', str(temp_sum/i))
    print(f'The sum of the temps is {str(sum(temps))}',f'and the average temp is {str(sum(temps)/len(temps))}')


# four_temps()

# Challenge Exercise #2: create a program with a while loop, that will ask the user to enter the sales with commission four times, 
# and on the 4th, time will sum the sales and commission.

def four_commissions():
    # i = 1
    sales_sum = 0
    commission_sum = 0
    print('Enter sales and commission rates for 4 sales. I will give you the sum of sales and the sum of commissions.')
    for x in range(4):
        i_sales = float(input('Enter the sales for sale ' + str(x+1) + '\n'))
        i_commission = float(input('Enter the commission rate for sale ' + str(x+1) + '\n')) / 100
        sales_sum += i_sales
        commission_sum += (i_sales * i_commission)
    # while i <= 4:
    #     i_sales = float(input('Enter the sales for sale: ' + str(i) + '\n'))
    #     i_commission = float(input('Enter the commission rate for sale: ' + str(i) + '\n'))
    #     sales_sum += i_sales
    #     commission_sum += (i_sales * i_commission)
    #     i += 1
    print('The sum of the sales is', '${:,.2f}'.format(sales_sum), '\nThe sum of commissions is', '${:,.2f}'.format(commission_sum))
four_commissions()

# Challenge Exercise #3: continuing with project #5, print odd and even number to a maximum of 10
def print_ten():
    print('I will display numbers 1-10, odd and even.')
    for num in [1,2,3,4,5,6,7,8,9,10]:
        print(num)
# print_ten()

# Challenge Exercise #4: continuing from project #6, delete the names in the array and add your first and last name using a 
# parallel for loops (use two for loops). The first for loop will loop through your last name, and the second for loop will 
# print your first name. See example below.

def print_loop():
    for x in ['Hornsby-Caban']:
        for y in ['Sean']:
            print('Your full name is',y,x)

# print_loop()


def hello_ten_worlds():
    for x in range(10):
        print('Hello world!')
# hello_ten_worlds()



def main():
    MAX_CHOICE = 5
    print('********************************')
    print('*    Class Exercise 3 Pt 1     *')
    print('*------------------------------*')
    print('*  1) Four Temps (Exercise #1) *')
    print('*  2) Four Sales (Exercise #2) *')
    print('*  3) Print Ten  (Exercise #3) *')
    print('*  4) Print Loop (Ex #4)       *')
    print('*  5) Hello World x 10 (Ex #5) *')
    print('*------------------------------*')
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
    elif choice == 3:
        print_ten()
        exit()
    elif choice == 4:
        print_loop()
        exit()
    elif choice == 5:
        hello_ten_worlds()
        exit()

# main()
