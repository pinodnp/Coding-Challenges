#!/usr/bin/env python
# coding: utf-8

# You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
# 
# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.
# 
# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 
# 
# Constraints:
# 
# trips.length <= 1000
# 
# trips[i].length == 3
# 
# 1 <= trips[i][0] <= 100
# 
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 
# 1 <= capacity <= 100000

# In[1]:


def carPooling(trips, capacity):
    """
    :type trips: List[List[int]]
    :type capacity: int
    :rtype: bool
    """
    current_passengers_at_car = 0
    current_location = 0
    start = []
    finish = []
    passengers = []

    for i in range(len(trips)):
        start.append(trips[i][1])
        finish.append(trips[i][2])
        passengers.append(trips[i][0])


    start_line = min(start)
    finish_line = max(finish)

    for i in range(start_line, finish_line):
        while i in start:

            current_passengers_at_car = current_passengers_at_car + passengers[start.index(i)]

            start[start.index(i)] = ""


        while i in finish:

            current_passengers_at_car -= passengers[finish.index(i)]


            finish[finish.index(i)] = ""


        if current_passengers_at_car > capacity:
            return False
        else:
            continue
    return True


# In[78]:


trips = [[3,6,9],[10,2,3],[1,6,8],[2,1,6],[9,3,9]]
capacity = 12
carPooling(trips, capacity)

