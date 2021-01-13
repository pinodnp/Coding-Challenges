#!/usr/bin/env python
# coding: utf-8

# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate digits.
# 
# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# In[102]:


#Didn't work but would have been more efficient
def getHint(secret, guess):
    countB = 0
    countC = 0
    s = []
    g = []
    
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            if secret[i] in s and countC>0 and guess.count(guess[i])<2:
                countC -=1
                countB +=1
                print(secret[i])
                print("yay")
                print(secret[i], guess[i])
                s.append(secret[i])
                print(secret, guess, s)
            else:
                countB +=1
                s.append(secret[i])
                print(secret[i])
                print("woho")
                print(secret, guess, s)
        else:
            print(secret [i])
            if secret[i] in guess:
                if secret[i] in s and guess.count(secret[i])>1:
                    countC +=1
                    print(secret[i], guess[i])
                    print("Nay")
                    s.append(secret[i])
                    g.append(guess[i])
                    print(secret, guess, s)
                if secret[i] not in s:
                    countC +=1
                    print(secret[i], guess[i])
                    print("lol")
                    s.append(secret[i])
                    g.append(guess[i])
                    print(secret, guess, s)

                
    return str(str(countB) + "A"+ str(countC) + "B")


# In[125]:


#Works fine but not super efficient
def getHint(secret, guess):
    countB = 0
    countC = 0
    s = []
    g = []
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            countB +=1
        else:
            g.append(guess[i])
            s.append(secret[i])
            continue
 
    
    for k in range(len(s)):
        if g[k] in s:
            countC+=1
            s.remove(g[k])
            
            
    return str(str(countB) + "A"+ str(countC) + "B")
    
    
        


# In[126]:


secret = "11"

guess = "10"

getHint(secret, guess)

