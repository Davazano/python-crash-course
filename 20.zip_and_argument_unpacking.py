# Often we will need to zip two or more lists together. zip transforms multiple lists
# into a single list of tuples of corresponding elements:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)        # is [('a', 1), ('b', 2), ('c', 3)]
 
# If the lists are different lengths, zip stops as soon as the first list ends.
# You can also “unzip” a list using a strange trick:
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

# The asterisk performs argument unpacking, which uses the elements of pairs as indi
# vidual arguments to zip. It ends up the same as if you’d called:
zip(('a', 1), ('b', 2), ('c', 3))

# which returns [('a','b','c'), ('1','2','3')].
# You can use argument unpacking with any function:
def add(a, b): return a + b

add(1, 2)      # returns 3
add([1, 2])    # TypeError!
add(*[1, 2])   # returns 3