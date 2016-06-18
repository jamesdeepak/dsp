# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are arrays in python. Major difference between a list and a tuple is that tuple are immutable (cannot change values) once created but lists are mutable. Once created, if we need to add/edit a tuple, we need to create a new tuple with our desired changes from the original tuple (original tuple is unchanged). However, lists can be modified as desired. Another difference between the two is the syntax to create these objects. While tuples use parenthesis, lists use square brackets.
Tuples work as keys in dictionary. Dictionary associate key objects to their values. Since lists allow duplicate items, having duplicate keys is not allowed in python dictionaries. However, tuples serve as excellent keys in dictionary.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists are both one-dimensional array to store information. While lists keep order, sets do not (i.e. items are indexed in a list). Also, list can include duplicate items while sets cannot. Eg. List = [‘one’, ‘two’, ‘three’, ‘two’] Set = [‘one’, ‘two’, ‘three’] . If we are just trying to find an element and do not care either about duplicates or order of the elements, sets are much faster than list. In order to store information in a set, the items must be hashable. Thus, in sets items are implemented using hash tables. Thus, when we are trying to find an element in a set we check whether element is at the position determined by its hash. However, in lists, we have to check one by one in every position until we find the item. Therefore, performance is better in sets compared to lists when we are just trying to find an element. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Purpose of lambda in python is to make quick one line mini function without giving any name. We can use lambda anywhere in our code where we might use function. We can also use lambda within a function. 
Eg. f = lambda x:x**2 + 5 . If we call f(4) in our code , we will get 21 . Another example using sort is while using dictionary: 
def sortByDict(): 
    sortedByKeyDict = sorted(faculty_dict2.items(), key = lambda x:x[1])
    print(sortedByKeyDict)



---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a simple way to create lists in python. In addition to number lists, we can also create lists of strings. 
Eg. cubeList = [x**3 for x in range(10)] This creates a list cubeList = [0,1,8,27,64,…..729] .

We can also do the same thing with map and Filter. For eg. 
Map:  r = [0,1,2,3…,9]
	mapCubeList = map(lambda x: x**3 , r)
for i in r:
	print(i) 
This yields the same result as the cubeList in list comprehension. Lists comprehension, maps and filters all have strengths and weakness in various situations. However, in a situation where all can be used, List comprehension is usually preferred. 

Set comprehension allows us to create sets just like list comprehension allows us to create lists.
Lets look at a example to understand dictionary comprehension. Say we have a dictionary that stores names as key and their expenses as values. There might be a situation where same individuals might have multiple expenses. However, while entering the data, if the dictionary key were set to be case sensitive, there might be situation where “Joe” and “joe” are stored as two different individuals. We can use dictionary comprehension to combine these keys into one and sum up their expense values into one expense. 


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





