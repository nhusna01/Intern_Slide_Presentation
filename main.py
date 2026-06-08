import streamlit as st

# ==============================
# 🎨 Sidebar Styling (CSS)
# ==============================
st.markdown(
    """
    <style>
    /* Sidebar background - premium deep blue gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002147, #001233);
    }

    /* Sidebar title */
    [data-testid="stSidebar"] h1 {
        color: #ffffff;       /* White text */
        font-weight: bold;    /* Bold font */
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }


    /* Sidebar buttons - styled like Slide Chapter expander */
.sidebar-button {
    display: flex;
    align-items: center;
    background-color: #3366cc;   /* Same as expander */
    border-radius: 8px;          /* Match expander corners */
    padding: 12px 18px;
    margin-bottom: 12px;
    transition: all 0.3s ease;
    cursor: pointer;
    border: 1px solid #ffd700;   /* Gold border */
    font-weight: bold;
    color: #ffffff;              /* White text */
}

.sidebar-button:hover {
    background-color: #5fa8f5;   /* Same hover as expander */
    border: 1px solid #ffd700;
    color: #ffffff;
}

.sidebar-button:active {
    background-color: #ffd700;   /* Gold highlight */
    color: #000000;              /* Black text for contrast */
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

# ==============================
# 📂 Sidebar Navigation
# ==============================
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

# ==============================
# 🖼️ Page Rendering Function
# ==============================
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

# ==============================
# 🏠 Homepage + Chapters Content
# ==============================
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
