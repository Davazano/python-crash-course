# collection of distinct elements:
s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2}
s.add(2) # s is still { 1, 2}
x = len(s) # equals 2
y = 2 in s # equals True
z = 3 in s # equals False

# We’ll use sets for two main reasons. The first is that in is a very fast operation on sets.
# If we have a large collection of items that we want to use for a membership test, a set
# is more appropriate than a list:

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set # very_fast to check

# The second reason is to find the distinct items in a collection:
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]
