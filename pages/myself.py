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
            font-size: 40px;
            color: #2c3e50;
            text-align: center;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }
        .chapter-caption {
            font-family: 'Courier New', monospace;
            font-size: 18px;
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

    st.markdown("<div class='chapter-title'>📖 Chapter 4 – Myself</div>", unsafe_allow_html=True)
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

    # Slider navigation
    page = st.slider("📖 Flip a page", 1, 6, 1)

    # Page content
    if page == 1:
        st.markdown("<div class='book-page'><h3>💡 Challenges & Ways to Overcome</h3>", unsafe_allow_html=True)
        st.table({
            "Challenge": ["Time Management", "Technical Skills Gap", "Communication Barriers"],
            "Solution": [
                "Weekly schedules & prioritization",
                "Self-learning, asking colleagues, practice",
                "Improved email etiquette, feedback from HR"
            ]
        })
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 2:
        st.markdown("<div class='book-page'><h3>🤝 HR Division & IT/Data Science Relation</h3>", unsafe_allow_html=True)
        st.table({
            "HR Process": ["Data Handling", "Analytics", "Automation"],
            "Relation to My Course": [
                "Ensuring data integrity like in data science",
                "Dashboards mirror analytical skills",
                "SPL modules connect with workflow automation"
            ]
        })
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 3:
        st.markdown("<div class='book-page'><h3>🎯 Goals & Objectives</h3>", unsafe_allow_html=True)
        st.table({
            "Objective": [
                "Gain HR exposure",
                "Apply IT/Data Science knowledge",
                "Improve communication & teamwork",
                "Contribute to HR projects"
            ],
            "Outcome": [
                "Hands-on HR workflow experience",
                "Used Streamlit & Power BI in HR",
                "Better email writing & collaboration",
                "Supported SPL module development"
            ]
        })
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 4:
        st.markdown("<div class='book-page'><h3>📊 Expectations vs Reality</h3>", unsafe_allow_html=True)
        st.table({
            "Expectation": [
                "Assist only with admin tasks",
                "Limited IT exposure"
            ],
            "Reality": [
                "Involved in HR system development & training modules",
                "Applied data visualization & Streamlit in HR processes"
            ]
        })
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 5:
        st.markdown("<div class='book-page'><h3>🚀 Future Plan</h3>", unsafe_allow_html=True)
        st.table({
            "Plan": [
                "Improve Power BI, Streamlit, GitHub skills",
                "Specialize in HR analytics",
                "Balance growth with running events",
                "Pursue data-driven HR/IT career"
            ],
            "Next Step": [
                "Practice with real datasets",
                "Explore HR analytics case studies",
                "Join more 5km races",
                "Apply for HR/IT hybrid roles"
            ]
        })

        st.markdown("### 🌟 Visualizing My Future")
        
        # Load animations (replace with actual Lottie URLs)
        umrah_anim = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_touohxv0.json")
        masters_anim = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")
        career_anim = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_puciaact.json")

        col1, col2, col3 = st.columns(3)

        with col1:
            st_lottie(umrah_anim, height=200, key="umrah")
            st.caption("Umrah with Parents")

        with col2:
            st_lottie(masters_anim, height=200, key="masters")
            st.caption("Continue Master’s Studies")

        with col3:
            st_lottie(career_anim, height=200, key="career")
            st.caption("Stable Career Path")

        st.markdown("</div>", unsafe_allow_html=True)

    elif page == 6:
        st.markdown("<div class='book-page'><h3>🎥 Internship Memories</h3>", unsafe_allow_html=True)
        st.video("videos/internship_memories.mp4")
        st.success("🎬 This video captures my favorite moments during the internship journey.")
        st.markdown("</div>", unsafe_allow_html=True)
