import streamlit as st
from modules.utils import download_file

# Page 1: SuperMenu
def supermenu_page():
    st.title("SuperMenu")
    
    # Cuisine selection
    cuisines = st.multiselect("Select Cuisines", ["American", "Mexican", "Italian", "Indian", "Chinese"])
    
    # File upload section
    file = st.file_uploader("Upload AIO Format XLSX", type=["xlsx"])
    
    # Submit button
    if st.button("Submit"):
        if file and cuisines:
            files = {"file": file.getvalue()}
            data = {"cuisines": ",".join(cuisines)}
            
            # API endpoint to send the data
            api_url = "http://yourapiurl.com/supermenu"
            file_content = download_file(api_url, files, data)
            
            if file_content:
                st.download_button("Download Processed File", file_content, "processed_file.xlsx")
        else:
            st.error("Please select cuisines and upload a file.")