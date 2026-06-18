import streamlit as st

# ==========================
# HR Org Chart Data
# ==========================
org_chart = {
    "Managing Director": "Hiroyuki Nishimoto",
    "KM Corporate Service": "Kei Tomita",
    "HR Division Head": "Rosmawati Haron",
    "HR Assistant Division Head": "Vacant",
    "Centre of Excellence": {
        "HR Business Partner": "Yuki Mimura",
        "Learning & Development Dept. Head": "Norkamariah Othman",
        "Team": [
            "Norizan Ishak (Senior Executive)",
            "Mohd Anuar Mohd Ariffin (Executive)",
            "Nurul Atiqah Mahmud (Executive)"
        ]
    },
    "Operational Excellence": {
        "HR Business Partner": "Zuraidah Ismail",
        "Talent Acquisition & IR Dept. Head": "Rosmawati Abd Rashid",
        "Team": [
            "Mohd Shukri Anuar (Section Head)",
            "Khairani Kamal (Senior Executive)",
            "Nur Hidayah Sanusi (Officer)"
        ],
        "Reward Management Dept. Head": "Zafidah Ismail",
        "General Affairs Section": [
            "Khairani Kamal (Senior Executive)",
            "Umar Yasriza (Executive)"
        ],
        "Compensation & Benefits Section": [
            "Fatasha Anis Muhamad Yusof (Senior Executive)",
            "Hazira Hafsa Razlian (Executive)"
        ]
    }
}


# ==========================
# Main Page
# ==========================
def hr_page():
    st.title("📖 Chapter 3")
    st.header("👥 HR Organizational Flowchart")

    org_chart["HR Division Head"] = st.text_input(
        "Update HR Division Head:",
        org_chart["HR Division Head"]
    )

    org_chart["HR Assistant Division Head"] = st.text_input(
        "Update HR Assistant Division Head:",
        org_chart["HR Assistant Division Head"]
    )

    st.subheader("📊 Current Structure")
    st.json(org_chart)

    st.subheader("📈 Flowchart View")
    st.graphviz_chart(render_flowchart(org_chart))

    st.markdown("---")

    # =====================================================
    # Learning & Development
    # =====================================================
    with st.expander("📚 Learning & Development", expanded=True):

        st.write(
            "Focuses on employee training, skill enhancement, and career growth."
        )

        tab1, tab2, tab3 = st.tabs([
            "🎓 Internship",
            "🏫 Training",
            "📝 BLA"
        ])

        # ================= Internship =================
        with tab1:

            st.subheader("Internship Process Flow")
            
            steps = [
                "📢 Opening",
                "📝 Application",
                "🔍 Screening",
                "📅 Interview",
                "📊 Evaluation",
                "✅ Offer",
                "🎓 Onboarding"
            ]
            
            selected = st.radio(
                "Select Recruitment Stage",
                steps,
                horizontal=True
            )
            
            workflow = {
                "📢 Opening": {
                    "title": "Internship Opening",
                    "desc": """
            The Human Resource Department publishes internship vacancies through:
            
            • Company Website
            • University Career Centre
            • LinkedIn
            • JobStreet
            • Email Collaboration
            """,
                    "status": "Completed",
                    "progress": 0.14
                },
            
                "📝 Application": {
                    "title": "Student Application",
                    "desc": """
            Students submit:
            
            • Resume/CV
            • Academic Transcript
            • Cover Letter
            • Internship Letter from University
            """,
                    "status": "120 Applications Received",
                    "progress": 0.28
                },
            
                "🔍 Screening": {
                    "title": "Resume Screening",
                    "desc": """
            HR reviews applications based on:
            
            • Academic Qualification
            • Skills
            • Relevant Experience
            • Availability
            """,
                    "status": "35 Candidates Shortlisted",
                    "progress": 0.42
                },
            
                "📅 Interview": {
                    "title": "Interview Session",
                    "desc": """
            Shortlisted candidates attend interviews.
            
            Interviewers evaluate:
            
            • Communication
            • Technical Knowledge
            • Personality
            • Motivation
            """,
                    "status": "Interview Ongoing",
                    "progress": 0.57
                },
            
                "📊 Evaluation": {
                    "title": "Candidate Evaluation",
                    "desc": """
            HR discusses interview feedback with department managers.
            
            Final candidates are selected.
            """,
                    "status": "Pending Approval",
                    "progress": 0.71
                },
            
                "✅ Offer": {
                    "title": "Offer Letter",
                    "desc": """
            Successful candidates receive:
            
            • Offer Letter
            • Reporting Date
            • Required Documents
            """,
                    "status": "Offer Sent",
                    "progress": 0.86
                },
            
                "🎓 Onboarding": {
                    "title": "Intern Onboarding",
                    "desc": """
            Interns complete:
            
            • Registration
            • Orientation
            • Department Assignment
            • Training
            """,
                    "status": "Completed",
                    "progress": 1.0
                }
            }
            
            info = workflow[selected]
            
            st.divider()
            
            col1, col2 = st.columns([2,1])
            
            with col1:
            
                st.markdown(f"### {info['title']}")
                st.info(info["desc"])
            
            with col2:
            
                st.metric("Status", info["status"])
                st.progress(info["progress"])

            st.divider()

            st.subheader("Activities Performed During Internship")

            st.markdown("**Orientation & Documentation**")
            st.video("videos/internship/orientation.mp4")

            st.markdown("**Intern Interview Session**")
            st.video("videos/internship/interview.mp4")

            st.markdown("**Intern Evaluation & Closing**")
            st.video("videos/internship/evaluation.mp4")

        # ================= Training =================
        with tab2:

            st.subheader("Training Process Flow")

            st.image(
                "images/training_flow.png",
                caption="Training Process Flow",
                use_container_width=True
            )

            st.divider()

            st.subheader("Activities Performed")

            st.markdown("**Training Registration**")
            st.video("videos/training/registration.mp4")

            st.markdown("**Training Coordination**")
            st.video("videos/training/coordination.mp4")

            st.markdown("**Training Execution**")
            st.video("videos/training/execution.mp4")

        # ================= BLA =================
        with tab3:

            st.subheader("Baseline Assessment (BLA) Process Flow")

            st.image(
                "images/bla_flow.png",
                caption="BLA Process Flow",
                use_container_width=True
            )

            st.divider()

            st.subheader("Activities Performed")

            st.markdown("**Assessment Preparation**")
            st.video("videos/bla/preparation.mp4")

            st.markdown("**Conducting BLA Session**")
            st.video("videos/bla/session.mp4")

            st.markdown("**Result Compilation & Analysis**")
            st.video("videos/bla/reporting.mp4")

    # =====================================================
    # Talent Acquisition
    # =====================================================
    with st.expander("🎯 Talent Acquisition & Industrial Relation"):

        st.write(
            "Handles recruitment, onboarding, and maintaining healthy employee relations."
        )

        st.metric(
            "New Hires",
            25,
            "+5 this month"
        )

    # =====================================================
    # Reward Management
    # =====================================================
    with st.expander("💎 Reward Management"):

        st.write(
            "Ensures fair compensation and manages employee benefits."
        )

        st.subheader("💰 Compensation & Benefits")

        st.write(
            "Salary structure, allowances, incentives, and employee perks."
        )

        st.progress(0.7)

        st.subheader("🏢 General Affairs")

        st.write(
            "Workplace facilities, employee welfare, and administrative support."
        )

        st.slider(
            "Employee Satisfaction Index",
            0,
            100,
            85
        )


# ==========================
# Graphviz Flowchart
# ==========================
def render_flowchart(org_chart):

    dot = """
    digraph HR {
        rankdir=TB;
        node [shape=box, style=filled, fontname="Helvetica"];

        HR [label="%s\\nManaging Director", color=lightblue];
        KM [label="%s\\nKM Corporate Service", color=lightyellow];
        Rosmawati [label="%s\\nHR Division Head", color=lightgreen];
        Vacant [label="%s\\nHR Assistant Division Head", color=lightgray];

        HR -> KM -> Rosmawati -> Vacant;
    """ % (
        org_chart["Managing Director"],
        org_chart["KM Corporate Service"],
        org_chart["HR Division Head"],
        org_chart["HR Assistant Division Head"],
    )

    # Centre of Excellence
    dot += 'Yuki [label="%s\\nHR Business Partner", color=lightcyan];' % (
        org_chart["Centre of Excellence"]["HR Business Partner"]
    )

    dot += 'Norkamariah [label="%s\\nL&D Dept. Head"];' % (
        org_chart["Centre of Excellence"]["Learning & Development Dept. Head"]
    )

    dot += "Vacant -> Yuki -> Norkamariah;"

    for member in org_chart["Centre of Excellence"]["Team"]:
        dot += f'"{member}" [color=white]; Norkamariah -> "{member}";'

    # Operational Excellence
    dot += 'Zuraidah [label="%s\\nHR Business Partner", color=lightpink];' % (
        org_chart["Operational Excellence"]["HR Business Partner"]
    )

    dot += 'RosmawatiR [label="%s\\nTA & IR Dept. Head"];' % (
        org_chart["Operational Excellence"]["Talent Acquisition & IR Dept. Head"]
    )

    dot += "Vacant -> Zuraidah -> RosmawatiR;"

    for member in org_chart["Operational Excellence"]["Team"]:
        dot += f'"{member}" [color=white]; RosmawatiR -> "{member}";'

    # Reward Management
    dot += 'Zafidah [label="%s\\nReward Management Dept. Head"];' % (
        org_chart["Operational Excellence"]["Reward Management Dept. Head"]
    )

    dot += "Zuraidah -> Zafidah;"

    for section in [
        "General Affairs Section",
        "Compensation & Benefits Section"
    ]:
        for member in org_chart["Operational Excellence"][section]:
            dot += f'"{member}" [color=white]; Zafidah -> "{member}";'

    dot += "}"

    return dot


# ==========================
# Run App
# ==========================
if __name__ == "__main__":
    hr_page()
