import streamlit as st

def intro_page():
    st.markdown("""
    <style>
    .profile-card {
        background: linear-gradient(135deg,
                    rgba(255,255,255,0.15),
                    rgba(255,255,255,0.05));
        backdrop-filter: blur(12px);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid rgba(255,215,0,0.5);
        box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        text-align: center;
        transition: transform 0.3s ease;
    }

    .profile-card:hover {
        transform: scale(1.02);
    }

    .profile-img {
        border-radius: 50%;
        border: 5px solid #FFD700;
        box-shadow: 0 0 20px rgba(255,215,0,0.6);
        margin-bottom: 15px;
    }

    .badge {
        display: inline-block;
        background-color: #3366CC;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
        font-weight: bold;
    }

    .typing {
        overflow: hidden;
        white-space: nowrap;
        border-right: .15em solid orange;
        animation:
            typing 4s steps(40, end),
            blink-caret .75s step-end infinite;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: orange; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    
    st.image("images/myself_icon.jpg", width=220)
    
    st.markdown("""
    <h1 style="color:#003366;text-align:center;">
        Nurul Husna Binti Mohd Napi
    </h1>
    
    <div class="typing" style="color:#3366CC;font-size:18px;text-align:center;">
        Welcome to My Internship Journey ✨
    </div>
    
    <div style="text-align:center; margin-top:20px;">
        <span class="badge">🎓 Year 4 Student</span>
        <span class="badge">💻 Information Technology</span>
        <span class="badge">🏫 Universiti Malaysia Kelantan</span>
        <span class="badge">🏢 HR Intern @ Kaneka Malaysia</span>
    </div>
    """, unsafe_allow_html=True)

  st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("### 🌟 Quick Facts About Me")
        
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Internship Duration", "20 Weeks")
            
            with col2:
                st.metric("Department", "HR")
            
            with col3:
                st.metric("Current Year", "Year 4")

      
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
