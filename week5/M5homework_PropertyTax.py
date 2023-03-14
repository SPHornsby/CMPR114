
ASSESSMENT_RATE= 0.6
TAX_RATE = 0.0072 # 72 cents per 100 dollars

def get_actual_value() -> float:
    return float(input('What is the actual value of the property? '))

def calculate_assessment_value(actual_value: float) -> float:
    return actual_value * ASSESSMENT_RATE

def calculate_property_tax(assessed_value: float) -> float:
    return assessed_value * TAX_RATE

def display_values(actual_value: float, assessed_value: float, property_tax: float) -> None:
    print(f'For a property with {format_cash(actual_value)}, the assessed value is {format_cash(assessed_value)}, and the proerpty tax is {format_cash(property_tax)}')

def format_cash(value: float) -> str:
    return '${:,.2f}'.format(value)

def main() -> None:
    """Asks user for actual value of a piece of property
    and displays the assessment value and the property tax."""
    actual_value = get_actual_value()
    assessed_value = calculate_assessment_value(actual_value)
    property_tax = calculate_property_tax(assessed_value)
    display_values(actual_value, assessed_value, property_tax)

    pass

if __name__ == '__main__':
    main()
