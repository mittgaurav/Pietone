# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:40:22 2019

@author: gaurav
"""


class Graph:
    """Graph class"""
    def __init__(self, size):
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.insert(i, [0] * size)

    def add_edge(self, i, j=None, weight=1):
        """add edge from i to j
        node. If already exists,
        update weight"""
        if i is not None and j is not None:
            assert i < len(self) and j < len(self)
            self.adj_matrix[i][j] = weight
            # in undirected, j points to i too
            if not self.is_directed():
                self.adj_matrix[j][i] = weight

    def remove_edge(self, i, j=None):
        """remove edge from i to j"""
        if i is not None and j is not None:
            self.adj_matrix[i][j] = 0
            if not self.is_directed():
                self.adj_matrix[j][i] = 0
        elif i is not None:  # remove node i
            self.adj_matrix[i] = [0] * len(self)

            # remove i from from all nodes
            for v in self.adj_matrix:
                v[i] = 0

    def __str__(self):
        return str(self.adj_matrix)

    def __repr__(self):
        return repr(self.adj_matrix)

    def __len__(self):
        return len(self.adj_matrix)

    def __getitem__(self, i):
        return self.adj_matrix[i]

    def nodes(self):
        """return nodelist"""
        return list(range(len(self.adj_matrix)))

    def edges(self, weights=False):
        """return edges"""
        res = dict()
        seen = set()  # ignore one of two-way undirected nodes
        for k in range(len(self)):
            for v in range(len(self.adj_matrix[k])):
                if self.is_directed() or (v not in seen):
                    # we haven't seen this node yet
                    if self.adj_matrix[k][v]:
                        res[(k, v)] = self.adj_matrix[k][v]
            seen.add(k)
        return res if weights else res.keys()

    @classmethod
    def is_directed(cls):
        """is graph directed"""
        return False

    @classmethod
    def is_multigraph(cls):
        """multiple edges between
        two nodes"""
        return False

    def __iter__(self):
        return iter(range(len(self.adj_matrix)))

    prev_pos = None

    def show(self):
        """show using mathplot"""
        import matplotlib.pyplot as plt
        import networkx as nx
        import warnings
        import matplotlib.cbook as mpc
        warnings.filterwarnings("ignore",
                                category=mpc.mplDeprecation)

        # Replace with spring layout
        # which is clearly prettier,
        # cuter, & less error-prone.
        pos = nx.random_layout(self)  # positions for all nodes

        if self.prev_pos and self.prev_pos.keys() == pos.keys():
            pos = self.prev_pos
        else:
            self.prev_pos = pos

        # nodes
        nx.draw_networkx_nodes(self, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(self, pos)

        # labels
        nx.draw_networkx_labels(self, pos, font_size=20)

        # edge weights
        nx.draw_networkx_edge_labels(self, pos,
                                     self.edges(weights=True))

        plt.xticks([])
        plt.yticks([])
        plt.show()

    @classmethod
    def graph(cls):
        """unweighted graph"""
        graph = cls(5)
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        return graph

    @classmethod
    def graphw(cls):
        """weighted graph"""
        graph = cls(5)
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        return graph


class DiGraph(Graph):
    """directed graph"""
    @classmethod
    def is_directed(cls):
        """directed graph"""
        return True

    @classmethod
    def dag(cls):
        """"Directed acyclic
        graph"""
        graph = cls(6)
        graph.add_edge(5, 0)
        graph.add_edge(5, 2)
        graph.add_edge(4, 0)
        graph.add_edge(4, 1)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)
        return graph


if __name__ == "__main__":
    for CLS in [Graph, DiGraph]:
        print(CLS.__name__)
        G = CLS.graph()
        G.show()
        G.remove_edge(1, 3)
        G.show()
        G.remove_edge(3)
        G.remove_edge(1)
        G.show()
