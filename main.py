import streamlit as st

# --- Sidebar Styling ---
st.markdown(
    """
    <style>
    /* Sidebar background - premium deep blue graimport streamlit as st

# --- Sidebar Styling ---
st.markdown(
    """
    <style>
    /* Sidebar background - premium deep blue gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002147, #001233);
    }

    /* Sidebar title */
    [data-testid="stSidebar"] h2 {
        color: #ffffff;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Sidebar buttons */
    .sidebar-button {
        display: flex;
        align-items: center;
        background-color: #0d2748; /* Default dark blue */
        border-radius: 10px;
        padding: 12px 18px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid #ffd700; /* Gold border */
        font-weight: bold;
        color: #ffffff;
    }
    .sidebar-button:hover {
        background-color: #4a90e2; /* Lighter royal/sky blue */
        border: 1px solid #ffd700;
        color: #ffffff; /* Text stays visible */
    }

    /* Active button styling */
    .sidebar-button:active {
        background-color: #ffd700; /* Gold highlight */
        color: #000000; /* Black text for contrast */
    }

    /* Expander styling - distinct color to pop out */
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

# Home button (separate)
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

# --- Page Rendering ---
def page_container(content_func, bg_color="#f8f9fa"):
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

# Example homepage + chapters
if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown(
        """
        <div class="hero-banner">
            <img src="images/home_icon.png" width="100">
            <h1>Welcome to Your Dashboard ✨</h1>
            <p>Premium design, smooth navigation, and clear insights.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
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
dient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002147, #001233);
    }

    /* Sidebar title */
    [data-testid="stSidebar"] h2 {
        color: #ffffff;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
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
        border: 1px solid #ffd700; /* Gold border */
        font-weight: bold;
        color: #ffffff;
    }
    .sidebar-button:hover {
        background-color: #3366cc; /* Lighter royal blue */
        transform: translateX(5px);
        border: 1px solid #ffd700;
        color: #ffffff; /* Keep text visible */
    }

    /* Expander styling - distinct color to pop out */
    [data-testid="stExpander"] {
        background-color: #0d2748 !important; /* Same blue as Home */
        border-radius: 8px;
        border: 1px solid #ffd700;
    }
    [data-testid="stExpander"] div {
        color: #ffffff !important;
        font-weight: bold;
    }

    /* Hero banner styling */
    .hero-banner {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(90deg, #001f4d, #003366);
        color: white;
        border-radius: 12px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.25);
    }
    .hero-banner h1 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .hero-banner p {
        font-size: 1.2rem;
        font-weight: 300;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")

# Home button (separate)
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

# --- Page Rendering ---
def page_container(content_func, bg_color="#f8f9fa"):
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

# Example homepage + chapters
if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown(
        """
        <div class="hero-banner">
            <img src="images/home_icon.png" width="100">
            <h1>Welcome to Your Dashboard ✨</h1>
            <p>Premium design, smooth navigation, and clear insights.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
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
