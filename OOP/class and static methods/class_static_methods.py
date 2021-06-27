                    # class methods and static methods

'''class methods
- @classmethod : passes class(cls) as a first argument
-  is also ,alternative constructors

static methods 
- takes on arguments 
- we include them in class, because they have some logical connection with the class
'''

class Employee(object):
    total_raise = 1.05
    def __init__(self,first_name,last_name,amount):
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def increment(self):
        self.amount = int(Employee.total_raise * self.amount)

    @classmethod # class method
    def apply_raise(cls,raise_by):
        cls.total_raise = raise_by

    @classmethod # alternative constructors
    def from_strings(cls,new_string):
        first,last,pay = new_string.split("-")
        return cls(first,last,pay) # returns a new object

    @staticmethod # date : wheather or not that was a work day
    def work_day(day):
        if day.weekday() == 5 or  day.weekday() == 5:
            return f'is not a working day >>{False}'
        return f'is working day >>{True}'
# NOTE :if we dont access instance or class anywhere within a function,then we can use a static method




emp_1 = Employee("first_name" , "Lsat_name" , 10000)
# calling of class method
Employee.apply_raise(1.04) # by this,it changes it class attribute total_raise from(1.05 to 1.04)
print(emp_1.amount)
emp_1.increment()
print(emp_1.amount)
# string
string_from = "name_A-name_B-50000"
# line 25 > created an other way of creting an object
alternative_constructor = Employee.from_strings(string_from)
print(alternative_constructor.first_name)
new_record = "Mohammed-Mouizuddin-171061101078"
Employee.from_strings(new_record)
print(new_record)
# static
import datetime
# date_current = datetime.date.today()
my_date = datetime.date(2021,3,24)
print(Employee.work_day(my_date))