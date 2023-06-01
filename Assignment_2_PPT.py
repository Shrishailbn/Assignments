#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Question 1
#Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) 
#such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

from itertools import combinations
nums = [1,4,3,2]

b=list(combinations(nums,2))
print(b)
f=min(b[0])+min(b[1])
s=min(b[2])+min(b[3])
t=min(b[4])+min(b[5])

max_sum=max(f,s,t)
print(max_sum)


# In[ ]:


#Question 2
#Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

#The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

#Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.


# In[36]:


#Question 3
#We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

#Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing 
#the order of the remaining elements.

class sol():
    def fun(self, nums: list[int])->int:
        c=Counter(nums)
        return max([v+c[k+1] for k,v in c.items() if k+1 in c]+[0])


# In[46]:


#You have a long flowerbed in which some of the plots are planted, and some are not.
#However, flowers cannot be planted in adjacent plots.
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
flowerbed = [1,0,0,0,1]
f=[0]+flowerbed+[0]
nf=[]

for i in range(1,len(f)-1):
    if f[i-1] and f[i] and f[i+1]==0:
        f[i]=1
        nf.append(f[i])
        n-=1


# In[47]:


#Question 5
#Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

import sys
 
def maxProduct(arr, n):
 
    if n < 3:
        return -1
 
    # will contain max product
    max_product = -(sys.maxsize - 1)
     
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                max_product = max(
                    max_product, arr[i]
                    * arr[j] * arr[k])
 
    return max_product
 
# Driver Program
arr = [1,2,3]
n = len(arr)
 
max = maxProduct(arr, n)
 
if max == -1:
    print("No Triplet Exits")
else:
    print("Maximum product is", max)


# In[79]:


#Question 6
#Given an array of integers nums which is sorted in ascending order, and an integer target,
#write a function to search target in nums. If target exists, then return its index. Otherwise,
#return -1.
#You must write an algorithm with O(log n) runtime complexity.

def find_num(n,target):
    for i in range(len(n)):
        if n[i] == target:
            print(i)


# In[80]:


find_num([-1,0,3,5,9,12],9)


# In[81]:


#An array is monotonic if it is either monotone increasing or monotone decreasing.

#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
#monotone decreasing if for all i <= j, nums[i] >= nums[j].

#Given an integer array nums, return true if the given array is monotonic, or false otherwise.

def check(arr):
    N = len(arr)
    inc = True
    dec = True
     
    # Loop to check if array is increasing
    for i in range(0, N-1):
       
        # To check if array is not increasing
        if arr[i] > arr[i+1]:
            inc = False
 
    # Loop to check if array is decreasing
    for i in range(0, N-1):
       
       # To check if array is not decreasing
        if arr[i] < arr[i+1]:
            dec = False
 
    # Pick one whether inc or dec
    return inc or dec
 
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 3]
 
    # Function call
    ans = check(arr)
    if ans == True:
        print("Yes")
    else:
        print("No")


# In[ ]:


#Question 8
#You are given an integer array nums and an integer k.

#In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

#The score of nums is the difference between the maximum and minimum elements in nums.

#Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

