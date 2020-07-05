# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:24:03 2020

@author: gaurav
"""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


ERROR = None


def input_check(str):
    global ERROR
    allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(i) != 5:
        ERROR = 'E1'
    elif i[0] != '(' or i[-1] != ')':
        ERROR = 'E1'
    elif i[2] != ',':
        ERROR = 'E1'
    elif i[1] not in allowed or i[3] not in allowed:
        ERROR = 'E1'
    elif i[1] == i[3]:
        ERROR = 'E1'
    else:
        return True
    return False


def print_tree(node):
    if not node:
        return
    print('(', end='')
    print(node.value, end='')

    # children - already sorted
    print_tree(node.left)
    print_tree(node.right)

    print(')', end='')


nodes_map = {}


INPUT = input().split(' ')
for i in INPUT:
    if not input_check(i):
        # highest error
        break
    par, child = i[1], i[3]

    par_node = nodes_map.setdefault(par, TreeNode(par))
    child_node = nodes_map.setdefault(child, TreeNode(child))

    # duplicate pair
    if child_node.parent and child_node.parent.value == par:
        ERROR = 'E2'

    if not par_node.left:
        par_node.left = child_node
    elif not par_node.right:
        par_node.right = child_node

        # lexicographically sorted
        if par_node.left.value > par_node.right.value:
            par_node.left, par_node.right = par_node.right, par_node.left
    else:
        # parent already has two children
        if not ERROR or ERROR > 'E3':
            ERROR = 'E3'

    if child_node.parent:
        if not ERROR or ERROR > 'E4':
            ERROR = 'E4'

    child_node.parent = par_node

# continue iff all is fine
if not ERROR:
    # cycle and root identification
    # one and only one node with None parent
    roots = [x for x in nodes_map.values() if not x.parent]

    if len(roots) == 0:
        ERROR = 'E4'
    elif len(roots) > 1:
        ERROR = 'E5'
    else:  # no errors
        root = roots[0]
        print_tree(root)

if ERROR:
    print(ERROR)
