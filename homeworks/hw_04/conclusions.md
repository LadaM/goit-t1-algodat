# Analysis of efficiency of sorting algorithms

## Algorithms
1. Mergesort
2. Quicksort
3. Timsort

## Data 
- 1000000 randomly generated numbers
- two runs:
  - uniformly distributed  integers
  - normally distributed floats 

## Performance
### Uniformly distributed data
| Sorting Algorithm | Time               |
|-------------------|--------------------|
| Mergesort         | 1.8922754580853507 |
| Quicksort         | 1.683277333038859  |
| Timsort           | 0.3032735000597313 |

### Normally distributed data
| Sorting Algorithm | Time               |
|-------------------|--------------------|
| Mergesort         | 1.876619791961275  |
| Quicksort         | 2.0127755840076134 |
| Timsort           | 0.3266889579826966 |

## Conclusions
1. Mergesort and Timsort have stable performance for both data distributions
2. Quicksort was much faster with uniformly distributed data
3. Timsort was at least 5 times faster than other algorithms
4. It doesn't make any sense to custom-code a sorting algorithm