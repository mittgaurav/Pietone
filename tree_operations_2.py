# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 18:59:02 2019

@author: gaurav
"""
from tree import Tree
import binary_searches as BSGE
from tree import Bst


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


def zigzap_level_order(root):
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


def spiral_print(tree):
    """
          1
       2     3
    4   5   6 7
    8 9 10
    spiral printing: 1 3 2 4 5 6 7 10 9 8

    Q1
    1
    2, 3
    4, 5, 6, 7
    8, 9, 10
    ----

    Q2
    1 - flag = left to right ---- 1
    2, 3 - flag = right to left --- 3 2
    4, 5, 6, 7 - flag = left to right ---- 4 5 6 7
    8, 9, 10 - flag = right to left ----- 10 9 8
    """
    if not tree:
        return

    arr = [tree]
    flag_lr = True

    while arr:
        # we figure out how many elements are
        # at this level. Then, we process all
        # of them. Hence, next time around we
        # will definitely have the next level
        nums = len(arr)
        current = 0
        while current < nums:
            this = arr[current]
            if this.left:
                arr.append(this.left)
            if this.right:
                arr.append(this.right)
            current += 1

        if flag_lr:
            print([_.data for _ in arr[:nums]])
        else:
            print([_.data for _ in reversed(arr[:nums])])

        flag_lr = not flag_lr
        arr = arr[nums:]


print(spiral_print.__name__)
print(T)
spiral_print(T)
print("===========================")
# ==================================
# ==================================


def lca(A, x, y):
    """least common ancestor"""
    if not A:
        return None
    assert x != y

    def inner(n):
        """return two things: the val found
        and whether we are done finding"""
        # if val is set and done is True: parent found
        # if val is set and done is not: child found
        # if val is not: nothing in there
        if not n:
            return (None, False)
        val1, done1 = inner(n.left)
        val2, done2 = inner(n.right)
        if done1:
            return val1, True
        if done2:
            return val2, True
        if val1 and val2:
            return n.data, True

        if not val1 and not val2:
            return (n.data, False) if (n.data == x or n.data == y) \
                else (None, False)

        val1 = val1 if val1 else val2
        return (n.data, True) if (n.data == x or n.data == y) \
            else (val1, False)

    val, done = inner(A)
    return val if done else None


print("least common ancestor")
T.right.data = 10
print(T)
print(lca(T, 2, 10))
print(lca(T, 4, 2))
print(lca(T, 4, 3))
print(lca(T, 0, 1))
print("===========================")
# ==================================
# ==================================


def dfs(node):
    """depth"""
    if not node:
        return

    print(node.data, end=' ')
    dfs(node.left)
    # print(node.data)
    dfs(node.right)
    # print(node.data)


print(T)
print('depth_first_search')
dfs(T)
print()

queue = []


def bfs(node):
    """breadth"""
    if not node:
        return

    queue.append(node)

    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


print('breadth_first_search')
bfs(T)
print()


queue = []


def spiral_print_bfs(node):
    """breadth"""
    if not node:
        return

    queue.append(node)

    forward = True

    while queue:
        # traverse as many times
        # as this level is there
        length_this_level = len(queue)
        i = 0
        while i < length_this_level:
            node = queue.pop(0)
            i += 1
            print(node.data, end=' ')

            first = node.left if forward else node.right
            secon = node.right if forward else node.left
            if first:
                queue.append(first)
            if secon:
                queue.append(secon)

        # we need reversing since
        # after adding in reverse
        # order we need to print.
        forward = not forward
        queue.reverse()


print('==spiral_print_bfs==')
spiral_print_bfs(T)
print()


def in_order_successor_bst(node, data, last_larger=None):
    """return in order successor
    two cases:
        1) node has right child:
            min val in right child
        2) last larger parent"""

    if not node:
        return None

    if node.data > data:
        last_larger = node.data
        return in_order_successor_bst(node.left, data, last_larger)
    elif node.data < data:
        return in_order_successor_bst(node.right, data, last_larger)
    else:
        if node.right:
            # right child exists
            # - find the minimum
            child = node.right
            while child.left:
                child = child.left
            return child.data
        else:
            return last_larger


print('==in_order_successor_bst==')
tree = Bst.bst()
print(tree)
print(tree.inorder())
print(4, in_order_successor_bst(tree, 4))
print(0, in_order_successor_bst(tree, 0))
print(1, in_order_successor_bst(tree, 1))
print(3, in_order_successor_bst(tree, 3))
print(5, in_order_successor_bst(tree, 5))
print(8, in_order_successor_bst(tree, 8))
print(9, in_order_successor_bst(tree, 9))


total = 0


def num_of_paths(tree):
    """find num of paths in a tree.
    for one node, count go through
    v. start/end with the node"""
    global total

    if not tree:
        # what starts at this node
        return 0

    # only ones that start at either child
    # are then ones that can start here +1
    l_t = num_of_paths(tree.left) if tree.left else 0
    r_t = num_of_paths(tree.right) if tree.right else 0

    # go through either children
    # can't go through this node
    l_t = (1 + l_t) if tree.left else 0
    r_t = (1 + r_t) if tree.right else 0
    t = l_t + r_t

    # overall, we need to add both
    # that start here and go thru.
    total += t + (l_t * r_t)

    return t


print('==num_of_paths==')
print(num_of_paths(tree), total)
tree = Bst(4, Bst(2, Bst(1), Bst(3)), Bst(6, Bst(5), Bst(7)))
total = 0
print(tree)
print(num_of_paths(tree), total)


def max_in_levels(tree):
    from collections import deque
    queue = deque()

    result = []
    queue.append(tree)
    while queue:
        size = len(queue)
        result.append(max([q.data for q in queue]))
        for _ in range(size):
            this = queue.popleft()
            if this.left:
                queue.append(this.left)
            if this.right:
                queue.append(this.right)
    return result


print("====", max_in_levels.__name__)
print(T, max_in_levels(T))
print(tree, max_in_levels(tree))
