def translate_word(word: str) -> str:
    pig = 'AY'
    if len(word) == 1:
        return word + pig
    else:
        split_word = [word[0], word[1 : len(word) +1]]
        reassembled_word = split_word[1] + split_word[0] + pig
        return reassembled_word

def translate_phrase(phrase: str)-> str:
    words = phrase.split(' ')
    pig_latin_words = []
    for word in words:
        pig_latin_words.append(translate_word(word))
    return ' '.join(pig_latin_words)

def main():
    try:
        phrase = input('Enter phrase to translate into pig latin: ')
        pig_latin_phrase = translate_phrase(phrase)
        print(pig_latin_phrase)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()