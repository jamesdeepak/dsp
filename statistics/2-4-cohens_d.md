[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> df = nsfg.ReadFemPreg()
totalwgt_lb = df['totalwgt_lb']
mean_all = totalwgt_lb.mean()
first_weights = totalwgt_lb[df.birthord == 1]
others_weights = totalwgt_lb[df.birthord != 1]
mean_first = first_weights.mean()
mean_other = others_weights.mean()

We can find the mean of first babies and other babies first and see if there is any significant difference. We can also tell whether first babies are lighter or not. 
Cohen's D gives us a way to quantify the difference between the groups. 
We can calculate cohen's D using following code:

def CohenEffectSize(group1, group2):
    diff = mean_first - mean_other

    var1 = first_weights.var()
    var2 = others_weights.var()
    n1, n2 = len(first_weights), len(others_weights)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
    
  After getting the cohen's D, we can compare this with the cohen's D we get from the pregnancy length.
    
