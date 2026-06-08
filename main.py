import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# ==============================
# 🎨 Sidebar Styling (CSS)
# ==============================
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001233, #002147, #003366, #004080);
        background-size: 200% 200%;
        animation: sparkle 6s ease-in-out infinite;   /* Shimmer effect */
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
    }

    /* Sidebar button */
    [data-testid="stButton"] {
        background-color: #3366cc !important;
        border-radius: 8px;
        border: 1px solid #ffd700;
    }
    [data-testid="stButton"] div {
        color: #ffffff !important;
        font-weight: bold;
    }
    [data-testid="stButton"]:hover {
        background-color: #5fa8f5 !important;
        border: 1px solid #ffd700;
    }

    /* Expander styling */
    [data-testid="stExpander"] {
        background-color: #3366cc !important;
        border-radius: 8px;
        border: 1px solid #ffd700;
    }
    [data-testid="stExpander"] div {
        color: #ffffff !important;
        font-weight: bold;
    }
    [data-testid="stExpander"]:hover {
        background-color: #5fa8f5 !important;
        border: 1px solid #ffd700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# 📂 Sidebar Navigation
# ==============================
st.sidebar.title("Navigation")

# Home button
if st.sidebar.button("🏠 Home", key="home_btn"):
    st.session_state.page = "Home"

# Expander for Slide Chapters
with st.sidebar.expander("📚 Slide Chapter", expanded=True):
    for i in range(1, 6):
        if st.sidebar.button(f"📖 Chapter {i}", key=f"chapter_{i}"):
            st.session_state.page = f"Chapter {i}"

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
if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    # Video background
    video_html = """
    <video autoplay muted loop style="
        position: fixed;
        top: 50;
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
            background: rgba(0,51,102,0.5); /* premium deep blue overlay */            ">
            <img src="images/home_icon.png" width="100">
            <h1>Welcome to My Internship Journey ✨</h1>
            <p style="color:red; font-weight:bold;">Use the sidebar to explore the Contents!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    
        # Centered button under banner
        st.markdown("<div style='text-align:center; margin-top:1rem;'>", unsafe_allow_html=True)
        if st.button("🎉 Start Presentation", key="start_btn"):
            st.balloons()
            st.toast("Welcome Everyone! Let’s dive into my internship journey.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Custom CSS for button styling
        st.markdown(
            """
            <style>
            /* Force all buttons to center-align */
            div[data-testid="stButton"] {
                display: flex-start;
                padding: 80px;
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
        
            /* Button text */
            div[data-testid="stButton"] > button p {
                color: #ffffff !important;             /* White text */
                font-weight: bold !important;
                font-size: 16px !important;
            }
        
            /* Hover effect */
            div[data-testid="stButton"] > button:hover {
                background-color: #5fa8f5 !important;  /* Lighter blue */
                border: 2px solid #ffd700 !important;  /* Gold border stays */
                box-shadow: 0 0 10px #ffd700;          /* Optional glow */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Title & Intro
        st.markdown("<h1 style='text-align:center;'>💻 Internship Presentation</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Kaneka Malaysia – HR & IT Internship</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Prepared by Nurul Husna, UMK – IT Student</p>", unsafe_allow_html=True)

        # Technical Skills
        st.subheader("📊 My Technical Skills")
        skills = {"Python": 70, "Streamlit": 80, "GitHub": 70, "Figma": 70, "Data Analytics": 80}
        for skill, level in skills.items():
            st.write(f"**{skill}**")
            st.progress(level)

        # Internship Learning Journey
        st.subheader("📈 Internship Learning Journey")
        data = pd.DataFrame({
            "Week": list(range(1, 7)),
            "Tasks Completed": np.random.randint(2, 10, 6),
            "Skills Improved": np.random.randint(1, 5, 6)
        })
        st.line_chart(data.set_index("Week"))

        # Quick Poll
        st.subheader("🔍 Quick Poll")
        choice = st.radio("Which skill should I improve next?", ["Python", "Streamlit", "Power BI", "GitHub"])
        st.write(f"Thanks! You voted for **{choice}** 💡")

    page_container(home_content, bg_color="#e6f7ff")

elif st.session_state.page == "Chapter 1":
    page_container(lambda: st.write("📖 Content for Chapter 1"))

elif st.session_state.page == "Chapter 2":
    page_container(lambda: st.write("📖 Content for Chapter 2"))

elif st.session_state.page == "Chapter 3":
    page_container(lambda: st.write("📖 Content for Chapter 3"))

elif st.session_state.page == "Chapter 4":
    page_container(lambda: st.write("📖 Content for Chapter 4"))

elif st.session_state.page == "Chapter 5":
    page_container(lambda: st.write("📖 Content for Chapter 5"))
