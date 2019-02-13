# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 18:59:02 2019

@author: gaurav
"""
from tree import Tree
import binary_search_ge as BSGE


def deepest_node(tree, depth=0):
    """find the deepest node;
    i.e. farthest from root"""
    if not tree:
        return None, depth

    L = r = tree
    d_l = d_r = 0
    if tree.left:
        L, d_l = deepest_node(tree.left, depth)
    if tree.right:
        r, d_r = deepest_node(tree.right, depth)

    node, depth = (L, d_l) if d_l >= d_r else (r, d_r)
    return node, depth + 1


T = Tree.tree()
T.right.left.right.left = Tree(9)
print(deepest_node.__name__)
print(T)
print(deepest_node(T))
print("===========================")
# ==================================
# ==================================


def tree_from_post_order(postorder):
    """construct a BST from post
    order traversal. We know the
    last elem is root. Left and
    right values are separately
    together. Separate left and
    right elems by determining
    root's place. Recurse"""
    if not postorder:
        return None

    data = postorder.pop()
    node = Tree(data)

    # There was only one node
    if not postorder:
        return node

    loc, _ = BSGE.binary_search_ge(postorder, data)

    # there is no right
    if loc == -1:
        loc = len(postorder)

    node.left = tree_from_post_order(postorder[:loc])
    node.right = tree_from_post_order(postorder[loc:])

    return node


print(tree_from_post_order.__name__)
print(tree_from_post_order([2, 4, 3, 6, 9, 8, 5]))
print(tree_from_post_order([8, 7, 6, 50, 40, 10]))
print(tree_from_post_order([1, 7, 5, 50, 40, 10]))
print("===========================")
# ==================================
# ==================================


def nodes_between_levels(tree, lev1=0, lev2=0):
    """find node between
    given two levels."""
    if not tree:
        return None

    queue = list()
    queue.append(tree)

    level = -1
    vals = list()
    while queue:
        level += 1
        num = len(queue)
        while num > 0:
            node = queue.pop(0)
            if lev1 <= level <= lev2:
                vals.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            num -= 1
    return vals


print(nodes_between_levels.__name__)
T = Tree.tree()
print(T)
print(nodes_between_levels(T, 0, 8))
print(nodes_between_levels(T, 1, 1))
print(nodes_between_levels(T, 2, 3))
print("===========================")
# ==================================
# ==================================


def vertical_order(tree, order=0):
    """nodes in vertical order"""
    if not tree:
        return {}

    indents = {order: [tree]}
    for k, v in vertical_order(tree.left, order-1).items():
        indents.setdefault(k, []).extend(v)
    for k, v in vertical_order(tree.right, order+1).items():
        indents.setdefault(k, []).extend(v)

    return indents


print(vertical_order.__name__)
T = Tree.tree()
print(T)
print(vertical_order(T))
print("===========================")
# ==================================
# ==================================


def link_level_nodes(tree):
    """link nodes at a level
    to next at same level"""
    if not tree:
        return

    class NewTree(Tree):
        """next link"""
        def __init__(self, tree):
            super(NewTree, self).__init__(tree.data,
                                          tree.left, tree.right)
            self.next = None

        def __str__(self):
            return str(self.data) + " -> " + str(self.next)

    queue = list()
    queue.append(tree)

    while queue:
        num = len(queue)
        prev = None
        first = None  # for printing
        while num:
            node = NewTree(queue.pop(0))
            if prev:
                prev.next = node
            else:
                first = node
            prev = node
            num -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(first)


print(link_level_nodes.__name__)
T = Tree.tree()
print(T)
link_level_nodes(T)
print("===========================")
# ==================================
# ==================================


def zigzap_level_order(root: 'TreeNode') -> 'List[List[int]]':
    """left, right, left, right..."""
    result = []
    queue = [root]
    l_to_r = True
    while queue:
        L = len(queue)
        arr = []
        for i in range(L):
            # Have to pop either
            # from left or right
            node = queue.pop(0 if l_to_r else L - i - 1)
            arr.append(node.data)

            if not l_to_r and node.left:
                # if popped from l to r
                # children are r to l
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if l_to_r and node.left:
                queue.append(node.left)
        l_to_r = not l_to_r
        result.append(arr)
    return result


print(zigzap_level_order.__name__)
print(T)
print(zigzap_level_order(T))
print("===========================")
# ==================================
# ==================================