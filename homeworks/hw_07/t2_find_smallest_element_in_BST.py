from avl_tree import AVLTree, Node


def find_smallest_element_in_BST(tree):
    """
    Finds the smallest element of a binary search tree
    """
    # if the tree is empty
    if not tree:
        return None

    node: Node = tree.root  # the root of the tree
    while node.left:
        node = node.left

    return node.key


if __name__ == "__main__":
    tree = AVLTree()
    keys = [-50, 1000, 10, 20, 30, 40, 50, 25, -1, 99, 0, 61]

    for key in keys:
        tree.insert_key(key)

    print(
        "The smallest element in the tree is = ",
        find_smallest_element_in_BST(tree)
    )
