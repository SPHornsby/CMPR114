
def getString() -> str:
    return input('Enter string to be analyzed: ')

def countConsonants(user_string: str) -> int:
    vowels = ['a','e','i','o','u']
    number_of_consonants = 0
    for char in user_string:
        if char.isalpha() and char.lower() not in vowels:
            number_of_consonants += 1
    return number_of_consonants

def countVowels(user_string: str) -> int:
    vowels = ['a','e','i','o','u']
    number_of_vowels = 0
    for char in user_string:
        if char.lower() in vowels:
            number_of_vowels += 1
    return number_of_vowels

def main():
    try:
        user_string = getString()
        vowels = countVowels(user_string)
        consonants = countConsonants(user_string)
        print(f'{user_string} has {vowels} vowels and {consonants} consonants')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
