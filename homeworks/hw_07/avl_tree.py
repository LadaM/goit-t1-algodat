class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        """
        Calculates the balance factor of the node that represents
        a difference in the hight of the left and right subtrees.
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, node):
        left = node.left  # the root of the left subtree
        temp = left.right

        left.right = node
        node.left = temp

        self.update_height(node)
        self.update_height(left)

        return left

    def rotate_left(self, node):
        right = node.right  # the root of the right subtree
        temp = right.left

        right.left = node
        node.right = temp

        self.update_height(node)
        self.update_height(right)

        return right

    def insert(self, root, key):
        """
        Insert a key into the binary search tree rooted at the given node.
        Args:
            root: The root of the binary search tree.
            key: The key to be inserted into the binary search tree.
        Returns:
            The updated root of the binary search tree after insertion.
        """
        # Base Case
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)
        balance = self.balance_factor(root)

        # Re-balancing the tree
        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def print_tree(self, root, level=0, prefix="Root: "):
        if root:
            print(" " * (level * 4) + prefix + str(root.key))
            if root.left or root.right:
                self.print_tree(root.left, level + 1, "L--- ")
                self.print_tree(root.right, level + 1, "R--- ")

    def display(self):
        self.print_tree(self.root)


if __name__ == "__main__":
    avl_tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25, -1, 99, 0, 61]

    for key in keys:
        avl_tree.insert_key(key)
        print(f"Inserted key: {key}, tree hight: {avl_tree.height(avl_tree.root)}")

    avl_tree.display()
