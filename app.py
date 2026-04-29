"""
CryptoGuard AI - Professional Cryptocurrency Security & Analysis Platform
Main application entry point with Streamlit configuration
"""

import streamlit as st
import json
from pathlib import Path

# Configure Streamlit
st.set_page_config(
    page_title="CryptoGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/AbdulRehmanRaza03/CryptoGuard-AI",
        "Report a bug": "https://github.com/AbdulRehmanRaza03/CryptoGuard-AI/issues",
        "About": "CryptoGuard AI - Your Personal Cryptocurrency Guardian"
    }
)

# Custom CSS for dark theme and professional styling
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary-color: #00D9FF;
        --secondary-color: #0A1628;
        --accent-color: #FF006E;
        --success-color: #00BB41;
        --warning-color: #FFB81C;
        --danger-color: #FF4444;
    }
    
    /* Dark theme background */
    .stApp {
        background: linear-gradient(135deg, #0A1628 0%, #1A2847 100%);
        color: #E0E0E0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F2438 0%, #1A3A52 100%);
        border-right: 2px solid #00D9FF;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #00D9FF;
        font-weight: 700;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #00D9FF 0%, #0099CC 100%);
        color: #0A1628;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #00FFFF 0%, #00CCFF 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0, 216, 255, 0.3);
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: #1A3A52;
        color: #E0E0E0;
        border: 2px solid #00D9FF;
        border-radius: 6px;
        padding: 10px;
    }
    
    /* Metric boxes */
    .metric-card {
        background: linear-gradient(135deg, #1A3A52 0%, #0F2438 100%);
        border: 2px solid #00D9FF;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0, 216, 255, 0.1);
    }
    
    /* Success message */
    .stSuccess {
        background-color: rgba(0, 187, 65, 0.1);
        border: 2px solid #00BB41;
        border-radius: 6px;
    }
    
    /* Warning message */
    .stWarning {
        background-color: rgba(255, 184, 28, 0.1);
        border: 2px solid #FFB81C;
        border-radius: 6px;
    }
    
    /* Error message */
    .stError {
        background-color: rgba(255, 68, 68, 0.1);
        border: 2px solid #FF4444;
        border-radius: 6px;
    }
    
    /* Info message */
    .stInfo {
        background-color: rgba(0, 216, 255, 0.1);
        border: 2px solid #00D9FF;
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.markdown("# 🛡️ CryptoGuard AI")
st.sidebar.markdown("---")

# Sidebar info
with st.sidebar:
    st.markdown("""
    ### Version 1.0.0
    
    **Your Personal Cryptocurrency Guardian**
    
    Protect, analyze, and secure your digital assets with AI-powered insights.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Features
    - 📊 Real-time Portfolio Tracking
    - 🔍 Advanced Risk Analysis
    - 🚨 Scam Detection System
    - 📈 Market Dashboard
    - 🤖 AI-Powered Insights
    """)
    
    st.markdown("---")
    
    # Footer links
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[GitHub](https://github.com/AbdulRehmanRaza03/CryptoGuard-AI)")
    with col2:
        st.markdown("[Docs](https://github.com/AbdulRehmanRaza03/CryptoGuard-AI)")
    with col3:
        st.markdown("[Support](https://github.com/AbdulRehmanRaza03/CryptoGuard-AI/issues)")

# Main content area - directed by page selection
def main():
    """Main application flow"""
    st.write("")  # Add spacing
    
    # Page routing handled automatically by Streamlit
    # Pages in the 'pages/' directory are automatically available
    
if __name__ == "__main__":
    main()
