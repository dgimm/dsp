# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they are both types of sequences. This means each element of these sequences are assigned an index and Python provides built-in functions to measure their length.

>> However, tuples are not as versatile as lists and one major difference is that tuples are immutable. As an example, modifying a list will affect the list itself and not return a modified list. Moreover, lists use square brackets whereas tuples use parentheses. Lastly, tuples will work as keys in dictionaries since keys have to be immutable objects.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> In contrast to lists, sets are unordered, cannot contain duplicates and are also immutable. As a result, sets are preferred over lists when membership is more important than order or frequency. Moreover, values in sets are hashable. Therefore, checking membership is generally faster with sets than lists.

>> A wedding registry would be an example of a list. You have a list of desired items in order and the list can be modified. On the other hand, G20 is an example of a set as membership is very important and order does not play a significant role.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a tool for building anonymous function objects. It takes parameters and a single expression, and the value of the expression is evaluated and returned. It is used when a relatively simple function is only expected to be used once (e.g., functions that take in other functions as arguments). Using lambda can improve the readability of the program as well.

>> Example i:
"""
Lambda function that triples the input value.
"""
triple = lambda x: x * 3
print (triple(3))

Example ii:
"""
Lambda function that sorts the list in custom order.
"""
grocery = [{'pomegranate': 3, 'blueberry': 1, 'cherry': 6}, {'pomegranate': 5, 'blueberry': 2, 'cherry': 4}]
grocery.sort(key=lambda x: x['cherry'])
print(grocery)

Example iii:
"""
Lambda function that filters out odd numbers.
"""
even = [52, 7, 14, 80, 29, 36]
even_filtered = list(filter(lambda x: (x % 2 == 0), even))
print even2

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a tool for deriving one list from an existing list. Each element in the list can be transformed as needed. Map is used to build one list while building another, whereas filter is used to only select some of the elements using conditional statements. Below are examples and equivalents with map and filter, followed by examples of set comprehension and dictionary comprehension.

Map:

def add(x):
    add = []
    for i in x:
        add.append(i + 2)
    return add
    
def add(x):
    return [i + 2 for i in x]

Filter:

def even(x):
    even = []
    for i in x:
        if i % 2 == 0:
            even.append(i)
    return even

def even(x):
    return [i for i in x if i % 2 == 0]

{x**2 for x in range(10)}

{x: x**2 for x in range(5)}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> The answer is 937 days.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> The answer is 513 days.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> The answer is 7850 days.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





