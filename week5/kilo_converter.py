
KILOMETERS_TO_MILES = 0.6214
def get_kilometers() -> float:
    return float(input('Enter the number of kilometers to convert: '))

def convert_to_miles(kilometers: float) -> float:
    return kilometers * KILOMETERS_TO_MILES

def display_conversion(kilometers: float, miles: float) -> None:
    print(f'{kilometers} kilometers converts to {miles} miles.')

def main() -> None:
    """Ask user to enter a distance in kilometers.
    Returns the distance converted into miles."""
    kilometers = get_kilometers()
    miles = convert_to_miles(kilometers)
    display_conversion(kilometers, miles)

if __name__ == '__main__':
    main()