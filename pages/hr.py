import streamlit as st


# ==========================================================
# Learning & Development
# ==========================================================
def learning_development():

    st.write("Focuses on employee training, skill enhancement, and career growth.")

    tab1, tab2, tab3 = st.tabs(
        ["🎓 Internship", "🏫 Training", "📝 BLA"]
    )

    # ------------------------------------------------------
    # Internship
    # ------------------------------------------------------
    with tab1:

        st.subheader("Internship Process Flow")

        if "internship_step" not in st.session_state:
            st.session_state.internship_step = 1

        details = {
            1:"Students submit internship applications.",
            2:"HR segregates applications.",
            3:"Departments request placement.",
            4:"Head of Department approval.",
            5:"Successful candidates receive confirmation.",
            6:"HR prepares internship documents.",
            7:"Briefing session.",
            8:"Handover to department.",
            9:"Internship period.",
            10:"Certificate & appreciation.",
            11:"Department evaluation."
        }

        cols = st.columns(11)

        for i in range(1,12):

            with cols[i-1]:

                if st.button(f"{i}", key=f"step{i}"):

                    st.session_state.internship_step = i

        st.divider()

        step = st.session_state.internship_step

        st.subheader(f"Step {step}")

        st.info(details[step])

        st.progress(step/11)

        if step == 7:

            st.success("Activities I was involved in")

            st.video("videos/briefing_session.mp4")

        elif step == 8:

            st.success("Activities I was involved in")

            st.video("videos/handover_process.mp4")

        elif step == 10:

            st.success("Activities I was involved in")

            st.video("videos/appreciation_event.mp4")

        else:

            st.info("This process was not directly handled by me.")


    # ------------------------------------------------------
    # Training
    # ------------------------------------------------------
    with tab2:

        st.subheader("Training Process")

        st.image(
            "images/training_flow.png",
            use_container_width=True
        )

        st.divider()

        st.write("Training Registration")

        st.video("videos/training/registration.mp4")

        st.write("Training Coordination")

        st.video("videos/training/coordination.mp4")

        st.write("Training Execution")

        st.video("videos/training/execution.mp4")


    # ------------------------------------------------------
    # BLA
    # ------------------------------------------------------
    with tab3:

        st.subheader("Baseline Assessment")

        st.image(
            "images/bla_flow.png",
            use_container_width=True
        )


# ==========================================================
# Reward Management
# ==========================================================
def reward_management():

    st.write("Ensures fair compensation and employee benefits.")

    tab1, tab2, tab3 = st.tabs(
        [
            "💰 Compensation",
            "🏢 General Affairs",
            "📝 Additional Tasks"
        ]
    )

    with tab1:

        st.subheader("Compensation & Benefits")

        st.write(
            """
            • Salary

            • Allowances

            • Employee Benefits

            • Incentives
            """
        )

        st.progress(0.7)

    with tab2:

        st.subheader("General Affairs")

        st.write(
            """
            • Employee Welfare

            • Company Events

            • Office Facilities

            • Administration
            """
        )

        st.slider(
            "Employee Satisfaction",
            0,
            100,
            85
        )

    with tab3:

        st.subheader("Additional Tasks")

        st.markdown("""
- Event Coordination

- Wellness Program

- Recognition Activities
""")


# ==========================================================
# TAIR
# ==========================================================
def tair_management():

    st.write(
        "Talent Acquisition & Industrial Relations"
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Recruitment",
            "Discipline",
            "Additional"
        ]
    )

    with tab1:

        st.markdown("""
- Job Posting

- Resume Screening

- Interview Arrangement

- Onboarding
""")

    with tab2:

        st.markdown("""
- Disciplinary Cases

- Grievance

- Employee Relations
""")

    with tab3:

        st.markdown("""
- Employee Engagement

- Policy Update

- Survey
""")


# ==========================================================
# Main Page
# ==========================================================
def hr_page():

    st.title("HR Organizational Flowchart")

    st.image(
        "images/hr_org_chart.png",
        use_container_width=True
    )

    st.write(
        "Select a department below."
    )

    if "selected_dept" not in st.session_state:

        st.session_state.selected_dept = "L&D"

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "📚 Learning & Development",
            use_container_width=True
        ):

            st.session_state.selected_dept = "L&D"

    with col2:

        if st.button(
            "💎 Reward Management",
            use_container_width=True
        ):

            st.session_state.selected_dept = "Reward"

    with col3:

        if st.button(
            "🎯 TAIR",
            use_container_width=True
        ):

            st.session_state.selected_dept = "TAIR"

    st.divider()

    if st.session_state.selected_dept == "L&D":

        with st.expander(
            "📚 Learning & Development",
            expanded=True
        ):

            learning_development()

    elif st.session_state.selected_dept == "Reward":

        with st.expander(
            "💎 Reward Management",
            expanded=True
        ):

            reward_management()

    elif st.session_state.selected_dept == "TAIR":

        with st.expander(
            "🎯 Talent Acquisition & Industrial Relation",
            expanded=True
        ):

            tair_management()
