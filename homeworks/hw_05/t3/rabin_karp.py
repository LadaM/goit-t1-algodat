def polynomial_hash(s: str, base=256, modulus=101):
    """
    Calculate the polynomial hash of the input string using the specified base and modulus.
    The hash value is calculated based on the polynomial representation of the string.
    Args:
        s (str): The input string
        base (int, optional): The base for the polynomial hash calculation. Defaults to 256.
        modulus (int, optional): The modulus for the polynomial hash calculation. Defaults to 101.
    Returns:
        int: The polynomial hash value of the input string
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(text, pattern):
    """
    Perform Rabin-Karp string search algorithm to find the first occurrence of
    the given pattern in the text by comparing the hash values of the pattern to hash values of the slices of the text.
    Takes in the text and pattern to search for and returns the index of the first occurrence of the pattern in the text,
    or -1 if the pattern is not found.
    """
    pattern_length = len(pattern)
    text_length = len(text)

    # Hash base and modulus
    base = 256
    modulus = 101

    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_slice_hash = polynomial_hash(text[:pattern_length], base, modulus)
    h_multiplier = pow(base, pattern_length - 1) % modulus

    # Iterating over text
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == current_slice_hash:
            if text[i : i + pattern_length] == pattern:
                return i

        if i < text_length - pattern_length:
            current_slice_hash = (
                current_slice_hash - ord(text[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(text[i + pattern_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


if __name__ == "__main__":
    main_string = "Being a developer is not easy"
    substring = "developer"

    position = rabin_karp_search(main_string, substring)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")
