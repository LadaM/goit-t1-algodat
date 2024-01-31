from avl_tree import AVLTree, Node


def find_the_largest_element_in_BST(tree):
    """
    Finds the largest element of a binary search tree
    """
    # if the tree is empty
    if not tree:
        return None

    node: Node = tree.root  # the root of the tree
    while node.right:
        node = node.right

    return node.key


if __name__ == "__main__":
    tree = AVLTree()
    keys = [-50, 1000, 10, 20, 30, 40, 50, 25, -1, 99, 0, 61]

    for key in keys:
        tree.insert_key(key)

    print(
        "The largest element in the tree is = ", find_the_largest_element_in_BST(tree)
    )
