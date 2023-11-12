import unittest

from lab3.src.balanced_tree import BinaryTree, is_tree_balanced


class TestIsTreeBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        self.assertEqual(is_tree_balanced(root), True)

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        self.assertEqual(is_tree_balanced(root), False)

    def test_empty_tree(self):
        self.assertEqual(is_tree_balanced(None), False)
    #
    def test_single_node_tree(self):
        root = BinaryTree(1)
        self.assertEqual(is_tree_balanced(root), True)


if __name__ == '__main__':
    unittest.main()
