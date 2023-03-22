
def WriteNumbers() -> None:
    """Asks the user to input three numbers. Gets the sum and average.
    Saves it all to file."""
    outfile = open('numbers.txt','a')
    num1 = int(input('enter #1 '))
    num2 = int(input('enter #2 '))
    num3 = int(input('enter #3 '))

    sum = num1 + num2 + num3
    avg = sum/3

    outfile.write("the 1st number is " + str(num1) + '\n')
    outfile.write("the 2st number is " + str(num2) + '\n')
    outfile.write("the 3st number is " + str(num3) + '\n')
    outfile.write("the avg number is " + str(avg) + '\n')
    outfile.write("the total number is " + str(sum) + '\n')

    print('data recorded')

def ReadNumbers() -> None:
    """Reads data from file and prints it."""
    infile = open('numbers.txt')
    for line in infile:
        print(line.rstrip('\n'))

def main() -> None:
    WriteNumbers()
    ReadNumbers()

if __name__ == '__main__':
    main()