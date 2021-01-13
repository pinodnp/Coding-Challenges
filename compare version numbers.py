#!/usr/bin/env python
# coding: utf-8

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
# 
# You may assume that the version strings are non-empty and contain only digits and the . character.
# 
# The . character does not represent a decimal point and is used to separate number sequences.
# 
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
# 
# You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

# In[44]:


def compareVersion(version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1= list((version1.split(".")))    
        v1 = [int(x) for x in v1]
        v2 = list((version2.split("."))) 
        v2 = [int(x) for x in v2]

        if len(v1)>len(v2):
            y = ("0" * (len(v1)-len(v2)))
            y = list(int(i) for i in y)
            v2.extend(y)
        elif len(v1)<len(v2):
            y = ("0" * (len(v2)-len(v1)))
            y = list(int(i) for i in y)
            v1.extend(y)
        
        for s in range(len(v1)):
            if v1[s]>v2[s]:
                return 1
            elif v1[s]<v2[s]:
                return -1
        else:
            return 0
        
        


# In[45]:


version1 = "0.1"
version2 = "1.1"
compareVersion(version1, version2)

