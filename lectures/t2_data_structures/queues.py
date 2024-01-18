from queue import Queue

# Створюємо чергу
q = Queue()

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

print(q.queue) # Output: deque(['a', 'b', 'c'])

# Видаляємо елемент
q.get()
print(q.queue) # Output: deque(['b', 'c'])

# Створюємо чергу з максимальним розміром
q_limited = Queue(maxsize = 3)

# Перевіряємо, чи черга порожня
print(q_limited.empty()) # Output: True

# Додаємо елементи
q_limited.put('a')
q_limited.put('b')
q_limited.put('c')

# Перевіряємо, чи черга повна
print(q_limited.full()) # Output: True

# Перевіряємо розмір черги
print(q_limited.qsize()) # Output: 3

# Видаляємо елементи
print(q_limited.get()) # Output: 'a'
print(q_limited.get()) # Output: 'b'