
def write_things():
    things_to_write = [
        'dog',
        'lemon',
        'Madagascar'
    ]

    fh = open('things.txt','w')
    for thing in things_to_write:
        fh.write(thing + '\n')
    fh.close()

def main():
    try:
        write_things()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()