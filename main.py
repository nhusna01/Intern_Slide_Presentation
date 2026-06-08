import streamlit as st

# --- Sidebar Styling ---
st.markdown(
    """
    <style>
    /* Sidebar background - premium deep blue gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002147, #001233);
    }

    /* Sidebar title - make it pop */
    [data-testid="stSidebar"] h2 {
        color: #ffd700; /* Gold accent */
        font-weight: 900; /* Extra bold */
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 22px;
        text-shadow: 0px 0px 8px rgba(255, 215, 0, 0.7); /* Glow effect */
    }

    /* Sidebar buttons */
    .sidebar-button {
        display: flex;
        align-items: center;
        background-color: #0d2748;
        border-radius: 10px;
        padding: 12px 18px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid #ffd700;
        font-weight: bold;
        color: #ffffff;
    }
    .sidebar-button:hover {
        background-color: #4a90e2; /* Lighter blue */
        border: 1px solid #ffd700;
        color: #ffffff;
    }

    /* Expander styling - distinct color */
    [data-testid="stExpander"] {
        background-color: #3366cc !important; /* Brighter blue */
        border-radius: 8px;
        border: 1px solid #ffd700;
    }
    [data-testid="stExpander"] div {
        color: #ffffff !important;
        font-weight: bold;
    }
    [data-testid="stExpander"]:hover {
        background-color: #5fa8f5 !important; /* Even lighter hover */
        border: 1px solid #ffd700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
