import streamlit as st
from modules.papermenu import papermenu_page
from modules.supermenu import supermenu_page
from modules.exporttoaio import export_to_aio_page
from modules.onlinetoaio import onlinetoaio_page

# Set up page configuration
st.set_page_config(page_title="AIO Menu Tool", layout="wide")

# Main navigation
def main():
    # Sidebar with title, description, and selectbox for services
    st.sidebar.title("AIO Menu Tool")  # Title for the sidebar
    
    # A selectbox that allows users to choose a service from a dropdown menu
    selected_service = st.sidebar.selectbox(
        "Select a Service", 
        ["SuperMenu", "Export to AIO", "Online to AIO", "OCR Menu"], 
        index=0  # Default service (SuperMenu)
    )
    
    # Adding some helpful info on the sidebar, e.g., info or contact links
    st.sidebar.markdown("---")
    
    # Action based on the selected service
    if selected_service == "SuperMenu":
        supermenu_page()
    elif selected_service == "Export to AIO":
        export_to_aio_page()
    elif selected_service == "Online to AIO":
        onlinetoaio_page()
    elif selected_service == "PaperMenu":
        papermenu_page()

if __name__ == "__main__":
    main()
