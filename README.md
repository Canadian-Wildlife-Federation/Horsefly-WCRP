# Horsefly River WCRP
This repository is built and maintained by the Canadian Wildlife Federation (CWF). The repository contains a jupyter book and a Quarto book used for the live reporting of the Horsefly River WCRP while pulling relevant data from [bcfishpass](https://github.com/smnorris/bcfishpass).

## Anaconda Prompt
One may want to use a virtual environment with python version 3.7 installed. Jupyter Book has a problem reconciling versions outside of python 3.7 when running locally.

## File structure
In order to change text within the **jupyter book**. only the .md files need to be changed.

For the quarto book, the .qmd files and their text should be updated after pulling the GitHub repo. 

## Quarto Book
In order to replicate the HORS-WCRP for other watersheds in BC using Quarto Book from this repo, follow the following steps:

 - Download quarto for your local machine: https://quarto.org/docs/download/. For more specific information on Quarto please refer to the documentation site: https://quarto.org/docs/guide/. 
 - After choosing your prefered method for rendering the quarto book (i.e., RStudio https://quarto.org/docs/tools/rstudio.html, VS Code https://quarto.org/docs/tools/vscode.html, the command line interface (CLI) of your choosing), clone this GitHub repo and open the folder in the IDE.
 - Because of the python and R code chunks within the qmd files, the environment to which the rederer points to when running python code among R code must be updated so that it reflects the Python executable on your local machine (the python.exe file). For the libraries to work properly, it is recommended to install a "virtual environment" in python on your local machine. Find a useful resource for creating a virtual environment in python here: https://docs.python.org/3/library/venv.html.
 - Change the text within the qmd files to reflect the information for the watershed you wish to make an WCRP for. Additionally, change the code in the API calls to reflect the watershed.


