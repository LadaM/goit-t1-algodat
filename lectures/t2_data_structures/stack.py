class Stack:
    def __init__(self):
        self.stack = []

    # Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

    # Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]


if __name__ == "__main__":
    s = Stack()
    s.push("a")
    s.push("b")
    s.push("c")
    print(s.peek())  # Output: 'c'
    print(s.pop())  # Output: 'c'
    print(s.peek())  # Output: 'b'
    print(s.is_empty())  # Output: False
