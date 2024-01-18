import hashlib
import os

data = "example data"

# Using SHA-256
hashed_data = hashlib.sha256(data.encode())
print(
    hashed_data.hexdigest()
)  # 44752f37272e944fd2c913a35342eaccdd1aaf189bae50676b301ab213fc5061


def get_hash(path):
    """Returns a hash for a file"""
    with open(path, "rb") as file:
        bytes = file.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash


def find_duplicates(directory):
    """Looks for the duplicates in the given directory"""
    hashes = {}
    duplicates = []
    for dir_path, dir_names, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dir_path, filename)
            file_hash = get_hash(path)
            if file_hash not in hashes:
                hashes[file_hash] = path
            else:
                duplicates.append((path, hashes[file_hash]))
    return duplicates


if __name__ == "__main__":
    duplicates = find_duplicates("/path/to/directory")
    for duplicate in duplicates:
        print(f"Duplicates: {duplicate[0]} & {duplicate[1]}")
