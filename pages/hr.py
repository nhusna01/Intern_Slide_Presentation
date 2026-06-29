import streamlit as st

    # ================= HR Page =================
    def hr_page():
        st.title("HR Organizational Flowchart")
    
        # Cover Page
        st.image("images/hr_org_chart.png", caption="HR Organizational Chart", use_container_width=True)
        st.write("Select a department to explore:")
    
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📚 Learning & Development"):
                st.session_state.selected_dept = "L&D"
        with col2:
            if st.button("💎 Reward Management"):
                st.session_state.selected_dept = "Reward"
        with col3:
            if st.button("🎯 TAIR"):
                st.session_state.selected_dept = "TAIR"
    
        # Show selected department details
        if "selected_dept" in st.session_state:
            if st.session_state.selected_dept == "L&D":
                with st.expander("📚 Learning & Development", expanded=True):
                    st.write("Focuses on employee training, skill enhancement, and career growth.")
                    tab1, tab2, tab3 = st.tabs(["🎓 Internship", "🏫 Training", "📝 BLA"])
                    with tab1: internship_flow()
                    with tab2: training_flow()
                    with tab3: bla_flow()
    
            elif st.session_state.selected_dept == "Reward":
                with st.expander("💎 Reward Management", expanded=True):
                    reward_management()
    
            elif st.session_state.selected_dept == "TAIR":
                with st.expander("🎯 Talent Acquisition & Industrial Relation", expanded=True):
                    tair_management()


    # =====================================================
    # Learning & Development
    # =====================================================
    with st.expander("📚 Learning & Development", expanded=True):
        st.write("Focuses on employee training, skill enhancement, and career growth.")

        tab1, tab2, tab3 = st.tabs(["🎓 Internship", "🏫 Training", "📝 BLA"])

        # ================= Internship =================
        with tab1:
            st.markdown("## 🎓 Internship Process Flow")

            # Initialize session state
            if "internship_step" not in st.session_state:
                st.session_state.internship_step = 1

            # Steps dictionary
            details = {
                1: "Students submit internship applications through email or the company website.",
                2: "HR segregates applications according to department requirements.",
                3: "Departments request placements via e-Mendix or HR proposes candidates.",
                4: "The Head of Department reviews and approves the request.",
                5: "Successful candidates receive confirmation via HR call.",
                6: "HR prepares Offer Letter, Placement Letter, and Reply Letter.",
                7: "Interns attend briefing sessions with MIS, HR, and Safety.",
                8: "Interns are handed over to the assigned department/plant.",
                9: "Interns undergo internships at Kaneka.",
                10: "Intern receives certificate and appreciation souvenir.",
                11: "Department evaluates the intern before completion."
            }

            # Step buttons
            cols = st.columns(11)
            for i in range(1, 12):
                with cols[i-1]:
                    if st.button(f"Step {i}", key=f"btn_step_{i}"):
                        st.session_state.internship_step = i

            # Display step info
            st.divider()
            st.markdown(f"## 📍 Step {st.session_state.internship_step}")
            st.info(details[st.session_state.internship_step])
            st.progress(st.session_state.internship_step / 11)

            # Show videos for specific steps
            if st.session_state.internship_step == 7:
                st.success("⭐⭐ Activities I was directly involved in ⭐⭐")
                st.video("videos/briefing_session.mp4")
            elif st.session_state.internship_step == 8:
                st.success("⭐⭐ Activities I was directly involved in ⭐⭐")
                st.video("videos/handover_process.mp4")
            elif st.session_state.internship_step == 10:
                st.success("⭐⭐ Activities I was directly involved in ⭐⭐")
                st.video("videos/appreciation_event.mp4")
            else:
                st.info("📌 These processes were part of the internship workflow, but I was not directly involved 📌.")

        # ================= Training =================
        with tab2:
            st.subheader("Training Process Flow")
            st.image("images/training_flow.png", caption="Training Process Flow", use_container_width=True)
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
            st.image("images/bla_flow.png", caption="BLA Process Flow", use_container_width=True)

    # =====================================================
    # Reward Management
    # =====================================================
    with st.expander("💎 Reward Management"):
        st.write("Ensures fair compensation and manages employee benefits.")
    
        # Create tabs for the two sections
        tab1, tab2 = st.tabs(["💰 Compensation & Benefits", "🏢 General Affairs"])
    
        # ================= Compensation & Benefits =================
        with tab1:
            st.subheader("💰 Compensation & Benefits")
            st.write("Salary structure, allowances, incentives, and employee perks.")
            st.progress(0.7)  # Example progress bar
    
        # ================= General Affairs =================
        with tab2:
            st.subheader("🏢 General Affairs")
            st.write("Workplace facilities, employee welfare, company events, and administrative support.")
            st.slider("Employee Satisfaction Index", 0, 100, 85)

         # ================= Additional Tasks =================
            with tab3:
                st.subheader("📝 Additional Tasks")
                st.write("Covers extra responsibilities under Reward Management such as:")
                st.markdown("- **Event Coordination** → Organizing employee appreciation events.")
                st.markdown("- **Wellness Programs** → Managing fitness challenges and health campaigns.")
                st.markdown("- **Recognition Initiatives** → Handling awards, certificates, and incentive posters.")


    # =====================================================
    # Talent Acquisition & Industrial Relation (TAIR)
    # =====================================================
    with st.expander("🎯 Talent Acquisition & Industrial Relation"):
        st.write("Handles recruitment, onboarding, and maintaining healthy employee relations.")
    
        # Create tabs for the three sections
        tab1, tab2, tab3 = st.tabs(["📋 Recruitment Process", "⚖️ Discipline & Grievance", "📝 Additional Tasks"])
    
        # ================= Recruitment Process =================
        with tab1:
            st.subheader("📋 Recruitment Process")
            st.write("Covers activities such as:")
            st.markdown("- **Job Posting** → Preparing and publishing job advertisements.")
            st.markdown("- **Application Screening** → Reviewing resumes and shortlisting candidates.")
            st.markdown("- **Interview Coordination** → Scheduling and conducting interviews with departments.")
            st.markdown("- **Onboarding** → Guiding new hires through orientation and documentation.")
    
        # ================= Discipline & Grievance =================
        with tab2:
            st.subheader("⚖️ Discipline, Grievance & Exposure")
            st.write("Focuses on maintaining healthy employee relations:")
            st.markdown("- **Disciplinary Actions** → Handling misconduct cases fairly and transparently.")
            st.markdown("- **Grievance Handling** → Addressing employee complaints and disputes.")
            st.markdown("- **Exposure Programs** → Promoting awareness sessions on workplace ethics and compliance.")
    
        # ================= Additional Tasks =================
        with tab3:
            st.subheader("📝 Additional Tasks")
            st.write("Extra responsibilities under TAIR include:")
            st.markdown("- **Employee Engagement** → Organizing team-building and bonding activities.")
            st.markdown("- **Policy Updates** → Assisting in drafting and updating HR policies.")
            st.markdown("- **Surveys & Feedback** → Conducting employee satisfaction surveys and reporting results.")


# Call the page function
hr_page()
