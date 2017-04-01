[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
n = np.random.random(1000)

pmf = thinkstats2.Pmf(n)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='Random', ylabel='PMF')

cdf = thinkstats2.Cdf(n)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random', ylabel='CDF')
```

It seems like numbers in the middle of the range are generated more frequently. Also, the distribution is not quite uniform.
