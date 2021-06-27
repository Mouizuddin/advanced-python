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
    raise_amount = 1.04
    def __init__(self,name,last,pay):
        self.name = name
        self.last = last
        self.pay = pay
    def full_name(self):
        return f'{self.name} {self.last}'
    @property
    def email(self):
        return f'{self.name} {self.last} @email.com'

    @classmethod
    def increment(cls,amount):
        cls.raise_amount = amount


class Develpoer(Employee):
    raise_amt = 100
    def __init__(self,name,last,pay,programming,lists= None):
        super().__init__(name,last,pay) #super() function returns an object that represents the parent class
        self.programming = programming
        if lists is None:
            self.lists = []
        else:
            self.lists = lists

    def add(self,adds):
      if adds not in self.lists:
          self.lists.append(adds)

    def show_list(self):
        count = 0
        for ii in self.lists:
            count +=1
            print(f'{count} in list {ii.full_name()}')


a = Employee("mohammed",'Mouizuddin',1000)
b = Develpoer('name-1','lastnae-2',52000,"programming-lamguage")
# print(b.raise_amt)
# print(b.programming)

print(b.add())