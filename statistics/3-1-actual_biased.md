[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
import nsfg
import thinkstats2
import math
import thinkplot

df2 = nsfg.ReadFemResp()

pmf = thinkstats2.Pmf(df2.numkdhh, label='numkdhh')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

pmf_biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, pmf_biased])
thinkplot.Config(xlabel='Children', ylabel='PMF')

print(pmf.Mean())
print(pmf_biased.Mean())
```
