import streamlit as st
from modules.utils import download_file

# Page 4: PaperMenu
def papermenu_page():
    st.title("PaperMenu")
    
    # Upload JPEG images
    files = st.file_uploader("Upload JPEG Images", type=["jpeg", "jpg"], accept_multiple_files=True)
    
    # Submit button
    if st.button("Submit"):
        if files:
            file_data = [f.getvalue() for f in files]
            api_url = "http://yourapiurl.com/papermenu"
            files = {f"file_{i}": (f"file_{i}.jpg", file_data[i], "image/jpeg") for i in range(len(file_data))}
            
            file_content = download_file(api_url, files)
            
            if file_content:
                st.download_button("Download Processed File", file_content, "processed_file.csv")
        else:
            st.error("Please upload at least one image.")