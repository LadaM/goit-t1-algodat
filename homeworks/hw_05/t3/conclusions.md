# String Search Algorithm Comparison

## Compared Algorithms
- Boyer-Moore
- Knuth-Morris-Pratt
- Rabin-Karp

## Test Cases
1. **Text 1** (ВИКОРИСТАННЯ АЛГОРИТМІВ У БІБЛІОТЕКАХ МОВ ПРОГРАМУВАННЯ)
   1. Existing string - "Експоненціальний пошук використовується для пошуку елементів шляхом переходу в експоненціальні позиції"
   2. Not existing string = "Дельфі́нові (Delphinidae) — родина ссавців підряду зубатих китів ряду китоподібних (Cetacea). Представники родини трапляються в усіх океанах і морях, а також у деяких річкових системах. Дельфінові видаються дуже розумними, вони швидко й гнучко можуть адаптуватися до нових ситуацій."
2. **Text 2** (Методи та структури даних для реалізації бази даних рекомендаційної системи соціальної мережі)
   1. Existing string - "Triples Storage and SPARQL Query Processing."
   2. Not existing string = "As Stephen King said – 'A short story is a different thing all together – a short story is like a kiss in the dark from a stranger.'"

## Results
Searching **text1** for 
> "Експоненціальний пошук використовується для пошуку елементів шляхом переходу в експоненціальні позиції"

| Algorithm          | Result        | Time (ms) |
|--------------------|---------------|-----------|
| Rabin-Karp         | Found at 7270 | 2.36954   |
| Knuth-Morris-Pratt | Found at 7270 | 1.52454   |
| Boyer-Moore        | Found at 7270 | 0.15337   |

Searching **text1** for
> "Дельфі́нові (Delphinidae) — родина ссавців підряду зубатих китів ряду китоподібних (Cetacea). Представники родини трапляються в усіх океанах і морях, а також у деяких річкових системах. Дельфінові видаються дуже розумними, вони швидко й гнучко можуть адаптуватися до нових ситуацій."

| Algorithm          | Result    | Time (ms) |
|--------------------|-----------|-----------|
| Rabin-Karp         | Not found | 4.61671   |
| Knuth-Morris-Pratt | Not found | 1.78746   |
| Boyer-Moore        | Not found | 0.181     |

Searching **text2** for
> "Triples Storage and SPARQL Query Processing."

| Algorithm          | Result         | Time (ms) |
|--------------------|----------------|-----------|
| Rabin-Karp         | Found at 16368 | 4.93208   |
| Knuth-Morris-Pratt | Found at 16368 | 2.02946   |
| Boyer-Moore        | Found at 16368 | 0.20762   |

Searching text2 for
> "As Stephen King said – 'A short story is a different thing all together – a short story is like a kiss in the dark from a stranger.'"

| Algorithm          | Result    | Time (ms) |
|--------------------|-----------|-----------|
| Rabin-Karp         | Not found | 5.93475   |
| Knuth-Morris-Pratt | Not found | 2.28313   |
| Boyer-Moore        | Not found | 0.10633   |


## Conclusions
* Boyer-Moore algorithm has the fastest and most consistent performance among all other algorithms for both cases and files
* Rabin-Karp's algorithms drops in performance the most when the searched string is not in the text
* Knuth-Morris-Pratt performs at least two times better than Rabin-Karp except for the case of text 1 with existing string that is quite close to the beginning of the text
  * For text 2 existing string was found at the further location and KPM was more than 2 times faster than Rabin-Karp in finding it