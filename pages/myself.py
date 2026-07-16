import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
def myself_page():
    # Stylized title
    st.markdown("""
        <style>
        .chapter-title {
            font-family: 'Georgia', serif;
            font-size: 60px;
            color: #2c3e50;
            text-align: center;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }
        .chapter-caption {
            font-family: 'Courier New', monospace;
            font-size: 24px;
            color: #555;
            text-align: center;
            animation: fadeIn 3s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='chapter-title'>📖 Chapter 5 – Challenges</div>", unsafe_allow_html=True)
    st.markdown("<div class='chapter-caption'>✨ Flip through my internship journey like a digital book ✨</div>", unsafe_allow_html=True)

    st.divider()

    # Add CSS styling for book-like pages
    st.markdown("""
        <style>
        .book-page {
            background-color: #fffaf0; /* light paper tone */
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 4px 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .book-page h3 {
            font-family: 'Georgia', serif;
            color: #4a4a4a;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        div[data-testid="stSlider"] label{
            font-size:28px !important;
            font-weight:bold !important;
        }
        
        div[data-testid="stSlider"] p{
            font-size:26px !important;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Slider navigation
    page = st.slider("📖 Flip a page", 1, 6, 1)

    # Page content
    if page == 1:
        st.markdown("<div class='book-page'><h3>💡 Challenges & Ways to Overcome</h3>", unsafe_allow_html=True)
    
        st.table({
            "Challenge": [
                "Understanding HR Policies and Procedures",
                "Learning to Use iSpring Suite for SPL Development",
                "Communication and Confidence in Sharing Ideas",
                "Adapting to a New Working Environment"
            ],
    
            "Ways to Overcome": [
                "Reviewed HR policies and internal documents, sought guidance from supervisors and colleagues, and asked questions whenever clarification was needed.",
                "Learned independently through online tutorials, hands-on practice, and guidance from colleagues to improve proficiency in developing Self-Paced Learning (SPL) modules.",
                "Became more proactive by asking questions, participating in discussions, and confidently sharing ideas to improve communication and teamwork.",
                "Observed workplace practices, accepted constructive feedback, learned from experienced colleagues, and gradually adapted to the organization's work culture."
            ]
        })
    
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 2:
        st.markdown("<div class='book-page'><h3>🤝 HR Division & IT/Data Science Relation</h3>", unsafe_allow_html=True)
    
        st.table({
            "Common Practice": [
                "Data Analysis",
                "Reporting",
                "Use of AI Tools",
                "Process Improvement",
                "Survey Analysis"
            ],
    
            "Application in HR & IT": [
                "Both HR and IT use data to identify trends and support decision-making. HR uses Excel, while IT applies tools like Python and Power BI for deeper analysis.",
                "Both HR and IT prepare reports to monitor performance. HR commonly uses Excel reports, while IT supports automated reports and interactive dashboards.",
                "Both HR and IT use AI tools to improve productivity, prepare documents, and generate ideas.",
                "Both HR and IT use process flows to organize workflows. IT can further support process improvement through digital solutions.",
                "Both HR and IT use data insights for planning, evaluation, and continuous improvement."

            ]
        })
    
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 3:
        st.markdown("<div class='book-page'><h3>📊 Expectations vs Reality</h3>", unsafe_allow_html=True)
    
        st.table({
            "Expectation": [
                "Perform mainly administrative tasks",
                "Limited opportunity to apply technical skills",
                "Minimal involvement in HR projects",
                "Observe workplace operations only"
            ],
    
            "Reality": [
                "Handled administrative responsibilities while contributing to HR initiatives and projects.",
                "Applied Python, Streamlit, Microsoft Excel, and data analytics in HR-related tasks.",
                "Participated in SPL development, employee engagement survey analysis, redesigning the OEMS flowchart for the Learning & Development (L&D) team, and HR documentation.",
                "Gained practical experience by collaborating with different departments within the HR Division and supporting continuous improvement activities."
            ]
        })
    
        st.markdown("</div>", unsafe_allow_html=True)

    elif page ==4:
        st.markdown("<div class='book-page'><h3>🚀 Future Plan</h3>", unsafe_allow_html=True)
        st.table({
            "Future Goal": [
                "Sponsor my parents to perform Umrah and Hajj",
                "Become proficient in Streamlit, GitHub, and data analytics",
                "Further my studies by pursuing a Master's degree",
                "Maintain a healthy work–life balance while advancing my career",
                "Establish a successful career in data-driven HR and IT"
            ],
            
            "Action Plan": [
                "Build a strong financial foundation through consistent saving",
                "Develop technical expertise by working on real-world projects",
                "Continue learning through professional development and certifications",
                "Set clear career milestones and monitor my progress",
                "Seek opportunities in HR Technology, HR Analytics, or IT-related roles"
            ]
        })

        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 6:
        st.markdown("<div class='book-page'><h3>🎥 Internship Memories</h3>", unsafe_allow_html=True)
        st.video("videos/internship_memories.mp4")
        st.success("🎬 This video captures my favorite moments during the internship journey.")
        st.markdown("</div>", unsafe_allow_html=True)
