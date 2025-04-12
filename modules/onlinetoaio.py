import streamlit as st
from modules.utils import download_file

# Page 3: OnlinetoAIO
def onlinetoaio_page():
    st.title("Online to AIO")
    
    # Section 1: Scraped Middleware File
    st.header("Scraped Middleware File")
    platform = st.selectbox("Select Platform", ["Toast", "UberEATS", "DoorDash"])
    url = st.text_input("Enter URL")
    
    # Section 2: Middleware to AIO
    st.header("Middleware To AIO")
    file = st.file_uploader("Upload Middleware File", type=["xlsx"])
    
    # Submit button
    if st.button("Submit"):
        if url and file:
            files = {"file": file.getvalue()}
            data = {"platform": platform, "url": url}
            api_url = "http://yourapiurl.com/onlinetoaio"
            file_content = download_file(api_url, files, data)
            
            if file_content:
                st.download_button("Download Processed File", file_content, "processed_file.xlsx")
        else:
            st.error("Please provide URL and upload a file.")