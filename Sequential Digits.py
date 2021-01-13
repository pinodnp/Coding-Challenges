#!/usr/bin/env python
# coding: utf-8

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# In[14]:


#runtime error: Memory error
def sequentialDigits(low, high):
    lst = []
    for i in range(low,high+1):

        for j in range(len(str(i))-1):

            if int(str(i)[j]) == int(str(i)[j+1])-1:

                continue
            else:
                break
        else:
            lst.append(i)
    return lst


# In[17]:


low = 10
high = 1000000000
sequentialDigits(low, high)


# In[ ]:


each 10 has 9 [1,2,3,4,5,6,7,8,9]
each 100 has 8  [12, 23, 34, 45, 56, 67, 78, 89]
each 1000 has 7 [123,234,345,456,567,678,789]
each 10000 has 6 [1234, 2345, 3456, 4567, 5678, 6789]
each 100000 has 5 [12345, 23456, 34567, 45678, 56789]
each 1000000 has 4 [123456, 234567, 345678, 456789]
each 10000000 has 3 [1234567, 2345678, 3456789]
each 100000000 has 2 [12345678, 23456789]
each 1000000000 has 1 [123456789]


# In[95]:


def sequentialDigits(low, high):
    num = [1,2,3,4,5,6,7,8,9]
    inverse_nums = [9,8,7,6,5,4,3,2,1]
    lst = []

    if len(str(low))!= len(str(high)):

        for i in range(len(str(low))-1, len(str(high))):
            if i<9:
                for j in range(0, inverse_nums[i]):
                    x = int("".join(map(str, num[j:j+num[i]])))
                    if x>=low and x<=high:
                        #print(i, j , int("".join([str(x) for x in num[j:j+num[i]]])))
                        lst.append(x)
            else:
                break

    else:
        i = len(str(high))-1
        for j in range(0, inverse_nums[i]):
            x = int("".join(map(str, num[j:j+num[i]])))
            if x>=low and x<=high:
                #print(i, j , int("".join([str(x) for x in num[j:j+num[i]]])))
                lst.append(x)

    return lst

    
    
    
    


# In[96]:


low = 234
high = 2314
sequentialDigits(low, high)


# In[69]:


low = 1000
high = 13000
if high> int("1"+ "0"*len(str(high))-1):
    b = len(str(high))
    a = len(str(low))-1
else:
    a = len(str(low))-1
    b = len(str(high))-1
for i in range(a,b):
        for j in range(0, inverse_nums[i]):
            print(i,j)


# In[56]:


len(str(low))-1


# In[57]:


len(str(high))-1


# In[64]:


inverse_nums[8]


# In[38]:


lst.append(int("".join([str(x) for x in num[0:i]])))


# In[39]:


lst


# In[ ]:


lst.append(int("".join([str(x) for x in num[0:1]])))
        


# In[76]:


low = 1000
high = 13000
num = [1,2,3,4,5,6,7,8,9]
inverse_nums = [9,8,7,6,5,4,3,2,1]
lst = []

if len(str(low))!= len(str(high)):
    for i in range(len(str(low))-1, len(str(high))):
        print(i,j)


# In[74]:


len(str(low))-1


# In[75]:


len(str(high))-1


# In[ ]:




