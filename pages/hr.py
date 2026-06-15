import streamlit as st

def hr_page():
    st.title("📖 Chapter 3")
    st.header("🤖 HR Organizational Chart (AI Style)")

    # Graphviz chart for hierarchy
    import streamlit as st

def hr_page():
    st.title("📖 Chapter 3")
    st.header("👥 HR Organizational Chart")

    st.graphviz_chart('''
    digraph HR {
        node [shape=box, style=filled, fontname="Helvetica"];
        
        HR [label="Hiroyuki Nishimoto\nManaging Director", color=lightblue];
        KM [label="Kei Tomita\nKM Corporate Service", color=lightyellow];
        Rosmawati [label="Rosmawati Haron\nHR Division Head", color=lightgreen];
        Vacant [label="Vacant\nHR Assistant Division Head", color=lightgray];

        HR -> KM -> Rosmawati -> Vacant;

        subgraph cluster_CoE {
            style=filled;
            color=lightcyan;
            label="Centre of Excellence";
            Yuki [label="Yuki Mimura\nHR Business Partner"];
            Norkamariah [label="Norkamariah Othman\nL&D Dept. Head"];
            Norizan [label="Norizan Ishak\nSenior Executive"];
            MohdAnuar [label="Mohd Anuar Mohd Ariffin\nExecutive"];
            Nurul [label="Nurul Atiqah Mahmud\nExecutive"];
            Yuki -> Norkamariah -> {Norizan MohdAnuar Nurul};
        }

        subgraph cluster_OE {
            style=filled;
            color=lightpink;
            label="Operational Excellence";
            Zuraidah [label="Zuraidah Ismail\nHR Business Partner"];
            RosmawatiR [label="Rosmawati Abd Rashid\nTA & IR Dept. Head"];
            MohdShukri [label="Mohd Shukri Anuar\nSection Head"];
            Khairani [label="Khairani Kamal\nSenior Executive"];
            NurHidayah [label="Nur Hidayah Sanusi\nOfficer"];
            Zafidah [label="Zafidah Ismail\nReward Management Dept. Head"];
            GA [label="General Affairs Section"];
            CB [label="Compensation & Benefits Section"];
            Zuraidah -> RosmawatiR -> {MohdShukri Khairani NurHidayah};
            Zuraidah -> Zafidah -> {GA CB};
        }
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
