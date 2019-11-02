#!/usr/bin/env python
# coding: utf-8

# In[11]:


cow_alive_list_test_1 = [False, False, True, True, True]


# In[17]:


cow_alive_list_test_2 = [False, False, False, True, True, True]


# In[22]:


#1 feladat: kód kijavítása

def my_solution2(cow_alive_list):
    fat_alive_cow_index = 0
    thin_alive_cow_index = len(cow_alive_list) - 1
    
    while (fat_alive_cow_index + 1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + 
                          thin_alive_cow_index) / 2)
        if cow_alive_list[middle_cow]:
            thin_alive_cow_index = middle_cow
        else:
            fat_alive_cow_index = middle_cow
            
    if cow_alive_list[thin_alive_cow_index]:
        return fat_alive_cow_index + 2
    else:
        return thin_alive_cow_index + 2
        


# In[ ]:


my_solution2(cow_alive_list_test_1)


# In[ ]:


my_solution2(cow_alive_list_test_2)


# In[26]:


#2. feladat: jkg_evaluators package

import sys
get_ipython().system('{sys.executable} -m pip install jkg_evaluators')


# In[48]:


from jkg_evaluators import dragonfind_10_to_500

def my_solution3(is_dead,
                 number_of_cows):

    middle_cow = int(number_of_cows / 2)
    step_length = number_of_cows
    
    while is_dead(middle_cow + 1) or not is_dead(middle_cow - 1):
        if step_length > 1:
            step_length = int(step_length / 2)
        if is_dead(middle_cow):
            middle_cow = int (middle_cow + step_length)
                
        else:
            middle_cow = int (middle_cow - step_length)
    
    if is_dead(middle_cow):
        return(middle_cow + 1)
    else:
        return(middle_cow)
        


# In[49]:


dragonfind_10_to_500.evaluate(my_solution3)


# In[6]:


def my_solution1(cow_alive_list):
    place = 0
    for cow_is_alive in cow_alive_list:
        place = place + 1
        if cow_is_alive:
            return place
    
    return place + 1
    


# In[7]:


my_solution1(cow_alive_list_test_1)


# In[ ]:





# In[ ]:




