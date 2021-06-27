def doc():
 """Decorator
is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure
Follows functions first class concept
"""

"""Recap:
first class functions : Allows to treat function like any other objects
"""
def outter_function(logging):
    def inner():
        print(logging) # free variable
    return inner # not executed
    # return inner()  #  executed

# closure gives you access to an outer function's scope from an inner function
hi = outter_function("Hi")
bye = outter_function("Bye")
# hi()
# bye()

# Is a function that takes another function as argument add extra functionality and returns another function without altering the scr code of  original function passed in

# def decorator_function(message):
#     def wrapper_function():
#         return message
#     return wrapper_function
#
# output = decorator_function('LOGGING')
# print(output())


def decorator_function(original_function):
    def wrapper_functon():
        print('Define Decorators?')
        return original_function()

    return wrapper_functon

def to_display(): # without modifying to_dispaly(), can add extra functionality
    return "Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure"

# () <- EXECUTES THE CODE
abc = decorator_function(to_display)
print(abc())

# @ :
@decorator_function
def original_function():
    return to_display()
print('====='*30)
print(original_function())

print('====='*30)
print("WITH ARGUMENT'S")

def decorator_function_2(original_function):
    def wrapper_function_2(*args,**kwrags):
        print(f"NAME OF THE FUNCTION IS {decorator_function.__name__}")
        print(f'ALL DOCUMENTATION GIVEN HERE ARE : {doc.__doc__}')
        return original_function(*args,**kwrags)
    return wrapper_function_2


@decorator_function_2
def details(a,b):
    return f'name {a} age {b} '

print(details("Mohammed mouizuddin",23))


# arguments to decorator
def prefix_decorator(prefix):
    def decorator_function_3(original_function):
        def wrapper_function_3(*args,**kwargs):
            print(f'{prefix} :<- smaple')
            return original_function(*args,**kwargs)
        return wrapper_function_3
    return decorator_function_3

print('======'*10)
@prefix_decorator('GOGGING')
def original_function():
    return to_display()
print(original_function())