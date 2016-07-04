[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> First we can create a list of random numbers (say 10,000 so that we have a big sample). 
randomNumberList = [random.random() for i in range(10000)]
Then we can look at the pmf and cdf of this list using thinkstats 2 function. Also, we can plot the pmf and cdf. 

For a uniform distribution, all the values have almost same probablity. Thus, the pmf plot should look like a flat top rectangle.
If our CDF generated from the randomnumber looks similar to the CDF of the uniform distribution, we can safely argue that our fucntion random.ramdom is truly random. 


