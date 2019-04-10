# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:22:48 2019

@author: gaurav
"""
from datetime import datetime

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


get_avg_time_spent()
