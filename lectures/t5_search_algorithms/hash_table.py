class HashTable:
    def __init__(self, size):
        self.size = size
        self.__table = [[] for _ in range(self.size)]

    def __str__(self):
        return str(self.__table)

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.__table[key_hash] is None:
            self.__table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.__table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.__table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.__table[key_hash] is not None:
            for pair in self.__table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


if __name__ == "__main__":
    fruits = HashTable(5)
    fruits.insert("apple", 10)
    fruits.insert("orange", 20)
    fruits.insert("banana", 30)
    print(fruits)
    print(fruits.get("apple"))
    print(fruits.get("orange"))
    print(fruits.get("banana"))
