
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    return choice

def look_up(birthdays):
    name = input('Enter a name ')
    if name in birthdays:
        print(birthdays[name])
    else:
        print('That name is not found.')
    

def add(birthdays):
    name = input('Enter a name: ')
    date = input('Enter a date (mm/dd/yyyy): ')

    return birthdays | {name: date}

def delete(birthdays):
    name = input('Enter a name: ')
    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')

    
def main():
    birthdays = {}
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            print(birthdays)
            look_up(birthdays)
        elif choice == ADD:
            birthdays = add(birthdays)
        elif choice == CHANGE:
            # change(birthdays)
            pass
        elif choice == DELETE:
            delete(birthdays)


if __name__ == '__main__':
    main()

