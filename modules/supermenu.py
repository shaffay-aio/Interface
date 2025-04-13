# TODO: add loading that processing has started
import streamlit as st
from modules.utils import download_file

# Page 1: SuperMenu
def supermenu_page():
    st.title("SuperMenu")
    
    # Cuisine selection
    cuisines = st.multiselect("Select Cuisines", ["american", "mexican"])
    
    # File upload section
    file = st.file_uploader("Upload AIO Format XLSX", type=["xlsx"])
    
    # Submit button
    if st.button("Submit"):
        if file and cuisines:
            files = {"file": file.getvalue()}
            data = {"cuisines": cuisines}
            
            # API endpoint to send the data
            api_url = "http://44.231.228.32:8041/supermenu"
            file_content = download_file(api_url, files=files, form_data=data)
            
            if file_content:
                st.download_button("Download Processed File", file_content, "supermenu-filled-aio-format.xlsx")
        else:
            st.error("Please select cuisines and upload a file.")