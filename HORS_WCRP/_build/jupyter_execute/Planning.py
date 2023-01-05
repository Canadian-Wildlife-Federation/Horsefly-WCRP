#!/usr/bin/env python
# coding: utf-8

# ```{include} /planning-md.md
# :end-before: "# Key Actors"
# ```

# In[1]:


import pandas as pd
import warnings
from myst_nb import glue
#from IPython.display import display, HTML

warnings.filterwarnings('ignore')


data = pd.read_csv('planning_team.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table1", data)


#newerror


# ```{glue:figure} Table1
# :name: "table1"
# 
# *Horsefly River watershed WCRP planning team members. Planning team members contributed to the development of this plan by participating in a series of workshops and document and data review. The plan was generated based on the input and feedback of the local groups and organizations listed in this table.*
# ```

# In[2]:


import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('key_actors_c.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table2", data)


# # Key Actors
# 
# ```{glue:figure} Table2
# :name: "table2"
# 
# *Additional Key Actors in the Horsefly River watershed. Key Actors are the individuals, groups, and/or organizations, outside of the planning team, with influence and relevant experience in the watershed, whose engagement will be critical for the successful implementation of this WCRP.* 
# ```

# ```{include} /planning-md.md
# :start-after: "# Key Actors"
# :end-before: "The primary geographic scope of this WCRP"
# ```

# ```{figure} figure1.png
# ---
# height: 400px
# width: 1000px
# name: fig1
# ---
# *The primary geographic scope — the Horsefly River watershed — located in the Fraser River system.*
# ```

# ```{include} /planning-md.md
# :start-after: "overwintering habitat in the watershed."
# :end-before: "The Horsefly River watershed comprises parts"
# ```

# In[3]:


import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('species_names.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table3", data)


# ```{glue:figure} Table3
# :name: "table3"
# 
# *Target fish species in the Horsefly River watershed. The Secwepemctsín and Western common and scientific species names are provided.*
# ```

# ```{include} /planning-md.md
# :start-after: "{cite}`XFN2021History`)."
# :end-before: "# Target species"
# ```

# ```{figure} figure2.png
# ---
# height: 400px
# width: 1000px
# name: fig2
# ---
# *Potentially accessible stream segments within the Horsefly River watershed. These do not represent useable habitat types, but rather identifies the stream segments within which habitat modelling and barrier mapping and prioritization was undertaken.*
# ```

# ```{include} /planning-md.md
# :start-after: "goal setting, and action planning {cite}`Mazany-Wright2021-rz`."
# :end-before: "Chinook Salmon are the first"
# ```

# In[4]:


from IPython.display import display, HTML
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('Chinook1.csv', index_col=False)

data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# In[5]:


from IPython.display import display, HTML
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

data1 = pd.read_csv('Chinook2.csv', index_col=False)

data1 = data1.style.hide_index().set_properties(**{'text-align': 'left'})

data1.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table4", data1)


# 
# ```{glue:figure} Table4
# :name: "table4"
# 
# *Chinook Salmon population assessments in the Horsefly River watershed. Conservation Unit assessments were undertaken by the [Pacific Salmon Foundation](https://www.salmonexplorer.ca/#!/fraser/chinook/middle-fraser-river-spring-5-2) ([2020](https://salmonwatersheds.ca/libraryfiles/lib_459.pdf)). Designated Unit assessments were undertaken by [COSEWIC](https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry/cosewic-assessments-status-reports/chinook-salmon-2018.html) (2018).*
# ```

# ```{include} /planning-md.md
# :start-after: "### Chinook Salmon | Kekèsu | Oncorhynchus tshawytscha "
# :end-before: "Coho Salmon are the most widely"
# ```

# In[6]:


import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('coho1.csv', index_col=False)
data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# In[7]:


import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('coho2.csv', index_col=False)
data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table5", data)


# 
# 
# ```{glue:figure} Table5
# :name: "table5"
# 
# *Coho Salmon population assessments in the Horsefly River watershed. Conservation Unit assessments were undertaken by the [Pacific Salmon Foundation](https://www.salmonexplorer.ca/#!/fraser/chinook/middle-fraser-river-spring-5-2) ([2020](https://salmonwatersheds.ca/libraryfiles/lib_459.pdf)). Designated Unit assessments were undertaken by [COSEWIC](https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry/cosewic-assessments-status-reports/chinook-salmon-2018.html) (2016).*
# ```

# ```{include} /planning-md.md
# :start-after: "Coho Salmon are the most widely"
# :end-before: "Sockeye Salmon have historically"
# ```

# In[8]:


import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('Sockeye1.csv', index_col=False)
data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])


# In[9]:


import warnings

warnings.filterwarnings('ignore')


data = pd.read_csv('Sockeye2.csv', index_col=False)
data = data.style.hide_index().set_properties(**{'text-align': 'left'})

data.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

glue("Table6", data)


# 
# 
# ```{glue:figure} Table6
# :name: "table6"
# 
# *Sockeye Salmon population assessments in the Horsefly River watershed. Conservation Unit assessments were undertaken by the [Pacific Salmon Foundation](https://www.salmonexplorer.ca/#!/fraser/chinook/middle-fraser-river-spring-5-2) ([2020](https://salmonwatersheds.ca/libraryfiles/lib_459.pdf)). Designated Unit assessments were undertaken by [COSEWIC](https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry/cosewic-assessments-status-reports/chinook-salmon-2018.html) (2017).*
# ```

# ```{include} /planning-md.md
# :start-after: "### Sockeye Salmon | Sqlelten7ùwi | Oncorhynchus nerka"
# ```
