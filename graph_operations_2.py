# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:57:19 2019

@author: gaurav
"""
from graph_adj_list import DiGraph
from graph_adj_list import Graph


def has_cycle(graph):
    """Whether the graph has cycle. A modified DFS
    that tracks visited nodes in current iteration."""
    if not graph:
        return False

    visited = set()

    def has_cycle_internal(i, parent=None):
        """Cycles. This function is invoked for every node, for num
        of edges time. Thus the overall, O(N * E). There does exist
        a better O(N + E) solution that calls internal fn only when
        child is not already seen. Seen is accumulated globally and
        child is popped if got no cycle"""
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
    """return nodes without a parent.
    It's useful for topological sort."""
    # get all nodes
    out = set(graph.nodes())

    # remove nodes that are pointed to.
    for node in graph.nodes():
        for k in graph[node]:
            out.discard(k)
    return out


FN = no_parent_nodes


def topological_sort(graph):
    """in a DAG, figure out topological sort"""
    # get parent nodes as stack this is list
    # of nodes for traversal, in stack order
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
    """Another sort. Entirely opposite to the first one. Here, we first
    consume leaf nodes, putting them in a stack and then keep adding"""
    if not graph:
        return []

    visited = set()
    stack = list()

    def inner(inn):
        """inner"""
        if inn in visited:
            return
        visited.add(inn)

        # first process children so no child
        # node added to stack directly first
        for child in graph[inn]:
            inner(child)
        # once leaves (children) are added
        # to stack, we add itself to stack
        stack.append(inn)

    for node in graph.nodes():
        inner(node)

    return list(reversed(stack))


def topo_sort(graph):
    """Using BF traversal: first gather indegree of each node.
    Then put zero degree parents in a queue. and process them.
    While processing them, we're decreasing indegree of every
    child of that node. Once the child's indegree is zero, it
    can be processed by enqueing in the queue & processing it.
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

    assert q, "topo sort not possible as no node without incoming node"

    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for child in graph[node]:
            # As parent node is processed, child has one fewer parent to
            # depend upon. When all parents are processed, we process it
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
    """Krushal's spanning tree. Keeps picking
    minimum edge as long as it avoids a cycle"""
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

    # We're caching the path to this node.
    # Can be performant with backtracking.
    path = {prev: ''}
    q = deque()
    q.append(prev)
    while q:
        node = q.popleft()
        for i, j, c in [[0, 1, 'N'], [0, -1, 'S'], [-1, 0, 'W'], [1, 0, 'E']]:
            next = (node[0] + i, node[1] + j)
            # This node is already visited in either
            # onwards journey, or in this traversal.
            if next in visited: continue
            path[next] = path[node] + c
            if next == (0, 0):
                return path[next]
            q.append(next)
            visited.add(next)
    return 'ERROR'


def shortest_return_no_repeat_backtrack(s):
    """Given string of NESW direction, gives the shortest path back
    to the starting point without taking any node/edge of before"""
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

    # backtrack generates the path
    # instead of storing it inline
    def backtrack(parents, next):
        if not parents: return ''
        s = ''
        while next in parents:
            diff = (next[0] - parents[next][0], next[1] - parents[next][1])
            if diff == (0, 1): s += 'N'
            if diff == (0, -1): s += 'S'
            if diff == (1, 0): s += 'E'
            if diff == (-1, 0): s += 'W'
            next = parents[next]

        return "".join(reversed(s))

    def backtrack2(parents, next):
        if next not in parents: return ''
        s = ''
        diff = (next[0] - parents[next][0], next[1] - parents[next][1])
        if diff == (0, 1): s += 'N'
        if diff == (0, -1): s += 'S'
        if diff == (1, 0): s += 'E'
        if diff == (-1, 0): s += 'W'
        return backtrack2(parents, parents[next]) + s

    parents = {}
    q = deque()
    q.append(prev)
    while q:
        node = q.popleft()
        for i, j, c in [[0, 1, 'N'], [0, -1, 'S'], [-1, 0, 'W'], [1, 0, 'E']]:
            next = (node[0] + i, node[1] + j)
            if next in visited: continue
            parents[next] = node
            if next == (0, 0):
                # reached (0,0), so backtrack
                # to generate the entire path
                assert backtrack(parents, next) == backtrack2(parents, next)
                return backtrack2(parents, next)
            q.append(next)
            visited.add(next)

    return 'ERROR'


print("====", shortest_return_no_repeat.__name__)
print(shortest_return_no_repeat('NNNENW'))
print(shortest_return_no_repeat_backtrack('NNNENW'))
print(shortest_return_no_repeat('NENWNENWNWNENWNEN'))
print(shortest_return_no_repeat_backtrack('NENWNENWNWNENWNEN'))


def find_alphabet_order_from_dict(words):
    """Given a sorted dictionary of words from an alien
    langauge. Determine the lexic-order of alphabets"""
    from collections import deque, defaultdict

    if not words: return ""
    if len(words) == 1: return words[0][0]

    no_parent_chars = set()
    indegree = defaultdict(lambda: set())
    outdegree = defaultdict(lambda: set())

    prev = words[0]
    for word in words[1:]:
        i, j = 0, 0
        while i < len(prev) and j < len(word):
            if prev[i] == word[j]:
                # Both chars are same. Hence, add to
                # the no_parent and move to next one
                if word[j] not in indegree:
                    no_parent_chars.add(word[j])
                i += 1
                j += 1
            else: # prev[i] < word[j]
                # This connection can be added
                if word[j] in no_parent_chars:
                    no_parent_chars.remove(word[j])
                if prev[i] not in outdegree:
                    outdegree[prev[i]] = set()
                if prev[i] not in no_parent_chars and prev[i] not in indegree:
                    no_parent_chars.add(prev[i])
                outdegree[prev[i]].add(word[j])
                if word[j] not in indegree:
                    indegree[word[j]] = set()
                indegree[word[j]].add(prev[i])
                break

        # if the two words are of different length
        # but all chars match till one is consumed
        # then the next in longer has no parent.
        if i == len(prev) and word[j] not in indegree:
            no_parent_chars.add(word[j])
        elif j == len(word)  and prev[i] not in indegree:
            no_parent_chars.add(prev[i])

        prev = word

    if len(no_parent_chars) != 1:
        return ""

    # topological sorting based on in and outdegree
    result = ""
    q = deque()
    q.append(no_parent_chars.pop())
    while q:
        char = q.popleft()
        result += char
        for child in outdegree[char]:
            if child in indegree:
                indegree[child].remove(char)
            if not indegree[child]:
                q.append(child)

    return result


FN = find_alphabet_order_from_dict
print("====", FN.__name__)
print("wertf", FN(["wrt", "wrf", "er", "ett", "rftt"]))
print("zx", FN(["z", "x"]))
print("", FN(["z", "x", "z"]))
print("", FN(["ab", "abc"]))
print("bdac", FN(["baa", "abcd", "abca", "cab", "cad"]))
print("cab", FN(["caa", "aaa", "aab"]))
print("xywz", FN(["xyz", "xwz", "wxy", "wyz"]), "should be xyw")
print("abcd", FN(["a", "b", "c", "d"]))
print("abcde", FN(["abc", "bcd", "cde", "dac", "decc", "ded", "dee"]))
print("xyz", FN(["x", "y", "z"]))
print("acb", FN(["ac", "ab", "b"]), "could be be cb")
print("abc", FN(["ab", "ac", "b"]))
print("acb", FN(["ac", "ab", "c"]))
