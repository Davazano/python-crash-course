# Functional Tools
def exp(base, power):
    return base ** power

# and we want to use it to create a function of one variable two_to_the whose input is a
# power and whose output is the result of exp(2, power).
# We can, of course, do this with def, but this can sometimes get unwieldy:
def two_to_the(power):
    return exp(2, power)

# A different approach is to use functools.partial:
from functools import partial
two_to_the = partial(exp, 2)     # is now a function of one variable
print two_to_the(3)              # 8

# You can also use partial to fill in later arguments if you specify their names:
square_of = partial(exp, power=2)
print square_of(3)               # 9
 
# It starts to get messy if you curry arguments in the middle of the function, so we’ll try to avoid doing that.

# We will also occasionally use map, reduce, and filter, which provide functional 
# alternatives to list comprehensions:
def double(x):
    return 2 * x
 
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]      # [2, 4, 6, 8]  
twice_xs = map(double, xs)              # same as above
list_doubler = partial(map, double)     # *function* that doubles a list
twice_xs = list_doubler(xs)             # again [2, 4, 6, 8]

#  You can use map with multiple-argument functions if you provide multiple lists:
def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]

# Similarly, filter does the work of a list-comprehension if:
def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]    # [2, 4]
x_evens = filter(is_even, xs)              # same as above
list_evener = partial(filter, is_even)     # *function* that filters a list
x_evens = list_evener(xs)                  # again [2, 4]

# And reduce combines the first two elements of a list, then that result with the third,
# that result with the fourth, and so on, producing a single result:
x_product = reduce(multiply, xs)           # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply)   # *function* that reduces a list
x_product = list_product(xs)               # again = 24