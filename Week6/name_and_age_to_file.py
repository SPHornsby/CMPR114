
def get_user_info() -> list:
    """Asks user for input."""
    first_name = input('Enter your first name: \n')
    last_name = input('Enter your last name: \n')
    age = input('Enter your age: \n')
    return [first_name, last_name, age]

def save_to_file(filename: str, data) -> None:
    """Opens a file and saves the data into the file."""
    file = open(filename, 'w')
    for item in data:
        file.write(f'{item}\n')
    file.close()

def read_from_file(filename: str) -> None:
    """Opens file, reads rows of data into memory,
    and then displays them."""
    file = open(filename, 'r')
    first_name = file.readline()

    while first_name != '':
        last_name = file.readline()
        age = file.readline()

        first_name.rstrip('\n')
        last_name.rstrip('\n')
        age.rstrip('\n')

        display_info(first_name, last_name, age)
        first_name = file.readline()
    file.close()

def display_info(first_name: str, last_name: str, age: str) -> None:
    """Appends informational data and prints the lines."""
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Age: {age}')

def main() -> None:
    filename = 'file.txt'
    save_to_file(filename, get_user_info())
    print()
    read_from_file(filename)

if __name__ == '__main__':
    main()