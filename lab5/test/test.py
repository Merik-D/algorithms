import unittest

from lab5.src.career import build_graph, max_experience


class TestMaxExperience(unittest.TestCase):
    def test1(self):
        levels = [
            [1],
            [2, 3],
            [4, 5, 6]
        ]
        graph = build_graph(levels)
        self.assertEqual(max_experience(graph, levels), 10)

    def test2(self):
        levels = [
            [5],
            [10, 2],
            [1, 8, 3],
            [6, 7, 9, 4]
        ]
        graph = build_graph(levels)
        self.assertEqual(max_experience(graph, levels), 32)

    def test3(self):
        levels = [
            [9999]
        ]
        graph = build_graph(levels)
        self.assertEqual(max_experience(graph, levels), 9999)

    def test4(self):
        levels = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        graph = build_graph(levels)
        self.assertEqual(max_experience(graph, levels), 12)

if __name__ == '__main__':
    unittest.main()
