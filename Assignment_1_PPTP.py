{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1fae03e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "list[0, 1]\n"
     ]
    }
   ],
   "source": [
    "#1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n",
    "#You may assume that each input would have exactly one solution, and you may not use the same element twice.\n",
    "#You can return the answer in any order\n",
    "\n",
    "#Input: nums = [2,7,11,15], target = 9\n",
    "\n",
    "nums = [2,7,11,15]\n",
    "target = 9\n",
    "\n",
    "if nums[0]+nums[1]==target:\n",
    "    print(list[0,1])\n",
    "\n",
    "elif nums[1]+nums[2]==target:\n",
    "    print(list[1,2])\n",
    "\n",
    "elif nums[2]+nums[3]==target:\n",
    "    print(list[2,3])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8807672c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['k', 2, 2, 'k']\n"
     ]
    }
   ],
   "source": [
    "#2. Gven an integer array nums and an integer val, remove all occurrences of val in nums in-place. \n",
    "#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.\n",
    "\n",
    "#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:\n",
    "\n",
    "#- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.\n",
    "#- Return k.\n",
    "\n",
    "nums = [3,2,2,3]\n",
    "val = 3\n",
    "num=[]\n",
    "\n",
    "for i in range(len(nums)):\n",
    "    if nums[i] == val:\n",
    "        nums[i]='k'\n",
    "print(nums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f4bc0638",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2]\n"
     ]
    }
   ],
   "source": [
    "#3. Given a sorted array of distinct integers and a target value, return the index if the target is found. \n",
    "#If not, return the index where it would be if it were inserted in order.\n",
    "\n",
    "#You must write an algorithm with O(log n) runtime complexity.\n",
    "\n",
    "nums = [1,3,5,6]\n",
    "target = 5\n",
    "k=[]\n",
    "for i in nums:\n",
    "    if i==target:\n",
    "        k.append(nums.index(i))\n",
    "print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "e2d3e810",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 4]\n"
     ]
    }
   ],
   "source": [
    "#4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. \n",
    "#The digits are ordered from most significant to least significant in left-to-right order. \n",
    "#The large integer does not contain any leading 0's.\n",
    "\n",
    "#Increment the large integer by one and return the resulting array of digits.\n",
    "digits = [1,2,3]\n",
    "\n",
    "for i in digits:\n",
    "    if i == max(digits):\n",
    "        i=i+1\n",
    "        digits[2]=i\n",
    "        print(digits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "e148e556",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 2, 3, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "#5. You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, \n",
    "#representing the number of elements in nums1 and nums2 respectively.\n",
    "\n",
    "#Merge nums1 and nums2 into a single array sorted in non-decreasing order.\n",
    "\n",
    "#The final sorted array should not be returned by the function, but instead be stored inside the array nums1.\n",
    "#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.\n",
    "\n",
    "nums1 = [1,2,3,0,0,0]\n",
    "m = 3\n",
    "nums2 = [2,5,6]\n",
    "n = 3\n",
    "\n",
    "num=nums1+nums2\n",
    "num.sort()\n",
    "for i in num:\n",
    "    if i == 0 in num:\n",
    "        num.remove(i)\n",
    "        \n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "d7610ecc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 1]\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "#6. Given an integer array nums, return true if any value appears at least twice in the array, \n",
    "#and return false if every element is distinct.\n",
    "\n",
    "nums = [1,2,3,1]\n",
    "\n",
    "repeaters=False\n",
    "for n1 in range(0,len(nums)):\n",
    "    for n2 in range(1,len(nums)):\n",
    "        if nums[n1]==nums[n2]:\n",
    "            print (nums)\n",
    "            print (nums[n1])\n",
    "            repeaters=True\n",
    "    if repeaters:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "8624eaad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[12, 3, 1, 0, 0]"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.\n",
    "\n",
    "#Note that you must do this in-place without making a copy of the array.\n",
    "\n",
    "nums = [0,1,0,3,12]\n",
    "nums.sort()\n",
    "nums.reverse()\n",
    "nums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "d9030236",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The repeating element is 2\n",
      "and the missing element is 3\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "#8.You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.\n",
    "\n",
    "#You are given an integer array nums representing the data status of this set after the error.\n",
    "\n",
    "#Find the number that occurs twice and the number that is missing and return them in the form of an array.\n",
    "\n",
    "def printTwoElements(nums,  n):\n",
    " \n",
    "    # sorting the array\n",
    "    nums.sort()\n",
    "    print(\"The repeating element is\",end=\" \")\n",
    "    for i in range(0, n - 1):\n",
    "        if(nums[i] == nums[i + 1]):\n",
    "            print(nums[i])\n",
    "            break\n",
    " \n",
    "    print(\"and the missing element is\",end=\" \")\n",
    "    for i in range(1, n + 1):\n",
    "        if(i != nums[i - 1]):\n",
    "            print(i)\n",
    "            break\n",
    "nums = [1,2,2,4]\n",
    "n = len(nums)\n",
    "print(printTwoElements(nums, n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ba91b35",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
