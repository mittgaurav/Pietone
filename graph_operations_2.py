# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:57:19 2019

@author: gaurav
"""
from graph_adj_list import DiGraph
from graph_adj_list import Graph


def has_cycle(graph):
    """Whether graph has cycle.
    A modified DFS that tracks
    visited nodes in current
    iteration."""
    if not graph:
        return False

    visited = set()

    def has_cycle_internal(i, parent=None):
        """Cycles. This function is
        invoked for every node, for
        num of edges time. Thus the
        overall it's O(N * E). There
        does exist a better O(N + E)
        solution that only goes into
        has_cycles_internal if child
        is not already seen. Seen is
        accumulated globally & child
        is popped if got no cycle"""
        visited.add(i)
        for child in graph[i]:
            if child not in visited:
                if has_cycle_internal(child, i):
                    return True
            elif parent != child:
                return True

        return False

    for node in graph:
        if node not in visited:
            if has_cycle_internal(node):
                return True
    return False


FN = has_cycle


def no_parent_nodes(graph):
    """return nodes that don't
    have a parent. It's useful
    to do topological sort."""
    # get all nodes
    out = set(graph.nodes())

    # remove nodes that
    # are pointed to.
    for node in graph.nodes():
        for k in graph[node]:
            out.discard(k)
    return out


FN = no_parent_nodes


def topological_sort(graph):
    """in a DAG, figure out
    the topological sort"""
    # get parent nodes as stack
    # this is list of nodes for
    # traversal, in stack order
    nodes = list(no_parent_nodes(graph))

    sort = list()
    visited = set()
    while nodes:
        node = nodes.pop()
        if node in visited:
            continue
        visited.add(node)
        sort.append(node)
        nodes.extend(graph[node])

    return sort


def topological_sort2(graph):
    """another sort. Totally opposite
    of the first one. Here, we first
    consume leaf nodes, putting them
    in a stack and then keep adding"""
    if not graph:
        return []

    visited = set()
    stack = list()

    def inner(inn):
        """inner"""
        if inn in visited:
            return
        visited.add(inn)

        # first process children
        # no child node added to
        # stack directly first.
        for child in graph[inn]:
            inner(child)
        # once leaves (children)
        # are added to stack, we
        # add itself to stack.
        stack.append(inn)

    for node in graph.nodes():
        inner(node)

    return list(reversed(stack))


def topo_sort(graph):
    """Using BF traversal: first
    gather indegree of each node.
    Then put zero degree parents
    in a queue. and process them.
    While processing them, we're
    decreasing indegree of every
    child of that node. Once the
    child's indegree is zero, it
    can be processed by enqueing
    in the queue & processing it.
    """
    from collections import deque
    if not graph: return []

    # Get indegree of each node
    indegree = {node: 0 for node in graph.nodes()}
    for node in graph.nodes():
        for child in graph[node]:
            indegree[child] += 1

    q = deque()
    # First add all nodes with no parent
    for child, indeg in indegree.items():
        if indeg == 0: q.append(child)

    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for child in graph[node]:
            # as parent node is processed,
            # the child has one less thing
            # to worry about. When nothing
            # remains, we process it
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)

    assert sum(indegree.values()) == 0, "topo sort not possible, cycle?"
    return result


if __name__ == "__main__":
    G = DiGraph.dag()
    G.show()
    for FN in [topological_sort, topological_sort2, topo_sort]:
        print(FN.__name__, FN(G))
    G = DiGraph.graph()
    G.show()
    for FN in [topological_sort, topological_sort2, topo_sort]:
        print(FN.__name__, FN(G))


def krushal(graph):
    """krushal's spanning tree.
    keep picking minimum edge as
    long as it avoids a cycle"""
    from priority_queue import MinHeap

    res = Graph()
    if not graph:
        return res

    def order(arr, parent, child):
        """parent <= child in min heap"""
        return arr[parent][2] <= arr[child][2]

    heap = MinHeap()
    heap.order = order

    for i, j in graph.edges(weights=True).items():
        heap.add((i[0], i[1], j))

    while len(heap) > 0:
        # - take the minimum edge
        # - add it to result graph
        # - remove iff we get cycle
        val = heap.pop()
        res.add_edge(val[0], val[1], val[2])
        if has_cycle(res):
            res.remove_edge(val[0], val[1])

    return res


if __name__ == "__main__":
    print("====", krushal.__name__)
    G = Graph.graphw()
    G.show()
    krushal(G).show()


def shortest_return_no_repeat(s):
    """Given string of NESW direction return
    the shortest path back to starting point
    except for any node or edge of before"""
    from collections import deque

    if not s: return ''

    # Find nodes traversed in onward journey
    # and the ending point. Starts at origin
    visited = set()
    prev = (0, 0)
    for c in s:
        if c == 'N': prev = (prev[0], prev[1] + 1)
        if c == 'S': prev = (prev[0], prev[1] - 1)
        if c == 'E': prev = (prev[0] + 1, prev[1])
        if c == 'W': prev = (prev[0] - 1, prev[1])
        visited.add(prev)

    # We are caching path to this
    # node. This can be performed
    # better with backtracking.
    path = {prev: ''}
    q = deque()
    q.append(prev)
    while q:
        node = q.popleft()
        for i, j, c in [[0, 1, 'N'], [0, -1, 'S'], [-1, 0, 'W'], [1, 0, 'E']]:
            next = (node[0] + i, node[1] + j)
            # This node is already visited
            # either in onward journey, or
            # In this traversal.
            if next in visited: continue
            path[next] = path[node] + c
            if next == (0, 0):
                return path[next]
            q.append(next)
            visited.add(next)
    return 'ERROR'

[["EZE","HBA"],["AXA","TIA"],

 ["TIA","AUA"],["ADL","EZE"],

 ["AUA","AXA"],

 ]


def shortest_return_no_repeat_backtrack(s):
    """Given string of NESW direction return
    the shortest path back to starting point
    except for any node or edge of before"""
    from collections import deque

    if not s: return ''

    # Find nodes traversed in onward journey
    # and the ending point. Starts at origin
    visited = set()
    prev = (0, 0)
    for c in s:
        if c == 'N': prev = (prev[0], prev[1] + 1)
        if c == 'S': prev = (prev[0], prev[1] - 1)
        if c == 'E': prev = (prev[0] + 1, prev[1])
        if c == 'W': prev = (prev[0] - 1, prev[1])
        visited.add(prev)

    def backtrack(parent, next):
        if not parent: return ''
        s = ''
        while next in parent:
            diff = (next[0] - parent[next][0], next[1] - parent[next][1])
            if diff == (0, 1): s += 'N'
            if diff == (0, -1): s += 'S'
            if diff == (1, 0): s += 'E'
            if diff == (-1, 0): s += 'W'
            next = parent[next]

        return "".join(reversed(s))

    parent = {}
    q = deque()
    q.append(prev)
    while q:
        node = q.popleft()
        for i, j, c in [[0, 1, 'N'], [0, -1, 'S'], [-1, 0, 'W'], [1, 0, 'E']]:
            next = (node[0] + i, node[1] + j)
            if next in visited: continue
            parent[next] = node
            if next == (0, 0):
                return backtrack(parent, next)
            q.append(next)
            visited.add(next)

    return 'ERROR'


print(shortest_return_no_repeat('NNNENW'))
print(shortest_return_no_repeat_backtrack('NNNENW'))
print(shortest_return_no_repeat('NENWNENWNWNENWNEN'))
print(shortest_return_no_repeat_backtrack('NENWNENWNWNENWNEN'))
