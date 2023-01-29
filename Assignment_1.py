#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
    * Expression
    hello Values
    -87.8 Values
    - Expression
    Expression()
    + Expression
    6 Values


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')
    Variables are expressions or symbols that you can use to store data in a program. Strings are data, so we can use them to fill up a variable.


# In[ ]:


3. Describe three different data types.
    1. Sequence- It is the ordered collection of similar or different data types. These are string, list, tuple.
    2. Numeric- In Python, numeric data type represent the data which has numeric value. Numeric value can be integer, floating number or even complex numbers. These values are defined as int, float and complex class in Python.
    3. Set- Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')
    An expression is combination of operators and operands. Expressions perform particular function and results in a value.


# In[ ]:


5. This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')
    An expression perform particular function and results in a value through interpreter. Statement used for creating variables or for displaying values Statement is used to assign a value to a variable.


# In[2]:


#6. After running the following code, what does the variable bacon contain?
bacon = 22
a=bacon + 1
print(a)


# In[3]:


#7. What should the values of the following two terms be?
#'spam' + 'spamspam'
#'spam'* 3

b='spam' + 'spamspam'
c='spam'* 3

print(b)
print(c)


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
    Variable names should not start with numbers


# In[ ]:


9. What three functions can be used to get the integer, floating-point number, or string
get_ipython().set_next_input('version of a value');get_ipython().run_line_magic('pinfo', 'value')
    int()
    float()
    str()


# In[ ]:


#10. Why does this expression cause an error? How can you fix it?
#'I have eaten' + 99 + 'burritos.'

Because string and integer concatenation is not allowed. It can be fixed as below.


# In[5]:


d='I have eaten ' + str(99) + ' burritos.'
print(d)


# In[ ]:




