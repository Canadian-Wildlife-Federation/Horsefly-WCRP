#!/usr/bin/env python
# coding: utf-8

# In[1]:


from docx import Document
from myst_nb import glue
from IPython.display import display, Markdown, display_markdown
from functions import head2txt
import pandas as pd
import markdown

# def pasteMD(filename):
#     def breakFun(x):
#         if len(x) == 0:
#             return("\n\n")
#         else:
#             return(x)

#     storeLines = filename.readlines()

#     print(storeLines)   
    
#     #str.cat(print(map(storeLines, FUN=function(x) breakFun(x))))

# pasteMD("markdown-file.md")


#display_markdown(Markdown("markdown-file.md"))


# ```{include} /markdown-file.md
# ```
