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
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 22px;
        text-shadow: 0px 0px 8px rgba(255, 215, 0, 0.7);
    }

    /* Home button styling */
    div[data-testid="stSidebar"] button[kind="secondary"] {
        background-color: #0d2748; /* Dark blue */
        color: #ffffff;
        border: 2px solid #ffd700; /* Gold border */
        border-radius: 10px;
        font-weight: bold;
        padding: 10px 16px;
        transition: all 0.3s ease;
    }
    div[data-testid="stSidebar"] button[kind="secondary"]:hover {
        background-color: #3366cc; /* Lighter blue on hover */
        color: #ffffff;
        border: 2px solid #ffd700;
    }

    /* Expander styling - distinct color to pop out */
    [data-testid="stExpander"] {
        background-color: #0d2748 !important; /* Same blue as Home */
        border-radius: 8px;
        border: 2px solid #ffd700;
    }
    [data-testid="stExpander"] div {
        color: #ffffff !important;
        font-weight: bold;
    }
    [data-testid="stExpander"]:hover {
        background-color: #3366cc !important; /* Lighter hover */
        border: 2px solid #ffd700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")

# Home button (styled in blue + gold border)
if st.sidebar.button("🏠 Home", key="home_btn"):
    st.session_state.page = "Home"

# Expander for Slide Chapters
with st.sidebar.expander("📚 Slide Chapter", expanded=True):
    if st.button("📖 Chapter 1"):
        st.session_state.page = "Chapter 1"
    if st.button("📖 Chapter 2"):
        st.session_state.page = "Chapter 2"
    if st.button("📖 Chapter 3"):
        st.session_state.page = "Chapter 3"
    if st.button("📖 Chapter 4"):
        st.session_state.page = "Chapter 4"
    if st.button("📖 Chapter 5"):
        st.session_state.page = "Chapter 5"
