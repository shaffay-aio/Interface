import streamlit as st
from modules.papermenu import papermenu_page
from modules.supermenu import supermenu_page
from modules.exporttoaio import export_to_aio_page
from modules.onlinetoaio import onlinetoaio_page

# Set up page configuration
st.set_page_config(page_title="AIO Menu Tool", layout="wide")

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