
def show_things(things):
    print(things)

def read_things():
    read_things = []
    fh = open('things.txt','r')
    for line in fh:
        read_things.append(line.rstrip('\n'))
    fh.close()
    return read_things

def main():
    try:
        things = read_things()
        show_things(things)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()