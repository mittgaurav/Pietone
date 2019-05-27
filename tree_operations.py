# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:31:32 2018

@author: gaurav
"""
from tree import Tree, Bst


def double_each_node(tree):
    """each node as left child"""
    if tree is None:
        return
    double_each_node(tree.left)
    double_each_node(tree.right)
    new = Tree(tree.data, tree.left)
    tree.left = new


FUNC = double_each_node
# ==================================
# ==================================


def mirror_spin_tree(tree):
    """mirror children"""
    if tree is None:
        return

    # swap left and right
    node = tree.right
    tree.right = tree.left
    tree.left = node

    mirror_spin_tree(tree.left)
    mirror_spin_tree(tree.right)


FUNC = mirror_spin_tree

if __name__ == "__main__":
    print(FUNC.__name__)
    T = Bst.tree2()
    print(T)
    FUNC(T)
    print(T)
    print("=======================")
# ==================================
# ==================================


def is_bst(tree, i=-999999, j=99999):
    """Whether given tree is a BST.
    Defines the limit for each node
    by dictating the possible values
    between parent and either limit:
    -inf for left and inf for right"""
    if tree is None:
        return True
    if tree.data < i or tree.data > j:
        return False
    return (is_bst(tree.left, i, tree.data) and
            is_bst(tree.right, tree.data, j))


if __name__ == "__main__":
    print(is_bst.__name__)
    T = Bst.tree()
    print(T, "is bst:", is_bst(T))

    T = Bst.bst2()
    print(T, "is bst:", is_bst(T))
    T = Tree.tree()
    print(T, "is bst:", is_bst(T))
    T = Tree.tree2()
    print(T, "is bst:", is_bst(T))
    print("=======================")
# ==================================
# ==================================


def preorder(tree):
    """preorder with stack"""
    output = list()
    if tree is None:
        return output

    stack = list()
    stack.append(tree)
    while stack:
        node = stack.pop()
        output.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return output


if __name__ == "__main__":
    print(preorder.__name__)
    print(T, preorder(T))
    print("=======================")
# ==================================
# ==================================


def find_path(tree, data):
    """find path till a node or value"""
    output = list()
    if tree is None or data is None:
        return output

    # DFS
    stack = list()
    stack.append(tree)

    # A parent whose both
    # children don't have
    # the data, has to be
    # removed from path.
    # Track all children,
    # and check parent.
    visited = dict()
    visited[None] = 0
    while stack:
        node = stack.pop()
        output.append(node)
        if data in (node, node.data):
            return output
        visited[node] = 0

        # To remove useless nodes and
        # parents with such children.
        while output:
            # if the node is not data
            # & has no child, remove.
            # if the node is not data
            # and has left/right seen,
            # remove and go to parent.
            cand = output[-1]
            if cand.right in visited and cand.left in visited:
                output.pop()
            else:  # some leg unseen.
                break

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return list()


def find_path_2(tree, data):
    """find path to a data"""
    if tree is None or data is None:
        return list()

    if data in (tree, tree.data):
        return [tree]
    path = find_path_2(tree.left, data)
    if path:
        return [tree] + path
    path = find_path_2(tree.right, data)
    if path:
        return [tree] + path

    return list()


def find_path_3_internal(tree, data, curr_path):
    """yet another find path"""
    if tree is None or data is None:
        return False

    curr_path.append(tree)
    if data in (tree, tree.data):
        return True

    if find_path_3_internal(tree.left, data, curr_path):
        return True
    if find_path_3_internal(tree.right, data, curr_path):
        return True
    curr_path.pop()

    return False


def find_path_3(tree, data):
    """yet another find path"""
    curr_path = []
    find_path_3_internal(tree, data, curr_path)
    return curr_path


if __name__ == "__main__":
    print("==== find path")
    T = Tree.tree()
    print(T)
    for FP in [find_path, find_path_2, find_path_3]:
        print("==", FP.__name__)
        print(3, FP(T, 3))
        print(7, FP(T, 7))
        print(0, FP(T, 0))
        print(6, FP(T, T.right.left))
        print(6, FP(T, T.right))

    T = Tree.tree2()
    print(T)
    for FP in [find_path, find_path_2, find_path_3]:
        print("==", FP.__name__)
        print(3, FP(T, 3))
        print(7, FP(T, 7))
        print(0, FP(T, 0))
        print(6, FP(T, T.right.left))
        print(5, FP(T, T.right))

    T.right.right = Tree(9, Tree(8, Tree(10)))
    print(T)
    for FP in [find_path, find_path_2, find_path_3]:
        print("==", FP.__name__)
        print(1, FP(T, 1))
        print('*', FP(T, '*'))
        print(9, FP(T, 9))
        print(8, FP(T, 8))
        print(10, FP(T, 10))
    print("=======================")
# ==================================
# ==================================


def num_elems_below(tree, i):
    """count less than i,
    minimum steps as possible"""
    if not tree:
        return 0

    if tree.data <= i:
        return (1 +
                num_elems_below(tree.left, i) +
                num_elems_below(tree.right, i))
    # tree.data > i
    return num_elems_below(tree.left, i)


if __name__ == "__main__":
    print(num_elems_below.__name__)
    T = Bst.tree()
    print(T)
    print(8, num_elems_below(T, 8))
    print(2, num_elems_below(T, 2))
    print(3, num_elems_below(T, 2))
    print(5, num_elems_below(T, 5))
    print("=======================")
# ==================================
# ==================================


def elems_in_range(tree, i, j):
    """print all vals in BST
    between given values.
    Result is sorted with as
    few nodes as possible"""
    vals = []
    if not tree:
        return vals

    if tree.data >= i:
        vals.extend(elems_in_range(tree.left, i, j))
    if i <= tree.data <= j:
        vals.append(tree)
    if tree.data <= j:
        vals.extend(elems_in_range(tree.right, i, j))
    return vals


def num_elems_in_range(tree, i, j):
    """count between two nums,
    incuding the nums. We can
    either use the above algo
    to determine all elems and
    then len() or one below.
    The below one is actually
    another view of above"""
    if not tree:
        return 0

    if i <= tree.data <= j:
        return (1 +
                num_elems_in_range(tree.left, i, j) +
                num_elems_in_range(tree.right, i, j))
    if tree.data < i:
        return num_elems_in_range(tree.right, i, j)
    # tree.data > j:
    return num_elems_in_range(tree.left, i, j)


def subtrees_in_range(tree, i, j, count=0):
    """How many subtrees of
    the tree have all nodes
    within a range?"""
    if not tree:
        return True, count

    # If a node is within a
    # range and its children
    # either don't exist or
    # are within range.
    left = right = False
    c_l = c_r = 0
    if tree.data >= i:
        left, c_l = subtrees_in_range(tree.left, i, j, count)
    if tree.data <= j:
        right, c_r = subtrees_in_range(tree.right, i, j, count)

    if left and right:
        return True, 1 + c_l + c_r
    return False, c_l + c_r


if __name__ == "__main__":
    T = Bst.tree()
    print(T)
    print(num_elems_in_range.__name__)
    print([2, 8], num_elems_in_range(T, 2, 8))
    print([3, 4], num_elems_in_range(T, 3, 4))
    print([0, 0], num_elems_in_range(T, 0, 0))
    print()
    print(elems_in_range.__name__)
    print([2, 8], elems_in_range(T, 2, 8))
    print([3, 4], elems_in_range(T, 3, 4))
    print([0, 0], elems_in_range(T, 0, 0))
    print()
    print(subtrees_in_range.__name__)
    print([2, 8], subtrees_in_range(T, 2, 8)[1])
    print("=======================")
# ==================================
# ==================================


def has_path_from_root_with_sum(tree, val):
    """whether tree has a path
    which sums to given val.
    Returns path from root"""
    if not tree:
        # if ask is 0, we are good
        return val == 0

    val -= tree.data
    return (has_path_from_root_with_sum(tree.left, val) or
            has_path_from_root_with_sum(tree.right, val))


if __name__ == "__main__":
    print(has_path_from_root_with_sum.__name__)
    T = Tree.tree()
    print(T)
    print(10, has_path_from_root_with_sum(T, 10))
    print(13, has_path_from_root_with_sum(T, 13))
    print(7, has_path_from_root_with_sum(T, 7))
    print(9, has_path_from_root_with_sum(T, 9))
    print(5, has_path_from_root_with_sum(T, 5))
    print("=======================")


def downward_paths_with_sum(tree, val, paths, curr_path):
    """[[has_path_from_root_with_sum]]
    with any node as root node"""
    if not tree:
        return

    # go top to down and accumulate
    # current path. Then, check for
    # all possible paths whether we
    # achieved the required sum.
    curr_path.append(tree.data)

    path_sum = 0
    for i in range(len(curr_path)-1, -1, -1):
        path_sum += curr_path[i]
        if path_sum == val:
            paths.append(curr_path[i:])

    downward_paths_with_sum(tree.left, val, paths, curr_path)
    downward_paths_with_sum(tree.right, val, paths, curr_path)

    curr_path.pop()


if __name__ == "__main__":
    print(downward_paths_with_sum.__name__)
    T = Tree(1, Tree(3, Tree(2), Tree(1, None, Tree(1))),
             Tree(-1, Tree(4, Tree(1), Tree(2)), Tree(5, None, Tree(6))))
    print(T)

    paths = []
    downward_paths_with_sum(T, 5, paths, [])
    print(paths)
    print("=======================")


def maximum_path_sum(tree):
    """find the maximum sum of
    a path in a tree"""
    def inner(tree, max_max=0):
        if not tree:
            return 0, 0

        left, max1 = inner(tree.left, max_max)
        right, max2 = inner(tree.right, max_max)

        # at each node, two things to consider
        # what should be sent up, and
        # what is the overall maximum
        max_send_up = max(tree.data, left + tree.data, right + tree.data)
        max_max = max(max_max, max1, max2,
                      max_send_up, left + tree.data + right)

        return max_send_up, max_max

    return inner(tree)[1]


if __name__ == "__main__":
    print(maximum_path_sum.__name__)
    T = Tree(1, Tree(3, Tree(2), Tree(1, None, Tree(1))),
             Tree(-1, Tree(4, Tree(1), Tree(2)), Tree(5, None, Tree(6))))
    print(T)

    print(maximum_path_sum(T))
    print(maximum_path_sum(T.right))
    print(maximum_path_sum(T.left))

    T = Tree(-3, Tree(-2), Tree(-1, None, Tree(-1)))
    print(T)
    print(maximum_path_sum(T))
    print("=======================")


def move_coins(tree):
    """given total n coins among
    n nodes, how many moves will
    be done to have one coin on
    each node"""
    if not tree:
        return 0, 0
    left_discrepancy, left_steps = move_coins(tree.left)
    right_discrepancy, right_steps = move_coins(tree.right)

    # discrepancy is the difference
    # that this node gives or takes
    # from its parent
    discrepancy = left_discrepancy + right_discrepancy + tree.data - 1
    steps = abs(discrepancy) + left_steps + right_steps
    return discrepancy, steps


if __name__ == "__main__":
    print(move_coins.__name__)
    T = Tree(0, Tree(1, Tree(3)), Tree(1, None, Tree(0)))
    print(T)
    print(move_coins(T))
