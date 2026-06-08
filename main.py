import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")

def nav_button(icon_path, label, page_name):
    col1, col2 = st.sidebar.columns([1,4])
    with col1:
        st.image(icon_path, width=30)
    with col2:
        if st.button(label, key=page_name):
            st.session_state.page = page_name

# Add buttons with icons
nav_button("images/home_icon.jpg", "Home", "Home")
nav_button("images/self_intro.svg", "Self Introduction", "Self Introduction")
nav_button("images/company_icon.png", "Company Background", "Company Background")
nav_button("images/hr_icon.png", "HR Division", "HR Division")
nav_button("images/self_development.png", "The Growth Roadmap", "The Growth Roadmap")

# --- Helper function for consistent layout ---
def page_container(content_func):
    st.markdown(
        """
        <style>
        .main {
            background-color: rgba(255,255,255,0.9);
            padding: 2rem;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        content_func()

# --- HOME ---
if st.session_state.page == "Home":
    # Background video
    video_html = """
    <video autoplay muted loop style="position:fixed; right:0; bottom:0; min-width:100%; min-height:100%; z-index:-1;">
        <source src="images/intro_vid.mp4" type="video/mp4"
    </video>
    """
    components.html(video_html, height=400)  # give height so video renders

    def home_content():
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

    page_container(home_content)

# --- INTRODUCTION ---
elif st.session_state.page == "Introduction":
    def intro_content():
        st.header("👩 Self Introduction – IT Student")
        st.write("I’m Husna, Year 4 student at Fakulti Sains Data dan Komputeran (UMK).")
        st.write("💡 Passionate about data analytics, e-learning tools, and interactive presentations.")
    page_container(intro_content)

# --- COMPANY BACKGROUND ---
elif st.session_state.page == "Company Background":
    def company_content():
        st.header("🏢 Company Background")
        st.write("Kaneka Malaysia – HR & IT Internship program overview.")
    page_container(company_content)

# --- HR DIVISION ---
elif st.session_state.page == "HR Division":
    def hr_content():
        st.header("👥 HR Division")
        st.write("Tasks and responsibilities in HR division.")
    page_container(hr_content)

# --- TRAINING DEVELOPMENT ---
elif st.session_state.page == "Training Development":
    def training_content():
        st.header("📚 Training Development")
        st.write("Learning modules and SPL creation tasks.")
    page_container(training_content)
