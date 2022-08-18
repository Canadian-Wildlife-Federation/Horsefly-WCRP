#!/usr/bin/env python
# coding: utf-8

# # Funding Sources
# 
# Table 14. Potential funding sources for plan implementation in the Horsefly River watershed. The Canadian Wildlife Federation and the planning team can coordinate proposal submission through these sources. 

# In[1]:


#creating table 14
import pandas as pd
import numpy as np

df = pd.DataFrame({"Funding Source": [
    
                                        "Land Based Investment Strategy ",

                                        "Environmental Enhancement Fund ",

                                        "Community Salmon Program ",

                                        "Southern Boundary Restoration and Enhancement Fund ",

                                        "Habitat Conservation Trust Foundation Enhancement and Restoration Grants ",

                                        "Environmental Damages Fund ",

                                        "Habitat Stewardship Program for Aquatic Species at Risk",


                                        "Canada Nature Fund for Aquatic Species at Risk", 

                                        "BC Salmon Restoration and Innovation Fund ",

                                        "Aboriginal Fund for Species at Risk" ,

                                        "Federal Gas Tax Fund - Community Works Fund", 

                                        "Disaster Mitigation and Adaptation Fund", 

                                        "Community Gaming Grants", 

                                        "Sitka Foundation ",

                                        "TULA Foundation ",

                                        "Vancouver Foundation" ,

                                        "BC Conservation Foundation Small Project Fund ",

                                        "Real Estate Foundation of BC General Grants "

                                        


                                        ],


                   "Spending Restrictions and Other Consideration ": [
                    
                    "Assessment and remediation of fish passage using provincial strategic approach. Primarily for remediation of Ministry-owned/orphaned barriers on forest service roads." ,

                    "Fish and wildlife passage improvements and restoration at stream and animal crossings at MOTI roads including culvert retrofits and replacement to restore Pacific salmon and trout access, and wildlife tunnels. Primarily for crossings linked to highway infrastructure.", 

                    "For projects supporting the protection, conservation and enhancement or rehabilitation of Pacific salmonids and their habitat. Funding for volunteer and not-for-profit community-based groups. Applicant must have a significant volunteer component to their group and to the project. Requires 50% match for funding (volunteer, in-kind, donation or other grants).",  

                    "Supports 3 activities: (1) develop improved information for resource management; (2) Rehabilitate and restore marine and freshwater habitat; and (3) enhance wild stock production through low technology techniques. Emphasis for funding is on stocks of conservation concern, particularly those contributing to a fishery and stocks of bilateral fishery relevance." ,

                    "Projects that focus on freshwater wild fish, native wildlife species and their habitats, have the potential to achieve a significant conservation outcome, while maintaining or enhancing opportunities for fishing, hunting, trapping, wildlife viewing and associated outdoor recreational activities. Primary focus is on provincially managed fisheries such as Steelhead and Westslope Cutthroat Trout. Requires 50% funding match.", 

                    "Direct funds received from fines, court orders and voluntary payments to priority projects that will benefit Canada’s natural environment, under 4 categories of improvement (in order of preference): (1) restoration, (2) environmental quality improvement, (3) research and development, and (4) education and awareness.", 

                    "Program for non-profits, Indigenous governments, academic institutions for activities that align with recovery actions identified in SARA recovery documents and/or COSEWIC assessment documents. Project must address one or more of 3 broad categories: (1) Important habitat for aquatic species at risk is improved and/or managed to meet their recovery needs; (2) Threats to aquatic species at risk and/or their habitat are stopped, removed, and/or mitigated; (3) Collaboration and partnerships support the conservation and recovery of aquatic species at risk. Limited to at-risk species listed under COSEWIC and/or SARA as threatened, endangered or special concern.",  

                    "Funding program aimed at addressing priority threats for aquatic species at risk listed as endangered, threatened or Special Concern by COSEWIC, as they align with existing federal, provincial or other local recovery plans. Limited to species in the Columbia and Fraser basins in BC, among other priority areas across Canada. Focus on multi-year, multi-partner initiatives that apply an ecosystem or multi-species approach and create a legacy by enabling recovery actions that carry beyond the life of the funding program. Amounts from $100K-$1M available per year. ",

                    "Funding for Indigenous enterprises, academia, industry associations, stewardship groups and commercial groups to support initiatives that support the protection and restoration of wild Pacific salmon and other BC fish stocks or ensure fish and seafood sector in BC is environmentally and economically sustainable. Five main priorities including species of concern rebuilding through habitat restoration with priority for projects that are part of a watershed-scale restoration plan/prioritization effort; build on successful previous restoration efforts; focus on critical habitat and/or the rehabilitation of natural ecosystem processes.",


                    "Program for Indigenous groups for activities that align with recovery actions identified in SARA recovery documents and/or COSEWIC assessment documents for species listed as Endangered, Threatened, or Special Concern by SARA or COSEWIC. Project must address one or more of 4 broad categories: (1) Habitat for species at risk is improved and/or managed to meet their recovery needs; (2) Threats to species at risk and/or their habitat are stopped, removed and/or mitigated; (3) Collaboration, information sharing and partnership between Indigenous communities, governments and organizations and other interested parties (e.g. federal/provincial/territorial governments, academia, industry, private sector) is enhanced; and (4) Capacity within Indigenous communities, to lead in the stewardship of species at risk and contribute to broader SARA implementation, is strengthened.",  

                    "Funding available to local governments from federal gas tax, with funds to be allocated for a variety of municipal projects/initiatives, including local roads/bridges and disaster mitigation. ",

                    "For those projects where flood risk is high: Funding available to local, regional and provincial governments, private sector, non-profit organizations, and Indigenous groups for projects aimed at reducing the socio-economic, environmental and cultural impacts triggered by natural hazards and extreme weather events and taking into consideration current and future impacts of climate change in communities and infrastructure at high risk. Includes both new construction of public infrastructure and modification/reinforcement of existing infrastructure. Projects must have a minimum of $20 M in eligible expenditures and can be bundled together.",  

                    "Funding for non-profit organizations (check funding program guidelines for specific eligibility requirements) for programs that help to protect and improve the environment by: (1) Conserving or revitalizing local ecosystems, (2) Reducing greenhouse gas emissions, (3) Providing community education or engagement opportunities related to the environment and agriculture or (4) Supporting the welfare of domestic animals and/or wildlife. Grants range from $100K-250K per year. ",


                    "Funding for registered charities, universities, and government agencies (qualified Canadian organizations) for projects related to coastline and watershed conservation and climate change in 4 key areas: \n 1. land, water, and ocean conservation \n 2. scientific research for nature and the environment \n 3. public engagement around the importance of a healthy environment \n 4. innovative conservation efforts in Canadian communities, at the local, provincial, and federal levels ",


                    "Supports various environmental programs of interest to the Foundation on a case-by-case basis. ",

                    "Granting agency for community, social and environmental initiatives for qualified Canadian organizations (charitable organizations, universities, government agencies). Granting programs change on an annual basis.",  

                    "Funding available to Non-profits, fish and wildlife clubs (sportsmen’s associations), businesses, local/regional governments, public organizations and First Nations for projects with demonstrated positive impact for fish, wildlife and habitat, including outreach programs. Preference given to projects where BCCF is not the sole funder. ",

                    "Funding for First Nations, charities and societies, non-governmental organizations, universities and colleges, trade associations, local and regional governments, and social enterprises registered as C3s for sustainable land use and real estate practices in BC. Funds up to 50% of cash portion of a project. "

                    


                   ]
                    })

df.style.hide_index()

