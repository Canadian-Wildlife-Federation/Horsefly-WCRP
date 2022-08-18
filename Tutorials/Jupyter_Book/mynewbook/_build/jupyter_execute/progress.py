#!/usr/bin/env python
# coding: utf-8

# # Progress Tracking Plan

# In[1]:


#creating table 12
import pandas as pd
import numpy as np

df = pd.DataFrame({"Goals / Objectives": [
                    "Goal 1: By 2040, the percent (%) of total linear habitat accessible to anadromous salmon will increase from 81% to 91% within the Horsefly River watershed. ",

                    "Goal 2: By 2023, the total area of overwintering habitat accessible to anadromous salmon will increase by 1,500 m2 within the Horsefly River watershed.",

                    "Objective 1: By 2040, 16 road-stream crossing barriers will be remediated in the Horsefly River watershed." ,

                    "Objective 2: By 2023, a minimum of 1 lateral barrier will be remediated in the Horsefly River watershed." ,

                    "Objective 3: By 2040, 4 dams will be remediated in the Horsefly River watershed." 

                    ],
                   "Indicator": [
                    
                    "Percent (%) of total linear habitat accessible ", 

                    "Total area (m2) of overwintering habitat accessible" , 

                    "The number (#) of road-stream crossings remediated" , 

                    "The number (#) of lateral barriers remediated ",

                    "The number (#) of dams remediated" 
                    ],
                    "Methods": [
                    "Field reports & as-built drawings informing the CWF Barrier Prioritization Model ",

                    "TBD",
                    "CWF tracking within the Barrier Prioritization Model + PSCIS database ",

                    "TBD ",

                    "CWF tracking within the Barrier Prioritization Model "

                    ],
                    "Timeframe": [
                    
                    "Annually", 

                    "TBD" , 

                    "Annually" , 

                    "TBD",

                    "Annually" 
                    ],
                    "Who": [
                    
                    "CWF – Nick M. ", 

                    "CWF – Nick M. " , 

                    "CWF – Nick M. & Betty" , 

                    "CWF – Nick M. & Betty",

                    "CWF – Nick M. & Betty" 
                    ],
                    "Comments": [
                    
                    
                    "See CWF companion document for detailed GIS procedures" ,

                    "Identified as a knowledge gap. Specifics are TBD. ",

                    "See CWF companion document for detailed GIS procedures" ,

                    "Identified as a knowledge gap. Specifics are TBD." ,

                    "See CWF companion document for detailed GIS procedures" 

 
                    ]
                    })

df.style.hide_index()

