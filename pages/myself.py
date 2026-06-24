import streamlit as st

def myself_page():
    st.title("📖 Chapter 4 – Myself")
    st.caption("✨ Flip through my internship journey like a digital book ✨")

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

    # Page 1 – Challenges
    with st.expander("📖 Page 1 – Challenges & Ways to Overcome"):
        st.markdown("<div class='book-page'>", unsafe_allow_html=True)
        st.table({
            "Challenge": ["Time Management", "Technical Skills Gap", "Communication Barriers"],
            "Solution": [
                "Weekly schedules & prioritization",
                "Self-learning, asking colleagues, practice",
                "Improved email etiquette, feedback from HR"
            ]
        })
        st.markdown("</div>", unsafe_allow_html=True)

    # Page 2 – HR Relation
    with st.expander("📖 Page 2 – HR Division & IT/Data Science Relation"):
        st.markdown("<div class='book-page'>", unsafe_allow_html=True)
        st.table({
            "HR Process": ["Data Handling", "Analytics", "Automation"],
            "Relation to My Course": [
                "Ensuring data integrity like in data science",
                "Dashboards mirror analytical skills",
                "SPL modules connect with workflow automation"
            ]
        })
        st.markdown("</div>", unsafe_allow_html=True)

    # Page 3 – Goals
    with st.expander("📖 Page 3 – Goals & Objectives"):
        st.markdown("<div class='book-page'>", unsafe_allow_html=True)
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

    # Page 4 – Expectations vs Gains
    with st.expander("📖 Page 4 – Expectations vs Reality"):
        st.markdown("<div class='book-page'>", unsafe_allow_html=True)
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

    # Page 5 – Future Plan
    with st.expander("📖 Page 5 – Future Plan"):
        st.markdown("<div class='book-page'>", unsafe_allow_html=True)
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
        st.markdown("</div>", unsafe_allow_html=True)

    # Page 6 – Memories
    with st.expander("📖 Page 6 – Internship Memories"):
        st.markdown("<div class='book-page'>", unsafe_allow_html=True)
        st.video("videos/internship_memories.mp4")
        st.success("🎬 This video captures my favorite moments during the internship journey.")
        st.markdown("</div>", unsafe_allow_html=True)
