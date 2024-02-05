# Monte Carlo Method for Integral Calculation

## Experiment description
Running a 100 experiments with 1000 points randomly and uniformly generated for each. In each step, algorithm generated values for x and y within the domain and range of function definition. The domain was specified by the integration limits a and b, the range was set to be non-negative and to the max value of the function `max(f(a), f(b))`. This allowed to generate points in the area within a rectangle with `width = |b - a|` and `height = max(f(a), f(b))`. For each point was checked, if it is below the line defined by the function. The average of all integral values calculated during experiments was taken.

## Proximity of monte-carlo calculated value to the value of the integral
Comparing to value of the integral calculated using `scipy.integrate.quad()` and the value estimated through monte-carlo simulation. For function `f(x) = x^2` and integral limits of `a = 0, b = 2` the quad value is `2.666...` and monte-carlo value is `2.646`. It seems to be close enough for human understanding, but probably not close enough for mathematical use.

## Conclusions
We can estimate quite well even with few experiments (100), but even closer with 1000. Depending on error tollerance, we need to run more experiments to become "closer" to the real value.