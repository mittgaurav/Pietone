# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:19:19 2019

@author: gaurav
"""
from graph_adj_list import Graph, DiGraph


def dfs(graph):
    """Graph's depth first traversal.
    Traverse from a node in one path
    as long as the it keeps on going.
    We keep track of visited nodes to
    avoid cyles."""
    if not graph:
        return

    visited = set()

    def dfs_internal(node=0):
        """internal"""
        if node in visited:
            return
        print(node, end=" ")
        visited.add(node)

        for link in graph[node]:
            dfs_internal(link)

    dfs_internal()

    # disconnected nodes
    # and paths therein.
    for node in graph.nodes():
        if node not in visited:
            dfs_internal(node)
    print("")


FS = dfs


def bfs(graph):
    """Breadth first traversal.
    Visit all children of node
    and then visit each child.
    Keep track of all visited
    nodes to avoid cyles."""
    if not graph:
        return

    visited = set()
    queue = list()

    def bfs_internal(node=0):
        """internal"""
        queue.append(node)
        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            print(node, end=" ")

            for k in graph[node]:
                queue.append(k)

    bfs_internal()

    # disconnected nodes
    for node in graph.nodes():
        if node not in visited:
            bfs_internal(node)

    print("")


FS = bfs


def dfs_stack(graph):
    """Depth first traversal.
    Stack and no recursion"""
    if not graph:
        return

    visited = set()
    stack = list()

    def dfs_internal(node=0):
        """internal"""
        stack.append(node)
        while stack:
            node = stack.pop()
            if node in visited:
                continue

            print(node, end=" ")
            visited.add(node)
            for link in graph[node]:
                stack.append(link)

    dfs_internal()

    # disconnected nodes
    for node in graph.nodes():
        if node not in visited:
            dfs_internal(node)

    print("")


FS = dfs_stack

if __name__ == "__main__":
    print(FS.__name__)
    G = Graph.graph()
    G.show()
    FS(G)
    G.remove_edge(1, 2)
    G.show()
    FS(G)
    G.remove_edge(2, 3)
    G.remove_edge(0, 4)
    G.show()
    FS(G)
    print("=======================")
# ==================================
# ==================================


def find_path(graph, i, j):
    """return path from i to j.
    Not necessarily the shortest
    path. But path nonetheless"""
    path = list()
    if not graph:
        return path

    if i not in graph or j not in graph:
        return path

    # To keep track of nodes whose
    # children are processed or in
    # the process. We add nodes to
    # path and remove after every
    # child is processed; bit like
    # find path fn in binary trees
    visited = set()

    def find_path_internal(i, j):
        """internal"""
        path.append(i)
        if i == j:
            return True

        visited.add(i)
        for child in graph[i]:
            if child in visited:
                # child is either already processed
                # as a parent or in the process of.
                continue
            if find_path_internal(child, j):
                return True
        path.pop()
        return False

    find_path_internal(i, j)

    visited = set()

    def find_path_internal_2(i, j):
        """internal"""
        if i == j:
            return [i]

        visited.add(i)
        for child in graph[i]:
            if child in visited:
                # child is either already processed
                # as a parent or in the process of.
                continue
            childpath = find_path_internal_2(child, j)
            if childpath:
                return [i] + childpath
        return []

    new_path = find_path_internal_2(i, j)
    assert path == new_path

    return path


FP = find_path


def find_all_paths(graph, i, j):
    """find all paths between nodes"""
    paths = list()
    if not graph:
        return paths
    if i not in graph or j not in graph:
        return paths

    # Track nodes that are
    # visited in this path.
    # Keep the others for
    # other paths. As DFS
    # means we track this
    # path to end first.
    visited = set()

    def find_internal(i, j):
        """internal"""
        visited.add(i)

        mypaths = list()
        if i == j:
            mypaths.append([i])
        for child in graph[i]:
            if child in visited:
                continue

            childpaths = find_internal(child, j)
            if childpaths:
                for path in childpaths:
                    path.insert(0, i)
                mypaths.extend(childpaths)
            # remove child node that
            # was added in internal.
            # We may revisit it via
            # another parent later.
            visited.remove(child)
        return mypaths

    return find_internal(i, j)


FP = find_all_paths


def find_min_path(graph, i, j):
    """Find path with fewest nodes.
    THIS IS NOT DIJKSTRA'S ALGORITHM
    which involves weighted edges"""
    path = list()
    if not graph:
        return path

    if i not in graph or j not in graph:
        return path

    visited = set()
    queue = list()
    parent = dict()

    def bfs_internal(node=0):
        """internal"""
        queue.append(node)
        visited.add(node)
        while queue:
            node = queue.pop(0)
            if node == j:
                return True

            for k in graph[node]:
                if k not in visited:
                    # shouldn't overwrite
                    # parent if parent is
                    # already known as it
                    # is already shortest
                    parent[k] = node
                    visited.add(k)
                    queue.append(k)
        return False

    if not bfs_internal(i):
        return path

    # Construct path from parents. j exists
    # and we made sure to have the shortest
    # path's parent in the parent structure
    while j in parent:
        path.insert(0, j)
        j = parent[j]
    path.insert(0, i)  # i's parent not there

    return path


FP = find_min_path

if __name__ == "__main__":
    print(FP.__name__)
    for CLS in [Graph, DiGraph]:
        print(CLS.__name__)
        G = CLS.graph()
        G.show()
        print(0, 1, FP(G, 0, 1))
        print(0, 0, FP(G, 0, 0))
        print(0, 4, FP(G, 0, 4))
        print(2, 4, FP(G, 2, 4))
        G.remove_edge(0, 1)
        G.remove_edge(1, 4)
        print(2, 4, FP(G, 2, 4))

        G = CLS()
        G.add_edge(0, 1)
        G.add_edge(0, 2)
        G.add_edge(1, 3)
        G.add_edge(3, 4)
        G.add_edge(4, 5)
        G.show()
        print(0, 5, FP(G, 0, 5))

        G = CLS()
        G.add_edge(0, 1)
        G.add_edge(0, 2)
        G.add_edge(2, 8)
        G.add_edge(8, 9)
        G.add_edge(9, 11)
        G.add_edge(11, 5)
        G.add_edge(5, 2)
        G.show()
        print(0, 5, FP(G, 0, 5))
    print("=======================")
# ==================================
# ==================================


def solve_word_straight(matrix, word):
    """find if a word exists in a matrix"""
    if not matrix or not matrix[0] or not word : return None

    rows = len(matrix)
    cols = len(matrix[0])
    first = word[0]
    sols = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == first:
                found = True
                for k in range(len(word)):
                    if j + k >= cols or matrix[i][j+k] != word[k]:
                        found = False
                        break

                if found:
                    sols.append(matrix[i][j:j+k+1])
                found = True
                for k in range(len(word)):
                    if i + k >= rows or matrix[i+k][j] != word[k]:
                        found = False
                        break

                if found:
                    sols.append(''.join([_[j] for _ in matrix[i:i+k+1]]))
    return sols or f"{word} NOT FOUND"


def solve_word_snakewise(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    first = word[0]

    visited = set()
    def dfs(x, y, tosee):
        if tosee == len(word):
            return True
        if (x, y) in visited:
            return False
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if matrix[x][y] != word[tosee]:
            return False

        visited.add((x, y))
        res = dfs(x+1, y, tosee+1) \
            or dfs(x, y+1, tosee+1) \
            or dfs(x-1, y, tosee+1) \
            or dfs(x, y-1, tosee+1)
        visited.remove((x, y))
        return res


    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == first:
                visited = set()
                tosee = 0
                if dfs(i, j, tosee):
                    return word, True

    return word, False


matrix = [
"face",
"book",
"moot",
"bake",
]


for solve_word in (solve_word_straight, solve_word_snakewise):
    print(solve_word(matrix, "face"))
    print(solve_word(matrix, "cook"))
    print(solve_word(matrix, "boots"))
    print(solve_word(matrix, "fate"))
    print(solve_word(matrix, "booa"))
    print(solve_word(matrix, "oo"))
    print(solve_word(matrix, "boot"))
    print(solve_word(matrix, "booot"))
    print(solve_word(matrix, "boooot"))
    print(solve_word(matrix, "booook"))
    print(solve_word(matrix, "boooook"))
    print(solve_word(matrix, "facoot"))
