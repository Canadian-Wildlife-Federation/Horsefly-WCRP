#!/usr/bin/env python
# coding: utf-8

# # Key Ecological Attributes and Current Connectivity Status

# In[1]:


import requests
import json
import pandas

def barrier_extent(barrier_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_extent/items.json?watershed_group_code=HORS&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    blocked_km = result[0]['all_habitat_blocked_km']
    blocked_pct = result[0]['all_habitat_blocked_pct']

    return blocked_km, blocked_pct

def barrier_count(barrier_type):
    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_count/items.json?watershed_group_code=HORS&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    n_passable = result[0]['n_passable']
    n_barrier = result[0]['n_barrier']
    n_potential = result[0]['n_potential']
    n_unknown = result[0]['n_unknown']

    sum_bar = (n_passable, n_barrier, n_potential, n_unknown)

    return n_passable, n_barrier, n_potential, n_unknown, sum(sum_bar)

def barrier_severity(barrier_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_barrier_severity/items.json?watershed_group_code=HORS&barrier_type=' + barrier_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    n_assessed_barrier = result[0]['n_assessed_barrier']
    n_assess_total = result[0]['n_assess_total']
    pct_assessed_barrier = result[0]['pct_assessed_barrier']

    return n_assessed_barrier, n_assess_total, pct_assessed_barrier

def watershed_connectivity(habitat_type):

    request = 'https://features.hillcrestgeo.ca/bcfishpass/functions/postgisftw.wcrp_watershed_connectivity_status/items.json?watershed_group_code=HORS&barrier_type=' + habitat_type

    response_api = requests.get(request)
    parse = response_api.text
    result = json.loads(parse)

    connect_stat = result[0]['connectivity_status']

    return str(round(connect_stat))


# The planning team devised two Key Ecological Attributes (KEAs) and associated indicators to assess the current connectivity status of the watershed – Accessible Habitat and Accessible Overwintering Habitat (Table 7). KEAs are the key aspects of anadromous salmon ecology that are being targeted by this WCRP. The connectivity status of Anadromous Salmon was used to establish goals to improve habitat connectivity in the watershed and will be the baseline against which progress is tracked over time. 
# 
# The current connectivity status assessment relies on GIS analyses to map known and modelled barriers to fish passage, identify stream reaches that have potential spawning and rearing habitat, estimate the proportion of habitat that is currently accessible to target species, and prioritize barriers for field assessment that would provide the greatest gains in connectivity. To support a flexible prioritization framework to identify priority barriers in the watershed, two assumptions are made: 1) any modelled (i.e., passability status is unknown) or partial barriers are treated as complete barriers to passage and 2) the habitat modelling is binary, it does not assign any habitat quality values. As such, the current connectivity status will be refined over time as more data on habitat and barriers are collected. For more detail on how the connectivity status assessments were conducted, see Appendix B. 

# Table 7. Connectivity status assessment for (a) linear habitat (spawning and rearing) and (b) overwintering habitat in the Horsefly River watershed. The Available Habitat KEA is evaluated by dividing the length of linear habitat that is currently accessible to target species by the total length of all linear habitat in the watershed. The Available Overwintering Habitat KEA is evaluated as the sum of all areal overwintering habitat that is accessible to target species. 

# In[2]:


#creating table 7
import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.DataFrame({"Target Species":["Andromous Salmon"],
                   "KEA":["Available Habitat"],
                   "Indicator":["% of total linear habitat"],
                   "Poor":["<80%"],
                   "Fair":[" "],
                   "Good":["81-90%"],
                   "Very Good":[">90%"],
                   "Current Status":[watershed_connectivity("ALL")],
                   "Comments": ["Indicator rating definitions are based on the consensus decisions of the planning team, including the decision not to define Fair. The current status is based on the CWF Barrier Prioritization Model output, which is current as of March 2022."]
                   })
df1 = pd.DataFrame({"Comments": ["Indicator rating definitions are based on the consensus decisions of the planning team, including the decision not to define “Fair”. The current status is based on the CWF Barrier Prioritization Model output, which is current as of March 2022."]})

def highlighttab7(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="<80%" : color = red
    elif val[0:].isdigit() and int(val) < 80 : color = red
    elif val==" ": color = yellow
    elif val=="81-90%"  : color = lgreen
    elif val[0:].isdigit() and (int(val) >= 80 and int(val) < 90) : color = lgreen 
    elif val ==">90%": color = dgreen
    elif val[0:].isdigit() and int(val) >= 90 : color = dgreen 
    else: color = 'white'
    return 'background-color: %s' % color

df.style.applymap(highlighttab7).hide_index()



# In[3]:


#creating table 7
import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.DataFrame({"Target Species":["Andromous Salmon"],
                   "KEA":["Available Overwintering Habitat"],
                   "Indicator":["Total Area (m2) of overwintering habitat accessible"],
                   "Poor":["?"],
                   "Fair":[" ?"],
                   "Good":["? "],
                   "Very Good":[" ? "],
                   "Current Status":[""],
                   "Comments": ["No baseline data exists on the extent of overwintering habitat in the watershed. A priority action is included in the Operational Plan (strategy 2.3) to develop a habitat layer, and this will be used to inform this connectivity status assessment in the future."]
                   })

def highlighttab7b(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="?" : color = red
    elif val[0:].isdigit() and int(val) < 80 : color = red
    elif val==" ?": color = yellow
    elif val=="? "  : color = lgreen
    elif val[0:].isdigit() and (int(val) >= 80 and int(val) < 90) : color = lgreen 
    elif val ==" ? ": color = dgreen
    elif val[0:].isdigit() and int(val) >= 90 : color = dgreen 
    else: color = 'white'
    return 'background-color: %s' % color

df.style.applymap(highlighttab7b).hide_index()


# ![Table7](Table7.png)

# # Barrier Types

# The following table highlights which barrier types pose the greatest threat to anadromous salmon in the watershed. The results of this assessment were used to inform the subsequent planning steps, as well as to identify knowledge gaps where there is little spatial data to inform the assessment for a specific barrier type. 
# 
# Table 8. Barrier Types in the Horsefly River watershed and barrier rating assessment results. For each barrier type listed, "Extent refers to the proportion of anadromous salmon habitat that is being blocked by that barrier type, "Severity" is the proportion of structures for each barrier type that are known to block passage for target species based on field assessments, and "Irreversibility" is the degree to which the effects of a barrier type can be reversed and connectivity restored. The amount of habitat blocked used in this exercise is a representation of total amount of combined spawning and rearing habitat. All ratings in this table have been updated from version 1.0 to version 2.0 of the Horsefly River Watershed Connectivity Remediation Plan based on the most recent field assessments.
# 
# ![table8](Table8.png)

# In[4]:


from ipywidgets import *
import pandas as pd

#condition
def condition(pct):
    rating = ""
    if pct < 20 : rating = "Low"
    elif (pct >= 20) and (pct < 50) : rating = "Medium"
    elif (pct >= 50) and (pct < 80) : rating = "High"
    else : rating = "Very High"
    return rating

#rating classifier
def rating(threat, barrier):
    if threat == "extent":
        if barrier == "DAM":
            pct = barrier_extent(barrier)[1]
            rating = condition(pct)
        elif barrier == "ROAD":
            pct = barrier_extent('ROAD, RESOURCE/OTHER')[1] + barrier_extent('ROAD, DEMOGRAPHIC')[1]
            rating = condition(pct)
    elif threat == "severity":
        if barrier == "DAM":
            pct = barrier_severity(barrier)[2]
            rating = condition(pct)
        elif barrier == "ROAD":
            pct = barrier_severity('ROAD, RESOURCE/OTHER')[2] + barrier_severity('ROAD, DEMOGRAPHIC')[2]
            rating = condition(pct)
            
    return rating
            

        




df = pd.DataFrame({"Barrier Types":["Road-Stream Crossings","Lateral Barriers","Small Dams(<3m height)","Trail-stream Crossings", "Natural Barriers"],
                   "Extent":[rating("extent", "ROAD"),"High",rating("extent", "DAM"), "Low", "Medium"],
                   "Severity":[rating("severity", "ROAD"),"Very High",rating("severity", "DAM"), "Low", "High"],
                   "Irreversibility":["Medium","High","High", "Medium", "Low"],
                   "Overall Threat Rating:":["Very High","High","Medium", "Low", "Low"]
                   })

def highlight(val):
    red = '#ff0000;'
    yellow = '#ffff00;'
    lgreen = '#92d050;'
    dgreen = '#03853e;'

    if val=="Very High": color = red
    elif val=="High": color = yellow
    elif val=="Medium": color = lgreen
    elif val =="Low": color = dgreen
    else: color = 'white'
    return 'background-color: %s' % color

df.style.applymap(highlight).hide_index()


# In[5]:


import requests
import json
import pandas
from myst_nb import glue



#glue class for variables to allow embedding in markdown
glue("dam_km", barrier_extent('DAM')[0])
glue("dam_pct", round(barrier_extent('DAM')[1]))
glue("total_barrier", barrier_severity('DAM')[1])



# ### Small Dams (<3 m height)
# 
# There are {glue:text}`total_barrier` mapped small dams on “potentially accessible” stream segments in the watershed, blocking a total of {glue:text}`dam_km` km (~{glue:text}`dam_pct`% of the total blocked habitat) of modelled spawning and rearing habitat for anadromous salmon, resulting in a medium extent. The extent rating of these structures was confirmed by the planning team. There are two known fish-passage structures in the watershed, including on the dam at the outlet of McKinley Lake. The remaining dams likely block passage for anadromous salmon and would require significant resources to remediate. However, due to the limited extent of dams in the watershed, a final pressure rating of Medium was assigned. Four small dams were identified on the priority barrier list (see Appendix C). Three of the dams require further assessment and confirmation of upstream habitat quality, and the dam observed at the outlet of Kwun Lake does not exist. 

# In[6]:


#glue class for variables to allow embedding in markdown
glue("resource_km", barrier_extent('ROAD, RESOURCE/OTHER')[0])
glue("resource_pct", round(barrier_extent('ROAD, RESOURCE/OTHER')[1]))
glue("demo_km", barrier_extent('ROAD, DEMOGRAPHIC')[0])
glue("demo_pct", round(barrier_extent('ROAD, DEMOGRAPHIC')[1]))
glue("resource_sev", round(barrier_severity('ROAD, RESOURCE/OTHER')[2]))
glue("demo_sev", round(barrier_severity('ROAD, DEMOGRAPHIC')[2]))

sum_road = (barrier_severity('ROAD, RESOURCE/OTHER')[1], barrier_severity('ROAD, DEMOGRAPHIC')[1])


glue("sum", sum(sum_road))


# ### Road-stream Crossings
# 
# Road-stream crossings are the most abundant barrier type in the watershed, with {glue:text}`sum` assessed and modelled crossings located on stream segments with modelled habitat. Demographic road crossings (highways, municipal, and paved roads) block {glue:text}`demo_km` km of habitat (~{glue:text}`demo_pct`% of the total blocked habitat), with {glue:text}`demo_sev`% of assessed crossings having been identified as barriers to fish passage. Resource roads block {glue:text}`resource_km` km of habitat (~{glue:text}`resource_pct`%), with {glue:text}`resource_sev`% of assessed crossings having been identified as barriers. The planning team felt that the data was underestimating the severity of road-stream crossing barriers in the watershed, and therefore decided to update the rating from High to Very High. The planning team also felt that an irreversibility rating of Medium was appropriate due to the technical complexity and resources required to remediate road-stream crossings. 

# ### Trail-stream crossings 
# 
# There is very little spatial data available on trail-stream crossings in the watershed, so the planning team was unable to quantify the true Extent and Severity of this barrier type. However, the planning team felt that trail-stream crossings are not prevalent within the watershed and that, where they do exist, they do not significantly impact passage for anadromous salmon. As most crossings will be fords or similar structures, remediation may not be required, or remediation costs associated with these barriers would be quite low. Overall, the planning team felt that the pressure rating for trail-stream crossings was likely Low; however, the lack of ground-truthed evidence to support this rating was identified as a knowledge gap within this plan. 

# ### Lateral Barriers 
# 
# There are numerous types of lateral barriers that potentially occur in the watershed, including dykes, berms, and linear development (i.e., road and rail lines), all of which can restrict the ability of anadromous salmon to move into floodplains, riparian wetlands, and other off-channel habitats. No comprehensive lateral barrier data exists within the watershed, so pressure ratings were based on qualitative local knowledge. Lateral barriers are not thought to be as prevalent as road- or rail-stream crossings but are likely very severe where they do exist. Significant lateral barriers are known to occur along the mainstem of the Horsefly River, which disconnect the mainstem river from historic floodplain and off-channel habitat. Overall, the planning team decided that a High pressure rating adequately captured the effect that lateral barriers are having on connectivity in the watershed. Work to begin quantifying and mapping lateral habitat will begin in 2022-23, as described in the Operational Plan under Strategy 2: Lateral barrier remediation.  

# ### Natural Barriers 
# 
# Natural barriers to fish passage can include debris flows, log jams, sediment deposits, etc., but natural features that have always restricted fish passage (e.g., waterfalls) are not considered under this barrier type. Natural barriers are difficult to include in a spatial prioritization framework due to their transient nature. The planning team identified known natural barriers that occur throughout the watershed, such as beaver dams and log jams. Generally, these natural barriers are only severe impediments to fish passage during low-flow years, but reduced baseflows have become more common in recent years. Based on this, the planning team felt that natural barriers will be severe most years where they exist, but are mostly reversible, resulting in an overall pressure rating of Low. 
