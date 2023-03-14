
def main():
    texas()
    print(california())

def texas():
    birds = int(input('How many birds does Texas have? '))
    print(f'Texas has {birds} birds.')

def california():
    birds = int(input('How many birds does California have? '))
    return f'California has {birds} birds.'


if __name__ == '__main__':
    main()