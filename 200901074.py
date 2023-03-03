#!/usr/bin/env python
# coding: utf-8

# In[1]:



print ("\t\t200901074 \n      SYED ABDULLAH ASHAR \n      CLEAN IS 0 & DIRT IS 1 ")
def vacuum_world():
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0', 'C': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum :(CAPITAL LETTER) ") #user_input of location vacuum is placed
    status_input = input("Enter status of " + location_input) #user_input if location is dirty or clean

    # determine the other two locations
    if location_input == 'A':
        location_b = 'B'
        location_c = 'C'
    elif location_input == 'B':
        location_b = 'A'
        location_c = 'C'
    else:
        location_b = 'A'
        location_c = 'B'

    status_input_b = input("Enter status of " + location_b)
    status_input_c = input("Enter status of " + location_c)

    print("Initial Location Condition" + str(goal_state))

    # clean the first location
    if status_input == '1':
        goal_state[location_input] = '0'
        cost += 1
        print("Cost for CLEANING " + location_input + " " + str(cost))

    # move to the second location
    if location_input != location_b:
        cost += 1
        print("COST for moving to " + location_b + " " + str(cost))
    if status_input_b == '1':
        goal_state[location_b] = '0'
        cost += 1
        print("Cost for CLEANING " + location_b + " " + str(cost))

    # move to the third location
    if location_input != location_c and location_b != location_c:
        cost += 1
        print("COST for moving to " + location_c + " " + str(cost))
    if status_input_c == '1':
        goal_state[location_c] = '0'
        cost += 1
        print("Cost for CLEANING " + location_c + " " + str(cost))

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

vacuum_world()


# In[ ]:




