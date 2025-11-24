class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    """
    Preorder (Прямой обход): Корень -> Левый -> Правый
    """
    result = []

    def traverse(node):
        if node is None:
            return
        result.append(node.val)  # Сначала обрабатываем корень
        traverse(node.left)  # Затем левое поддерево
        traverse(node.right)  # Затем правое поддерево

    traverse(root)
    return result


def inorder_traversal(root):
    """
    Inorder (Центральный обход): Левый -> Корень -> Правый
    """
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)  # Сначала левое поддерево
        result.append(node.val)  # Затем корень
        traverse(node.right)  # Затем правое поддерево

    traverse(root)
    return result


def postorder_traversal(root):
    """
    Postorder (Концевой обход): Левый -> Правый -> Корень
    """
    result = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)  # Сначала левое поддерево
        traverse(node.right)  # Затем правое поддерево
        result.append(node.val)  # В конце корень
    traverse(root)
    return result
# Пример использования
if __name__ == "__main__":
    # Создаем тестовое дерево:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Preorder (К-Л-П):", preorder_traversal(root))  # [1, 2, 4, 5, 3]
    print("Inorder (Л-К-П):", inorder_traversal(root))  # [4, 2, 5, 1, 3]
    print("Postorder (Л-П-К):", postorder_traversal(root))  # [4, 5, 2, 3, 1]
