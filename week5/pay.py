
def get_hours_worked() -> float:
    return float(input('Input the number of hours worked: '))

def get_wage() -> float:
    return float(input('Input the hourly wage '))

def get_total_pay(hours_worked: float, wage: float) -> float:
    return hours_worked * wage

def display_pay(total_pay: float) -> None:
    print('The total pay is', '${:,.2f}'.format(total_pay))

def main() -> None:
    """Gets user input for hours worked and wage, calculates the total pay, and prints it."""
    hours_worked = get_hours_worked()
    wage = get_wage()
    total_pay = get_total_pay(hours_worked, wage)
    display_pay(total_pay)
    
if __name__ == '__main__':
    main()
