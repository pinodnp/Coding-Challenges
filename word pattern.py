#!/usr/bin/env python
# coding: utf-8

# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# 
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
# 
# Solution accepted and beated 85% in runtime and 98% of the people in memory usage

# In[11]:


def wordPattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = list(str.split(" "))
        new_lst = []
        d = {}
        for i in range(len(lst)):
            if lst[i] not in new_lst:
                new_lst.append(lst[i])
                d[lst[i]] = [i]
            else:
                d[lst[i]].append(i)
        
        print(d)
        
        lst_p = list(pattern)
        new_lst_p=[]
        d_p={}
        for j in range(len(lst_p)):
            if lst_p[j] not in new_lst_p:
                new_lst_p.append(lst_p[j])
                d_p[lst_p[j]] = [j]
            else:
                d_p[lst_p[j]].append(j)
        print(d_p)
        
        if len(new_lst) !=len(new_lst_p):
            return False
        
        else:
            for x in range(len(new_lst)):
                if d[new_lst[x]] != d_p[new_lst_p[x]]:
                    return False
                else:
                    continue
            else:
                return True
        
        
        
        
       
                
            
        
        


# In[12]:


pattern = "abba"
str = "dog cat cat dog"
wordPattern(pattern, str)

