#  Regular expressions provide a way of searching text. They are incredibly useful but
# also fairly complicated, so much so that there are entire books written about them.
# We will explain their details the few times we encounter them; here are a few examples of how to use them in Python:
import re

print all([                       # all of these are true, because             
    not re.match("a", "cat"),     # * 'cat' doesn't start with 'a'
    re.search("a", "cat"),        # * 'cat' has an 'a' in it    
    not re.search("c", "dog"),    # * 'dog' doesn't have a 'c' in it
    3 == len(re.split("[ab]", "carbs")),   # * split on a or b to ['c','r','s']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # * replace digits with dashes
])  # prints True