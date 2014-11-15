#!/usr/bin/python

import unittest
from edges import Edge
from graphs import Graph
from fleury import FleuryDFS, FleuryBFS

# 0 --- 1     2
# |     |   / |
# |     |  /  |
# |     | /   |
# 3 --- 4 --- 5

class TestFleuryUndirectedGraph(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=False)
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(0, 3), Edge(1, 4),
            Edge(3, 4), Edge(4, 2), Edge(4, 5), Edge(2, 5)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_fleury_dfs(self):
        algorithm = FleuryDFS(self.G)
        algorithm.run(0)
        expected_cycle = [0, 1, 4, 2, 5, 4, 3, 0]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_fleury_bfs(self):
        algorithm = FleuryBFS(self.G)
        algorithm.run()
        expected_cycle = [0, 1, 4, 2, 5, 4, 3, 0]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, FleuryDFS, self.G)
        self.assertRaises(ValueError, FleuryBFS, self.G)

    def tearDown(self): pass

# 0 --o 1     2
# o     |   / o
# |     |  /  |
# |     o o   |
# 3 o-- 4 --o 5

class TestFleuryDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.N = 6           # number of nodes
        self.G = Graph(self.N, directed=True)
        self.nodes = [0, 1, 2, 3, 4, 5]
        self.edges = [Edge(0, 1), Edge(3, 0), Edge(1, 4),
            Edge(4, 3), Edge(2, 4), Edge(4, 5), Edge(5, 2)]
        for node in self.nodes:
            self.G.add_node(node)
        for edge in self.edges:
            self.G.add_edge(edge)

    def test_fleury_dfs(self):
        algorithm = FleuryDFS(self.G)
        algorithm.run()
        expected_cycle = [0, 1, 4, 5, 2, 4, 3, 0]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_fleury_bfs(self):
        algorithm = FleuryBFS(self.G)
        algorithm.run()
        expected_cycle = [0, 1, 4, 5, 2, 4, 3, 0]
        self.assertEqual(len(algorithm.eulerian_cycle), len(self.edges) + 1)
        self.assertEqual(algorithm.eulerian_cycle, expected_cycle)

    def test_eulerian(self):
        self.G.add_edge(Edge(1, 2))
        self.assertRaises(ValueError, FleuryDFS, self.G)
        self.assertRaises(ValueError, FleuryBFS, self.G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
