import sys
import re

# matches any non-word characters (e.g. punctuation)
pattern = re.compile(r'[\W_]+')

"""mapper function
Accepts a string of words (read from stdin)
and yields individual words mapped to their
initial count, i.e. 1.
"""

def mapper(line):
    
    # split the input into a list of words
    words = line.split()

    for word in words:
        # for each word remove any punctuation
        word = pattern.sub('',word)
        # yield the key and value seperated by a tab
        yield '{}\t{}'.format(word.lower(),1)

for line in sys.stdin:
    
    # mapper() returns a generator
    map  = mapper(line)

    # each mapped item is sent to stdout
    for item in map:
        print(item)