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

        # Display Internship Flowchart
        st.image(
            "images/internship_flowchart.png",
            caption="Internship Process Flow",
            use_container_width=True
        )
    
        st.divider()

        if "internship_step" not in st.session_state:
            st.session_state.internship_step = 1

        details = {
            1: "Students submit their internship applications through email or the official Kaneka Malaysia website, together with the required documents such as their resume, cover letter, and university internship letter.",
        
            2: "The HR department reviews and categorizes all applications based on the requested department, internship period, academic background, and current departmental vacancies.",
        
            3: "The relevant department submits an internship placement request through the e-Mendix system, or HR recommends suitable candidates based on the department's requirements.",
        
            4: "The Head of Department (HOD) evaluates the proposed candidate's qualifications and approves the internship request before the recruitment process continues.",
        
            5: "Successful applicants are contacted by the HR Person-in-Charge (PIC) via phone call or email to confirm their acceptance, internship schedule, and reporting details.",
        
            6: "HR prepares all necessary internship documents, including the Offer Letter, Placement Letter, Reply Letter, and any additional administrative documents required before reporting.",
        
            7: "On the first day, interns attend orientation and briefing sessions conducted by the HR Department, MIS Team, and Safety Department to introduce company policies, workplace rules, and safety procedures.",
        
            8: "After completing the orientation, interns are officially handed over to their assigned department or production plant, where they are introduced to their supervisors and daily responsibilities.",
        
            9: "Interns carry out their internship by completing assigned projects, participating in departmental activities, learning company processes, and gaining practical working experience under the supervision of their mentors.",
        
            10: "Upon successful completion of the internship, HR prepares and presents an Internship Certificate together with a token of appreciation as recognition of the intern's contribution.",
        
            11: "Before the internship ends, the department supervisor completes an evaluation form to assess the intern's overall performance, technical skills, communication, teamwork, discipline, and professionalism."
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

            st.video("images/internship1.mp4")

        elif step == 8:

            st.success("Activities I was involved in")

            st.video("images/internship2.mp4")

        elif step == 10:

            st.success("Activities I was involved in")

            st.video("images/internship3.mp4")

        else:

            st.info("This process was not directly handled by me.")


    # ------------------------------------------------------
    # Training
    # ------------------------------------------------------
    with tab2:
    
        st.subheader("Training Process Flow")
    
        # Display Training Flowchart
        st.image(
            "images/training_flowchart.png",
            caption="Training Process Flow",
            use_container_width=True
        )
    
        st.divider()
    
        if "training_step" not in st.session_state:
            st.session_state.training_step = 1
    
        details = {
            1: "The department identifies training requirements based on business needs, new employees, promotions, job changes, or competency development.",
    
            2: "L&D analyzes training needs and identifies competency gaps based on departmental requirements.",
    
            3: "A training plan is prepared, including training objectives, schedule, participants, and training type.",
    
            4: "The training proposal form is submitted together with the required supporting documents for approval.",
    
            5: "The proposal is reviewed, approved, and coordinated with the relevant departments before implementation.",
    
            6: "Suitable training providers and courses are evaluated and selected based on quality, cost, and training objectives.",
    
            7: "The approved training is conducted according to the planned schedule.",
    
            8: "Employees' knowledge and skills are evaluated to determine whether the training objectives have been achieved.",
    
            9: "Employees who successfully meet the required competency level are confirmed as competent."
        }
    
        cols = st.columns(9)
    
        for i in range(1, 10):
    
            with cols[i-1]:
    
                if st.button(f"{i}", key=f"training_step{i}"):
    
                    st.session_state.training_step = i
    
        st.divider()
    
        step = st.session_state.training_step
    
        st.subheader(f"Step {step}")
    
        st.info(details[step])
    
        st.progress(step / 9)
    
        # Only Step 7 contains your activity
        if step == 7:
    
            st.success("Activities I was involved in")
    
            st.video("videos/training_session.mp4")
    
        else:
    
            st.info("This process was not directly handled by me.")
    

    # ------------------------------------------------------
    # BLA
    # ------------------------------------------------------
    with tab3:
    
        st.subheader("Baseline Assessment (BLA) Process Flow")
    
        # Display BLA Flowchart
        st.image(
            "images/bla_flowchart.png",
            caption="Baseline Assessment (BLA) Process Flow",
            use_container_width=True
        )
    
        st.divider()

        st.markdown("### 🎯 Objective of Baseline Assessment (BLA)")

        st.info("""
        **Objective:**
        
        To identify gaps in the technical skills, knowledge, and competency levels of employees
        based on the requirements of their respective job positions.
        """)
        
        st.divider()
    
        if "bla_step" not in st.session_state:
            st.session_state.bla_step = 1
    
        details = {
            1: "Develop the BLA competency framework based on job functions and required competency levels.",
    
            2: "Conduct a challenge session with Top Management to review and improve the proposed BLA framework.",
    
            3: "Obtain management approval before implementing the BLA framework.",
    
            4: "Compile the approved BLA competency standards for implementation.",
    
            5: "Conduct the BLA pre-assessment to evaluate employees' current competency levels.",
    
            6: "Analyze assessment results and identify competency gaps.",
    
            7: "Develop suitable gap closure activities such as training, coaching, mentoring, or OJT.",
    
            8: "Implement the planned competency development activities.",
    
            9: "Conduct a BLA re-assessment to measure competency improvement.",
    
            10: "Review the gap closure results to determine whether competency requirements have been achieved.",
    
            11: "Confirm employees who have successfully achieved the required competency level.",
    
            12: "Monitor employees' competency and performance for continuous improvement."
        }
    
        cols = st.columns(12)
    
        for i in range(1, 13):
    
            with cols[i-1]:
    
                if st.button(f"{i}", key=f"bla_step{i}"):
    
                    st.session_state.bla_step = i
    
        st.divider()
    
        step = st.session_state.bla_step
    
        st.subheader(f"Step {step}")
    
        st.info(details[step])
    
        st.progress(step / 12)
    
        st.info("This process was not directly handled by me.")

    
        # ------------------------------------------------------
        # My Contribution
        # ------------------------------------------------------
        st.divider()
    
        st.success("💻 My Contribution: BLA Self-Paced Learning (SPL) Development")
    
        st.write("""
        During my internship, I was assigned to develop the **Baseline Assessment (BLA)
        Self-Paced Learning (SPL) module** using **iSpring Suite**.
    
        My responsibilities included:
        - Designing the learning module structure.
        - Creating interactive learning content.
        - Organizing training materials.
        - Publishing the module for employees' self-paced learning.
        """)
    
        st.video("videos/bla_spl_development.mp4")


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
            "Additional Tasks"
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

    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 1rem;
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
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

            st.session_state.selected_dept = "RM"

    with col3:

        if st.button(
            "🎯  Talent Acquisition & Industrial Relation",
            use_container_width=True
        ):

            st.session_state.selected_dept = "TA&IR"

    st.divider()

    if st.session_state.selected_dept == "L&D":

        with st.expander(
            "📚 Learning & Development",
            expanded=True
        ):

            learning_development()

    elif st.session_state.selected_dept == "RM":

        with st.expander(
            "💎 Reward Management",
            expanded=True
        ):

            reward_management()

    elif st.session_state.selected_dept == "TA&IR":

        with st.expander(
            "🎯 Talent Acquisition & Industrial Relation",
            expanded=True
        ):

            tair_management()
