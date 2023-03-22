
def getname()->str:
    return input('enter the fullname ')

def get_midterm_grade()->float:
    return float(input('enter midterm grade. '))

def get_final_grade()->float:
    return float(input('enter final grade. '))

def get_grade_calculations(grades: list)->list:
    try:
        total = sum(grades)
        avg = total/len(grades)
        return [total, avg, letter_grade(avg)]
    except:
        print('huh')

def letter_grade(avg: float)-> str:
    try:
        if avg > 100:
            raise ValueError('Average cannot be greater than 100.') 
        if avg >= 90:
            return 'A'
        if avg >= 80:
            return 'B'
        if avg >= 70:
            return 'C'
        if avg >= 60:
            return 'D'
        
    except ValueError as e:
        print(e.args)
    

def save_grades(name: str, midterm: str, final:str, total:str, avg:str, letter:str)->None:
    try:
        fh = open('grades.txt','a')
        fh.write('\n Name: ' + name + ', Midterm Grade: ' + midterm + ', Final Grade: ' + final + ', Total Grade:' + total + ', Average Grade (points): ' + avg + ', Letter Grade: ' + letter)
    except:
        return
    
def main():
    try:
        name = getname()
        midterm = get_midterm_grade()
        final = get_final_grade()
        total, avg, letter = get_grade_calculations([midterm, final])
        save_grades(name, str(midterm), str(final), str(total), str(avg), letter)
    except ValueError as v:
        print(v)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()