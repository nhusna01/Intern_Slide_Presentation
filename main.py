import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Internship Presentation", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("📑 Navigation")

# Default page setup
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Home button (separate from other pages)
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"

# Contents section with expandable menu
with st.sidebar.expander("📂 Contents", expanded=True):
    choice = st.radio(
        "Select a page:",
        ["Introduction", "Company Background", "HR Division", "Internship Tasks", "Reflection", "Thank You"],
        key="contents_choice"
    )
    # Only update if not clicking Home
    if st.session_state.page != "Home":
        st.session_state.page = choice

# --- HOME ---
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align:center; color:#2E86C1;'>💻 Internship Presentation</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#117A65;'>Kaneka Malaysia – HR & IT Internship</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px;'>Prepared by Nurul Husna, UMK – IT Student</p>", unsafe_allow_html=True)
    st.image("cover_image.png", use_column_width=True)
    st.success("🚀 Use the sidebar to explore the Contents!")
    if st.button("🎉 Start Presentation"):
        st.balloons()

# --- INTRODUCTION ---
elif st.session_state.page == "Introduction":
    st.header("👩 Self Introduction – IT Student")
    st.write("I’m Husna, Year 4 student at Fakulti Sains Data dan Komputeran (UMK).")
    st.write("💡 Passionate about data analytics, e-learning tools, and interactive presentations.")
