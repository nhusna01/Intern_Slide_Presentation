import streamlit as st
import pandas as pd
import numpy as np

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
            font-size: 16px;
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
        <h2 style="font-size:70px; font-weight:bold; font-family: 'Great Vibes', cursive; color:#003366; margin:0;">
             SELF-INTRODUCTION 
        </h2>
    </div>
    """, unsafe_allow_html=True)

    
    # 🌟 Profile Image
    st.markdown(
        """
        <style>
            .profile-pic {
                display: flex;
                justify-content: center;
                align items: center;
                margin-top: 20px;
            }
            .profile-pic img {
                width: 220px;
                height: 220px;
                border-radius: 50%;        /* 👈 makes it circular */
                border: 5px solid gold;    /* 👈 gold border */
                object-fit: cover;         /* 👈 keeps aspect ratio */
            }
        </style>
        <div class="profile-pic">
             <img src="https://nhusna01.github.io/Intern_Slide_Presentation/images/myself_icon.jpg">
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(
        """
        <h1 style="color:#003366; font-size: 45px; text-align:center;">
            Nurul Husna Binti Mohd Napi
        </h1>

        <div style="text-align:center;">
            <div class="typing" style="color:#3366CC; font-size:24px;">
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
        font-size: 28px;
        font-weight: bold;
        color: #FFD700;
        margin-bottom: 12px;
    }
    
    .fact-value {
        font-size: 22px;
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
        font-size: 24px;
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
                <span class="tooltiptext">HR Field Supervisor</span>
            </div>
            <div class="fact-icon">👩‍💼</div>
            <div class="fact-title">Supervisor</div>
            <div class="fact-value" style="text-align:left; font-size:22px;">
                Mdm Norkamariah & Mdm Zuraidah 
            </div>
        </div>
        """, unsafe_allow_html=True)

    
    with col3:
        st.markdown("""
        <div class="fact-card">
            <div class="tooltip">❓
                <span class="tooltiptext">26 Weeks</span>
            </div>
            <div class="fact-icon">📅</div>
            <div class="fact-title">Internship Duration</div>
            <div class="fact-value">
                3/2/2026 - 21/7/2026
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

    # ==============================
    # 🌸 Global Subheader Styling
    # ==============================
    st.markdown(
        """
        <style>
            .stMarkdown h3, .stSubheader {
                font-size: 35px !important;   /* Force subheader size */
                font-weight: 700;             /* Make it bold */
                color: #2c3e50;               /* Optional: darker text color */
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    

    # ==============================
    # 🌸 About Me
    # ==============================
    st.markdown(
        """
        <h3 style='font-size:35px; font-weight:700; color:#2c3e50;'>
            🌸 About Me
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <style>
            .about-text {
                font-size: 24px;       /* Bigger font size */
                line-height: 1.8;
                font-weight: 600;
                color: #2c3e50;
                text-align: justify;
            }
        </style>
        <div class="about-text">
            I am the eldest of four siblings and currently 24 years old. I love desserts 🍰 and <br>
            enjoy adventurous activities like hiking and any sports that keep me active and energized. <br>
        </div>
        """,
        unsafe_allow_html=True
    )

    

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

   
    # ==============================
    # 🌟 Global Skill Styling
    # ==============================
    st.markdown(
        """
        <style>
            .skill-text {
                font-size: 22px;       /* Bigger font size for all skills */
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 6px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # ==============================
    # 🔑 Skill Level Function
    # ==============================
    def skill_level(percent):
        if percent < 60:
            return "Beginner"
        elif percent < 80:
            return "Intermediate"
        elif percent < 90:
            return "Advanced"
        else:
            return "Expert"
    
    # ==============================
    # 💻 Technical Skills 
    # ==============================
    st.markdown(
        """
        <h3 style='font-size:35px; font-weight:700; color:#2c3e50;'>
            💻 Technical Skills
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    technical_skills = {
        "Python Programming": 75,
        "Data Preparation": 90,
        "Data Analytics": 90,
        "Data Visualization": 95,
        "Machine Learning": 85,
        "Data Mining": 90,
    }
    
    for skill, level in technical_skills.items():
        st.markdown(
            f"<div class='skill-text'>{skill} – {level}% ({skill_level(level)})</div>",
            unsafe_allow_html=True
        )
        st.progress(level)

    
    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
    
    # ==============================
    # 🤝 Soft Skills 
    # ==============================
    st.markdown(
        """
        <h3 style='font-size:35px; font-weight:700; color:#2c3e50;'>
            🤝 Soft Skills
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    soft_skills = {
        "Communication": 85,
        "Teamwork": 90,
        "Problem-Solving": 75,
        "Adaptability": 85,
        "Time Management": 85,
        "Creativity": 90,
    }
    
    for skill, level in soft_skills.items():
        st.markdown(
            f"<div class='skill-text'>{skill} – {level}% ({skill_level(level)})</div>",
            unsafe_allow_html=True
        )
        st.progress(level)

    
    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
    
    # ==============================
    # 🛠️ Tools & Technologies 
    # ==============================
    st.markdown(
        """
        <h3 style='font-size:35px; font-weight:700; color:#2c3e50;'>
            🛠️ Tools & Technologies
        </h3>
        """,
        unsafe_allow_html=True
    )

    
    tools = {
        "GitHub": 85,
        "Streamlit": 90,
        "Figma": 80,
        "Canva": 95,
        "Google Colab": 95,
        "VS Code": 75,
    }
        
    for tool, level in tools.items():
        st.markdown(
            f"<div class='skill-text'>{tool} – {level}% ({skill_level(level)})</div>",
            unsafe_allow_html=True
        )
        st.progress(level)

    
    st.markdown(
        "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
        unsafe_allow_html=True
    )

    
    # ==============================
    # 🌟 Hobbies & Fun Facts
    # ==============================
    st.markdown(
        """
        <h3 style='font-size:35px; font-weight:700; color:#2c3e50;'>
            🌟 Hobbies & Fun Facts
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    # CSS styling
    st.markdown(
        """
        <style>
            .stImage img {
                width: 180px;
                height: 180px;
                margin: 15px;
                border-radius: 12px;
                object-fit: cover;
                box-shadow: 0 4px 12px rgba(0,0,0,0.25);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .stImage img:hover {
                transform: scale(1.05);
                box-shadow: 0 6px 18px rgba(0,0,0,0.35);
                cursor: pointer;
            }
            .hobby-text {
                text-align: center;
                font-size: 23px;
                font-weight: bold;
                margin-top: 8px;
                color: #003366;
                transition: color 0.3s ease, text-shadow 0.3s ease;
            }
            .hobby-text:hover {
                color: #ffd700;
                text-shadow: 0 0 8px #ffd700;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Use columns to align images side by side
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.image("images/movie2.png")
        st.markdown("<div class='hobby-text'>🎬 Enjoy watching thrillers & action movies, especially zombie survival stories</div>", unsafe_allow_html=True)
    
    with col2:
        st.image("images/music1.png")
        st.markdown("<div class='hobby-text'>🎵 Chill out with Justin Bieber tracks while doing assignments</div>", unsafe_allow_html=True)
    
    with col3:
        st.image("images/gaming.jpg")
        st.markdown("<div class='hobby-text'>🎮 Play games with my siblings whenever we get some free time</div>", unsafe_allow_html=True)
    
    with col4:
        st.image("images/badminton.jpg")
        st.markdown("<div class='hobby-text'>🏸 Weekend badminton matches with friends to relax and have fun</div>", unsafe_allow_html=True)
    
    with col5:
        st.image("images/hiking2.png")
        st.markdown("<div class='hobby-text'>🥾 Hiking around Bukit Keluang & Kemaman to enjoy the fresh air and nature</div>", unsafe_allow_html=True)
    
   
    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )


    # ==============================
    # 📞 Contact
    # ==============================
    st.markdown(
        """
        <h3 style='font-size:35px; font-weight:700; color:#2c3e50;'>
            📞 Contact
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
       """
       <style>
           .contact-box {
               background: linear-gradient(90deg, #023e8a, #0096c7);
               color: white;
               padding: 25px;
               border-radius: 12px;
               box-shadow: 0 4px 12px rgba(0,0,0,0.25);
               text-align: center;
               font-family: 'Segoe UI', sans-serif;
           }
           .contact-item {
               font-size: 24px;   /* Increased font size */
               margin: 14px 0;
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
       </style>
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
       <div class="contact-box">
           <div class="contact-item"><i class="fas fa-phone"></i> <a href="tel:01112957400" style="color:white; text-decoration:none;"><b>011-12957400</b></a></div>
           <div class="contact-item"><i class="fas fa-envelope"></i> <a href="mailto:nhusna.napi@gmail.com" style="color:white; text-decoration:none;"><b>nhusna.napi@gmail.com</b></a></div>
           <div class="contact-item"><i class="fas fa-laptop-code"></i> For IT support inquiries (e.g., data analysis)</div>
       </div>
       """,
       unsafe_allow_html=True
    )

