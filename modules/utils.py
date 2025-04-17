import requests
import streamlit as st

def download_file(api_url, files=None, json_data=None, form_data=None, params=None):
    """
    Send request to API endpoint and return the response content.
    
    Parameters:
    - api_url: The URL of the API endpoint
    - files: Dictionary or list of tuples for file uploads (for multipart/form-data)
    - json_data: Dictionary for JSON payload (for application/json)
    - form_data: Dictionary for form data (for multipart/form-data or application/x-www-form-urlencoded)
    
    Returns:
    - Response content if successful, None otherwise
    """
    if json_data:
        # For JSON endpoints like /scraper
        response = requests.post(api_url, json=json_data)
    elif params:
        # For json and file uploads        
        response = requests.post(api_url, files=files, params=params)        
    else:
        # For file upload endpoints like /ocr
        response = requests.post(api_url, files=files, data=form_data)
    
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error while processing request. Status: {response.status_code}, Message: {response.text}")
        return None