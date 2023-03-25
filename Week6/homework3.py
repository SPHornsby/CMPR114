
def write_loop():
    fh = open('number_list.txt','w')
    for i in range(100):
        fh.write(str(i+1)+'\n')
    fh.close()

def main():
    try:
        write_loop()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()