import streamlit as st

# Step 1: Define HR org chart in JSON/dict
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

# Step 2: Editable inputs
def hr_page():
    st.title("📖 Chapter 3")
    st.header("👥 Editable HR Organizational Chart")

    # Editable fields for key roles
    org_chart["HR Division Head"] = st.text_input(
        "Update HR Division Head:", org_chart["HR Division Head"]
    )
    org_chart["HR Assistant Division Head"] = st.text_input(
        "Update HR Assistant Division Head:", org_chart["HR Assistant Division Head"]
    )

    org_chart["Centre of Excellence"]["HR Business Partner"] = st.text_input(
        "Update Centre of Excellence HR Business Partner:",
        org_chart["Centre of Excellence"]["HR Business Partner"]
    )

    org_chart["Operational Excellence"]["HR Business Partner"] = st.text_input(
        "Update Operational Excellence HR Business Partner:",
        org_chart["Operational Excellence"]["HR Business Partner"]
    )

    # Show updated JSON structure
    st.subheader("📊 Current Structure (Editable JSON)")
    st.json(org_chart)

    # Render Graphviz chart
    st.subheader("📈 Visual Org Chart")
    st.graphviz_chart(render_graph(org_chart))


# Step 3: Function to render Graphviz chart dynamically
def render_graph(org_chart):
    dot = "digraph HR { node [shape=box, style=filled, fontname='Helvetica'];"

    # Top hierarchy
    dot += f'HR [label="{org_chart["Managing Director"]}\\nManaging Director", color=lightblue];'
    dot += f'KM [label="{org_chart["KM Corporate Service"]}\\nKM Corporate Service", color=lightyellow];'
    dot += f'Rosmawati [label="{org_chart["HR Division Head"]}\\nHR Division Head", color=lightgreen];'
    dot += f'Vacant [label="{org_chart["HR Assistant Division Head"]}\\nHR Assistant Division Head", color=lightgray];'
    dot += "HR -> KM -> Rosmawati -> Vacant;"

    # Centre of Excellence
    dot += f'Yuki [label="{org_chart["Centre of Excellence"]["HR Business Partner"]}\\nHR Business Partner", color=lightcyan];'
    dot += f'Norkamariah [label="{org_chart["Centre of Excellence"]["Learning & Development Dept. Head"]}\\nL&D Dept. Head"];'
    dot += "Vacant -> Yuki -> Norkamariah;"
    for member in org_chart["Centre of Excellence"]["Team"]:
        dot += f'"{member}" [color=white]; Norkamariah -> "{member}";'

    # Operational Excellence
    dot += f'Zuraidah [label="{org_chart["Operational Excellence"]["HR Business Partner"]}\\nHR Business Partner", color=lightpink];'
    dot += f'RosmawatiR [label="{org_chart["Operational Excellence"]["Talent Acquisition & IR Dept. Head"]}\\nTA & IR Dept. Head"];'
    dot += "Vacant -> Zuraidah -> RosmawatiR;"
    for member in org_chart["Operational Excellence"]["Team"]:
        dot += f'"{member}" [color=white]; RosmawatiR -> "{member}";'

    dot += f'Zafidah [label="{org_chart["Operational Excellence"]["Reward Management Dept. Head"]}\\nReward Management Dept. Head"];'
    dot += "Zuraidah -> Zafidah;"
    for section in ["General Affairs Section", "Compensation & Benefits Section"]:
        for member in org_chart["Operational Excellence"][section]:
            dot += f'"{member}" [color=white]; Zafidah -> "{member}";'

    dot += "}"
    return dot


# Run page
if __name__ == "__main__":
    hr_page()



    st.markdown("---")

    # Interactive expanders with metrics
    with st.expander("📚 Learning & Development"):
        st.write("Focuses on employee training, skill enhancement, and career growth.")
        st.metric("Active Programs", 12, "+3 this quarter")

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
