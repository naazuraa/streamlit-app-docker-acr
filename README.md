# streamlit-app-docker-acr

Test app for Streamlit deployment using Docker on Azure Container Registry and Azure App Service

## Requirements to Get Started

1. Install Docker on your local machine. If you're using company laptop, an admin pass from ICT is needed. Download the installation file here: https://docs.docker.com/desktop/install/windows-install/

2. Install Visual Studio Code 

3. Install Azure Tools and Docker extension in Visual Studio Code

4. Install Azure CLI (needed in case of error in authenticating user). Link here: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli


## Step 1: Ensure all required files are in the same directory

Ensure you have have these four files

1. Python file that contains your streamlit code
2. Dockerfile that containes configuration 
3. YML file for your docker compose instruction
4. Requirements.txt for lists of library needed for your Python script

Below are sample code to have in the files

### app.py
```
import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Test App")
st.markdown("This is an app to try out deployment on Azure using Docker")

uploaded_file = st.file_uploader("Upload a CSV file containing latitude and longitude of your cities of choice", accept_multiple_files=False)

if uploaded_file is not None:
    file_container = st.expander("Check your uploaded CSV file")
    shows = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    file_container.write(shows)

    df = pd.read_csv(uploaded_file)
    df.columns = ['city','lat','lon']
    st.write(df)
    st.map(df)
```   
### Dockerfile
```
FROM python:3.9.0
EXPOSE 8501
CMD mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /app
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
```

### docker-compose.yml
```
services:
  streamlit:
    build:
      dockerfile: ./Dockerfile
      context: ./ 
    ports:
      - "8081:8501"
  ```
### requirements.txt
```
streamlit==1.11.1
azure-core
pandas
```

  
## Step 2: Build image and push to Azure Container Registry

1. Right click on YML file and choose compose up. This will build the image
2. Go under Docker extension and check latest image is there
3. Right click on the latest image and push
4. Choose the correct azure container registry. Make sure you are signed in to the Azure portal
5. Push is usscesful when the last line shows something similar to this:

(latest: digest: sha256:887d9cd8a4b2c716c73b85d7a34e5ed0f21443e7d9d3aa896d10de4f3f765adf size: 3262)
   
## Step 3: Create Azure App Service 
In Azure portal, create a new app service and use the container image as the source for the web app. Click create and wait at least around 5 minutes before the web app can show up. 

Sample CSV file to test the app https://github.com/naazuraa/streamlit-app-docker-acr/blob/main/my.csv


