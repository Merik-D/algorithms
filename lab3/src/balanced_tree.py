class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    def height(node: BinaryTree):
        if node is None:
            return False
        left = height(node.left)
        right = height(node.right)
        if abs(left - right) > 1:
            return False

        return max(left, right) + 1

    return bool(height(node))
