import random

class UniversalHash:
    def __init__(self, size, max_key):
        self.size = size
        self.prime = self._next_prime(max_key)
        self.a = random.randint(1, self.prime - 1)
        self.b = random.randint(0, self.prime - 1)

    def _next_prime(self, n):
        while True:
            n += 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                return n

    def hash(self, key):
        return ((self.a * key + self.b) % self.prime) % self.size


if __name__ == "__main__":
    hasher = UniversalHash(100, 1000)
    print(hasher.hash(123))
    print(hasher.hash(456))
    