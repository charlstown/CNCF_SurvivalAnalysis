# CNCF Survival Analysis

For this assignment we have developed a survival analysis on the *Cloud Native Computing Foundation* database using Python scripts, Jupyter Notebooks, ElasticSearch and Kibana.

## 1. Team members

- Carlos Grande 

- Verónica Gómez 

- Pablo Olmos

  

## 2. Repository structure

The repository is organize by folders following the next categories:

- **01_data**: this folder contains all the data needed for the assignment.
  - cncf_git_data.json
  - cncf_git_mapping.json
- **02_src**: this folder contains the library needed to load data and execute the notebooks.
  - elastic_loader.py
  - elastic_finder.py
- **03_notebooks**: this folder contains the notebooks elaborated for the work.
  - 01_LoadingData.ipynb
  - 02_ExploratoryDataAnalysis.ipynb
  - 03_SurvivalAnalysis.ipynb
- **04_results**: this folder contains the resulting images from the Dashboards.
  - Screen_01.png
  - Screen_02.png
  - Screen_Dashboard.png
- **05_exports**: this folder contains the final objects exported from kibana.
- **README.md**: file with the instructions to understand the repository.
- **MDS_Report.pdf**: final report from the assignment.



## 3. Run the repository

To run the repository you need to follow the next instructions:

1. Run **ElasticSearch** and **Kibana**.
2. Open de **DataLoader** notebook, and follow the instructions.
3. Once the Elastic Index has been created run **the notebooks**.
4. Finally open the kibana site and import the objects from the **05_exports** folder.

## 4. Screenshots

![Screen_Dashboard](E:\Datos\00_WIP\00_MasterDataScience\03_DataScience III\RecuperacionInformacion\04_Practicas\0621_PracticaFinal\04_results\Screen_Dashboard.png)

## References & Links

- Cloud Native Computing Foundations website: https://www.cncf.io/
- Github repository: 