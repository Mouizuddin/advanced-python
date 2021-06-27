print("Property decorators")
#  allows the class attributes to have getters,setters,deleters functionality
# define a method, which can act like an attribute
class Sample():
    def __init__(self,n,l,s):
        self.n = n
        self.l = l
        self.s = s
        # self.email = n + ' ' + l +'@gmail.com'

    @property
    def full_name(self):
        return f'{self.n} {self.l}'
    @property
    def email(self):
        return f'{self.n} {self.l} @email.com'

    @full_name.setter
    def full_name(self,name):
        n , l = name.split(" ")
        self.n = n
        self.l = l


obj_1 = Sample('Mohammed','Mouizuddin',1000)
# obj_1.n = "new name"
# print(obj_1.n)
# print(obj_1.email)
# print(obj_1.full_name)
obj_1.full_name = "sdfdfdf sdddfdfdfdf"
print("--"*10)
print(obj_1.n)
print(obj_1.email)
print(obj_1.full_name)
