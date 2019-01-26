# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:50:01 2019

@author: gaurav
"""


class Graph:
    """Graph class"""
    def __init__(self):
        self.adj_list = dict()

    def add_edge(self, i, j=None, weight=1):
        """add edge from i to j
        node. If already exists,
        update weight"""
        if i is not None and j is not None:
            self.adj_list.setdefault(i, dict())[j] = weight

            # make sure we have the j node
            self.adj_list.setdefault(j, dict())

            # in undirected, j points to i too
            if not self.is_directed():
                self.adj_list[j][i] = weight
        elif i is not None:  # empty node i
            self.adj_list.setdefault(i, dict())

    def remove_edge(self, i, j=None):
        """remove edge from i to j"""
        if i is not None and j is not None:
            self.adj_list.setdefault(i, {j: None}).pop(j)
            if not self.is_directed():
                self.adj_list.setdefault(j, {i: None}).pop(i)
        elif i is not None:  # remove node i
            self.adj_list.setdefault(i, None)
            self.adj_list.pop(i)

            # remove i from from all nodes
            for v in self.adj_list.values():
                v.setdefault(i, None)
                v.pop(i)

    def __str__(self):
        return str(self.adj_list)

    __repr__ = __str__

    def __len__(self):
        return len(self.adj_list)

    def __getitem__(self, k):
        return self.adj_list[k]

    def nodes(self):
        """return nodelist"""
        return self.adj_list.keys()

    def edges(self, weights=False):
        """return edges"""
        res = dict()
        seen = set()  # ignore one of two-way undirected nodes
        for k, v in self.adj_list.items():
            for kk, vv in v.items():
                if self.is_directed() or (kk not in seen):
                    # we haven't seen this node yet
                    res[(k, kk)] = vv
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
        return iter(self.adj_list)

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
        graph = cls()
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
        graph = cls()
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
        graph = cls()
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
