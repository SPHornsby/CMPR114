

class Pet:
    '''Pet takes three option arguments, type, age, name'''
    def __init__(self, type='unicorn', age=100, name='sparkles'):
        self.__animal_type = type
        self.__age = age
        self.__name = name

    def __str__(self):
        return self.__name +' '+ str(self.__animal_type) +' '+ str(self.__age)
    
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    
    def set_age(self, a):
        self.__age = a
    def set_name(self,n):
        self.__name = n
    def set_animal_type(self,t):
        self.__animal_type = t


class Employee:
    def __init__(self,name,idnumber,dept,job):
        self.__name = name
        self.__idnumber = idnumber
        self.__department = dept
        self.__job_title = job

    def __str__(self):
        return self.__name +' '+ str(self.__idnumber) +' '+ self.__department + ' ' + self.__job_title + '\n'
    
class RetailItem:
    def __init__(self,description,units_in_inventory,price):
        self.__description = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def __str__(self):
        return self.__description +' '+ str(self.__units_in_inventory) +' '+ self.__price + '\n'