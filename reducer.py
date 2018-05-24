import sys

current_item = None
current_count = 0

for line in sys.stdin:
    # split input
    item, count = line.split('\t')

    # cast input count to integer
    count = int(count)
    
    # if the current item is the same as
    # the last item add 1 to the count
    if item == current_item:
        current_count += count
    else:
        if current_item:
            print('{}\t{}'.format(current_item, current_count))
        current_item = item
        current_count = count

if current_item == item:
    print('{}\t{}'.format(current_item, current_count))