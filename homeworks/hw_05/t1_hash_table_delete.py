class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        # no key_value pairs stored in the bucket yet
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value  # override value for the same key
                    return True
            self.table[key_hash].append(
                key_value
            )  # append key-value pair if key is different
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def items(self):
        return [pair for bucket in self.table for pair in bucket if pair is not None]

    def delete(self, key):
        key_hash = self.hash_function(key)

        if self.table[key_hash] is None:
            return False
        for i, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                self.table[key_hash].pop(i)
                return True
        return False


if __name__ == "__main__":
    table = HashTable(5)
    table.insert("k1", 10)
    table.insert("k2", 20)
    table.insert("k3", 30)
    table.insert("k4", 40)
    table.insert("k5", 50)
    # Collision - key-value pair will be stored in the same bucket with some other key-value
    table.insert("k6", 60)
    table.insert("k1", 40)  # Overwrite

    # getting the keys
    print(table.get("k1"))
    print(table.get("k6"))

    # getting all keys and values before deleting
    print(table.items())

    if table.delete("k1"):
        print(table.items())

    # removing all keys from the table
    for k, v in table.items():
        table.delete(k)

    print(table.items())
