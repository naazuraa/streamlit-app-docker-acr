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
