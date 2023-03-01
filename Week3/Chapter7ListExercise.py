# Challenge Exercise #4
def total():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for value in numbers:
        sum += value
    
    average = sum/len(numbers)
    print(f'The total is {sum}, the average is {average}')

    fh = open('numbers.text', 'w')
    for value in numbers:
        fh.write(str(value) + '\n')
    fh.close()

# total()


# Weekly Sales
def weekly_sales_report():
    print("Enter the sales for each day of the week")
    weekly_sales = []
    for i in range(7):
        weekly_sales.append(float(input(f'Enter sales for day {i+1}: ')))
    total = 0
    for day in weekly_sales:
        total += day
    report = f'Total sales for the week was: ${total}'
    print(report)
    fh = open('weekly_sales.txt', 'w')
    fh.write(report)
    fh.close()

# weekly_sales_report()

def rainfall_app():
    monthly_totals = [['Jan',0],['Feb',0],['Mar',0],['Apr',0],['May',0],['Jun',0],['Jul',0],['Aug',0],['Sep',0],['Oct',0],['Nov',0],['Dec',0]]
    highest_rainfall = 0
    lowest_rainfall = 65000
    highest_month = ''
    lowest_month = ''
    total_rainfall = 0
    for month in monthly_totals:
        rainfall = float(input(f'Enter the rainfall for {month[0]}: '))
        month[1] = rainfall
        total_rainfall += rainfall
        if rainfall > highest_rainfall:
            highest_rainfall = rainfall
            highest_month = month[0]
        if rainfall < lowest_rainfall:
            lowest_rainfall = rainfall
            lowest_month = month[0]
    total = f'Total rainfall was {total_rainfall}. Average montly rainfall was {total_rainfall/12}.'
    highest = f'The month with the most rain was {highest_month}, with {highest_rainfall} inches of rain.'
    lowest = f'The month with the least rain was {lowest_month}, with {lowest_rainfall} inches of rain.'
    output = [total,highest,lowest]
    fh = open('rainfall.txt','w')
    for line in output:
        print(line)
        fh.write(line)
    fh.close()

rainfall_app()