
def encode(phrase: str, shift: int):
    encoded = ''
    for char in phrase:
        # if char == ' ':       # keep space as space
        #     encoded += ' '
        if(char.isupper()):
            encoded += chr((ord(char) + shift -65) % 26 + 65) # zeroes the ordinal,applies the shift, mods the number and then unzeros it back to the upper case range
        elif(char.islower()):
            encoded += chr((ord(char) + shift -97) % 26 + 97) # same as above for lower case letters
        else:
            encoded += char
    return encoded

def main():
    try:
        phrase = input('Enter phrase to ciper: ')
        shift = int(input('Enter shift distance: '))
        encoded_phrase = encode(phrase,shift)
        print(encoded_phrase)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()