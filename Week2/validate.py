def validate(number, min, max):
    if number < min or number > max:
        print('That number is not possible.')
        exit()
    else:
        return number