import streamlit as st

def hr_page():
    st.title("📖 Chapter 3")
    st.header("🤖 HR Organizational Chart (AI Style)")

    # Graphviz chart for hierarchy
    st.graphviz_chart('''
    digraph HR {
        node [shape=box, style=filled, color=lightblue, fontname="Helvetica"];
        HR -> "Learning & Development";
        HR -> "Talent Acquisition & Industrial Relation";
        HR -> "Reward Management";
        "Reward Management" -> "Compensation & Benefits";
        "Reward Management" -> "General Affairs";
    }
    ''')

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
