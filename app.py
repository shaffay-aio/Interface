import streamlit as st
import requests

# Set up page configuration
st.set_page_config(page_title="AIO Menu Tool", layout="wide")

# Helper function to trigger API and return downloadable file
def download_file(api_url, files, data=None):
    response = requests.post(api_url, files=files, data=data)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Error while processing request.")
        return None

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

# Page 2: ExporttoAIO
def export_to_aio_page():
    st.title("Export to AIO")
    
    # Platform selection
    platform = st.selectbox("Select Platform", ["Toast", "Clover", "Square"])
    
    # File upload based on platform
    if platform == "Toast":
        files = [st.file_uploader(f"Upload File {i+1}", type=["xlsx"], key=f"toast_{i+1}") for i in range(7)]
    else:
        files = [st.file_uploader(f"Upload File", type=["xlsx"], key="single_file")]
    
    # Online enhancement checkbox
    apply_online_enhancement = st.checkbox("Apply Online Enhancement")
    online_file = None
    if apply_online_enhancement:
        online_file = st.file_uploader("Upload Online Enhancement File", type=["xlsx"])
    
    # Submit button
    if st.button("Submit"):
        if any(f is not None for f in files):  # At least one file must be uploaded
            file_data = [f.getvalue() for f in files if f is not None]
            api_url = "http://yourapiurl.com/exporttoaio"
            files = {f"file_{i}": (f"file_{i}.xlsx", file_data[i], "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") for i in range(len(file_data))}
            data = {"platform": platform, "apply_online_enhancement": apply_online_enhancement}
            if online_file:
                files["online_file"] = online_file.getvalue()
            
            file_content = download_file(api_url, files, data)
            
            if file_content:
                st.download_button("Download Processed File", file_content, "processed_file.xlsx")
        else:
            st.error("Please upload at least one file.")

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

# Main navigation
def main():
    page = st.sidebar.radio("Select a Page", ["SuperMenu", "Export to AIO", "Online to AIO", "PaperMenu"])
    
    if page == "SuperMenu":
        supermenu_page()
    elif page == "Export to AIO":
        export_to_aio_page()
    elif page == "Online to AIO":
        onlinetoaio_page()
    elif page == "PaperMenu":
        papermenu_page()

if __name__ == "__main__":
    main()
