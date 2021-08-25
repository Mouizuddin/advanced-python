'''Exception
 Program terminates as soon as it encounters an error
 An error can be a syntax error or an exception.

1) The try and except Block: Handling Exceptions
The try and except block,is used to catch and handle exceptions

2) Raising an Exception
use raise keyword  to throw an exception if a condition occurs
The statement can be complemented with a custom exception.

3) The AssertionError Exception (given logic is true or false)
We assert that a certain condition is met.
If this condition turns out to be True,The program can continue.
If the condition turns out to be False, you can have the program throw an AssertionError exception

'''

''' 1) Try and except block
try:
	yourcode...
except:
	yourcode...
'''
try:
    num = 1
    result = num / 0 # Exception ,we handel in except block
    # var_1 = var_2

except ZeroDivisionError as zero: # handel general exception
    print(f'{zero} is not possiable')

except NameError as name_error:
    print(f'{name_error} ')
else:
    print(result)
    print("This will excute if there is no exception's")

finally:
    print("Tihs is will run even if there is error/exception or not")

print("======"*10)


def raise_exception():
    print('Raising an exception')
    try:
        file = open('testing.txt')
        if file.name != 'testing.txt':
            raise TypeError("THIS IS A TESTING ERROR")
    except Exception as exp:
        print(exp)
    else:
        for i in file:
            print(i)

# raise_exception()

# The AssertionError Exception (given logic is true or false)
# assert_1 = 10 > 10
# print(assert_1)
#
# assert 10 > 10 # this will raise a AssertionError since the condtion is FALSE
try:
    condition = 10
    assert condition > 10
    print(True)
except AssertionError :
    print(False)

# even / oddd check using assert
def even_odd():
    try:
        user = int(input("Number: "))
        assert user % 2 == 0
        print("Even Number")
    except Exception :
        print(f'Is not even ')

even_odd()