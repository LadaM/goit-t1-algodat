# Analysis of efficiency of sorting algorithms

## Algorithms
1. Insertion sort
2. Mergesort
3. Quicksort
4. Timsort

## Data 
- randomly generated numbers
  - 1'000'000
  - 100'000
- distribution
  - uniformly distributed  integers
  - normally distributed floats 

## Performance
### Uniformly distributed data
#### 1'000'000 numbers WITHOUT insertion sort
| Sorting Algorithm | Time               |
|-------------------|--------------------|
| Mergesort         | 1.8922754580853507 |
| Quicksort         | 1.683277333038859  |
| Timsort           | 0.3032735000597313 |

#### 100'000 numbers including insertion sort
| Sorting Algorithm | Time                |
|-------------------|---------------------|
| Insertion sort    | 573.215369625017    |
| Mergesort         | 0.2611778751015663  |
| Quicksort         | 0.24319620802998543 |
| Timsort           | 0.03838241600897163 |

### Normally distributed data
#### 1'000'000 numbers WITHOUT insertion sort
| Sorting Algorithm | Time               |
|-------------------|--------------------|
| Mergesort         | 1.876619791961275  |
| Quicksort         | 2.0127755840076134 |
| Timsort           | 0.3266889579826966 |

#### 100'000 numbers including insertion sort
| Sorting Algorithm | Time                 |
|-------------------|----------------------|
| Insertion sort    | 574.1235506249359    |
| Mergesort         | 0.26553237496409565  |
| Quicksort         | 0.2630662500159815   |
| Timsort           | 0.043476250022649765 |

## Conclusions
1. Insertion sort is VERY slow (when I started the run with 1'000'000 numbers it wasn't finished in what seemed like an eternity but more likely was about 30min which is kind of eternity for a computer program unless we're not talking about training neural networks or downloading node packages)
2. Insertion sort is at least 2'000 times slower than any other of the analysed algorithms
3. => Quadratic complexity is really bad for larger datasets
4. Mergesort and Timsort have stable performance for both data distributions
5. Quicksort was faster with uniformly distributed data
6. Timsort was at least 5 times faster than other algorithms
7. It doesn't make any sense to custom-code a sorting algorithm
8. On the smaller dataset the performance of the Timsort was more unstable for different data distributions (slower for normally distributed data)