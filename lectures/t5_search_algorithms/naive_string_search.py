def naive_search(main_string, pattern):
    m = len(pattern)
    n = len(main_string)

    # For each char in the main string
    for i in range(n - m + 1):
        j = 0

        while j < m:
            if main_string[i + j] != pattern[j]:
                break  # getting out of the inner loop
            j += 1

        # We've searched the whole pattern and found it
        if j == m:
            return i

    return -1

if __name__ == "__main__":
    main_string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    position = naive_search(main_string, pattern)

    if position > -1:
        print(f"Found at {position}")
    else:
        print("Not found")
