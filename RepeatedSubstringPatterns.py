#!/usr/bin/env python
# coding: utf-8

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

# In[12]:


def repeatedSubstringPattern(s):

    for i in range(1, len(s)):
        new_s = [s[x:x+i] for x in range(0, len(s), i)]
        if all(elem == new_s[0] for elem in new_s)==True:
            return True
        else:
            continue
    else:
        return False


# In[13]:


s="ababab"
repeatedSubstringPattern(s)


# In[7]:


s="ababab"
for i in range(1, len(s)):
    for x in range(0,len(s), i):
        x = s[x:x+i]
        print(x)


# In[ ]:




