#!/usr/bin/env python
# coding: utf-8

# In[1]:


from docx import Document
from myst_nb import glue
from IPython.display import display, Markdown, display_markdown
from functions import head2txt

document = Document('MASTER_Horsefly_WCRP.docx')


par1 = head2txt(document,'Acknowledgements', 3)[0]
par2 = head2txt(document,'Acknowledgements', 3)[1]
par3 = head2txt(document,'Acknowledgements', 3)[2]


# # Horsefly River Watershed Secwepemcúl’ecw Connectivity Remediation Plan: 2021 - 2040
# 
# 
# ![foto](spawn.jpg.jpg)
# 
# 
# **Canadian Wildlife Federation**
# 
# **350 Michael Cowpland Drive** 
# 
# **Kanata, Ontario K2M 2W1** 
# 
# **Telephone: 1-877-599-5777 | 613-599-9594** 
# 
# **www.cwf-fcf.org** 
# 
# **© 2022**
# 
# Suggested Citation: 
# 
# Mazany-Wright, N., S. M. Norris, J. Noseworthy, B. Rebellato, S. Sra, and N. W. R. Lapointe. 2022. Horsefly River Watershed Connectivity Remediation Plan: 2021- 2040. Canadian Wildlife Federation. Ottawa, Ontario, Canada.  
# 
# [Download full PDF here!](https://github.com/Canadian-Wildlife-Federation/Horsefly-WCRP/raw/master/Tutorials/Jupyter_Book/mynewbook/_build/pdf/book.pdf)
# 
#  
# 
# 
# # Acknowledgements
# 
# This plan represents the culmination of a collaborative planning process undertaken in the Horsefly River watershed over many months of work with a multi-partner planning team of individuals and groups passionate about the conservation and restoration of freshwater ecosystems and the species they support. Plan development was funded by the BC Salmon Restoration and Innovation Fund, Canada Nature Fund for Aquatic Species at Risk, and the RBC Bluewater Project. We were fortunate to benefit from the feedback, guidance, and wisdom of many groups and individuals who volunteered their time throughout this process — this publication would not have been possible without the engagement of our partners and the planning team (see {numref}`table1`). 
# 
# We recognize the incredible fish passage and connectivity work that has occurred in the Horsefly River watershed to date, and we are excited to continue partnering with local groups and organizations to build upon existing initiatives and provide a road map to push connectivity remediation forward over the next 20 years and beyond. 
# 
# The Canadian Wildlife Federation recognizes that the lands and waters that form the basis of this plan are the traditional unceded territory of the Northern Secwepemc people. We are grateful for the opportunity to learn from the stewards of this land and work together to benefit Pacific Salmon. A special thank you to Nishitha Singi for sharing the traditional Secwepemctsín names used in this plan. 
# 

# In[2]:


# display(Markdown(par1))
# display(Markdown(par2))
# display(Markdown(par3))

