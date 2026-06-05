import streamlit as st

st.set_page_config(page_title="Internship Presentation", layout="wide")

st.sidebar.title("📑 Navigation")

# Contents section with expandable menu
choice = st.radio(
    "Select a page:",
    ["Home", "Introduction", "Company Background", "HR Division", "Internship Tasks", "Reflection", "Thank You"],
    key="contents_choice"
)
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
