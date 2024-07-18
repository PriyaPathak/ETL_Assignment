# ETL Assignment - Data Scientist 
![](https://img.shields.io/badge/-Python-informational?logo=Python&color=9F9393) ![](https://img.shields.io/badge/docker-BLUE)

## File Structure

**- ETL_code**
- data : 
    - dataset : contains the dataset formed by scraped data which is then consumed in a DASK API 
    - excel_data : contains the .xlsx file which is scraped from the given web link
    - html_data : all the html files stored after scraping
    - zip_data : the scraped html files are zipped and stored in this folder
- log : This folder contains the debug.log file that stores all the log information related to the ETL run.
- modules : BaseModule file contains the source code of the implementation.
- test: Contains the Pytest unit tests configured to test the module implementation. 

**-main.py:** This is the py file that executes the complete functionality.  
**-Dockerfile:** Contains the definitions to create the Docker container.  
**-requirements.txt:** Contains the packages required to build the application in Docker.  

## Package Information 
- beautifulsoup4 : https://pypi.org/project/beautifulsoup4/ 
- dask[complete] : Dask is a free and open-source library for parallel computing in Python. Dask helps you scale your data science and machine learning workflows. https://docs.dask.org/en/stable/ 
- openpyxl : a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files. https://pypi.org/project/openpyxl/ 
- pytest : pytest is a mature full-featured Python testing tool that helps you write better programs. https://pypi.org/project/pytest/ 
- requests : The requests module in Python allows you to exchange requests on the web. https://pypi.org/project/requests/ 
- urllib3 : The urllib3 module is a powerful, sanity-friendly HTTP client for Python. https://pypi.org/project/urllib3/ 
- XlsxWriter : XlsxWriter is a Python module that can be used to write text, numbers, formulas and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file. https://pypi.org/project/XlsxWriter/ 

## Running the code in local IDE:
### 1. Creating Virtual Environment 
You can use any of the tools like venv, conda to create virtual env to store your packages in an isolated env. For this project I used anaconda to create a virtual env and install dependencies from requirements text file. 
```
conda create -n <env_name> python=3.8
```
### 2. Activating Virtual Env
```
conda activate <env_name>
```
### 3. Installing requirements.txt packages 
```
pip install -r requirements.txt
```

### 4. Now, to initiate the code run the main file within virtual env

## Building and Running Docker Container:
#### _Using containerisation it becomes very easy to deploy applications on cloud in production. Since I have used DASK for the transformations, it can leverage the distributed cluster to process large amount of data._ 

Please use the following steps to Build and Run the Docker container.
### Build the Docker container(Please make sure Docker is installed in your system):
After pulling this repository to your system , navigate to the location where the repository is stored.
Then use the following command to build the container :
```
docker build -t etl_assignment:test . 
```

### Run the Container 
You can run the Container by using the following command :
```
docker run  etl_assignment:test
```
However , please note that this will run the application code and after that the container will exit.

To keep the container running please use the following command:
```
docker run -it etl_assignment:test bash
```
This will attach a bash shell with the container and you will access the following dir in container :
```
root@972bb8eeb53f:/usr/app/src# 
```

To run the file run the following in the shell : 
```
root@972bb8eeb53f:/usr/app/src# python main.py
```
This will run the entire process . 
To run the unit test please run the following:
```
root@972bb8eeb53f:/usr/app/src# pytest
```

### Attaching the Container to an IDE:

If you are using VScode then you can install the following extension from the VS-Code marketplace :
```
https://code.visualstudio.com/docs/containers/overview
```
This will help you to attach an IDE with the Container( installs a VS-Code server inside the container ) and then you can then use the IDE to run the code inside the Container Enviornment itself.
