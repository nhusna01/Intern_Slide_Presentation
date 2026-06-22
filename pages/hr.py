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
            def internship_flow():
        
                st.markdown("## 🎓 Internship Process Flow")
            
                # ---------- Row 1 ----------
                c1,c2,c3,c4,c5,c6,c7 = st.columns(7)
            
                with c1:
                    if st.button("①\n📧\nApplication",use_container_width=True):
                        st.session_state.step=1
            
                with c2:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)
            
                with c3:
                    if st.button("②\n🔍\nScreening",use_container_width=True):
                        st.session_state.step=2
            
                with c4:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)
            
                with c5:
                    if st.button("③\n📝\nPlacement",use_container_width=True):
                        st.session_state.step=3
            
                with c6:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)
            
                with c7:
                    if st.button("④\n👩‍💼\nApproval",use_container_width=True):
                        st.session_state.step=4
            
                # ---------- Row 2 ----------
                st.write("")
            
                c1,c2,c3,c4,c5,c6,c7 = st.columns(7)
            
                with c1:
                    if st.button("⑥\n🎉\nConfirmation",use_container_width=True):
                        st.session_state.step=6
            
                with c2:
                    st.markdown("<h1 style='text-align:center;'>⬅️</h1>",unsafe_allow_html=True)
            
                with c3:
                    if st.button("⑤\n✅\nDocuments Preparation",use_container_width=True):
                        st.session_state.step=5
            
                with c4:
                    st.markdown("<h1 style='text-align:center;'>⬇️</h1>",unsafe_allow_html=True)
            
                with c5:
                    if st.button("⑦\n📄\nReport Duty & Briefing",use_container_width=True):
                        st.session_state.step=7
            
                with c6:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)
            
                with c7:
                    if st.button("⑧\n🎓\nHandover",use_container_width=True):
                        st.session_state.step=8
            
                # ---------- Row 3 ----------
                st.write("")
            
                c1,c2,c3,c4,c5 = st.columns(5)
            
                with c1:
                    if st.button("⑨\n🤝\nAppreciation",use_container_width=True):
                        st.session_state.step=9
            
                with c2:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)
            
                with c3:
                    if st.button("⑩\n🎁\nEvaluation",use_container_width=True):
                        st.session_state.step=10
            
                with c4:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>",unsafe_allow_html=True)
            
                with c5:
                    if st.button("⑪\n📊\nEvaluation",use_container_width=True):
                        st.session_state.step=11
            
                if "step" not in st.session_state:
                    st.session_state.step=1
            
                details={
                    1:"Students submit internship applications through email or the company website.",
                    2:"HR segregates applications according to department requirements.",
                    3:"There are two options: either any HOD/Departments submit internship placement requests through e-Mendix, or HR proposes suitable candidates to the requesting department.",
                    4:"The Head of Department(HOD) reviews and approves the internship request.",
                    5:"Successful candidates receive confirmation via a call from HR.",
                    6:"HR prepares the Offer Letter(OL), Placement Letter(PL), and Reply Letter(RL) via email.",
                    7:"Interns attend briefing sessions with MIS, HR, and Safety departments.",
                    8:"The intern is handed over to the assigned department/plant.",
                    9:"Interns undergo internships at Kaneka.",
                    10:"The intern receives a certificate of completion and an appreciation souvenir from Kaneka.",
                    11:"The department evaluates the intern before completing the internship."         
                }
            
                st.divider()
            
                st.markdown(f"## 📍 Step {st.session_state.step}")
            
                st.info(details[st.session_state.step])
            
                st.progress(st.session_state.step/11)
            
            
                if st.session_state.step == 7:
                    st.success("⭐⭐ These were the internship activities that I was directly involved in. ⭐⭐")
                    st.subheader("Activities Performed During Internship")
                    st.video("videos/briefing_session.mp4")
                
                elif st.session_state.step == 8:
                    st.success("⭐⭐ These were the internship activities that I was directly involved in. ⭐⭐")
                    st.subheader("Activities Performed During Internship")
                    st.video("videos/handover_process.mp4")
                
                elif st.session_state.step == 10:
                    st.success("⭐⭐ These were the internship activities that I was directly involved in. ⭐⭐")
                    st.subheader("Activities Performed During Internship")
                    st.video("videos/appreciation_event.mp4")
                
                else:
                    st.info("📌 These processes were part of the internship workflow, but I was not directly involved 📌.")
                    st.divider()
                    
                                      
            internship_flow()
        
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
