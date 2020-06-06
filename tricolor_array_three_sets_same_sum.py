# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

choices = ['R', 'G', 'B']
RESULT = 'impossible'


def is_stable(A, result):
    # let's check if this array is stable
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(A)):
        if result[i] == 'R':
            s1 += A[i]
        elif result[i] == 'G':
            s2 += A[i]
        elif result[i] == 'B':
            s3 += A[i]

    return s1 == s2 and s1 == s3


def solve(A, result, i):
    global RESULT

    if i == len(A):
        # goal
        # this can be easily modified
        # to count number of solution
        if is_stable(A, result):
            RESULT = result
            return True
    else:
        # choice
        for c in choices:
            result = result[:i] + c + result[i+1:]
            if solve(A, result, i+1):
                return True
    return False


def solution(A):
    # basically break array into three sets
    # such that their sums are equal.
    # max 18 elements - hence 18C3 combinations
    s = sum(A)

    individual_sum = s / 3

    # sum is not divisible by 3
    if s // 3 != individual_sum:
        return RESULT

    # we may still not find a solution
    # as breakup of array is remaining
    result = 'R' * len(A)
    if individual_sum == 0:
        return result

    solve(A, result, 0)

    return RESULT


print(solution([2, 5, 3, 4, 7]))
RESULT = 'impossible'
print(solution([1, 2, 3, 4, 5, 6, 7]))
RESULT = 'impossible'
print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
