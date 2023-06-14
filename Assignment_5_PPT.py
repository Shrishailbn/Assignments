#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Convert 1D Array Into 2D Array

#You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

#The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

#Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.



if m*n != len(original):
    return []
      
ans = []
for i in range(0, m*n, n):
    ans.append(original[i:i+n])
            
return ans


# In[18]:


#You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. 
#The last row of the staircase may be incomplete.

class Solution:
    def arrangeCoins(n: int) -> int:
        l,r=1,n
        rows = 0
        
        while  l<=r:
            mid=(l+r)//2
            coins=(mid/2)(mid+1)
            if coins>n:
                r=mid-1
            else:
                l=mid+1
                rows=max(mid,rows)

        return rows

#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-#decreasing order.

def sortSquare(arr, n):
 
    # First convert each array
    # elements into its square
    for i in range(n):
        arr[i]= arr[i] * arr[i]
    arr.sort()
 

arr = [-6, -3, -1, 2, 4, 5]
n = len(arr)
 
print("Before sort")
for i in range(n):
    print(arr[i], end = " ")
 
print("\n")
 
sortSquare(arr, n)
 
print("After sort")
for i in range(n):
    print(arr[i], end = " ")
# In[20]:


nums1 = [1,2,3]
nums2 = [2,4,6]

for i in nums1:
    for j in nums2:
        if i == j:
            print(i,j)
            nums1.remove(i==j)
print (nums1) 
print (nums2)


# In[26]:


#Given two 0-indexed integer arrays nums1 and nums2, retur a list answer of size 2 where:
#- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

#Note that the integers in the lists may be returned in any order.


nums1 = [1,2,3]
nums2 = [2,4,6]

for i in nums1:
    for j in nums2:
        if i == j:
            print(i,j)
            nums1.remove(i==j)
print (nums1) 


# In[27]:


#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears 
#once or twice, return an array of all the integers that appears twice.

numRay = [4,3,2,7,8,2,3,1]
arr_size = len(numRay)
for i in range(arr_size):
  
    x = numRay[i] % arr_size
    numRay[x] = numRay[x] + arr_size
  
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " ")


# In[ ]:




