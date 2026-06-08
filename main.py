import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar layout
st.sidebar.title("Navigation")

# Home button with image
col1, col2 = st.sidebar.columns([1,4])
with col1:
    st.image("images/home_icon.jpg", width=30)  # Your uploaded image
with col2:
    if st.button("Home"):
        st.session_state.page = "Home"

# Other pages
if st.sidebar.button("Introduction"):
    st.session_state.page = "Introduction"

if st.sidebar.button("Company Background"):
    st.session_state.page = "Company Background"

if st.sidebar.button("HR Division"):
    st.session_state.page = "HR Division"

if st.sidebar.button("Training Development"):
    st.session_state.page = "Training Development"

# Page content
if st.session_state.page == "Home":
    st.header("Welcome to the Home Page")
    st.write("This is your cover page with the Home icon.")

elif st.session_state.page == "Introduction":
    st.header("Introduction")
    st.write("Content for the Introduction page.")

elif st.session_state.page == "Company Background":
    st.header("Company Background")
    st.write("Content for the Company Background page.")

elif st.session_state.page == "HR Division":
    st.header("HR Division")
    st.write("Content for the HR Division page.")

elif st.session_state.page == "Training Development":
    st.header("Training Development")
    st.write("Content for the Training Development page.")
col1, col2 = st.sidebar.columns([1,4])


# --- HOME ---
if st.session_state.page == "Home":
    # Background video using HTML
    video_html = """
    <video autoplay muted loop style="position:fixed; right:0; bottom:0; min-width:100%; min-height:100%; z-index:-1;">
        <source src="intro_vid.mp4" type="video/mp4">
    </video>
    """
    components.html(video_html, height=0)  # height=0 so it doesn't take space

    # Overlay content
    st.markdown("<h1 style='text-align:center; color:white;'>💻 Internship Presentation</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:white;'>Kaneka Malaysia – HR & IT Internship</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:white;'>Prepared by Nurul Husna, UMK – IT Student</p>", unsafe_allow_html=True)

    st.success("🚀 Use the sidebar to explore the Contents!")
    if st.button("🎉 Start Presentation"):
        st.balloons()
        st.toast("Welcome Everyone! Let’s dive into my internship journey.")

    st.subheader("📊 My Technical Skills")
    skills = {"Python": 70, "Streamlit": 80, "GitHub": 70, "Figma": 70, "Data Analytics": 80}
    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

    st.subheader("📈 Internship Learning Journey")
    data = pd.DataFrame({
        "Week": list(range(1, 7)),
        "Tasks Completed": np.random.randint(2, 10, 6),
        "Skills Improved": np.random.randint(1, 5, 6)
    })
    st.line_chart(data.set_index("Week"))

    st.subheader("🔍 Quick Poll")
    choice = st.radio("Which skill should I improve next?", ["Python", "Streamlit", "Power BI", "GitHub"])
    st.write(f"Thanks! You voted for **{choice}** 💡")

# --- INTRODUCTION ---
elif st.session_state.page == "Introduction":
    st.header("👩 Self Introduction – IT Student")
    st.write("I’m Husna, Year 4 student at Fakulti Sains Data dan Komputeran (UMK).")
    st.write("💡 Passionate about data analytics, e-learning tools, and interactive presentations.")
