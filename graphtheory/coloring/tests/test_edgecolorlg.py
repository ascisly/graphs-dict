#!/usr/bin/python

import unittest
from graphtheory.structures.edges import Edge
from graphtheory.structures.graphs import Graph
from graphtheory.coloring.edgecolorlg import EdgeColoringWithLineGraph

#     a     d
#  0 --- 1 --- 2 
#  |   / |   / |  4 colors (best)
# c| b/ c| b/ c|
#  | /   | /   |
#  3 --- 4 --- 5
#     d     a

class TestEdgeColoring(unittest.TestCase):

    def setUp(self):
        self.N = 6
        self.G = Graph(self.N)
        self.nodes = range(self.N)
        self.edges = [
            Edge(0, 1), Edge(0, 3), Edge(1, 3), Edge(1, 4), Edge(1, 2), 
            Edge(2, 4), Edge(2, 5), Edge(3, 4), Edge(4, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)
        #self.G.show()

    def test_line_graph_coloring(self):
        algorithm = EdgeColoringWithLineGraph(self.G)
        algorithm.run()
        for edge in self.G.iteredges():
            self.assertNotEqual(algorithm.color[edge], None)
        for node in self.G.iternodes():
            color_set = set()
            for edge in self.G.iteroutedges(node):
                if edge.source > edge.target:
                    color_set.add(algorithm.color[~edge])
                else:
                    color_set.add(algorithm.color[edge])
            self.assertEqual(len(color_set), self.G.degree(node))
        #print algorithm.color
        all_colors = set(algorithm.color[edge] for edge in self.G.iteredges())
        self.assertEqual(len(all_colors), 4)

    def test_exceptions(self):
        self.assertRaises(ValueError, EdgeColoringWithLineGraph,
            Graph(5, directed=True))

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF