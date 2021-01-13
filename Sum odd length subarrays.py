#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer accepted on the first go
def sumOddLengthSubarrays(arr):
    total_sum = 0

    for i in range(len(arr)):
        for j in range(len(arr),-1,-1):
            if i<j and len(arr[i:j])%2 !=0:
                total_sum = total_sum + sum(arr[i:j])
    return total_sum


# In[ ]:


arr = [1,2]
sumOddLengthSubarrays(arr)

