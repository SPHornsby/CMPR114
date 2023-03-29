import pickle

def main():
    end_of_file = False
    input_file = open('info.dat', 'rb')

    while not end_of_file:
        try:
            person = pickle.load(input_file)
            display_data(person)
        except EOFError:
            end_of_file = True
    
    input_file.close()

def display_data(person):
    print('Name:', person['name'])
    print('Age:', person['Age'])
    print('Weight:', person['Weight'])
    print()

if __name__ == '__main__':
    # fh = open('info.dat','wb')
    # pickle.dump({'name': 'Sean', 'Age': 46, 'Weight': 'Don\'t worry about it'}, fh)
    # fh.close()
    main()

