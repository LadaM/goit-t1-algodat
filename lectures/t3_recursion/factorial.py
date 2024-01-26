def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return None
    if n in [0, 1]:  # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive case


def factorial_with_steps(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return None
    if n in [0, 1]:  # base case
        print(f"Base case: factorial({n}) = 1")
        return 1
    result = n * factorial_with_steps(n - 1)  # recursive case
    print(f"Recursive case: factorial({n}) = {result}")
    return result


if __name__ == "__main__":
    print(factorial(5))
    print(factorial_with_steps(5))
