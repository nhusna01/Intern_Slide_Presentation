import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

from pages.intro import intro_page
from pages.company import company_page
from pages.hr import hr_page
from pages.myself import myself_page
from pages.additional import additional_page

st.set_page_config(
    page_title="Internship Presentation",
    page_icon="🎓",
    layout="wide"
) 

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True) 

# ==============================
# 🎨 Global Button Styling (CSS)
# ==============================
st.markdown(
    """
    <style>
    /* Force all buttons to center-align */
    div[data-testid="stButton"] {
        display: flex;
        justify-content: center;
    }

    /* Style the actual button */
    div[data-testid="stButton"] > button {
        background-color: #3366cc !important;  /* Deep blue */
        border: 2px solid #ffd700 !important;  /* Gold border */
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        margin: auto !important;
        cursor: pointer;
    }

    /* Button text (All Chapters Button) */
    div[data-testid="stButton"] > button p {
        color: #ffffff !important;             /* White text */
        font-weight: bold !important;
        font-size: 16px !important;
    }

    /* Expander text (Slide Chapter) */
    [data-testid="stExpander"] div[data-testid="stButton"] > button p {
        color: #ffffff !important;             /* White text */
        font-weight: bold !important;
        font-size: 16px !important;
    }

    /* Hover effect for All Chapters */
    div[data-testid="stButton"] > button:hover {
        background-color: #5fa8f5 !important;  /* Lighter blue */
        border: 2px solid #ffd700 !important;  /* Gold border stays */
        box-shadow: 0 0 10px #ffd700;          /* Optional glow */
    }

    /* Hover effect for Slide Chapter */
    [data-testid="stExpander"] div[data-testid="stButton"] > button:hover {
        background-color: #5fa8f5 !important;
        border: 2px solid #ffd700 !important;
        box-shadow: 0 0 10px #ffd700 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# 🎨 Sidebar Styling (CSS)
# ==============================
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001233, #002147, #003366, #004080);
        background-size: 200% 200%;
        animation: sparkle 6s ease-in-out infinite;
        box-shadow: inset 0 0 25px rgba(255, 215, 0, 0.25);
        border-right: 3px solid #ffd700;
        transition: background 0.8s ease-in-out;
    }
    [data-testid="stSidebar"]:hover {
        background: linear-gradient(180deg, #002147, #003366, #004080, #0055aa);
    }

    @keyframes sparkle {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Sidebar title */
    [data-testid="stSidebar"] h1 {
        color: #ffffff;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 34px;   
        margin-top:-25px;
        margin-bottom: -10px;
    }

    /* Slide Chapter expander header */
    [data-testid="stExpander"] details summary {
        background-color: #3366cc !important;
        border: 2px solid #ffd700 !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        color: white !important;
        font-weight: bold !important;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    /* Hover effect - same as Home button */
    [data-testid="stExpander"] details summary:hover {
        background-color: #5fa8f5 !important;
        border: 2px solid #ffd700 !important;
        box-shadow: 0 0 10px #ffd700 !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# 📂 Sidebar Navigation
# ==============================

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# UMK logo with custom spacing
st.sidebar.markdown(
    "<div style='margin-top:-5px; margin-bottom:-50px;'>",
    unsafe_allow_html=True
)
st.sidebar.image("images/UMK_logo2.png", width=200)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Sidebar title
st.sidebar.title("HomePage")

# Home button
if st.sidebar.button(
    "🏠 Home",
    key="home_btn",
    use_container_width=True
):
    st.session_state.page = "Home"

# Slide Chapters Expander
with st.sidebar.expander("**📚 Slide Chapter**", expanded=False):

    if st.button("📖 Chapter 1", key="chapter1", use_container_width=True):
        st.session_state.page = "Chapter 1"
        st.rerun()

    if st.button("📖 Chapter 2", key="chapter2", use_container_width=True):
        st.session_state.page = "Chapter 2"
        st.rerun()

    if st.button("📖 Chapter 3", key="chapter3", use_container_width=True):
        st.session_state.page = "Chapter 3"
        st.rerun()

    if st.button("📖 Chapter 4", key="chapter4", use_container_width=True):
        st.session_state.page = "Chapter 4"
        st.rerun()

    if st.button("📖 Chapter 5", key="chapter5", use_container_width=True):
        st.session_state.page = "Chapter 5"
        st.rerun()

# ==============================
# 🖼️ Page Rendering Function
# ==============================
def page_container(content_func, bg_color="#3366cc"):
    st.markdown(
        f"""
        <style>
        .page-box {{
            background-color: {bg_color};
            padding: 2rem;
            border-radius: 14px;
            box-shadow: 0 6px 14px rgba(0,0,0,0.25);
            transition: all 0.3s ease-in-out;
            margin-top: 1rem;
        }}
        .page-box:hover {{
            transform: scale(1.01);
            box-shadow: 0 8px 18px rgba(0,0,0,0.35);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown("<div class='page-box'>", unsafe_allow_html=True)
        content_func()
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# 🏠 Homepage + Chapters Content
# ==============================
if st.session_state.page == "Home":
    # Video background
    video_html = """
    <video autoplay muted loop style="
        position: fixed;
        top: 80;
        left: 50;
        width: 100%;
        height: 100vh;
        z-index: -1;
        object-fit: contain;
        background-color: black;
    ">
        <source src="https://nhusna01.github.io/Intern_Slide_Presentation/images/intro_vid.mp4" type="video/mp4">
    </video>
    """
    components.html(video_html, height=550)

    # Overlay content
    def home_content():
        # Hero Banner
        st.markdown(
            """
            <div class="hero-banner" style="
                padding: 2rem;
                border-radius: 20px;
                text-align: center;
                color: white;
                position: relative;
                z-index: 1;
                background: rgba(0,51,102,0.5);
            ">
                <img src="images/Kaneka_logo.png" width="100">
                <h1>Welcome to My Internship Journey ✨</h1>
                <p style="color:red; font-weight:bold;">Use the sidebar to explore the Contents!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Start Presentation button 
        st.markdown(
            """
            <div id="start-btn-container" style="
                display: flex;
                justify-content: center;
                align-items:center;
                margin-top: 1rem;
                width: 100%;
            ">
            """,
            unsafe_allow_html=True
        )
        
        if st.button("🎉 Start Presentation", key="start_btn"):
            st.balloons()
            st.toast("Welcome Everyone! Let’s dive into my internship journey.")
        
        st.markdown("</div>", unsafe_allow_html=True)


        # Title & Intro
        st.markdown("<h1 style='text-align:center;'>💻 Internship Presentation</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Kaneka Malaysia – HR Internship</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Prepared by Nurul Husna, UMK – IT Student</p>", unsafe_allow_html=True)

        # Internship Learning Journey
        st.subheader("📈 Internship Learning Journey")
        data = pd.DataFrame({
            "Week": list(range(1, 7)),
            "Tasks Completed": np.random.randint(2, 10, 6),
            "Skills Improved": np.random.randint(1, 5, 6)
        })
        st.line_chart(data.set_index("Week"))

    page_container(home_content, bg_color="#e6f7ff")


elif st.session_state.page == "Chapter 1":
    intro_page()

elif st.session_state.page == "Chapter 2":
    company_page()

elif st.session_state.page == "Chapter 3":
    hr_page()

elif st.session_state.page == "Chapter 4":
    myself_page()

elif st.session_state.page == "Chapter 5":
    additional_page()
