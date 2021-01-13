#!/usr/bin/env python
# coding: utf-8

# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:
# 
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
# 
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
# 
# Note:
# 
# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
# 

# In[24]:


def isRobotBounded(instructions):
    position = [0,0,"n"]
    loop = 0

    #(x,y, orientation)

    #orientation can be n,s,e,w
    while loop<=200:
        for i in instructions:
            if i =="R":
                if position[2] == "n":
                    position[2] = "w"
                elif position[2] == "s":
                    position[2] ="e"
                elif position[2] == "e":
                    position[2] = "n"
                elif position[2] == "w":
                    position[2] = "s"

            elif i =="L":
                if position[2] == "n":
                    position[2] = "e"
                elif position[2] == "s":
                    position[2] = "w"
                elif position[2] == "e":
                    position[2] = "s"
                elif position[2] =="w":
                    position[2] = "n"

            elif i =="G":
                if position[2] == "n":
                    position[0] +=1
                elif position[2] == "s":
                    position[0] -=1
                elif position[2] == "e":
                    position[1] -=1
                else:
                    position[1] +=1

    
        loop +=1
        if position == [0,0,"n"]:
            return True

    else:
        return False


# In[26]:


instructions = "GG"
isRobotBounded(instructions)


# In[6]:


countL = 0
countR = 0
countG = 0

for i in instructions:
    if i =="G":
        countG +=1
    elif i =="R":
        countR +=1
    else:
        countL +=1
print("L:" + str(countL),"R:" + str(countR), "G:" + str(countG) )


# In[20]:


instructions = "GGLLGG"
position = [0,0,"n"]
loop = 0

#(x,y, orientation)
#G = straight
#L = turns 90 degrees left
#R = turns 90 degrees right

#orientation can be n,s,e,w
while loop<=4:
    for i in instructions:
        print(i)
        if i =="R":
            if position[2] == "n":
                position[2] = "w"
            elif position[2] == "s":
                position[2] ="e"
            elif position[2] == "e":
                position[2] = "n"
            elif position[2] == "w":
                position[2] = "s"

        elif i =="L":
            if position[2] == "n":
                position[2] = "e"
            elif position[2] == "s":
                position[2] = "w"
            elif position[2] == "e":
                position[2] = "s"
            elif position[2] =="w":
                position[2] = "n"

        elif i =="G":
            if position[2] == "n":
                position[0] +=1
            elif position[2] == "s":
                position[0] -=1
            elif position[2] == "e":
                position[1] -=1
            else:
                position[1] +=1
        
        print(position)
    loop +=1
    if position == [0,0"n"]:
        return True

else:
    return False


# In[ ]:




