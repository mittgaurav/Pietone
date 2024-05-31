# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:25:49 2024

Given list of statements that tell

<pre>
CustomerEnter <customer_id> <line_number> <num_items>
BasketChange <customer_id> <new_num_items>
LineService <customer_id> <num_processed_items>
LinesService
</pre>

Figure out the order of customers being processed

Python data structures are not sorted, not even set.

@author: gaurav
"""
from collections import defaultdict, deque
import bisect

lines = deque()
line_custs = defaultdict(lambda: deque())
cust_lines = defaultdict(lambda: -1)
cust_num_items = defaultdict(int)
orig_cust_num_items = defaultdict(int)


def service_items(customer_id, line_number, num_processed_items):
    items_this_cust = cust_num_items.pop(customer_id)
    # print('gaga', customer_id, line_number, num_processed_items, items_this_cust)
    if num_processed_items >= items_this_cust:
        # print('gaga', customer_id, line_number, num_processed_items, items_this_cust)
        # all items are processed for this customer
        line_custs[line_number].popleft()
        cust_lines.pop(customer_id)
        print(customer_id)
    else:
        cust_num_items[customer_id] = items_this_cust - num_processed_items

    return num_processed_items - items_this_cust

if __name__ == "__main__":
    import sys

    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "CustomerEnter":
            customer_id = int(line[1])
            line_number = int(line[2])
            num_items = int(line[3])

            if num_items == 0:
                print(customer_id)
                continue

            cust_lines[customer_id] = line_number
            line_custs[line_number].append(customer_id)

            bisect.insort(lines, line_number)
            cust_num_items[customer_id] = num_items
            orig_cust_num_items[customer_id] = num_items
        elif line[0] == "BasketChange":
            customer_id = int(line[1])
            new_num_items = int(line[2])

            if new_num_items == 0:
                sys.stdout.write(customer_id)

                # remove customer
                line_number = cust_lines.pop(customer_id)
                cust_num_items.pop(customer_id)
                orig_cust_num_items.pop(customer_id)

                # remove customer from line
                line_custs[line_number].remove(line_custs[line_number].index(customer_id))
                continue

            orig_num_items = orig_cust_num_items[customer_id]
            if orig_num_items < new_num_items:
                # send to the back
                line_number = cust_lines[customer_id]
                # print(cust_lines, line_custs[line_number], line_custs[line_number].index(customer_id))
                del line_custs[line_number][line_custs[line_number].index(customer_id)]
                line_custs[line_number].append(customer_id)

            cust_num_items[customer_id] += new_num_items - orig_num_items
            orig_cust_num_items[customer_id] = new_num_items

        elif line[0] == "LineService":
            line_number = int(line[1])
            num_processed_items = int(line[2])
            # TODO Implement
            if not num_processed_items:
                continue
            if not line_custs[line_number]:
                continue
            while num_processed_items > 0:
                if not line_custs[line_number]:
                    break
                customer_id = line_custs[line_number][0]
                num_processed_items = service_items(customer_id, line_number, num_processed_items)

        elif line[0] == "LinesService":
            for line_number in lines:
                dq = line_custs[line_number]
                if dq:
                    customer_id = dq[0]
                    num_processed_items = 1
                service_items(customer_id, line_number, num_processed_items)

        else:
            raise Exception("Malformed input!")
