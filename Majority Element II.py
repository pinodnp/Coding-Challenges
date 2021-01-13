#!/usr/bin/env python
# coding: utf-8

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.

# In[1]:


def majorityElement(nums):
    result = []
    for num in set(nums):
        if nums.count(num)> len(nums)/3:
            result.append(num)
        else:
            continue
    return result


# In[7]:


nums = [3,2,3]
majorityElement(nums)


# In[ ]:




