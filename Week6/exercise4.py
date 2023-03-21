
def read_employee_file() -> None:
    emp_file = open('employees.txt','r')

    name = emp_file.readline()
    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name.rstrip('\n')
        id_num.rstrip('\n')
        dept.rstrip('\n')

        print(f'Name: {name}')
        print(f'ID NUMBER: {id_num}')
        print(f'DEPARTMENT: {dept}')

        name = emp_file.readline()

    emp_file.close()

def main() -> None:
    num_emps = int(input('enter the number of employee records'))
    emp_file = open('employees.txt','w')
    for count in range(1, num_emps+1):
        print('enter data for emplyee #', count)

        name = input('Name: ')
        id_num = input('ID NUMBER: ')
        dept = input('DEPARTMENT: ')

        emp_file.write(name +'\n')
        emp_file.write(id_num +'\n')
        emp_file.write(dept +'\n')

        print()
    emp_file.close()
    print('recorded')

    read_employee_file()

if __name__ == '__main__':
    main()