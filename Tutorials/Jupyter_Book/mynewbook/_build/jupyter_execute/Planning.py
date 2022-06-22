#!/usr/bin/env python
# coding: utf-8

# # Planning Team

# Table 1. Horsefly River watershed WCRP planning team members. Planning team members contributed to the development of this plan by participating in a series of workshops and document and data review. The plan was generated based on the input and feedback of the local groups and organizations listed in this table.

# In[1]:


from IPython.display import display, HTML
import pandas as pd

data = pd.read_csv('tables\planning_team.csv', index_col=False).style.hide_index()

display(data)

