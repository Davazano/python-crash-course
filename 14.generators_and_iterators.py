# A problem with lists is that they can easily grow very big. range(1000000) creates an
# actual list of 1 million elements. If you only need to deal with them one at a time, this
# can be a huge source of inefficiency (or of running out of memory). If you potentially
# only need the first few values, then calculating them all is a waste.
 
# A generator is something that you can iterate over (for us, usually using for) but
# whose values are produced only as needed (lazily).

# One way to create generators is with functions and the yield operator:
def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

# The following loop will consume the yielded values one at a time until none are left:
for i in lazy_range(10):
    do_something_with(i)

#  (Python actually comes with a lazy_range function called xrange, and in Python 3,
# range itself is lazy.) This means you could even create an infinite sequence:
def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

#  although you probably shouldn’t iterate over it without using some kind of break logic.

# The flip side of laziness is that you can only iterate through a generator once. If you need to iterate through something multiple
# times, you’ll need to either recreate the generator each time or use a list.

# A second way to create generators is by using for comprehensions wrapped in parentheses
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
#  Recall also that every dict has an items() method that returns a list of its key-value
# pairs. More frequently we’ll use the iteritems() method, which lazily yields the
# key-value pairs one at a time as we iterate over it.