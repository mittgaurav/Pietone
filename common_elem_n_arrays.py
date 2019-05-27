# -*- coding: utf-8 -*-
"""
Created on Tue May 28 02:00:55 2019

@author: gaurav
"""


def common_elem_in_n_sorted_arrays(arrays):
    """find the common elements in
    n sorted arrays without using
    extra memory"""
    if not arrays:
        return []

    result = []
    first = arrays[0]
    for i in first:  # for each element
        are_equal = True

        # match first arr's elements
        # with each arrays' elements
        # and based on whether first
        # element is ==, >, or <, we
        # take appropriate step. And
        # if all match, store elem.
        for array in arrays[1:]:
            if not array:
                # any array has been consumed
                return result
            if i == array[0]:
                array.pop(0)
            elif i > array[0]:
                # bring array up to level of first
                while array and array[0] < i:
                    array.pop(0)
                # somehow array does have that elem
                if array and array[0] == i:
                    array.pop(0)
                else:
                    are_equal = False
            else:  # first[i] < array[0]
                # first is smaller, break
                # and take the next first
                are_equal = False
                break

        if are_equal:
            result.append(i)

    return result


ARR = [
        [10, 160, 200, 500, 500],
        [4, 150, 160, 170, 500],
        [2, 160, 200, 202, 203],
        [3, 150, 155, 160, 300],
        [3, 150, 155, 160, 301]
        ]

print(common_elem_in_n_sorted_arrays(ARR))

ARR = [
        [23, 24, 34, 67, 89, 123, 566, 1000, 1224],
        [11, 22, 23, 24, 33, 37, 185, 566, 987, 1223, 1224, 1234],
        [23, 24, 43, 67, 98, 566, 678, 1224],
        [1, 4, 5, 23, 24, 34, 76, 87, 132, 566, 665, 1224],
        [1, 2, 3, 23, 24, 344, 566, 1224]
        ]

print(common_elem_in_n_sorted_arrays(ARR))
