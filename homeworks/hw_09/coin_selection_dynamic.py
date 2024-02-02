def choose_coins_dynamic(coins, amount):
    # Represents the minimum number of coins needed to make up amount i
    min_coin_count = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins needed to make up amount 0
    min_coin_count[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            # Check if the current coin can be used to make up the amount i
            if coin <= a:
                # Choose the min of current coin denomination or the number of coins of previous denomination + 1
                min_coin_count[a] = min(min_coin_count[a], min_coin_count[a - coin] + 1)

    # If min_coin_count[amount] is still set to float('inf'), no combination of coins was found
    if min_coin_count[amount] == float('inf'):
        return None

    # Find the combination of coins that can make up the amount
    chosen_coins = {}
    remaining_amount = amount
    for coin in reversed(coins):
        while remaining_amount >= coin and min_coin_count[remaining_amount] == min_coin_count[remaining_amount - coin] + 1:
            # Use this coin in the solution
            chosen_coins[coin] = chosen_coins.get(coin, 0) + 1
            remaining_amount -= coin

    return chosen_coins


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50]
    test_amounts = [1, 2, 5, 10, 20, 50, 11, 15, 68, 89]

    for amount in test_amounts:
        res = amount, choose_coins_dynamic(coins, amount)
        print(f"Amount: {amount}, result: {res}")