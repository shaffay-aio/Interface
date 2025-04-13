# TODO: add loading that processing has started
import streamlit as st
import requests

# Page 4: PaperMenu
def papermenu_page():
    st.title("OCR Menu")
    
    # Upload JPEG images
    files = st.file_uploader("Upload JPEG Images", type=["jpeg", "jpg"], accept_multiple_files=True)
    
    # Submit button
    if st.button("Submit"):
        if files:
            # Prepare files for sending to the API as multipart form data
            files_dict = []
            
            # Add each uploaded file to the files_dict with the same form field name 'images'
            for uploaded_file in files:
                files_dict.append(
                    ('images', (uploaded_file.name, uploaded_file.getvalue(), f'image/{uploaded_file.type.split("/")[1]}'))
                )
            
            api_url = 'http://44.231.228.32:8042/ocr'
            
            # Send the files to the API via a POST request
            response = requests.post(api_url, files=files_dict)
            
            if response.status_code == 200:
                # Assuming the server returns the processed file in the response
                file_content = response.content
                st.download_button("Download Processed File", file_content, "ocr-menu.csv")
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        else:
            st.error("Please upload at least one image.")