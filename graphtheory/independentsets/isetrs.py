#!/usr/bin/python

import random

# Tutaj _used i independent_set jest typu set.
class RandomSequentialIndependentSet1:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        self._used = set()
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        node_list = list(self.graph.iternodes())
        random.shuffle(node_list)   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            self._used.add(source)
            self._used.update(self.graph.iteradjacent(source))
        for source in node_list:
            if source in self._used:
                continue
            self.independent_set.add(source)
            self._used.add(source)
            self._used.update(self.graph.iteradjacent(source))
        self.cardinality = len(self.independent_set)


# Tutaj _used jest dict, a independent_set jest typu set.
class RandomSequentialIndependentSet2:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = set()
        self.cardinality = 0
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        node_list = list(self.graph.iternodes())
        random.shuffle(node_list)   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set.add(source)
            self._used[source] = True
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
        for source in node_list:
            if self._used[source]:
                continue
            self.independent_set.add(source)
            self._used[source] = True
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
        self.cardinality = len(self.independent_set)


# Tutaj _used i independent_set jest dict. Wygodne dla C++.
class RandomSequentialIndependentSet3:
    """Find a maximal independent set."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        for edge in self.graph.iteredges():
            if edge.source == edge.target:   # for multigraphs
                raise ValueError("a loop detected")
        self.independent_set = dict((node, False) for node in self.graph.iternodes())
        self.cardinality = 0
        self._used = dict((node, False) for node in self.graph.iternodes())
        self.source = None

    def run(self, source=None):
        """Executable pseudocode."""
        node_list = list(self.graph.iternodes())
        random.shuffle(node_list)   # O(V) time
        if source is not None:
            self.source = source
            self.independent_set[source] = True
            self._used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                self._used[target] = True
        for source in node_list:
            if self._used[source]:
                continue
            self.independent_set[source] = True
            self._used[source] = True
            self.cardinality += 1
            for target in self.graph.iteradjacent(source):
                self._used[target] = True


RandomSequentialIndependentSet = RandomSequentialIndependentSet1

# EOF
