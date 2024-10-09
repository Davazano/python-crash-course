#  Not infrequently, you’ll want to iterate over a list and use both its elements and their
# indexes:
# not Pythonic
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)

# also not Pythonic
i = 0
for document in documents:
    do_something(i, document)
    i += 1

# The Pythonic solution is enumerate, which produces tuples (index, element):
for i, document in enumerate(documents):
    do_something(i, document)

# Similarly, if we just want the indexes:
for i in range(len(documents)): do_something(i)     # not Pythonic
for i, _ in enumerate(documents): do_something(i)   # Pythonic