#!/usr/bin/env python
# coding: utf-8

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a maximal substring consisting of non-space characters only.

# In[1]:


def lengthOfLastWord(s):
    s_lst = s.split(" ")
    
    for i in range(len(s_lst)-1,-1,-1):
    
        if len(s_lst[i])>0:
            return len(s_lst[i])
        else:
            continue
    else:
        return 0


# In[4]:


s = "a "
lengthOfLastWord(s)

