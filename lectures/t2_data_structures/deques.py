from collections import deque

d = deque()
print(d)  # deque([])

# adding elements is efficient for both left and right side
d.append('right')
d.appendleft('left')
print(d)  # deque(['left', 'right'])

# getting elements from the beginning or the end is also very efficient
d.pop()
d.popleft()
print(d)  # deque([])

# extending the deque with multiple elements
d.extend(['a', 'b', 'c'])
d.extendleft(['x', 'y', 'z'])
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

# rotation moves elements by n positions 
d.rotate(2)
print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

d.rotate(-2)
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])


# the size of the deque can be limited
deque_of_3 = deque(maxlen=3)
deque_of_3.extend([1, 2, 3])
print(deque_of_3)  # deque([1, 2, 3])
deque_of_3.append(4)
print(deque_of_3)  # deque([2, 3, 4])