# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:57:19 2019

@author: gaurav
"""
from graph_adj_list import DiGraph


def has_cycle(graph):
    """Whether graph has cycle.
    A modified DFS that tracks
    visited nodes in current
    iteration."""
    if not graph:
        return False

    visited = set()

    def has_cycle_internal(i):
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
        for child in graph[i]:
            if child in seen:
                return True
            if has_cycle_internal(child):
                return True
            seen.add(child)
        return False

    for node in graph:
        seen = set()
        if node not in visited:
            if has_cycle_internal(node):
                return True
            visited.add(node)
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
