# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 19:45:13 2018

Print Tree's outer boundary
from right to left nodes.

@author: gaurav
"""
from tree import Tree


def lower_boundary(tree):
    """leaf nodes right to left"""
    output = list()
    if not tree:
        return output

    stack = list()
    stack.append(tree)
    while stack:
        node = stack.pop()

        if (not node.left) or (not node.right):
            output.append(node)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return output


def left_nodes_backward(tree):
    """left nodes from child to parent"""
    output = list()
    if not tree:
        return output

    queue = list()
    queue.append(tree)
    while queue:
        node = queue.pop(0)
        output.append(node)

        if node.left:
            queue.append(node.left)
    output.reverse()
    return output


def right_nodes(tree):
    """right nodes from root"""
    output = list()
    if not tree:
        return output

    queue = list()
    queue.append(tree)
    while queue:
        node = queue.pop(0)
        output.append(node)

        if node.right:
            queue.append(node.right)
    return output


t = Tree.tree()
print(t)

leaves = lower_boundary(t)
left_nodes = left_nodes_backward(t)
right_nodes = right_nodes(t)

# The last and first nodes are duplicated
print(right_nodes + leaves[1:-1] + left_nodes)
