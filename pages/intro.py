import streamlit as st

def intro_page():
    st.header("🙋‍♀️ Self Introduction")

    # Profile section
    st.markdown(
        """
        <div style="text-align:center; padding:1rem; background:rgba(0,51,102,0.1); border-radius:12px;">
            <img src="images/profile_photo.png" width="200" style="border-radius:50%; border:3px solid #ffd700;">
            <h2 style="color:#003366;">Nurul Husna Binti Mohd Napi</h2>
            <p style="font-weight:bold; color:#3366cc;">Year 4 Student – Bachelor of Information Technology with Honours (UMK)</p>
            <p style= "color:#3366cc;">Intern at Kaneka Malaysia – HR Department</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # About Me
    st.subheader("🌸 About Me")
    st.write(
        """
        Hi, my name is Husna! I am currently a Year 4 student at UMK, 
        pursuing Data Science. During my internship at Kaneka Malaysia, 
        I support HR and IT tasks including eform creation, SPL module development, 
        and administrative work. I enjoy learning new tools and improving my technical skills.
        """
    )

    # Skills
    st.subheader("🛠️ My Skills")
    skills = {
        "Python": 70,
        "Streamlit": 80,
        "GitHub": 70,
        "Figma": 70,
        "Data Analytics": 80,
        "Power BI": 50
    }
    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

    # Interests
    st.subheader("💡 My Interests")
    st.markdown(
        """
        - 📚 Learning e-learning tools (iSpring, NotebookLM)
        - ✉️ Improving professional communication and email writing 
        - 📊 Exploring data analytics fundamentals (draw.io)
        - 🎨 Interactive presentation tools (Canva, Streamlit, Figma)
        """
    )

    # Contact
    st.subheader("📞 Contact Me")
    st.write("Phone: 011-12957400")
    st.write("Email: nhusna.napi@gmail.com")
