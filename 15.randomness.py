#  As we learn data science, we will frequently need to generate random numbers, which
# we can do with the random module:
import random

four_uniform_randoms = [random.random() for _ in range(4)]
#  [0.8444218515250481,      # random.random() produces numbers
#   0.7579544029403025,      # uniformly between 0 and 1
#   0.420571580830845,       # it's the random function we'll use
#   0.25891675029296335]     # most often

#  The random module actually produces pseudorandom (that is, deterministic) numbers 
# based on an internal state that you can set with random.seed if you want to get
# reproducible results
random.seed(10)         # set the seed to 10
print random.random()   # e.g 0.57140259469
random.seed(10)         # reset the seed to 10
print random.random()   # e.g 0.57140259469 again

# We’ll sometimes use random.randrange, which takes either 1 or 2 arguments and
# returns an element chosen randomly from the corresponding range():
random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]

#  There are a few more methods that we’ll sometimes find convenient. random.shuffle
# randomly reorders the elements of a list:
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten
# e.g [2, 5, 1, 9, 7, 3, 8, 6, 4, 0]   (your results will probably be different)

#  If you need to randomly pick one element from a list you can use random.choice:
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me

#  And if you need to randomly choose a sample of elements without replacement (i.e.,
# with no duplicates), you can use random.sample
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # e.g [16, 36, 10, 6, 25, 9]

# To choose a sample of elements with replacement (i.e., allowing duplicates), you can
# just make multiple calls to random.choice:
four_with_replacement = [random.choice(range(10))
    for _ in range(4)]
# eg. [9, 4, 4, 2]

