
def get_nums() -> None:
    """Gets three numbers from a user."""
    global nums
    nums = [
        int(input('Enter the first number: ')),
        int(input('Enter the second number: ')),
        int(input('Enter the third and final number: '))
    ]

def add() -> None:
    """Takes 3 numbers and returns the sum of those numbers."""
    global total
    total= sum(nums)

def average_nums() -> None:
    """Averages three numbers"""
    global average
    average = total/3

def main():
    get_nums()
    add()
    average_nums()
    print(total, average)

if __name__ == '__main__':
    main()