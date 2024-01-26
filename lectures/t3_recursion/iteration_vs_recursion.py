def sum_up_iter(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_up_recursive(n):
    if n in [0, 1]:
        return n
    else:
        return n + sum_up_recursive(n - 1)


if __name__ == "__main__":
    print(f"{sum_up_iter(5)} = {sum_up_recursive(5)}")
