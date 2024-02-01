def choose_coins_dynamic(coins, amount):
    sorted_coins = sorted(coins, reverse=True)  # sort coins large to small
    res = {coin: 0 for coin in coins}  # dictionary {coin_denomination: number_of_coins}
    rest_sum = amount # remaining sum
    
    for coin in sorted_coins:
        while coin <= rest_sum:
            if coin in res:
                res[coin] += 1
            else:
                res[coin] = 1
            rest_sum -= coin

    return res

    
if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50]
    test_amounts = [1, 2, 5, 10, 20, 50, 11, 15, 68, 89]

    for amount in test_amounts:
        res = amount, choose_coins_dynamic(coins, amount)
        print(f"Amount: {amount}, result: {res}")
        