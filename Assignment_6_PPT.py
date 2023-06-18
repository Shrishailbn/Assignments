#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

#- s[i] == 'I' if perm[i] < perm[i + 1], and
#- s[i] == 'D' if perm[i] > perm[i + 1].

#Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """


# In[3]:


#You are given an m x n integer matrix matrix with the following two properties: - 
    #Each row is sorted in non-decreasing order. - The first integer of each row is greater than the last integer of the previous row. 
    #Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*. You must write a solution in O(log(m * n)) time complexit using python

def search(mat, n, x):
    if(n == 0):
        return -1
 
    # Traverse through the matrix
    for i in range(n):
        for j in range(n):
 
            # If the element is found
            if(mat[i][j] == x):
                print("Element found at (", i, ",", j, ")")
                return 1
 
    print(" Element not found")
    return 0
 
 
# Driver code
if __name__ == "__main__":
    mat =  [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
 

search(mat, 3, 3)


# In[4]:


#Given an array of integers arr, return *true if and only if it is a valid mountain array*.

#Recall that arr is a mountain array if and only if:

#- arr.length >= 3
#- There exists some i with 0 < i < arr.length - 1 such that:
#    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def isMountainArray(arr):
 
    if (len(arr) < 3):
        return False
    flag = 0
    i = 0
    for i in range(1, len(arr)):
        if (arr[i] <= arr[i - 1]):
            break
 
    if (i == len(arr) or i == 1):
        return False
 
    while i < len(arr):
        if (arr[i] >= arr[i - 1]):
            break
        i += 1
    return i == len(arr)
 
# Driver Code
if __name__ == "__main__":
 
    arr = [1, 2, 3, 4, 9,
           8, 7, 6, 5]
    if (isMountainArray(arr)):
        print("true")
    else:
        print("false")


# In[5]:


#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

def findSubArray(arr, n):
 
    sum = 0
    maxsize = -1
 
    # Pick a starting point as i
 
    for i in range(0, n-1):
     
        sum = -1 if(arr[i] == 0) else 1
 
        # Consider all subarrays starting from i
 
        for j in range(i + 1, n):
         
            sum = sum + (-1) if (arr[j] == 0) else sum + 1
 
            # If this is a 0 sum subarray, then
            # compare it with maximum size subarray
            # calculated so far
 
            if (sum == 0 and maxsize < j-i + 1):
                 
                maxsize = j - i + 1
                startindex = i
             
         
     
    if (maxsize == -1):
        print("No such subarray");
    else:
        print(startindex, "to", startindex + maxsize-1);
 
    return maxsize
 
# Driver program to test above functions
arr = [1, 0, 0, 1, 0, 1, 1]
size = len(arr)
findSubArray(arr, size)


# In[7]:


#The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

#- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

#Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

def minValue(A, B, n):
 
    # Sort A and B so that minimum and maximum
    # value can easily be fetched.
    A.sort()
    B.sort()
 
    # Multiplying minimum value of A and maximum
    # value of B
    result = 0
    for i in range(n):
        result += (A[i] * B[n - i - 1])
 
    return result
 
 
# Driven Program
A = [5,3,4,2]
B = [4,2,2,5]
n = len(A)
print (minValue(A, B, n))


# In[ ]:


#An integer array original is transformed into a doubled array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

#Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

#def findOriginal(arr):
 
    # Stores the numbers and
    # their frequency
    numFreq = {}
 
    # Add number with their frequencies
    # in the hashmap
    for i in range(0, len(arr)):
        if (arr[i] in numFreq):
            numFreq[arr[i]] += 1
        else:
            numFreq[arr[i]] = 1
 
    # Sort the array
    arr.sort()
 
    # Initialize an arraylist
    res = []
 
    for i in range(0, len(arr)):
       
        # Get the frequency of the number
        freq = numFreq[arr[i]]
        if (freq > 0):
           
            # Element is of original array
            res.append(arr[i])
 
            # Decrement the frequency of
            # the number
            numFreq[arr[i]] -= 1
 
            twice = 2 * arr[i]
 
            # Decrement the frequency of
            # the number having double value
            numFreq[twice] -= 1
 
    # Return the resultant string
    return res
 
# Driver Code
arr = [4, 1, 2, 2, 2, 4, 8, 4]
res = findOriginal(arr)
 
# Print the result list
for i in range(0, len(res)):
    print(res[i], end=" ")


# In[ ]:


#Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

