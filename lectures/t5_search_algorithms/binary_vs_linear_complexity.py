import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 50)
linear_search_steps = n
binary_search_steps = np.log2(n)

plt.figure(figsize=(10, 6))
plt.plot(n, linear_search_steps, label="Linear Search", color="blue")
plt.plot(n, binary_search_steps, label="Binary Search", color="green")
plt.xlabel("Elements (n)")
plt.ylabel("Steps")
plt.title("Complexity Comparison of Linear and Binary Search")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
