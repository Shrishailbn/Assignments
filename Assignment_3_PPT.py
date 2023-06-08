#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Question 1
#Given an integer array nums of length n and an integer target, find three integers
#in nums such that the sum is closest to the target.
#Return the sum of the three integers.

def find_close_triplet(arr, n, target, count, sum, ind, ans, minm):
    if ind == n:
        if count == 3:
            if abs(target - sum) < minm[0]:
                minm[0] = abs(target - sum)
                ans[0] = sum
        return
    find_close_triplet(arr, n, target, count + 1, sum + arr[ind], ind + 1, ans, minm)
    
    find_close_triplet(arr, n, target, count, sum, ind + 1, ans, minm)
if __name__ == "__main__":
  #Input array
  arr = [-1, 2, 1, -4]
target = 1
n = len(arr)
minm = [float('inf')]
ans = [0]

find_close_triplet(arr, n, x, 0, 0, 0, ans, minm)
print(ans[0])


# In[10]:


#Given an array nums of n integers, return an array of all the unique quadruplets
#[nums[a], nums[b], nums[c], nums[d]] such that:
#           ● 0 <= a, b, c, d < n
#           ● a, b, c, and d are distinct.
 #          ● nums[a] + nums[b] + nums[c] + nums[d] == target

    
class Pair:
    def __init__(self, x, y):
        self.index1 = x
        self.index2 = y
 
# Function to find the all the unique quadruplets
# with the elements at different indices
def GetQuadruplets(nums, target):
    # Store the sum mapped to a list of pair indices
    map = {}
 
    # Generate all possible pairs for the map
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            # Find the sum of pairs of elements
            sum = nums[i] + nums[j]
 
            # If the sum doesn't exist then update with the new pairs
            if sum not in map:
                map[sum] = [Pair(i, j)]
            # Otherwise, add the new pair of indices to the current sum
            else:
                map[sum].append(Pair(i, j))
 
    # Store all the Quadruplets
    ans = set()
 
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            lookUp = target - (nums[i] + nums[j])
 
            # If the sum with value (K - sum) exists
            if lookUp in map:
                # Get the pair of indices of sum
                temp = map[lookUp]
 
                for pair in temp:
                    # Check if i, j, k and l are distinct or not
                    if pair.index1 != i and pair.index1 != j and pair.index2 != i and pair.index2 != j:
                        l1 = [nums[pair.index1], nums[pair.index2], nums[i], nums[j]]
                         
                        # Sort the list to avoid duplicacy
                        l1.sort()
                         
                        # Update the set
                        ans.add(tuple(l1))
 
    # Print all the Quadruplets
    print(*reversed(list(ans)), sep = '\n')
 
# Driver Code
arr = [1, 0, -1, 0, -2, 2]
K = 0
GetQuadruplets(arr, K)


# In[11]:


#Given a sorted array of distinct integers and a target value, return the index if the
#target is found. If not, return the index where it would be if it were inserted in order.

def find_index(arr, n, K):
     
    # Traverse the array
    for i in range(n):
         
        # If K is found
        if arr[i] == K:
            return i
             
        # If arr[i] exceeds K
        elif arr[i] > K:
            return i
             
    # If all array elements are smaller
    return n
 
# Driver Code
arr = [1, 3, 5, 6]
n = len(arr)
K = 2
print(find_index(arr, n, K))


# In[12]:


#You are given a large integer represented as an integer array digits, where each
#digits[i] is the ith digit of the integer. The digits are ordered from most significant
#to least significant in left-to-right order. The large integer does not contain any
#leading 0's.

def AddOne(digits):
    
    # initialize an index (digit of units)
    index = len(digits) - 1
      
    # while the index is valid and the value at [index] ==
    # 9 set it as 0
    while (index >= 0 and digits[index] == 9):
        digits[index] = 0
        index -= 1
          
    # if index < 0 (if all digits were 9)
    if (index < 0):
        
        # insert an one at the beginning of the vector
        digits.insert(0, 1)
          
    # else increment the value at [index]
    else:
        digits[index]+=1
  
  
digits = [1,2,3]
  
AddOne(digits)
  
for digit in digits:
    print(digit, end =' ')


# In[14]:


#Given a non-empty array of integers nums, every element appears twice except
#for one. Find that single one.

def findSingle(A, ar_size):
    
    # iterate over every element
    for i in range(ar_size):
        
        # Initialize count to 0
        count = 0
        for j in range(ar_size):
            
            # Count the frequency
            # of the element
            if(A[i] == A[j]):
                count += 1
  
        # If the frequency of
        # the element is one
        if(count == 1):
            return A[i]
            
    # If no element exist
    # at most once
    return -1
  
ar = [2, 2,1]
n = len(ar)
# Function call
print("Element occurring once is", findSingle(ar, n))


# In[16]:


#You are given an inclusive range [lower, upper] and a sorted unique integer array
#nums, where all elements are within the inclusive range.

#A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

#Return the shortest sorted list of ranges that exactly covers all the missing
#numbers. That is, no element of nums is included in any of the ranges, and each
#missing number is covered by one of the ranges.

def findMissing(arr, n, low, high):
    # Loop through the range of numbers from low to high
    for i in range(low, high+1):
        found = False
     
        # Loop through the array to check if i exists in it
        for j in range(n):
            if arr[j] == i:
                found = True
                break
     
        # If i is not found in the array, print it
        if not found:
            print(i, end=' ')
 
# Driver's code
if __name__ == '__main__':
    # Input array
    arr = [0,1,3,50,75]
    n = len(arr)
    low = 1
    high = 10
 
    # Function call
    findMissing(arr, n, low, high)


# In[19]:


#Given an array of meeting time intervals where intervals[i] = [starti, endi],
#determine if a person could attend all meetings.

class meeting:
 
    def __init__(self, start, end, pos):
 
        self.start = start
        self.end = end
        self.pos = pos
 
# Function for finding maximum
# meeting in one room
 
 
def maxMeeting(l, N):
 
    # Initialising an arraylist
    # for storing answer
    ans = []
 
    # Sorting of meeting according to
    # their finish time.
    l.sort(key=lambda x: x.end)
 
    # Initially select first meeting
    ans.append(l[0].pos)
 
    # time_limit to check whether new
    # meeting can be conducted or not.
    time_limit = l[0].end
 
    # Check for all meeting whether it
    # can be selected or not.
    for i in range(1, N):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
 
    # Print final selected meetings
    for i in ans:
        print(i + 1, end=" ")
 
    print()
 
 
# Driver's code
if __name__ == '__main__':
 
    # Starting time
    s = [1, 3, 0, 5, 8, 5]
 
    # Finish time
    f = [2, 4, 6, 7, 9, 9]
 
    # Number of meetings.
    N = len(s)
 
    l = []
 
    for i in range(N):
 
        # Creating object of meeting
        # and adding in the list
        l.append(meeting(s[i], f[i], i))
 
    # Function call
    maxMeeting(l, N)


# In[ ]:




