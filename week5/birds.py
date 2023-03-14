
def get_counts() -> list:
    return [int(input('How many birds does Texas have? ')),int(input('How many birds does California have? '))]

def show_texas(birds: str) -> None:
    print(f'Texas has {birds} birds.')

def show_california(birds: str) -> None:
    print( f'California has {birds} birds.')

def main() -> None:
    """Asks user for bird counts from two states and then displays those counts."""
    texas_birds, california_birds = get_counts()
    show_texas(texas_birds)
    show_california(california_birds)

if __name__ == '__main__':
    main()