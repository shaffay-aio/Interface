import streamlit as st
from modules.utils import download_file
import time

# Page 3: OnlinetoAIO
def onlinetoaio_page():
    st.title("Online to AIO")
    
    ################
    # SECTION - 1  #
    ################

    # Section 1: Scraped Middleware File
    st.header("Scraped Middleware File")
    platform = st.selectbox("Select Platform", ["Doordash", "Ubereats", "Toast"])
    url = st.text_input("Enter URL")
    
    # Submit button for Section 1
    submit_section1 = st.button("Submit URL", key="section1_submit")

    # State for processing flags
    if 'section1_processing' not in st.session_state:
        st.session_state.section1_processing = False
        
    # Section 1 submit logic
    if submit_section1 and not st.session_state.section1_processing:
        if url:
            st.session_state.section1_processing = True
            with st.spinner("Processing Section 1..."):
                data = {"platform": platform, "input_url": url}
                api_url = "http://44.231.228.32:8040/scraper"
                file_content = download_file(api_url, json_data=data)
                
                if file_content:
                    st.session_state.section1_processing = False
                    st.download_button("Download Midleware", file_content, "middleware.xlsx")
                else:
                    st.session_state.section1_processing = False
                    st.error("Error processing Section 1. Please try again.")
        else:
            st.error("Please provide URL for Section 1.")

    ################
    # SECTION - 2  #
    ################

    # Section 2: Middleware to AIO
    st.header("Middleware To AIO")
    file = st.file_uploader("Upload Middleware File", type=["xlsx"])

    # Submit button for Section 2
    submit_section2 = st.button("Submit Middleware", key="section2_submit")
    
    if 'section2_processing' not in st.session_state:
        st.session_state.section2_processing = False

    # Section 2 submit logic
    if submit_section2 and not st.session_state.section2_processing:
        if file:
            st.session_state.section2_processing = True
            with st.spinner("Processing Section 2..."):
                files = {"file": file.getvalue()}
                api_url = "http://44.231.228.32:8040/onlinetoaioformatter"
                file_content = download_file(api_url, files=files)
                
                if file_content:
                    st.session_state.section2_processing = False
                    st.download_button("Download Processed File Section 2", file_content, "aio-format.xlsx")
                else:
                    st.session_state.section2_processing = False
                    st.error("Error processing Section 2. Please try again.")
        else:
            st.error("Please upload a file for Section 2.")
    
    # Disable other section's button during processing
    if st.session_state.section1_processing:
        st.session_state.section2_processing = True
    if st.session_state.section2_processing:
        st.session_state.section1_processing = True