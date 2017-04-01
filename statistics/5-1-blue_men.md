[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
import nsfg
import thinkstats2
import math
import thinkplot
import numpy as np
import scipy.stats

mu = 178
sigma = 7.7
x = scipy.stats.norm(loc=mu, scale=sigma)

a = x.cdf(177.8)
b = x.cdf(185.5)
print(b-a)
```

34.5% of the male population are in the range.
