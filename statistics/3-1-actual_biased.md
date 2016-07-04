[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> First of all I would get the actual pmf (actual_pmf) . Then I would copy the actual pmf and name it as biased_pmf. Then I can do something like this to make this biased 

for x, p in actual_pmf.Items():
    biased_pmf.Mult(x, x)

Then, we can plot both of them and also calculate their means for comparison. 
actual_pmf.Mean()
biased_pmf.Mean()

    
