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
        node = nodes.pop(0)
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
        for child in graph[inn]:
            inner(child)
        stack.append(inn)

    for node in graph.nodes():
        inner(node)

    return list(reversed(stack))


if __name__ == "__main__":
    G = DiGraph.dag()
    G.show()
    for FN in [topological_sort, topological_sort2]:
        print(FN.__name__, FN(G))
    G = DiGraph.graph()
    G.show()
    for FN in [topological_sort, topological_sort2]:
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
