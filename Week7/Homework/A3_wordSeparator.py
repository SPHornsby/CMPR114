
def break_into_words(phrase: str) -> str:
    spaced_phrase = ''
    for char in phrase:
        if char.isupper():
            spaced_phrase += ' '
        spaced_phrase += char
    return spaced_phrase.lstrip().rstrip()

def get_phrase():
    return input('Enter a phrase in TitleCase with no spaces: ')

def main():
    try:
        phrase = get_phrase()
        spaced_phrase = break_into_words(phrase)
        print(spaced_phrase)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()