def build_shift_table(pattern):
    """Create a table of shifts for Boyer-Moore search"""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    # Creating a table of shifts for pattern (substring)
    shift_table = build_shift_table(pattern)
    i = 0  # start index for the main text

    # Iterating over the main text
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # start at the end of the pattern

        # Comparing pattern with the substring starting from the end
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # If the characters match, decrement j

        # If the whole pattern is matched
        if j < 0:
            return i  # we found the pattern at index i

        # Shifting the index using the shift table
        # This allows to jump to the next possible occurrence of the pattern
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # If pattern is not found, return -1
    return -1


if __name__ == "__main__":
    test_text = "Being a developer is not easy"
    search_pattern = "developer"

    position = boyer_moore_search(test_text, search_pattern)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")
