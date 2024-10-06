# Booleans in Python work as in most other languages, except that they’re capitalized:
one_is_less_than_two = 1 < 2    # equals True      
true_equals_false = True == False # equals False

# Python uses the value None to indicate a nonexistent value. It is similar to other lan
# guages’ null:
x = None
print x == None    # prints True, but is not Pythonic
print x is None    # prints True, and is Pythonic

# Python lets you use any value where it expects a Boolean. The following are all “Falsy”
# • False
#  • None
#  • [] (an empty list)
#  • {} (an empty dict)
#  • ""
#  • set()
#  • 0
#  • 0.0

# This allows you to easily use if state ments to test for empty lists or empty strings or empty dictionaries or so on. It also
# sometimes causes tricky bugs if you’re not expecting this behavior:
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""
 
# A simpler way of doing the same is:
first_char = s and s[0]
 
# since and returns its second value when the first is “truthy,” the first value when it’s
# not. Similarly, if x is either a number or possibly None:
safe_x = x or 0

all([True, 1, { 3 }])   # True
all([True, 1, {}])      # False, {} is falsy
any([True, 1, {}])      # True, True is truthy
all([])                 # True, no falsy elements in the list
any([])                 # False, no truthy elements in the list