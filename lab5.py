#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 5 Write a program to implement Fuzzy Relations(Max-Min composition)

import numpy as np
def max_min_composition(R, S):
    result = np.zeros((R.shape[0], S.shape[1]))
    
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            max_min = 0
            for k in range(R.shape[1]):
                max_min = max(max_min, min(R[i, k], S[k, j]))
            result[i, j] = max_min
    return result

R = np.array([[0.7, 0.6], [0.8, 0.3]])
S = np.array([[0.8, 0.1, 0.4], [0.5, 0.6, 0.7]])

result = max_min_composition(R, S)
print("Result of Max-min Composition:")
print(result)


# In[ ]:




