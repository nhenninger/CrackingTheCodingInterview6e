import unittest
from nodes import GraphNode
from q04_01_route_between_nodes import (route_between_nodes_dfs,
                                        route_between_nodes_bfs)


class TestQ04_01RouteBetweenNodes(unittest.TestCase):

    # 0----->1<-----2<-
    # |\__   |\____   |
    # v   |  v     v  |
    # 5   -->4<----3---

    def setUp(self):
        self.head = GraphNode(0)
        self.n1 = GraphNode(1)
        self.n2 = GraphNode(2)
        self.n3 = GraphNode(3)
        self.n4 = GraphNode(4)
        self.n5 = GraphNode(5)
        self.head.children = [self.n1, self.n4, self.n5]
        self.n1.children = [self.n3, self.n4]
        self.n2.children = [self.n1]
        self.n3.children = [self.n2, self.n4]

    def test_route_between_nodes0(self):
        self.assertTrue(route_between_nodes_dfs(self.head, self.n4))

    def test_route_between_nodes1(self):
        self.assertFalse(route_between_nodes_dfs(self.n4, self.head))

    def test_route_between_nodes2(self):
        self.assertTrue(route_between_nodes_dfs(self.head, self.n3))

    def test_route_between_nodes3(self):
        self.assertFalse(route_between_nodes_dfs(self.n3, self.head))

    def test_route_between_nodes4(self):
        self.assertTrue(route_between_nodes_dfs(self.head, self.n2))

    def test_route_between_nodes5(self):
        self.assertFalse(route_between_nodes_dfs(self.n2, self.head))

    def test_route_between_nodes6(self):
        self.assertFalse(route_between_nodes_dfs(self.n5, self.n4))

    def test_route_between_nodes7(self):
        self.assertFalse(route_between_nodes_dfs(self.n4, self.n5))

    def test_route_between_nodes8(self):
        self.assertFalse(route_between_nodes_dfs(self.n5, self.n1))

    def test_route_between_nodes9(self):
        self.assertFalse(route_between_nodes_dfs(self.n1, self.n5))

    def test_route_between_nodes10(self):
        self.assertFalse(route_between_nodes_dfs(self.n5, self.n2))

    def test_route_between_nodes11(self):
        self.assertFalse(route_between_nodes_dfs(self.n2, self.n5))

    def test_route_between_nodes12(self):
        self.assertFalse(route_between_nodes_dfs(self.n5, self.n3))

    def test_route_between_nodes13(self):
        self.assertFalse(route_between_nodes_dfs(self.n3, self.n5))

    def test_route_between_nodes14(self):
        self.assertTrue(route_between_nodes_bfs(self.head, self.n4))

    def test_route_between_nodes15(self):
        self.assertFalse(route_between_nodes_bfs(self.n4, self.head))

    def test_route_between_nodes16(self):
        self.assertTrue(route_between_nodes_bfs(self.head, self.n3))

    def test_route_between_nodes17(self):
        self.assertFalse(route_between_nodes_bfs(self.n3, self.head))

    def test_route_between_nodes18(self):
        self.assertTrue(route_between_nodes_bfs(self.head, self.n2))

    def test_route_between_nodes19(self):
        self.assertFalse(route_between_nodes_bfs(self.n2, self.head))

    def test_route_between_nodes20(self):
        self.assertFalse(route_between_nodes_bfs(self.n5, self.n4))

    def test_route_between_nodes21(self):
        self.assertFalse(route_between_nodes_bfs(self.n4, self.n5))

    def test_route_between_nodes22(self):
        self.assertFalse(route_between_nodes_bfs(self.n5, self.n1))

    def test_route_between_nodes23(self):
        self.assertFalse(route_between_nodes_bfs(self.n1, self.n5))

    def test_route_between_nodes24(self):
        self.assertFalse(route_between_nodes_bfs(self.n5, self.n2))

    def test_route_between_nodes25(self):
        self.assertFalse(route_between_nodes_bfs(self.n2, self.n5))

    def test_route_between_nodes26(self):
        self.assertFalse(route_between_nodes_bfs(self.n5, self.n3))

    def test_route_between_nodes27(self):
        self.assertFalse(route_between_nodes_bfs(self.n3, self.n5))


if __name__ == '__main__':
    unittest.main()
