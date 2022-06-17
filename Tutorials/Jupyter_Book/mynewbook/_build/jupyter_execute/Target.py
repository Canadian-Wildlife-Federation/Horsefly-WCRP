#!/usr/bin/env python
# coding: utf-8

# # Target species

# Target species represent the ecologically and culturally important species for which habitat connectivity is being conserved and/or restored in the watershed. In the Horsefly River watershed, the planning team selected Anadromous Salmon as the target species group, which comprises Chinook Salmon, Coho Salmon, and Sockeye Salmon. The selection of these target species was driven primarily by the targets species of the primary fund supporting this planning work. 

# ### Anadromous Salmonids

# Anadromous salmon are cultural and ecological keystone species that contribute to productive ecosystems by contributing marine-derived nutrients to the watershed and forming an important food source for other species. Salmon species are sacred to the NStQ, having sustained life, trading economies, and culture since time immemorial (Williams Lake First Nation 2021, Xatśūll First Nation 2021, N. Singi pers. comm.). The stewardship of the resources and fisheries in their traditional territories are imbued in the spirit of the NStQ through a symbiotic relationship based on respect – the NStQ never take more salmon than is needed and there is no waste. The entirety of the salmon is used - smoked and dried to sustain the NStQ through the winter months, the roe harvested for consumption, salmon oil rendered to be stored and traded, and the skin used to store the oil (Wilson et al. 1998, Xatśūll First Nation 2021, N. Singi pers. comm.). The salmon runs begin to return to the Horsefly River watershed in early August, and the NStQ traditionally celebrate and feast at this time. The harvest of the salmon strengthens the cultural connection to the land and the waters, providing an important food source for communities and the opportunity to pass knowledge and ceremony to future generations through fishing and fish processing (Xatśūll First Nation 2021, Williams Lake First Nation 2021). 
# 
# Anadromous salmon populations in the Horsefly River watershed have declined significantly in the past few decades, with the populations of all three focal species being listed as Threatened or Endangered by the Committee On the Status of Endangered Wildlife In Canada (COSEWIC). This has been exacerbated by the Big Bar landslide on the Fraser River in 2019, leading the four NStQ communities to voluntarily close the salmon fishery from 2019-2022. The stewardship of their waters continues through the work of the NStQ member communities and the Northern Shuswap Tribal Council. See Appendix A for maps of modelled anadromous salmon habitat in the Horsefly River Watershed. 

# ### Chinook Salmon | Kekèsu | Oncorhynchus tshawytscha 

# Table 4. Chinook Salmon population assessments in the Horsefly River watershed. Conservation Unit assessments were undertaken by the [Pacific Salmon Foundation](https://www.salmonexplorer.ca/#!/fraser/chinook/middle-fraser-river-spring-5-2) ([2020](https://salmonwatersheds.ca/libraryfiles/lib_459.pdf)). Designated Unit assessments were undertaken by [COSEWIC](https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry/cosewic-assessments-status-reports/chinook-salmon-2018.html) (2018).

# In[1]:


from IPython.display import display, HTML
import pandas as pd

data = pd.read_csv('tables\chinook.csv', index_col=False).style.hide_index()

display(data, metadata={
    "tags": [
        "hide_input",
    ]
})

