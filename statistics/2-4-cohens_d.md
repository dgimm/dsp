[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```
import nsfg
import thinkstats2
import math


df = nsfg.ReadFemPreg()

live = df[df.outcome == 1]

first = live[live.birthord == 1]
other = live[live.birthord != 1]

first_wgt = first['totalwgt_lb']
other_wgt = other['totalwgt_lb']

print(first_wgt.mean())
print(other_wgt.mean())

first_lng = first['prglngth']
other_lng = other['prglngth']

print(first_lng.mean())
print(other_lng.mean())

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
    
CohenEffectSize(first_wgt, other_wgt)
CohenEffectSize(first_lng, other_lng)
```

First babies are neither lighter or heavier than others. Cohen's d equals 0.08 and whether in comparison to Cohen's d of pregnancy length or not, the birth order has a minimal effect on birth weight.
