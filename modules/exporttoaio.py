import streamlit as st
from modules.utils import download_file

API_ENDPOINTS = {
    "Toast":   "http://localhost:8043/toast",
    "Clover":  "http://localhost:8043/clover",
    "Square":  "http://localhost:8043/square",
}

TOAST_LABELS = ["Menu", "Menu Group", "Menu Item", "Menu Option Group", "Menu Option", "Item Selection", "Item Modifier Selection"]

def export_to_aio_page():

    st.title("Export to AIO")

    platform = st.selectbox("Select Platform", ["Toast", "Clover", "Square"])

    # ── File‑upload widgets ─────────────────────
    if platform == "Toast":
        toast_files = [
            st.file_uploader(label, type=["xlsx"], key=f"toast_{i}")
            for i, label in enumerate(TOAST_LABELS)
        ]
        files_to_send = toast_files                              # 7 required files
    else:
        export_file = st.file_uploader("Upload Export File", type=["xlsx"], key=f"{platform}_file")
        files_to_send = [export_file]                            # 1 required file

    # ── Optional Online‑enhancement upload ──────
    apply_online = st.checkbox("Apply Online Enhancement")
    online_file  = None
    if apply_online:
        online_file = st.file_uploader("Upload Online Middleware File", type=["xlsx"], key="online_file")

    # ── Submit ──────────────────────────────────
    if st.button("Submit"):
        # ---------- Mandatory‑file validation ----------
        if any(f is None for f in files_to_send):
            st.error("Please upload all required export files for the selected platform.")
            return
        if apply_online and online_file is None:
            st.error("Online middleware file is required when the enhancement checkbox is ticked.")
            return

        # ---------- Build multipart‑form payload ----------
        files = {
            f"file_{i}": (f.name, f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            for i, f in enumerate(files_to_send)
        }
        if online_file:
            files["online_file"] = (
                online_file.name,
                online_file,
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

        data = {
            "platform": platform,
            "apply_online_enhancement": apply_online,   # backend flag
        }

        # ---------- Pick endpoint & call API ----------
        api_url = API_ENDPOINTS[platform]
        file_content = download_file(api_url, files, data)

        # ---------- Offer download ----------
        if file_content:
            st.download_button(
                "Download Processed File",
                file_content,
                f"{platform.lower()}‑processed.xlsx",
            )
