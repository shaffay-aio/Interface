import streamlit as st
from utils import download_file

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