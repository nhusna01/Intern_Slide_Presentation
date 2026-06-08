import streamlit as st

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
        color: #f0f0f0;
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
        border: 1px solid #1a3a6e;
    }
    .sidebar-button:hover {
        background-color: #1a3a6e;
        transform: translateX(5px);
        border: 1px solid #ffd700; /* Gold accent */
    }
    .sidebar-label {
        font-weight: 600;
        font-size: 16px;
        color: #ffffff;
    }

    /* Expander styling - distinct color to pop out */
    [data-testid="stExpander"] {
        background-color: #1a3a6e !important; /* Lighter navy shade */
        border-radius: 8px;
        border: 1px solid #ffd700;
    }
    [data-testid="stExpander"] div {
        color: #ffffff !important;
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
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"

# Expander for contents
with st.sidebar.expander("📂 Contents", expanded=True):
    if st.button("👤 Introduction"):
        st.session_state.page = "Introduction"
    if st.button("🏢 Company Background"):
        st.session_state.page = "Company Background"
    if st.button("👥 HR Division"):
        st.session_state.page = "HR Division"
    if st.button("🌱 The Growth Roadmap"):
        st.session_state.page = "The Growth Roadmap"

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

# Example homepage content
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
elif st.session_state.page == "Introduction":
    page_container(lambda: st.write("👤 This is the Introduction page."))
elif st.session_state.page == "Company Background":
    page_container(lambda: st.write("🏢 Company Background details here."))
elif st.session_state.page == "HR Division":
    page_container(lambda: st.write("👥 HR Division information here."))
elif st.session_state.page == "The Growth Roadmap":
    page_container(lambda: st.write("🌱 Growth Roadmap content here."))
