from collections import deque
import re


def test_palindrome(word: str) -> bool:
    # case of letters is irrelevant as well as spacing
    test_word = re.sub(r"\W", "", word).lower()
    # base case - empty string is a palindrome as well as a string with one character
    if len(test_word) <= 1:
        return True

    word_deque = deque(test_word)    
    while len(word_deque) > 1:
        first = word_deque.popleft()
        last = word_deque.pop()
        if first != last:
            return False

    return True


if __name__ == "__main__":
    test_words = [
        "98789",
        "121",
        "my name is Lada",
        "cat",
        "ada",
        "adam",
        "Mr. Owl ate my metal worm.",
        "kayak",
        " ",
        "",
        "22",
    ]
    for word in test_words:
        print(
            f"'{word}' is "
            + ("not " if not test_palindrome(word) else "")
            + "a palindrome"
        )
