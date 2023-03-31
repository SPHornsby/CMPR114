
def get_most_frequent(word: str) -> str:
    letters = dict()
    for char in word:
        if char in letters:
            letters[char] += 1
        else:
            newletter = {char:1}
            letters = letters | newletter
    sorted_letters_by_frequency = sorted(letters.items(), key = lambda x:x[1], reverse=True)
    highest_frequency = sorted_letters_by_frequency[0][1]
    most_frequent_letters = []
    for i in sorted_letters_by_frequency:
        if i[1] == highest_frequency:
            most_frequent_letters.append(i[0])
    return most_frequent_letters

def main():
    get_most_frequent('dresser')
    

if __name__ == '__main__':
    main()
