from node import Node


class BinarySearchTree:
    root: Node = None

    def __init__(self, root_key: int = None):
        if root_key:
            self.root = Node(root_key)

    def __str__(self, level=0, prefix="Root: ", node=None):
        if node is None:
            node = self.root
        if node is None:  # if the tree is empty
            return ""
        ret = "\t" * level + prefix + str(node.val) + "\n"
        if node.left:
            ret += self.__str__(level + 1, prefix="L--- ", node=node.left)
        if node.right:
            ret += self.__str__(level + 1, prefix="R--- ", node=node.right)
        return ret

    def search(self, key):
        current = self.root
        while current is not None and current.val != key:
            if key < current.val:
                current = current.left
            else:
                current = current.right
        return current

    def insert(self, key: int, node: Node = None):
        """
        Insert a new node with the given key into the binary tree.
        Parameters:
            key (int): The value of the new node.
            node (Node): The node where the new node will be inserted.
        """
        if node is None and self.root is None:
            self.root = Node(key)
        elif node is None:
            self.insert(key, self.root)
        else:
            if key < node.val:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.insert(key, node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self.insert(key, node.right)

    def min_value_node(self, curr_node=None):
        if curr_node is None:
            curr_node = self.root
        if curr_node is None:  # if the tree is empty
            return None
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node


if __name__ == "__main__":
    tree = BinarySearchTree(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    print(tree)

    print(tree.min_value_node().val)

    tree.delete(5)
    print(tree)
