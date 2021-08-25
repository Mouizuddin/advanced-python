"""Generator
1) Allows  to create own iterator functions
2) And return a iterator object, not a single value
3) yield statement is used rather than a return statement
"""

# a function to square  numbers
def square (num):
    lists = []
    for i in num:
        lists.append(i*i)
    return lists   # returns a list

my_list = [1,2,3,4,5,6,7,8,9,10]
print(square(my_list))
print("====="*10)


# Generator functions allow you to declare a function that behaves like an iterator
def generators(num): # behaves function like an iterator
    yield num * num
#  print(generators(1)) : <generator object generators at 0x0000021CD9B34200>

def generator_function(num):
    for i in num:
        yield i * i
output = generator_function(my_list)
print(list(output))

# generator comprehension
sample = range(10+1)
generator_comprehension = (loop**2 for loop in sample) # a generator object
# Either loop througt it or cast it to a list and get the output

'''
for i in generator_comprehension:
    print(i,end=' ')
print()
        ( OR )
cast it to any collection data type
print(list(generator_comprehension))
'''
