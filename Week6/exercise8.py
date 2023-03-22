import random

def create_random_numbers()->list:
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1,10))
    return numbers

def save(numbers:list)->None:
    print('creating/opening file...')
    fh = open('rand.txt','a')
    print(f'writing {str(numbers)} to file.')
    fh.write(str(numbers) + '\n')
    fh.close()
    print('file saved.')

def read()->None:
    print('loading file...')
    fh = open('rand.txt','r')
    print('contents:\n')
    for line in fh:
        print(line)
    fh.close()
    print('eof')
def main():
    numbers = create_random_numbers()
    save(numbers)
    read()

if __name__ == '__main__':
    main()