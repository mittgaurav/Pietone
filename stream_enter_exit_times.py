# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:22:48 2019

@author: gaurav
"""
import random
from datetime import datetime
from binary_searches import binary_search_greater, binary_search_ge

STREAMS = [  # user id - step - time - enter?
    (10, 1, datetime(2014, 4, 11, 8, 0), True),
    (12, 1, datetime(2014, 4, 11, 8, 5), True),
    (10, 1, datetime(2014, 4, 11, 8, 5), False),
    (13, 1, datetime(2014, 4, 11, 8, 5), True),
    (14, 1, datetime(2014, 4, 11, 8, 10), True),
    (10, 2, datetime(2014, 4, 11, 8, 10), True),
    (13, 1, datetime(2014, 4, 11, 8, 11), False),
    (12, 1, datetime(2014, 4, 11, 8, 12), False),
    (15, 1, datetime(2014, 4, 11, 8, 12), True),
    (13, 2, datetime(2014, 4, 11, 8, 15), True),
    (15, 1, datetime(2014, 4, 11, 8, 20), False),
    (10, 2, datetime(2014, 4, 11, 8, 30), False),
    (15, 2, datetime(2014, 4, 11, 8, 30), True),
    (12, 2, datetime(2014, 4, 11, 8, 32), True),
    (12, 2, datetime(2014, 4, 11, 8, 32), False),
    (13, 2, datetime(2014, 4, 11, 8, 40), False),
    (15, 2, datetime(2014, 4, 11, 8, 45), False),
    ]


def get_avg_time_spent():
    """calculate average time
    spent in each step"""
    curr_step_start = {}
    curr_step = {}
    avg_times = {}
    for s in STREAMS:
        user, step, time, enter = s

        if not enter:  # exiting. collect time for it
            time_taken = time - curr_step_start[user]
            if step not in avg_times:
                count = 1
            else:  # have seen this step. acccumulate
                time_taken += avg_times[step][0] * avg_times[step][1]
                count = avg_times[step][1] + 1
            avg_times[step] = (time_taken / count, count)

        # where is my user?
        curr_step[user] = step if enter else None
        curr_step_start[user] = time

    print("avg_time:", avg_times)
    print("cur_step:", curr_step)


print("====", get_avg_time_spent.__name__)
get_avg_time_spent()
print("=======================")

# Given logs of start and end
# times of users logins, find
# how many users were online
# at a given instant of time
BEGIN = 0
END = 100
TIMES = []
for _ in range(END // 2):
    start = random.randint(BEGIN, END)
    end = random.randint(start, END)
    TIMES.append((start, end))
# for the sake of reproducibility
TIMES = [(2, 94), (4, 13), (6, 48), (10, 65), (11, 14),
         (16, 73), (16, 37), (16, 86), (18, 19), (19, 72),
         (19, 27), (20, 53), (26, 54), (27, 43), (29, 69),
         (31, 55), (36, 96), (36, 44), (39, 82), (40, 67),
         (44, 78), (50, 56), (54, 59), (56, 85), (56, 69),
         (61, 94), (61, 61), (62, 65), (66, 76), (67, 94),
         (70, 86), (70, 86), (71, 83), (73, 84), (73, 84),
         (75, 83), (75, 77), (77, 80), (77, 94), (80, 83),
         (81, 97), (82, 83), (84, 92), (88, 100), (89, 89),
         (90, 98), (91, 98), (93, 100), (93, 100), (98, 100)]


def online_at_given_time(t):
    """num of users online
    at a given time"""
    starts = sorted(map(lambda x: x[0], TIMES))
    ends = sorted(map(lambda x: x[1], TIMES))

    # how many have entered till now.
    # people entering right now are also in
    enters = binary_search_greater(starts, t)
    enter = enters[0] if enters[0] != -1 else len(starts)

    # how many have exited till now.
    # people exiting right now are still in
    exits = binary_search_ge(ends, t)
    exitt = exits[0] if exits[0] != -1 else len(ends)

    return enter - exitt


print(sorted(TIMES, key=lambda x: x[0]))
print("==", online_at_given_time.__name__)
print(0, online_at_given_time(0))
print(10, online_at_given_time(10))
print(9, online_at_given_time(9))
print(49, online_at_given_time(49))
print(100, online_at_given_time(100))
print(101, online_at_given_time(101))
print("=======================")


def online_at_any_time():
    """num of users online
    at any time. cached"""
    starts = sorted(map(lambda x: x[0], TIMES))
    ends = sorted(map(lambda x: x[1], TIMES))

    statuses = [0] * (END + 1)
    for i in range(BEGIN, END + 1):
        if i > 0:
            statuses[i] = statuses[i-1]
        while starts and starts[0] == i:
            statuses[i] += 1
            starts.pop(0)

        while ends and ends[0] == i-1:
            statuses[i] -= 1
            ends.pop(0)

    assert [print(x, y) for x, y in zip(list(range(1, END)), statuses)]
    return lambda t: statuses[t]


print("==", online_at_any_time.__name__)
online_at_given_time = online_at_any_time()
print(0, online_at_given_time(0))
print(10, online_at_given_time(10))
print(9, online_at_given_time(9))
print(49, online_at_given_time(49))
print(100, online_at_given_time(100))
# print(101, online_at_given_time(101))
print("=======================")
