MapReduce Word Count Example
============================

This is just a simple word count program to help understand how MapReduce works.
To try it out run: `$ cat words.txt | python3 mapper.py | sort -t 1 | python3 reducer.py | sort -t$'\t' -k2 -rn`.
The file `words.txt1` is pipped to `mapper.py` which splits the lines into indivdual words and maps
each word to a value of one (output is `{word}<tab>{count}`). The output is sorted and sent to the reducer, which sums up and prints the total occurences of each word (again the format is `{word}<tab>{count}`). The output is finally sorted in descending order by number of occurences.