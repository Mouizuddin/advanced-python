'''Class
- Is a blueprint which we use to create objects (Are like code templates)
- Logically group data and attributes
'''

# Make a clsss
class Testing():
    pass

# object's
obj_1 =  Testing() # obj_1 -> object of the class (Testing)

# creating instances manually
obj_1.name = "MANULA INSTANCE ONE"
print(obj_1.name)

print('==='*10)

class Employe():
    def __init__(self,firts_name,last_name): # by using self instances are passed automatically
        # self is just a naming convention
        self.first_name = firts_name
        self.last_name = last_name

    def email(self): # A method
        return f'{self.first_name}_{self.last_name}@company.com'

emp_1 = Employe('FIRST_NAME','LAST_NAME')
print(emp_1.email())