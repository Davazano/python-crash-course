#  Every Python list has a sort method that sorts it in place. If you don’t want to mess
# up your list, you can use the sorted function, which returns a new list:
x = [4,1,2,3]
y = sorted(x)     # is [1,2,3,4], x is unchanged
x.sort()          # now x is [1,2,3,4]

# If you want elements sorted from largest to smallest, you can specify a reverse=True
# parameter. And instead of comparing the elements themselves, you can compare the
# results of a function that you specify with key:
# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key=abs, reverse=True)  # is [-4,3,-2,1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
    key=lambda (word, count): count,
    reverse=True)