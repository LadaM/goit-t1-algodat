from avl_tree import AVLTree, Node


def sum_up_tree_keys(tree: AVLTree):
    """
    Sums up the keys of a binary search tree that has numeric keys
    """
    # if the tree is empty
    if not tree or not tree.root:
        return 0

    return (
        tree.root.key
        + sum_up_node_keys(tree.root.left)  # sum up left subtree
        + sum_up_node_keys(tree.root.right)  # sum up right subtree
    )


def sum_up_node_keys(node: Node):
    if not node:
        return 0
    return node.key + sum_up_node_keys(node.left) + sum_up_node_keys(node.right)


if __name__ == "__main__":
    empty_tree = AVLTree()
    print(
        "The sum of the keys in the empty tree is =", sum_up_tree_keys(empty_tree)
    )  # should be 0

    one_node_tree = AVLTree()
    one_node_tree.insert_key(10)
    print(
        "The sum of the keys in the tree with one node is =",
        sum_up_tree_keys(one_node_tree),
    )  # should be 10

    large_tree = AVLTree()
    keys = [-50, 1000, 10, 20, 30, 40, 50, 25, -1, 99, 0, 61, -500]
    for key in keys:
        large_tree.insert_key(key)

    print("The sum of the keys in the tree is =", sum_up_tree_keys(large_tree))
