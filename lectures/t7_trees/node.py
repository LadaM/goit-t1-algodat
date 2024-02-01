class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def preorder_traversal(root: Node):
    if root:
        print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root: Node):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


def postorder_traversal(root: Node):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of binary tree is")
    preorder_traversal(root)

    print("\nInorder traversal of binary tree is")
    inorder_traversal(root)

    print("\nPostorder traversal of binary tree is")
    postorder_traversal(root)
