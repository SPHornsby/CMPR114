
STATE_SALES_TAX = 0.05 # 5%
COUNTY_SALES_TAX = 0.025 # 2.5%

def get_sales() -> float:
    return float(input('What was the total sales? '))

def calculate_taxes(sales: float) -> list:
    return [sales*STATE_SALES_TAX, sales*COUNTY_SALES_TAX
            ]

def display(sales: float, taxes: list) -> None:
    print(f'On {format_cash(sales)} sales, the state tax is {format_cash(taxes[0])}, the county tax is {format_cash(taxes[1])}, making the total tax {format_cash(sum(taxes))}')

def format_cash(value: float) -> str:
    return '${:,.2f}'.format(value)

def main() -> None:
    """Asks user for total sales, calculates and displays sales, state tax, county tax and total tax"""
    sales = get_sales()
    taxes = calculate_taxes(sales)
    display(sales, taxes)

if __name__ == '__main__':
    main()