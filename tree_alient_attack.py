# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:25:07 2018

Two ways of doing it:
    a) create another data
structure that has pointer
to parent node. Do BFS on
all nodes keeping track of
each level. Number of such
levels is the time taken.

    b) For each node from
root till attack node, get
the maximum depth of other
leg. That plus time taken
to reach till that leg is
time to finish that leg.
also consider the height
from current node. Max of
all these is time taken.

@author: gaurav
"""
from tree import Tree
from tree_operations import find_path


def alien_attack(tree, node):
    """how long it will take aliens
    to spread all over the state"""
    if not tree or not node:
        return 0
    if tree is node:
        # attack at root
        return tree.max_level()

    class Etree():
        """Tree with pointer to parent"""
        def __init__(self, tr, parent=None):
            self.data = tr.data
            self.left = Etree(tr.left, self) if tr.left else None
            self.right = Etree(tr.right, self) if tr.right else None
            self.parent = parent

        def find(self, node):
            """Find tree node. We
            just check data and if
            tree's got duplicates,
            it gives any of them"""
            if self.data == node.data:
                return self
            return ((self.right.find(node) if self.right else None)
                    or
                    (self.left.find(node) if self.left else None))

    etree = Etree(tree)
    node = etree.find(node)
    assert node  # must not be none

    time = 0  # or -1, max_level - 1
    visited = dict()
    queue = list()
    queue.append(node)
    while len(queue) is not 0:
        level_length = len(queue)
        time += 1
        while level_length > 0:
            # consume a level together
            this = queue.pop(0)
            for x in [this.left, this.right, this.parent]:
                if x and x not in visited:
                    # not visited yet
                    queue.append(x)
            visited[this] = 0
            level_length -= 1

    return time


def attack_no_parent(tree, node):
    """No parent pointer"""
    if not tree or not node:
        return 0
    if tree is node:
        # attack at root
        return tree.max_level()

    # path from root to attack
    path = find_path(tree, node)
    if len(path) is 0:
        return 0

    # time to traverse tree
    # rooted at attack node
    start = path.pop()
    time = start.max_level()

    # for each node in path
    # from root, find depth
    # of other leg and also
    # time to reach the leg
    i = 2  # attack, parent
    while len(path) > 0:
        this = path.pop()

        # The other child of parent
        other = this.right if this.left == start else this.left
        if other:
            time = max(time, i + other.max_level())
        i += 1
        start = this

    return time


t = Tree.tree()
t.right.right = Tree(0, Tree(0, Tree(1, Tree(4))))
print(t)
for fun in [alien_attack, attack_no_parent]:
    print(fun.__name__)
    print(repr(t.left.right), ':', fun(t, t.left.right))
    print(repr(t.left), ':', fun(t, t.left))
    print(repr(t.right), ':', fun(t, t.right))
    print(repr(t.right.left.right), ':', fun(t, t.right.left.right))
