# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:50:21 2024

@author: gaurav
"""
def is_valid_parentheses(s):
    if not s: return True

    # keep count of open brackets
    # and at the end it must be 0
    opens = 0
    for c in s:
        if c == ')':
            if not opens: return False
            opens -= 1
        else: opens += 1

    return not opens


print(is_valid_parentheses.__name__)
print(is_valid_parentheses('((())())'))
print(is_valid_parentheses('((())()'))
print(is_valid_parentheses('((())'))
print(is_valid_parentheses('(()())'))
print(is_valid_parentheses('((()()()()(((())'))


VALID = {
    ')': '(',
    ']': '[',
    '}': '{',
}


def is_valid_multi_parentheses(s):
    """
    Multiple types of brackets
    Need a stack to keep track
    of the type of parentheses
    """
    if not s: return True

    stack = []
    for c in s:
        if c in ')]}':
            if not stack or stack.pop() != VALID[c]:
                return False
        else:
            stack.append(c)
    return not stack


print(is_valid_multi_parentheses.__name__)
print(is_valid_multi_parentheses('((())())'))
print(is_valid_multi_parentheses('(([])[({{}})])'))
print(is_valid_multi_parentheses('(([])[({{}})])]'))
print(is_valid_multi_parentheses('[(())](([])[({{}})])'))
print(is_valid_multi_parentheses('[(())](([])[({{}})])]'))


def longest_single_parentheses(s):
    if not s: return 0

    # Store the location of all opening
    # brackets and calculate the length
    # on getting a closing one. Get max
    maxim = 0
    stack = []
    for i in range(len(s)):
        if s[i] == ')':
            if not stack: continue
            maxim = max(maxim, i - stack.pop() + 1)
        else:
            stack.append(i)
    return maxim


print(longest_single_parentheses.__name__)
print(longest_single_parentheses(')()())'))
print(longest_single_parentheses(')()())((())((())))'))
print(longest_single_parentheses(')()())((())((())))'))
print(longest_single_parentheses(')())()))'))


def longest_parentheses(s):
    if not s: return 0

    # Store the location of all opening
    # brackets and calculate the length
    # on getting a closing one. In fact
    # keep a number to say when current
    # location started.
    maxim = 0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == ')':
            if not stack: continue

            stack.pop()
            if stack:
                maxim = max(maxim, i - stack[-1])
            else:
                stack.append(i)
        else:
            stack.append(i)
    return maxim


print(longest_parentheses.__name__)
print(longest_parentheses(')()())'))
print(longest_parentheses(')()())((())((())))'))
print(longest_parentheses(')()())((())((())))'))
print(longest_parentheses(')())()))'))


def longest_parentheses_2(s):
    if not s: return 0

    maxim = 0

    # do both left and right
    # directions, in case we
    # missed some in one way
    def one_way(maxim, key='('):
        left, rite = 0, 0
        for c in s:
            if c == key: left += 1
            else:        rite += 1

            if rite > left:
                # as soon as right are
                # more than left, it's
                # not possible to have
                # valid parentheses so
                # reset left and right
                left, rite = 0, 0
            elif left == rite:
                maxim = max(maxim, left + rite)
        return maxim

    maxim = one_way(maxim)
    s = reversed(s)
    maxim = one_way(maxim, ')')

    return maxim


print(longest_parentheses_2.__name__)
print(longest_parentheses_2(')()())'))
print(longest_parentheses_2('(()'))
print(longest_parentheses_2(')()())((())((())))'))
print(longest_parentheses_2('((()()()()(((())'))
print(longest_parentheses_2(')())()))'))
