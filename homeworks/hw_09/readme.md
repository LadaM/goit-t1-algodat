# Coin Change Problem
Given a set of coin denominations and a target amount, find the minimum number of coins needed to make up that amount. Additionally, determine the specific combination of coins that achieves the minimum count.

## Solutions
1. Greedy algorithm
2. Dynamic programming algorithm

## Tests
* `coins = {1, 2, 5, 10, 20, 50}`
* randomly generated amounts between 1 and 1000 with `amounts_counts = [10, 100, 1000, 10000]`
* measuring problem-solving time using `timeit.deafault_timer`

## Results

| Algorithm      | # Amounts | Time (ms)  |
|----------------|-----------|------------|
| Greedy         | 10        | 0.06971    |
| Dynamic        | 10        | 6.54746    |
| Simple Dynamic | 10        | 5.20896    |
| -              | -         | -          |
| Greedy         | 100       | 0.31629    |
| Dynamic        | 100       | 61.57013   |
| Simple Dynamic | 100       | 69.85425   |
| -              | -         | -          |
| Greedy         | 1000      | 3.10062    |
| Dynamic        | 1000      | 559.09287  |
| Simple Dynamic | 1000      | 459.60758  |
| -              | -         | -          |
| Greedy         | 10000     | 27.03379   |
| Dynamic        | 10000     | 4484.67450 |
| Simple Dynamic | 10000     | 4472.42613 |

## Conclusions
* Greedy solution is more efficient, especially when running it many times for different amounts
* The simple dynamic solution 
  * returning just a number of coins and not which coins have to be used for exchange
  * isn't significantly faster than the full dynamic solution
  * so backtracking to find the number of coins for each denomination isn't taking too long
* Greedy solution 
  * does only one pass through the coin denomination 
  * doesn't use additional data except a variable to keep track of the current amount `O(1)`
  * in most cases will come up with an optimal solution
* Dynamic programming algorithm
  * requires two steps
    * building a table containing min coins that have to be used for each amount
    * back-tracking the coins in reverse order to check which coins are to be used for exchange
  * requires additional data for table of min coin counts for all amounts `O(n)` where `n = amount`
* Unless we really have to make sure that we have the most optimal solution
  * greedy algorithm is working good enough
  * is more understandable
  * has fewer steps
  * doesn't require additional memory