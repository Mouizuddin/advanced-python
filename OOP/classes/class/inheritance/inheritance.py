# Inheritance
# Inheritance is a mechanism in which one class acquires the property of another class
                    #   use:
#  makes it easier to create and maintain an application.
# This also provides an opportunity to reuse the code functionality and fast implementation time.

# Example :
class Sample(object):
    def __init__(self):
        pass
    def method_1(self):
        return "Parent class"

class Sample_2(Sample):
    pass

# obj_1 = Sample()
# obj_2 = Sample_2()
#
# print(obj_2.method_1()) # Inheritance concept (MRO)
# print(help(Sample_2)) # Method resolution order

# Inheritance

class Employee():
    def  __init__(self,first_name ,last_name, annual_sal):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_sal = annual_sal

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Developer(Employee):
    def  __init__(self,first_name ,last_name, annual_sal,office_location=True):
        super().__init__(first_name ,last_name, annual_sal)
        # super -> lets you access methods from a parent class from within a child class
        self.office_location  = office_location

    def location(self):
        return f'Developers office  is located in {self.office_location} '

class Manager(Employee):
    def __init__(self, first_name, last_name, annual_sal,list_of_emp=None):
        super().__init__(first_name, last_name, annual_sal)
        if list_of_emp is None:
            self.list_of_emp = []
        else:
            self.list_of_emp = list_of_emp
    def add_emp(self,name):
        if name not in self.list_of_emp:
            self.list_of_emp = self.list_of_emp.append(name)

    def remove_emp(self,name):
        if name  in self.list_of_emp:
            self.list_of_emp = self.list_of_emp.remove(name)

    def all_emp(self):
        for i in self.list_of_emp:
            print(f'handles ->  {i.full_name()}')


emp_1 = Employee('FIRST_NAME','LAST_NAME',100000)
dev_1 = Developer('DEV_FIRST_NAME','DEV_LAST_NAME',200000,'India' ) # developer is a subclass of employee class
dev_2 = Developer('DEV_FIRST_NAME_2','DEV_LAST_NAME_2',60000,'India' )
manager = Manager('MANAGER_FIRST_NAME','MANAGER_LAST_NAME',70000,[dev_1,emp_1,dev_2])

print(issubclass(Developer,Employee))  # TRUE
print(dev_1.office_location)
print(dev_1.location())
print(manager.first_name)

print(manager.full_name())

