
def get_info() -> list: 
    return [str(input('Enter your first name: ')),     \
            str(input('Enter your last name: ')),      \
            str(input('Enter your street address: ')), \
            str(input('Enter your city: ')),           \
            str(input('Enter your state: ')),          \
            str(input('Enter your zip code: ')),       \
            ]

def main():
    first_name, last_name, street_address, city, state, zip = get_info()
    print(f'{first_name} {last_name} at {street_address} in {city}, {state}, {zip}')

if __name__ == '__main__':
    main()