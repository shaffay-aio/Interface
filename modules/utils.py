import requests
import streamlit as st

# Helper function to trigger API and return downloadable file
def download_file(api_url, files, data=None):

    response = requests.post(api_url, files=files, data=data)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error while processing request. {response.text}")
        return None