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
    
            st.video("videos/training1.mp4")
    
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

    
    # ------------------------------------------------------
    # Compensation & Benefits
    # ------------------------------------------------------
    with tab1:
    
        st.subheader("💼 Compensation & Benefits")
    
        st.divider()
    
        # -------------------------------
        # Payroll Section
        # -------------------------------
        with st.expander("💰 Payroll", expanded=True):
    
            # Two images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image("images/payroll1.png", caption="Payroll Overview", use_container_width=True)
            with col2:
                st.image("images/payroll2.png", caption="Payroll Activities", use_container_width=True)
    
            st.markdown("""
            **Wage Period**
            - Any month from 21st day of previous month to 20th day of the month.
    
            **Payment of Wages**
            - 27th every month.
    
            **Overtime Definition**
            - Work exceeding 8 hours.
            - After completed 30 minutes, considered OT.
    
            **My Involvement**
            - Assist calculate the extra OT.
            - Assist check eligibility for Housing Loan Interest Subsidy (employees exceeding 240 months).
            - Assist change work schedule in Oracle system for shift employees (iMODA plant).
            """)
    
        # -------------------------------
        # Medical Management Section
        # -------------------------------
        with st.expander("🏥 Medical Management", expanded=True):
    
            # Two images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image("images/medical1.png", caption="Medical Benefits", use_container_width=True)
            with col2:
                st.image("images/medical2.png", caption="Insurance & Entitlement", use_container_width=True)
    
            st.markdown("""
            **Medical Benefits**
            - Inpatient
            - Outpatient
            - Dental
            - Optical
    
            **Insurance (GTL)**
            - Group Term Life.
    
            **Medical Entitlement for Dependent Hospitalization**
            - Specialist Visit.
    
            **My Involvement**
            - Processing monthly medical invoice received from TPA (Third Party Administration).
            - Assist verifying invoice amount, stamp VOP, segregate according to company.
            """)
    
        # -------------------------------
        # Statutory Contribution & Other Deductions Section
        # -------------------------------
        with st.expander("📑 Statutory Contribution & Other Deductions", expanded=True):
    
            # Two images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image("images/contribution1.png", caption="Statutory Contributions", use_container_width=True)
            with col2:
                st.image("images/contribution2.png", caption="Other Deductions", use_container_width=True)
    
            st.markdown("""
            **Statutory Contribution**
            - Mandatory deductions required by law.
            - Examples: EPF, SOCSO & EIS, Income Tax.
    
            **Other Deductions**
            - Voluntary deductions by agreement.
            - Examples: Zakat, Motor Vehicle Loan (MVL), Tabung Haji, ASNB, Union Membership Fee.
    
            **My Involvement**
            - Stamp date received, segregate according to organization (LHDN, Tabung Haji, Zakat).
            - Fill in employee details for SOCSO (‘Borang 34’ for accident case).
            """)


    # ------------------------------------------------------
    # General Affairs
    # ------------------------------------------------------
    with tab2:
    
        st.subheader("🏢 General Affairs")
    
        st.divider()
    
        # -------------------------------
        # Employee Welfare Section
        # -------------------------------
        with st.expander("🤝 Employee Welfare", expanded=True):
    
            # Two images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image("images/welfare1.png", caption="Employee Welfare Programs", use_container_width=True)
            with col2:
                st.image("images/welfare2.png", caption="Support & Assistance", use_container_width=True)
    
            st.markdown("""
            **Overview**
            - Welfare initiatives to support employees’ well-being.
            - Includes health, safety, and financial assistance programs.
    
            **Examples**
            - Subsidies and allowances.
            - Employee support services.
            - Attend Kaneka Health Talk regarding the Sleep Apnea, and Mental Health, Stress, & Well-being.
            """)
    
        # -------------------------------
        # Company Events Section
        # -------------------------------
        with st.expander("🎉 Company Events", expanded=True):
    
            # Two images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image("images/events1.png", caption="Annual Company Event", use_container_width=True)
            with col2:
                st.image("images/events2.png", caption="Team Building Activities", use_container_width=True)
    
            st.markdown("""
            **Overview**
            - Organized events to strengthen employee engagement and teamwork.
    
            **Examples**
            - Attend Kaneka Annual Dinner appreciation and festive (Hari Raya) celebrations.
            - Attend HR Team building sessions to build team bonding.
            - Kaneka Run Ekiden, calculate the amount of payment for Ekiden.
            """)
    
        # -------------------------------
        # Company Facilities Section
        # -------------------------------
        with st.expander("🏭 Company Facilities", expanded=True):
    
            # Two images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image("images/facilities1.png", caption="Office Facilities", use_container_width=True)
            with col2:
                st.image("images/facilities2.png", caption="Plant Facilities", use_container_width=True)
    
            st.markdown("""
            **Overview**
            - Facilities provided to ensure a safe and productive work environment.
    
            **Examples**
            - Office amenities and meeting rooms.
            - Plant facilities for shift employees.
            - Recreational and common areas.
            """)

       

    with tab3:

        st.subheader("🌟 Additional Tasks & Activities")
    
        st.write(
            "Besides my daily responsibilities in the Reward Management department, "
            "I also participated in several company events and activities."
        )
    
        # ------------------------------------------------------
        # Jamuan Raya
        # ------------------------------------------------------
        with st.expander("🎉 Jamuan Raya 2026 (Admin 2 Committee)", expanded=True):
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.image(
                    "images/raya1.png",
                    caption="Event Preparation",
                    use_container_width=True
                )
    
            with col2:
                st.image(
                    "images/raya2.png",
                    caption="Hari Raya Celebration",
                    use_container_width=True
                )
    
            st.markdown("""
    **Role**
    - Assisted the **Admin 2 Committee** in organizing the Hari Raya celebration.
    - Supported event preparation and logistics.
    - Helped ensure the event ran smoothly.
    """)
    
        # ------------------------------------------------------
        # Karakuri Competition
        # ------------------------------------------------------
        with st.expander("🏆 Karakuri Competition", expanded=True):
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.image(
                    "images/karakuri1.png",
                    caption="Competition Project",
                    use_container_width=True
                )
    
            with col2:
                st.image(
                    "images/karakuri2.png",
                    caption="Award Ceremony",
                    use_container_width=True
                )
    
            st.markdown("""
    **Achievement**
    - Participated in the **Karakuri Competition**.
    - Worked together with the team throughout the competition.
    - 🥈 **Won Second Place.**
    """)
    
        # ------------------------------------------------------
        # Kaneka Run Ekiden
        # ------------------------------------------------------
        with st.expander("🏃 Kaneka Run Ekiden", expanded=True):
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.image(
                    "images/ekiden1.png",
                    caption="Race Day",
                    use_container_width=True
                )
    
            with col2:
                st.image(
                    "images/ekiden2.png",
                    caption="Team Photo",
                    use_container_width=True
                )
    
            st.markdown("""
    **Achievement**
    - Participated in the **Kaneka Run Ekiden**.
    - Represented the HR Department.
    - 🥉 **Won Third Place.**
    """)


# ==========================================================
# TAIR
# ==========================================================
def tair_management():

    st.write(
        "Talent Acquisition & Industrial Relations"
    )

    tab1, tab2 = st.tabs(
        [
            "Recruitment",
            "Discipline",
        ]
    )

    # ------------------------------------------------------
    # Recruitment
    # ------------------------------------------------------
    with tab1:
    
        st.subheader("Recruitment Process Flow")
    
        # Display Recruitment Flowchart
        st.image(
            "images/iv.png",
            caption="Recruitment Process Flow",
            use_container_width=True
        )
    
        st.divider()
    
        if "recruitment_step" not in st.session_state:
            st.session_state.recruitment_step = 1
    
        details = {
            1: "Formal Manpower Request: Requestor submits an electronic Manpower Request form (e-MPR) via the Mendix system.",
            
            2: "Resume Bank Distribution: Talent Acquisition PIC shares the compiled resume bank with the designated hiring panel for review.",
            
            3: "Interview Coordination: TA PIC manages the logistics of the Interview session, including aligning the panel’s schedule and booking the necessary meeting rooms.",
            
            4: "The Interview Session: Managed by the TA PIC, the Interview takes place on the appointed day (this is a critical milestone in the process).",
            
            5: "Pre-Employment Medical Checkup: The successful candidate is required to complete a medical examination before the process can proceed.",
            
            6: "The Official Offer: Once accepted, the TA PIC officially informs the candidate and provides them with a formal offer letter.",
            
            7: "Reporting Dates & Feedback: The TA PIC emails the reporting duty date to the successful candidate, while simultaneously sending feedback or status updates to unsuccessful applicants.",
            
            8: "Onboarding & Training: The process concludes as the new staff member joins the team and undergoes On-the-Job (OJT) training."
        }
    
        cols = st.columns(8)
    
        for i in range(1, 9):
    
            with cols[i-1]:
    
                if st.button(f"{i}", key=f"recruitment_step{i}"):
    
                    st.session_state.recruitment_step = i
    
        st.divider()
    
        step = st.session_state.recruitment_step
    
        st.subheader(f"Stage {step}")
    
        st.info(details[step])
    
        st.progress(step / 8)
    
        # Example: Only Stage 4 contains your activity
        if step == 4:
            st.success("Activities I was involved in")
            st.video("videos/iv.mp4")
        else:
            st.info("This process was not directly handled by me.")


    with tab2:
    
        st.subheader("⚖️ Discipline Management")
    
        # Display Employee Conduct & Resolution Guide
        st.image(
            "images/discipline1.png",
            caption="Employee Conduct and Resolution Guide",
            use_container_width=True
        )
    
        st.divider()
    
        # Disciplinary & Misconduct Management
        with st.expander("⚖️ Disciplinary & Misconduct Management", expanded=True):
    
            st.markdown("""
    **Definition**
    
    Misconduct refers to any act or behavior that violates the company's Terms and Conditions of Employment or Company Rules.
    
    **Misconduct Categories**
    
    🔹 **Level 1 – Minor Misconduct**
    - Minor violations of company rules.
    - Example: Late attendance.
    
    🔹 **Level 2 – Serious Misconduct**
    - Repeated or more serious violations.
    - Example: Habitual late attendance.
    
    🔹 **Level 3 – Major Misconduct**
    - Severe misconduct that may lead to disciplinary action.
    - Example: Unauthorized use or falsification of a signature.
    """)
    
        # Grievance Procedure
        with st.expander("🤝 Grievance Procedure", expanded=True):
    
            st.markdown("""
    The grievance procedure provides employees with a fair and systematic way to resolve workplace issues.
    
    **Step 1 – Immediate Superior**
    - Discuss the issue with your immediate superior within **3 working days**.
    
    **Step 2 – Division / Production Head**
    - If unresolved, escalate the issue within **5 working days**.
    
    **Step 3 – Human Resources**
    - Submit a formal appeal to HR within **7 working days** if the issue remains unresolved.
    """)
    
        # Employee Engagement & Support
        with st.expander("📢 Employee Engagement & Support", expanded=True):
    
            st.markdown("""
    **Support Channels**
    - 📞 Kaneka Care
    - 📧 HR Helpdesk
    - 🛡️ Whistleblower Hotline
    
    **Employee Engagement**
    - HR Policy Briefings
    - Business Code of Conduct Sessions
    - Employee Awareness & Communication Programs
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
