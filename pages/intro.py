import streamlit as st


def intro_page():
    # ==============================
    # 🎨 Custom CSS Styling
    # ==============================
    st.markdown(
        """
        <style>
        .profile-card {
            background: linear-gradient(
                135deg,
                rgba(255,255,255,0.15),
                rgba(255,255,255,0.05)
            );
            backdrop-filter: blur(12px);
            padding: 40px;
            border-radius: 25px;
            border: 2px solid rgba(255,215,0,0.5);
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            text-align: center;
            margin-bottom: 25px;
        }

        .badge {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 280px;
            height: 50px;
            background-color: #3366CC;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            margin: 5px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }

        .typing {
            overflow: hidden;
            white-space: nowrap;
            border-right: .15em solid orange;
            animation:
                typing 4s steps(40, end),
                blink-caret .75s step-end infinite;
            display: inline-block;
        }

        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: orange; }
        }

        .contact-box {
            background-color: rgba(51,102,204,0.08);
            padding: 15px;
            border-radius: 12px;
            border-left: 5px solid #3366CC;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ==============================
    # 🙋‍♀️ Self Introduction
    # ==============================
    # Profile Card
    st.markdown("""
    <div class="profile-card">
        <h2 style="font-size:40px; font-weight:bold; color:#003366; margin:0;">
            SELF-INTRODUCTION 🙋‍♀️
        </h2>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div style="text-align:center;">
        <img src="app/static/myself_icon.jpg"
             width="220"
             style="
                border-radius:50%;
                border:5px solid gold;
             ">
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style="color:#003366; text-align:center;">
            Nurul Husna Binti Mohd Napi
        </h1>

        <div style="text-align:center;">
            <div class="typing" style="color:#3366CC; font-size:18px;">
                Here's a quick introduction to who I am.💖
            </div>
        </div>

        <br>

        <div style="text-align:center;">
            <span class="badge">👩‍💼 Year 4 Student</span>
            <span class="badge">💻 Information Technology</span>
            <span class="badge">🏫 Universiti Malaysia Kelantan</span>
            <span class="badge">🏢 HR Intern @ Kaneka Malaysia</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

   

    # ==============================
    # 🌟 Quick Facts
    # ==============================
    st.markdown(
        """
        <h2 style="
            text-align:center;
            color:#003366;
            margin-bottom:30px;
        ">
            🌟 Quick Facts About Me
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    # Custom card styling
    st.markdown("""
    <style>
    .fact-card {
        background: linear-gradient(135deg, #3366CC, #5FA8F5);
        color: white;
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #FFD700;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        height: 180px;
        position: relative;   /* ADD THIS */
    }
    
    .fact-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.3);
    }
    
    .fact-icon {
        font-size: 35px;
        margin-bottom: 10px;
    }
    
    .fact-title {
        font-size: 16px;
        font-weight: bold;
        color: #FFD700;
        margin-bottom: 12px;
    }
    
    .fact-value {
        font-size: 12px;
        font-weight: bold;
    }
    
    /* ADD EVERYTHING BELOW */
    .tooltip {
        position: absolute;
        top: 10px;
        right: 12px;
        cursor: pointer;
        font-size: 16px;
    }
    
    .tooltiptext {
        visibility: hidden;
        width: 140px;
        background-color: white;
        color: black;
        text-align: center;
        border-radius: 8px;
        padding: 8px;
        position: absolute;
        top: -5px;
        right: 25px;
        z-index: 1;
        font-size: 12px;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="fact-card">
            <div class="tooltip">❓
                <span class="tooltiptext">Data Science</span>
            </div>
            <div class="fact-icon">🎓</div>
            <div class="fact-title">Specialization</div>
            <div class="fact-value">
                Bachelor of Information Technology
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fact-card">
            <div class="tooltip">❓
                <span class="tooltiptext">HR Industry Supervisor</span>
            </div>
            <div class="fact-icon">👩‍💼</div>
            <div class="fact-title">Supervisor</div>
            <div class="fact-value">
                Pn. Norkamariah Othman
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="fact-card">
            <div class="tooltip">❓
                <span class="tooltiptext">3/2/2026 - 21/7/2026</span>
            </div>
            <div class="fact-icon">📅</div>
            <div class="fact-title">Internship Journey</div>
            <div class="fact-value">
                26 Weeks
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

        
    # ==============================
    # 🌸 About Me
    # ==============================
    st.subheader("🌸 About Me")

    st.write(
        """
        During my internship at Kaneka Malaysia, I contribute to HR and IT projects such as eForm creation,
        SPL module development, training support, simple data analysis, and administrative tasks. I am 
        passionate about learning new technologies, exploring innovative tools, and continuously enhancing 
        both my technical and professional skills.
        
        """
    )
    

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

    
    # ==============================
    # 🛠️ Skills
    # ==============================
    st.subheader("🛠️ My Skills")

    technical_skills = {
        "Python": 70,
        "Streamlit": 80,
        "GitHub": 70,
        "Figma": 70,
        "Data Analytics": 80,
        "Power BI": 50,
    }

    for skill, level in technical_skills.items():
        st.write(f"**{skill}**")
        st.progress(level)


    # Add vertical spacing
    st.markdown("<div style='margin:30px;'></div>", unsafe_allow_html=True)


    # Soft Skills
    soft_skills = {
        "Communication": 85,
        "Teamwork": 90,
        "Problem-Solving": 75,
        "Adaptability": 85,
        "Time Management": 80,
        "Creativity": 90,
    }
    
    st.markdown("### 🤝 Soft Skills")
    for skill, level in soft_skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

    
    # ==============================
    # 🌟 Hobbies & Fun Facts
    # ==============================
    st.subheader("🌟 Hobbies & Fun Facts")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🏃 Running", "🎶 Music", "🎮 Gaming", "📸 Photography", "✈️ Traveling"]
    )
    
    with tab1:
        st.image("images/movie.jpg", width=150)
    
    with tab2:
        st.image("images/music.jpg", width=150)
    
    with tab3:
        st.image("images/gaming.jpg", width=150)
    
    with tab4:
        st.image("images/badminton.jpg", width=150)
    
    with tab5:
        st.image("images/hiking.jpg", width=150)


    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )


    # ==============================
    # 📞 Contact
    # ==============================
    st.subheader("📞 Contact Me")

    st.markdown(
       """
       <style>
           .contact-box {
               background: linear-gradient(135deg, #1f1c2c, #89CFF0);
               color: white;
               padding: 20px;
               border-radius: 12px;
               box-shadow: 0 4px 12px rgba(0,0,0,0.25);
               text-align: center;
               font-family: 'Segoe UI', sans-serif;
           }
           .contact-item {
               font-size: 18px;
               margin: 12px 0;
           }
           .contact-item span {
               margin-right: 8px;
               color: #ffd700;
           }
           .contact-box:hover {
               transform: scale(1.02);
               transition: 0.3s ease-in-out;
               box-shadow: 0 6px 18px rgba(0,0,0,0.35);
           }
       </style
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">>
       <div class="contact-box">
           <div class="contact-item"><i class="fas fa-phone"></i> 011-12957400</div>
           <div class="contact-item"><i class="fas fa-envelope"></i> nhusna.napi@gmail.com</div>
       </div>
       <hr style='border:0; height:3px; background: linear-gradient(135deg, #1f1c2c, #89CFF0);'>
       """,
       unsafe_allow_html=True
    )
        
