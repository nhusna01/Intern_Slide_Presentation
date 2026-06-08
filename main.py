import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")

# Custom CSS to standardize all sidebar buttons
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #f0f8ff;
        color: #333;
        font-weight: 600;
        font-size: 16px;
        border-radius: 8px;
        padding: 12px 20px;   /* consistent padding */
        margin-bottom: 12px;  /* consistent spacing */
        width: 100%;          /* full width for all buttons */
        min-height: 45px;     /* consistent height for all buttons */
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #cce7ff;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Home button separate ---
st.sidebar.subheader("🏠 Home")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"

# --- Expander for contents ---
with st.sidebar.expander("📂 Contents", expanded=True):
    if st.button("Introduction"):
        st.session_state.page = "Introduction"
    if st.button("Company Background"):
        st.session_state.page = "Company Background"
    if st.button("HR Division"):
        st.session_state.page = "HR Division"
    if st.button("The Growth Roadmap"):
        st.session_state.page = "The Growth Roadmap"


# --- Helper function for consistent container style ---
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

# --- HOME ---
if st.session_state.page == "Home":
    video_html = """
    <video autoplay muted loop style="position:fixed; right:0; bottom:0; min-width:100%; min-height:100%; z-index:-1;">
        <source src="images/intro_vid.mp4" type="video/mp4">
    </video>
    """
    components.html(video_html, height=400)

    def home_content():
        st.markdown("<h1 style='text-align:center;'>💻 Internship Presentation</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Kaneka Malaysia – HR & IT Internship</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Prepared by Nurul Husna, UMK – IT Student</p>", unsafe_allow_html=True)

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

    page_container(home_content, bg_color="#e6f7ff")

# --- INTRODUCTION ---
elif st.session_state.page == "Introduction":
    def intro_content():
        st.header("👩 Self Introduction – IT Student")
        st.write("I’m Husna, Year 4 student at Fakulti Sains Data dan Komputeran (UMK).")
        st.write("💡 Passionate about data analytics, e-learning tools, and interactive presentations.")
    page_container(intro_content, bg_color="#fff0f5")

# --- COMPANY BACKGROUND ---
elif st.session_state.page == "Company Background":
    def company_content():
        st.header("🏢 Company Background")
        st.write("Kaneka Malaysia – HR & IT Internship program overview.")
    page_container(company_content, bg_color="#f5fffa")

# --- HR DIVISION ---
elif st.session_state.page == "HR Division":
    def hr_content():
        st.header("👥 HR Division")
        st.write("Tasks and responsibilities in HR division.")
    page_container(hr_content, bg_color="#ffffe0")

# --- TRAINING DEVELOPMENT ---
elif st.session_state.page == "The Growth Roadmap":
    def growth_content():
        st.header("📚 The Growth Roadmap")
        st.write("Learning modules and SPL creation tasks.")
    page_container(growth_content, bg_color="#f0fff0")
