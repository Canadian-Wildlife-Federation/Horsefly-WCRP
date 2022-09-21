#!/usr/bin/env python
# coding: utf-8

# # Planning Team

# Table 1. Horsefly River watershed WCRP planning team members. Planning team members contributed to the development of this plan by participating in a series of workshops and document and data review. The plan was generated based on the input and feedback of the local groups and organizations listed in this table.

# In[1]:


from IPython.display import display, HTML
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


data = pd.read_csv('tables\planning_team.csv', index_col=False).style.hide_index()

display(data)


# # Key Actors
# 
# Table 2. Additional Key Actors in the Horsefly River watershed. Key Actors are the individuals, groups, and/or organizations, outside of the planning team, with influence and relevant experience in the watershed, whose engagement will be critical for the successful implementation of this WCRP. 

# In[2]:


from IPython.display import display
import pandas as pd

data = pd.read_csv('tables\key_actors.csv', index_col=False)

data.style.hide_index().set_properties(**{'text-align': 'left'})

