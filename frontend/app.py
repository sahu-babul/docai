import os
import streamlit as st
from dotenv import load_dotenv

from process_files import process_files_tab
from explore_data import explore_data_tab

## IMPORTANT: Instructions on how to run the Streamlit app locally can be found in the README.md file.


# Load environment variables
load_dotenv()

# Initialize the session state variables if they are not already set
def initialize_session_state():
    env_vars = {
        'system_prompt': "SYSTEM_PROMPT",
        'schema': "OUTPUT_SCHEMA",
        'blob_conn_str': "BLOB_CONN_STR",
        'blob_url' : "BLOB_ACCOUNT_URL",
        'container_name': "CONTAINER_NAME",
        'cosmos_url': "COSMOS_URL",
        'cosmos_key': "COSMOS_KEY",
        'cosmos_db_name': "COSMOS_DB_NAME",
        'cosmos_documents_container_name': "COSMOS_DOCUMENTS_CONTAINER_NAME",
        'cosmos_config_container_name': "COSMOS_CONFIG_CONTAINER_NAME"
    }
    for var, env in env_vars.items():
        if var not in st.session_state:
            st.session_state[var] = os.getenv(env)

# Initialize the session state variables
initialize_session_state()

# Set page config
st.set_page_config(
    page_title="Document AI",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for tab styling
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #f0f2f6;
        border-radius: 4px;
        padding: 10px 20px;
        margin: 0 2px;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Main app
st.title("Document OCR/AI System")

# Create tabs
tab1, tab2 = st.tabs(["📝 Process Files", "🔍 Explore Data"])

# Tab content
with tab1:
    process_files_tab()

with tab2:
    explore_data_tab()
