'''Exception
 Program terminates as soon as it encounters an error
 An error can be a syntax error or an exception.

1) Raising an Exception
use raise keyword  to throw an exception if a condition occurs
The statement can be complemented with a custom exception.

2) The AssertionError Exception
We assert that a certain condition is met.
If this condition turns out to be True,The program can continue.
If the condition turns out to be False, you can have the program throw an AssertionError exception

3) The try and except Block: Handling Exceptions
The try and except block,is used to catch and handle exceptions
'''
import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet('Alex')

def reteap(loop):
    def decorators(main):
        def inner (*args,**kwargs):
            for _ in range(loop):
                result = main(*args,**kwargs)
            return result
        return inner
    return decorators
@reteap(loop=4)
def testing():
    print('mouiz')
testing()

