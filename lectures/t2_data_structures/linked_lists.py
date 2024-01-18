class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def has_next(self):
        return bool(self.next)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_parent(self, node: Node):
        if not self.head or node == self.head:
            return None
        parent = self.head
        while parent.has_next() and parent.next != node:
            parent = parent.next
        if parent.has_next():
            return parent
        return None

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Need to have a node for insert_after operation")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, node: Node, new_data):
        if not node:
            print("Need to have a node for insert_before operation")

        if not self.head or self.head == node:
            self.prepend(new_data)
            return

        parent = self.find_parent(node)
        if parent:
            new_node = Node(new_data)
            parent.next = new_node
            new_node.next = node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key):
        cur: Node = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def print_list(self):
        current = self.head
        while current:
            next_node = current.next
            print(current.data, end=" -> " if next_node else "")
            current = next_node
        print()


if __name__ == "__main__":
    llist = LinkedList()

    # inserting elements in the beginning of the linked list
    llist.prepend(5)
    llist.prepend(10)
    llist.prepend(15)

    # inserting elements at the end of the linked list
    llist.append(20)
    llist.append(25)

    # printing the linked list
    print("Зв'язний список:")
    llist.print_list()

    # deleting a node from the linked list
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # searching an element
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    llist.insert_before(element, 27)
    twenty = llist.search_element(20)
    llist.insert_before(twenty, 99)
    llist.print_list()
