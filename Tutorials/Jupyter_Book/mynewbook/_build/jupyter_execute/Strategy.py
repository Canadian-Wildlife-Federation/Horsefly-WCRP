#!/usr/bin/env python
# coding: utf-8

# # Strategies & Actions
# 
# Table 10. Effectiveness evaluation of identified conservation strategies and associated actions to improve connectivity for target species in the Horsefly River watershed. The planning team identified five broad strategies to implement through this WCRP, 1) crossing remediation, 2) lateral barrier remediation, 3) dam remediation, 4) barrier prevention, and 5) communication and education. Individual actions were qualitatively evaluated based on the anticipated effect each action will have on realizing on-the-ground gains in connectivity. Effectiveness ratings are based on a combination of "Feasibility and "Impact", Feasibility is defined as the degree to which the project team can implement the action within realistic constraints (financial, time, ethical, etc.) and Impact is the degree to which the action is likely to contribute to achieving one or more of the goals established in this plan.
# 
# Strategy 1: Crossing Remediation

# In[1]:


import numpy as np
from IPython.display import display
import pandas as pd

data = pd.read_csv('tables\Strategy1.csv', index_col=False)

def fix_table(val):
    return str(val)

def highlighttab7(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="Medium" or val=="Need more information": color = yellow
    elif val=="Very high" or val=="Very effective" : color = lgreen
    elif val =="High" or val=="Effective": color = dgreen
    else: color = 'white'
    return 'background-color: %s' % color

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index()


# Strategy 2: Lateral Barrier Remediation	

# In[2]:


data = pd.read_csv('tables\Strategy2.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index()


# Strategy 3: Dam Remediation

# In[3]:


data = pd.read_csv('tables\Strategy3.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index()


# Strategy 4: Barrier Prevention

# In[4]:


import pandas as pd

data = pd.read_csv('tables\Strategy4.csv', index_col=False)




data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index()

#display(data)


# Strategy 5: Communication and Education

# In[5]:


data = pd.read_csv('tables\Strategy5.csv', index_col=False)

data = data.replace(np.nan, '', regex=True)

data = data.applymap(fix_table)

data.style.applymap(highlighttab7).hide_index()

