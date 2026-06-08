import streamlit as st

# --- Sidebar Styling ---
st.markdown(
    """
    <style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #001f4d; /* Dark Blue */
    }

    /* Sidebar buttons */
    .sidebar-button {
        display: flex;
        align-items: center;
        background-color: #003366;
        border-radius: 8px;
        padding: 10px 16px;
        margin-bottom: 10px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .sidebar-button:hover {
        background-color: #004080;
        transform: scale(1.02);
    }
    .sidebar-label {
        font-weight: 600;
        font-size: 16px;
        color: #ffffff;
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
def page_container(content_func, bg_color="#f0f8ff"):
    st.markdown(
        f"""
        <style>
        .page-box {{
            background-color: {bg_color};
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: all 0.3s ease-in-out;
        }}
        .page-box:hover {{
            transform: scale(1.01);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
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
    page_container(lambda: st.write("Welcome to the Homepage! 🎉"))
elif st.session_state.page == "Introduction":
    page_container(lambda: st.write("This is the Introduction page."))
elif st.session_state.page == "Company Background":
    page_container(lambda: st.write("Company Background details here."))
elif st.session_state.page == "HR Division":
    page_container(lambda: st.write("HR Division information here."))
elif st.session_state.page == "The Growth Roadmap":
    page_container(lambda: st.write("Growth Roadmap content here."))
