# -*- coding: utf-8 -*-
"""
tree.py
- Tree (Binary Tree)
- Bst
"""


class Tree():
    """Binary tree"""
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def max_level(self):
        """height of tree"""
        return max(self.left.max_level() if self.left else 0,
                   self.right.max_level() if self.right else 0) + 1

    @classmethod
    def tree(cls):
        """return a demo binary tree"""
        return Tree(1,
                    Tree(2, Tree(4), Tree(3)),
                    Tree(6, Tree(6, Tree(0), Tree(7))))

    @classmethod
    def tree2(cls):
        """return another demo binary tree"""
        return Tree(2,
                    Tree(1, Tree(4), Tree(3)),
                    Tree(5, Tree(6, Tree(0), Tree(7))))

    @classmethod
    def str_node_internal(cls, nodes, level, levels):
        """internal of prints"""
        ret = ''
        if len([x for x in nodes if x is not None]) is 0:
            return ret

        floor = levels - level
        endge_lines = int(pow(2, max(floor - 1, 0)))
        first_spaces = int(pow(2, floor) - 1)
        between_spaces = int(pow(2, floor + 1) - 1)

        ret += first_spaces * ' '

        new_nodes = list()
        for node in nodes:
            if node is not None:
                ret += str(node.data)
                new_nodes.append(node.left)
                new_nodes.append(node.right)
            else:
                ret += ' '
                new_nodes.append(None)
                new_nodes.append(None)

            ret += between_spaces * ' '
        ret += '\n'

        for i in range(1, endge_lines + 1):
            for node in nodes:
                ret += (first_spaces - i) * ' '
                if node is None:
                    ret += ((endge_lines * 2) + i + 1) * ' '
                    continue

                if node.left is not None:
                    ret += '/'
                else:
                    ret += ' '

                ret += (i + i - 1) * ' '

                if node.right is not None:
                    ret += '\\'
                else:
                    ret += ' '

                ret += ((endge_lines * 2) - i) * ' '

            ret += '\n'

        ret += cls.str_node_internal(new_nodes, level + 1, levels)

        return ret

    def __str__(self):
        levels = self.max_level()
        return self.str_node_internal([self], 1, levels)

    def __repr__(self):
        return str(self.data)

    def __len__(self):
        """num of nodes"""
        return ((len(self.left) if self.left else 0) +
                (len(self.right) if self.right else 0) + 1)


class Bst(Tree):
    """Binary Search Tree"""
    def __init__(self, data=None, left=None, right=None):
        Tree.__init__(self, data, left, right)

    @classmethod
    def bst(cls):
        """return demo BST"""
        return Bst(4,
                   Bst(1, Bst(0), Bst(3)),
                   Bst(8, Bst(6, Bst(5), Bst(7))))

    @classmethod
    def bst2(cls):
        """another demo BST"""
        return Tree(4,
                    Tree(3, Tree(0), Tree(3)),
                    Tree(5, None, Tree(7, Tree(6), Tree(9))))

    tree = bst
    tree2 = bst2

    def insert(self, data):
        """insert into BST"""
        if self.data is None:
            self.data = data
            return

        if data > self.data:
            if self.right is None:
                self.right = Bst(data)
                return
            return self.right.insert(data)

        if data <= self.data:
            if self.left is None:
                self.left = Bst(data)
                return
            return self.left.insert(data)

    def find(self, data):
        """find node that
        got data in BST"""
        if self.data == data:
            return self
        elif self.data > data:
            if self.left is not None:
                return self.left.find(data)
        elif self.data < data:
            if self.right is not None:
                return self.right.find(data)
        return None

    def find_node_and_parent(self, data, parent=None):
        """find node and
        parent in bst"""
        if self.data == data:
            return self, parent
        elif self.data > data:
            if self.left:
                return self.left.find_node_and_parent(data, self)
        elif self.data < data:
            if self.right:
                return self.right.find_node_and_parent(data, self)

        return None, None

    def find_max_and_parent(self, parent=None):
        """max val in BST"""
        if self.right:
            return self.right.find_max_and_parent(self)
        return self, parent

    def find_min_and_parent(self, parent=None):
        """min val in BST"""
        if self.left:
            return self.left.find_min_and_parent(self)
        return self, parent

    def delete(self, data):
        """delete node from BST"""
        node, parent = self.find_node_and_parent(data, None)
        if node is None:
            return

        if node.left:
            # replace with just smaller
            can, par = node.left.find_max_and_parent(node)
            new_data = can.data
            if par:
                # delete just smaller
                par.delete(new_data)
            else:
                # left itself is just smaller
                node.left = None
            node.data = new_data
            return

        if node.right:
            can, par = node.right.find_min_and_parent(node)
            new_data = can.data
            if par:
                par.delete(new_data)
            else:
                node.right = None
            node.data = new_data
            return

        # if no children
        if parent is None:
            # root. There is nothing
            node.data = None
            return

        # which child exists?
        if parent.left is node:
            parent.left = None
        else:  # parent.right is node
            parent.right = None
