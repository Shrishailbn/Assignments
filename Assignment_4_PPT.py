#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1
#Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, 
#return a sorted array of only the integers that appeared in all three arrays.

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

def findCommon(ar1, ar2, ar3, n1, n2, n3):
 
    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0
 
    # Iterate through three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):
 
        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print (ar1[i])
            i += 1
            j += 1
            k += 1
 
        # x < y
        elif ar1[i] < ar2[j]:
            i += 1
 
        # y < z
        elif ar2[j] < ar3[k]:
            j += 1
 
        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k += 1
 
 
# Driver program to check above function
ar1 = [1,2,3,4,5]
ar2 = [1,2,5,7,9]
ar3 = [1,3,4,5,8]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print ("Common elements are")
findCommon(ar1, ar2, ar3, n1, n2, n3)

    


# In[ ]:


#Question 2

#Given two0-indexed integer arrays nums1 and nums2, returna list answer of size 2 where:

#- answer[0] is a list of all distinct integers in nums1 which are not present in nums2
#- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.


# In[18]:


#Question 3
#Given a 2D integer array matrix, return the transpose of matrix.
#The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

from array import *
import numpy as np
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#mat=array('i',matrix)
old_mat=np.array(matrix)

transpos=old_mat.T
print(transpos)


# In[ ]:


#Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such 
#that the sum of min(ai, bi) for all i is maximized. 
#Return the maximized sum.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        i = 1
        
        while n >= i:
            n-=i
            rows+=1
            i+=1
               
        return rows


# In[21]:


#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

nums = [-4,-1,0,3,10]

def sortSquare(arr, n):
 
    # First convert each array
    # elements into its square
    for i in range(n):
        arr[i]= arr[i] * arr[i]
    arr.sort()
 

arr = [-4,-1,0,3,10]
n = len(arr)
 
print("Before sort")
for i in range(n):
    print(arr[i], end = " ")
 
print("\n")
 
sortSquare(arr, n)
 
print("After sort")
for i in range(n):
    print(arr[i], end = " ")


# In[23]:




def shuffleArray(a, n):
 
    # Rotate the element to the left
    i, q, k = 0, 1, n
    while(i < n):    
        j = k
        while(j > i + q):
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        i += 1
        k += 1
        q += 1
 
a = [2,5,1,3,4,7]
n = len(a)
shuffleArray(a, int(n / 2))
for i in range(0, n):
    print(a[i], end = " ")


# In[ ]:




