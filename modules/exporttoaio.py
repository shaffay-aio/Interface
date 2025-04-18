import streamlit as st
from modules.utils import download_file

# API URLs for each platform
# TODO: any deployment links
API_ENDPOINTS = {
    "Toast" : "http://44.231.228.32:8043/toast",
    "Clover": "http://44.231.228.32:8043/clover",
    "Square": "http://44.231.228.32:8043/square",
}

# Toast file labels (7 files)
TOAST_LABELS = [ "menu", "menu_group", "menu_item", "menu_option_group", "menu_option", "item_selection", "item_modifier_selection"]

def export_to_aio_page():
    st.title("Export to AIO")

    # Platform selection
    platform = st.selectbox("Select Platform", ["Toast", "Clover", "Square"])

    # ── File upload widgets ─────────────────────
    if platform == "Toast":
        # Toast has 7 required files
        toast_files = [
            st.file_uploader(label, type=["csv"], key=f"toast_{i}")
            for i, label in enumerate(TOAST_LABELS)
        ]
        files_to_send = toast_files  # All 7 files are required for Toast
    else:
        # Clover and Square have only one required file
        export_file = st.file_uploader("Upload Export File", type=["xlsx"], key=f"{platform}_file")
        files_to_send = [export_file]  # Only 1 file required for Clover/Square

    # ── Optional Online Enhancement upload ──────
    apply_online = st.checkbox("Apply Online Enhancement")
    online_file = None
    if apply_online:
        online_file = st.file_uploader("Upload Online Middleware File", type=["xlsx"], key="online_file")

    # ── Submit button logic ──────────────────────
    if st.button("Submit"):
        # ---------- Mandatory file validation ----------
        if any(f is None for f in files_to_send):
            st.error("Please upload all required export files for the selected platform.")
            return
        if apply_online and online_file is None:
            st.error("Online middleware file is required when the enhancement checkbox is ticked.")
            return

        # ---------- Build multipart form payload ----------
        files = {}
        
        # For Toast, map the 7 files to the correct parameter names (matching backend)
        # TODO: connect and test toast 
        if platform == "Toast":
            files = {}
            for i, file in enumerate(files_to_send):
                files.update({TOAST_LABELS[i] : file.getvalue()})
        
        # For Clover and Square, use a single file for export
        else:
            # TODO: test square + get clover complete result
            files = {"export_file": files_to_send[0].getvalue()}

        # Include online file if uploaded
        if online_file:
            files.update({"online_file": online_file.getvalue()})
        
        # ---------- Pick the correct API endpoint and send request ----------
        api_url = API_ENDPOINTS[platform]
        file_content = download_file(api_url, files=files, params={"apply_online_enhancer": apply_online})

        # ---------- Offer file download to user ----------
        if file_content:
            st.download_button(
                "Download Processed File",
                file_content,
                f"{platform.lower()}-processed.xlsx",
            )
