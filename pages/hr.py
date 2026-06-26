import streamlit as st

def hr_page():
    st.title("HR Organizational Flowchart")

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
    # Talent Acquisition
    # =====================================================
    with st.expander("🎯 Talent Acquisition & Industrial Relation"):
        st.write("Handles recruitment, onboarding, and maintaining healthy employee relations.")
        st.metric("New Hires", 25, "+5 this month")

    # =====================================================
    # Reward Management
    # =====================================================
    with st.expander("💎 Reward Management"):
        st.write("Ensures fair compensation and manages employee benefits.")
        st.subheader("💰 Compensation & Benefits")
        st.write("Salary structure, allowances, incentives, and employee perks.")
        st.progress(0.7)
        st.subheader("🏢 General Affairs")
        st.write("Workplace facilities, employee welfare, and administrative support.")
        st.slider("Employee Satisfaction Index", 0, 100, 85)

# Call the page function
hr_page()
