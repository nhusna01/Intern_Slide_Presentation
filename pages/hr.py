import streamlit as st
# HR Org Chart Data
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

def hr_page():
    st.title("📖 Chapter 3")
    st.header("👥 HR Organizational Flowchart")

    # Editable fields
    org_chart["HR Division Head"] = st.text_input("Update HR Division Head:", org_chart["HR Division Head"])
    org_chart["HR Assistant Division Head"] = st.text_input("Update HR Assistant Division Head:", org_chart["HR Assistant Division Head"])

    # Show JSON
    st.subheader("📊 Current Structure")
    st.json(org_chart)

    # Flowchart visualization
    st.subheader("📈 Flowchart View")
    st.graphviz_chart(render_flowchart(org_chart))
    
    st.markdown("---")

    with st.expander("📚 Learning & Development"):
        st.write(
            "Focuses on employee training, skill enhancement, and career growth."
        )
        
    with st.expander("🎯 Talent Acquisition & Industrial Relation"):
        st.write(
            "Handles recruitment, onboarding, and maintaining healthy employee relations."
        )
        st.metric("New Hires", 25, "+5 this month")

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
    dot += 'Yuki [label="%s\\nHR Business Partner", color=lightcyan];' % org_chart["Centre of Excellence"]["HR Business Partner"]
    dot += 'Norkamariah [label="%s\\nL&D Dept. Head"];' % org_chart["Centre of Excellence"]["Learning & Development Dept. Head"]
    dot += "Vacant -> Yuki -> Norkamariah;"
    for member in org_chart["Centre of Excellence"]["Team"]:
        dot += f'"{member}" [color=white]; Norkamariah -> "{member}";'

    # Operational Excellence
    dot += 'Zuraidah [label="%s\\nHR Business Partner", color=lightpink];' % org_chart["Operational Excellence"]["HR Business Partner"]
    dot += 'RosmawatiR [label="%s\\nTA & IR Dept. Head"];' % org_chart["Operational Excellence"]["Talent Acquisition & IR Dept. Head"]
    dot += "Vacant -> Zuraidah -> RosmawatiR;"
    for member in org_chart["Operational Excellence"]["Team"]:
        dot += f'"{member}" [color=white]; RosmawatiR -> "{member}";'

    # Reward Management
    dot += 'Zafidah [label="%s\\nReward Management Dept. Head"];' % org_chart["Operational Excellence"]["Reward Management Dept. Head"]
    dot += "Zuraidah -> Zafidah;"
    for section in ["General Affairs Section", "Compensation & Benefits Section"]:
        for member in org_chart["Operational Excellence"][section]:
            dot += f'"{member}" [color=white]; Zafidah -> "{member}";'

    dot += "}"
    return dot


    st.markdown("---")

    # Interactive expanders with metrics
    with st.expander("📚 Learning & Development", expanded=True):        
        st.write("Focuses on employee training, skill enhancement, and career growth.")
        
    tab1, tab2, tab3 = st.tabs([
        "🎓 Internship",
        "🏫 Training",
        "📝 BLA"
    ])

    # ================= Internship =================
    with tab1:
        st.subheader("Internship Process Flow")

        st.image(
            "images/internship_flow.png",
            caption="Internship Process Flow",
            use_container_width=True
        )

        st.divider()

        st.subheader("Activities Performed")

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

    with st.expander("🎯 Talent Acquisition & Industrial Relation"):
        st.write("Handles recruitment, onboarding, and maintaining healthy employee relations.")
        st.metric("New Hires", 25, "+5 this month")

    with st.expander("💎 Reward Management"):
        st.write("Ensures fair compensation and manages employee benefits.")

        st.subheader("💰 Compensation & Benefits")
        st.write("Salary structure, allowances, incentives, and employee perks.")
        st.progress(0.7)  # Example progress bar

        st.subheader("🏢 General Affairs")
        st.write("Workplace facilities, employee welfare, and administrative support.")
        st.slider("Employee Satisfaction Index", 0, 100, 85)

if __name__ == "__main__":
    hr_page()

