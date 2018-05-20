import sys

current_item = None
current_count = 0

for line in sys.stdin:
    item, count = line.split('\t')

    count = int(count)

    if item == current_item:
        current_count += count
    else:
        if current_item:
            print('{}\t{}'.format(current_item, current_count))
        current_item = item
        current_count = count

if current_item == item:
    print('{}\t{}'.format(current_item, current_count))