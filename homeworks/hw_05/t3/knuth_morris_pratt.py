def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for the given pattern.
    :param pattern: The input pattern for which to compute the LPS array.
    :return: The LPS array representing the length of the longest proper prefix which is also a proper suffix for each index in the pattern.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    m = len(pattern)
    n = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < n:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == m:
            return i - j

    return -1  # if pattern not matched


if __name__ == "__main__":
    raw = ("Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження "
           "підрядка в тексті.")
    search_pattern = "алг"

    print(kmp_search(raw, search_pattern))
