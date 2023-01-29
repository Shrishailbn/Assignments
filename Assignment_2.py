#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
    True = 1
    False = 0


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
    and
    or
    not


# In[ ]:


3. Make a list of each Boolean operator. (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
    True and True is True.

True and False is False.

False and True is False.

False and False is False.

True or True is True.

True or False is True.

False or True is True.

False or False is False.

not True is False.

not False is True.


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')


# In[3]:


(5 > 4) and (3 == 5)


# In[4]:


not (5 > 4)


# In[5]:


(5 > 4) or (3 == 5)


# In[6]:


not ((5 > 4) or (3 == 5))


# In[7]:


(True and True) and (True == False)


# In[8]:


(not False) or (not True)


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
    <, >, ==, <=, >=, !=


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.


# In[9]:


# the equal to condition is ==, example to write 5 equal to 5, it is written as bellow.
5==5


# In[ ]:


#the assignment operator is =, i.e as shown below.
a=5


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


# In[12]:


spam = 0

#1st block
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
else:
    print('ham')
    
#2nd block    
print('spam')

#3rd block  
print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# In[ ]:


spam=input('enter number: ')

if spam == 1:
    print('Hello')
    if spam==2:
        print('Howdy')
else:
    print('Greetings!')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
     We can use CTRL + C 


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

break = The break statement leads to an immediate exit of the innermost switch or enclosing loop. 
continue = The continue statement begins the next iteration of the while, enclosing for, or do loop.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[ ]:


# range(10) gives numbers in the range of 0 to 9
for i in range(10):
    print(i)


# In[19]:


# range(0, 10) gives numbers in the range of 0 to 9 starting point is defined here.
for i in range(0,10):
    print(i)


# In[ ]:


# range(0, 10,1) gives numbers in the range of 0 to 9 in a step of 1 and starting point is defined here .
for i in range(0,10,1):
    print(i)


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


# In[21]:


#for loop
for i in range(1,11):
    print(i)


# In[1]:


i = 1
while(i<=10):
    print(i)
    i += 1


# In[ ]:


13. If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


from spam import bacon()

