#!/usr/bin/python

class UnorderedSequentialNodeColoring:
    """Find an unordered sequential (US) node coloring.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with nodes (values are colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    """
    # Idea taka jak w 
    # http://edu.i-lo.tarnow.pl/inf/alg/001_search/0142.php

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")

    def run(self):
        """Executable pseudocode."""
        for source in self.graph.iternodes():
            self._greedy_color(source)

    def _greedy_color(self, source):   # a list is faster then a set
        """Give node the smallest possible color."""
        n = self.graph.v()   # memory O(V)
        used = [False] * n   # is color used?
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                used[self.color[target]] = True
        for c in xrange(n):   # check colors
            if not used[c]:
                self.color[source] = c
                break
        return c

# EOF
