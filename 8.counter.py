# A Counter turns a sequence of values into a defaultdict(int)-like object mapping
# keys to counts. We will primarily use it to create histograms:

from collections import Counter
c = Counter([0, 1, 2, 0]) # c is (basically) { 0:2, 1:1, 2:1}

# This gives us a very simple way to solve our word_counts problem:
word_counts = Counter(document)

# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print word, count