#!/usr/bin/env python
# coding: utf-8

# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Your algorithm should run in O(n) time and uses constant extra space.

# In[32]:


#Accepted with run time and memory constraints!!!!!!!
#This is the smart solution, depending on the length of the list instead of the values 
#(as 1,2,3 can't be on the list if the len(list)=2)
def firstMissingPositive(nums):
    new_nums = sorted(nums)
    if nums!=[]:  
        for i in range(1, len(new_nums)+1):
            if i not in new_nums:
                return i
        else:
            return new_nums[-1]+1 
    else:
        return 1
                


# In[33]:


nums = [2147483647]
firstMissingPositive(nums)


# In[15]:


#memory error: This is the naive solution
def firstMissingPositive(nums):
    new_nums = sorted(nums)
    if nums!=[]:
        for i in range(1,new_nums[-1]):
            if i not in new_nums:
                return i
        else:
            return new_nums[-1]+1
    else:
        return 1


# In[ ]:


#Fastes run time solution submitted: Not sure what they are doing here
def firstMissingPositive(nums):
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n


# In[ ]:


#best memory efficient solution: Very similar to mine as a concept but using a while loop
def firstMissingPositive(nums):
    mis_ele = 1
    i = 0
    while i < len(nums):
        if mis_ele in nums:
            mis_ele += 1
        else:
            break
        i += 1
    return mis_ele
        

