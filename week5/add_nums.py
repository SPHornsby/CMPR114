
def add(num1 :int|float, num2 :int|float, num3 :int|float) -> int|float:
    """Takes 3 numbers and returns the sum of those numbers."""
    global total
    total= num1 + num2 + num3
    # return total

def main():
    add(3,4,5)
    print(total)

if __name__ == '__main__':
    main()