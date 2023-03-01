def validate(number, min = -64000, max = 64000):
    if number < min or number > max:
        print('That number is not possible.')
        exit()
    else:
        return number
        