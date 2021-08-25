# First Class Function : Treat function just like anyother object or variable
"""First-class function
A programming language is said to be First class function if it treats functions as
First class citizens

First class citizens :
In a programming language is an entity which supports all the operations generally avaliable
to other entities, includes
- assigned to a variable
- returned from a function
- include being passed as a argument
"""
def test():
    return "First class functions"

# () <- executes the function
function_variable = test() # assignig to a variable
print(function_variable)
print(test)

def testing_2(number):
    return number * number

function_variable_2 = testing_2
print(function_variable_2(12))

# higher order functions : pass functions as arguments and return function as result of other function

# passing function as a argument (like a map function)
def squares(number):
    return  number* number

def my_map(function , lists):
    result = []
    for i in lists:
        result.append(function(i))
    return result

output = my_map(squares , [1,2,3,4,5,6,7,8,9,10])
print(output)

# return a function from another function

def outter_function():
    def inner_function():
        return "This is a inner function"
    return inner_function # outter_function functions returns inner_function


higher_order_function = outter_function()
print(higher_order_function())
print("======"*10)


# example :02
def greeting(message):
    def display_message():
        print(f"{message} This is message from greeting function")
    return display_message() # executing here

output = greeting("LOGGING MESSAGE")

print("======"*10)

# example :03
def tag(tags):
    def inner(para):
        return f'<{tags}> {para} </{tags}>'
    return inner

p = tag("h1")
output_2 = tag("h2")
print(p('helo'))
print(output_2("HIGHER ORDER FUNCTION'S"))
# closure gives you access to an outer function's scope from an inner function
print('====='*5)
def outter(text): # --------> outer function scope
    def inner():
        return text # -------> access from an inner function

    return inner

output_3 = outter("CLOUSERS") # closure
print(output_3())