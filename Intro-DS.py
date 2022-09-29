#!/usr/bin/env python
# coding: utf-8

# In[45]:


A = np.array([3,7,2,4,5])

print(A)


# In[32]:


B = np.array([(1,4),(1,5),(9,2)])
print(B)


# In[46]:


## First element of A 
print(A[0])

##Fifth element of A
print(A[3])

##Last element of A
print(A[-1])

A.size
A.shape


# In[47]:


## Second element in third row of B

print(B[2][1])

print(B.size)

print(B.shape)


# In[12]:


import numpy as np

n_scores = np.array([
   [63, 72, 75, 51, 83],

   [44, 53, 57, 56, 48],

   [71, 77, 82, 91, 76],

   [67, 56, 82, 33, 74],

   [64, 76, 72, 63, 76],

   [47, 56, 49, 53, 42],

   [91, 93, 90, 88, 96],

   [61, 56, 77, 74, 74],
])


print(n_scores.size)


# In[13]:


print(n_scores.shape)


# In[15]:


print(np.max(n_scores))


# In[21]:


print(n_scores.max(axis = 1))


# In[20]:


print(n_scores.max(axis = 0))


# In[19]:


filtered_scores = n_scores[:,1:-1]

print(filtered_scores)

print(filtered_scores.shape)

print(filtered_scores.max(axis=1))


# In[53]:


np.arange(2.0,3.0,0.1)


# In[56]:


import numpy as np

temperatures_week_1= np.array([9.3, 9.6, 7.4, 7.0, 8.5, np.nan, 9.2])
temperatures_week_2=np.array([8.6,6.8, np.nan, 8.1, np.nan, np.nan, 10.1])

print(temperatures_week_1)

print (temperatures_week_2)

print(temperatures_week_1.size)
print(temperatures_week_2.size)

print (temperatures_week_1.max())

print (np.nanmax(temperatures_week_1))

print(temperatures_week_2.max()) 
print(np.nanmax(temperatures_week_2))

print(np.maximum (temperatures_week_1, temperatures_week_2))

print (np. fmax(temperatures_week_1, temperatures_week_2))


# In[59]:


print(np.maximum (temperatures_week_1, temperatures_week_2))



# In[ ]:





# In[69]:


import numpy as np 
A = np.array([

[87, 60, 71, 59, 67], [59, 53, 90, 80, 58],

[80, 89, 60, 79, 77],

[67, 79, 40, 69, 87],

[86, 96, 92, 73, 61],

[70, 66, 75, 80, 57],

[83, 83, 64, 63, 58],

[89, 39, 72, 78, 49],

])

B = np.array([

[36, 59, 75, 51, 68],

[68, 53, 64, 56, 48],

[79, 77, 82,68, 65], [67, 56, 82, 78, 74],

[64, 76, 72, 63, 76],

[47, 76, 49, 53, 42], [91, 93, 90, 88, 96],

[61, 56, 42, 87, 28],

])



print (np.minimum(A, B))


# In[66]:


np.max(A)
np.max(B)

