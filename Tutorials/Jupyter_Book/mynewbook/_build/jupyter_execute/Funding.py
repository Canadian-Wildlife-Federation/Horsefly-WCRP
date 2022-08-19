#!/usr/bin/env python
# coding: utf-8

# # Funding Sources
# 
# Table 14. Potential funding sources for plan implementation in the Horsefly River watershed. The Canadian Wildlife Federation and the planning team can coordinate proposal submission through these sources. 

# In[1]:


from IPython.display import display
import pandas as pd

data = pd.read_csv('tables\Table14.csv', index_col=False).style.hide_index()

display(data)

