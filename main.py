import streamlit as st
import pandas as pd
import numpy as np

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
with st.sidebar.expander("📂 Outline", expanded=True):
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

    # Interactive welcome
    st.success("🚀 Use the sidebar to explore the Contents!")
    if st.button("🎉 Start Presentation"):
        st.balloons()
        st.toast("Welcome Husna! Let’s dive into Data Science 🚀")

    # Fun progress bars for skills
    st.subheader("📊 My Technical Skills")
    skills = {
        "Python": 80,
        "Streamlit": 60,
        "GitHub": 50,
        "Power BI": 40,
        "Data Analytics": 70
    }
    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

    # Interactive chart
    st.subheader("📈 Internship Learning Journey")
    data = pd.DataFrame({
        "Week": list(range(1, 7)),
        "Tasks Completed": np.random.randint(2, 10, 6),
        "Skills Improved": np.random.randint(1, 5, 6)
    })
    st.line_chart(data.set_index("Week"))

    # Fun interactive widget
    st.subheader("🔍 Quick Poll")
    choice = st.radio("Which skill should I improve next?", ["Python", "Streamlit", "Power BI", "GitHub"])
    st.write(f"Thanks! You voted for **{choice}** 💡")

# --- INTRODUCTION ---
elif st.session_state.page == "Introduction":
    st.header("👩 Self Introduction – IT Student")
    st.write("I’m Husna, Year 4 student at Fakulti Sains Data dan Komputeran (UMK).")
    st.write("💡 Passionate about data analytics, e-learning tools, and interactive presentations.")
