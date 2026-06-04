import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Internship Presentation", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("📑 Navigation")

# Home button
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"

# Contents section with expandable menu
with st.sidebar.expander("📂 Contents", expanded=True):
    choice = st.radio(
        "Select a page:",
        ["Intro Page", "HR Department Page", "Company Background", "Internship Tasks", "Reflection", "Thank You"],
        key="contents_choice"
    )
    st.session_state.page = choice

# --- Main Display ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align:center;'>Internship Presentation</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Kaneka Malaysia – HR & IT Internship</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Prepared by Husna, UMK</p>", unsafe_allow_html=True)
    st.image("cover_image.png", use_column_width=True)
    st.markdown("---")
    st.success("Use the sidebar to explore the Contents!")

elif st.session_state.page == "Intro Page":
    st.header("👩 Self Introduction")
    st.write("Year 4 student at Fakulti Sains Data dan Komputeran (UMK)...")

elif st.session_state.page == "HR Department Page":
    st.header("📊 HR Organizational Chart")
    st.write("Here is the HR department structure...")

elif st.session_state.page == "Company Background":
    st.header("🏢 Company Background")
    st.write("Kaneka Malaysia overview...")

elif st.session_state.page == "Internship Tasks":
    st.header("📝 Internship Tasks")
    st.write("Tasks completed during internship...")

elif st.session_state.page == "Reflection":
    st.header("💡 Reflection")
    st.write("Key learnings and experiences...")

elif st.session_state.page == "Thank You":
    st.header("🙏 Thank You")
    st.write("Appreciation message and closing remarks.")
