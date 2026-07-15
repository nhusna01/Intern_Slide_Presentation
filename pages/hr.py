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
    
            st.video("images/training.mp4")
    
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
            st.markdown("""
    
            **Overtime Definition**
            - Work exceeding **8 hours per day** is considered overtime.
            - Only after completing **30 minutes of extra work** does it count as OT.

            **Attendance Award**
            - Recognition for employees with consistent attendance

            | Activity                  | Purpose                                       | Impact on HR / Payroll                  |
            |---------------------------|-----------------------------------------------|-----------------------------------------|
            | **Overtime Calculation**  | Ensures fair pay for extra hours worked.      | Prevents disputes, keeps payroll accurate. |
            | **Shift Schedule Mgmt**   | Keeps rosters correct for shift employees.    | Ensures proper tracking and wage calculation. |
            | **Attendance Award Check**| Recognizes reliable employees.                | Boosts morale, encourages punctuality.   |
                
            **My Involvement**
            - Assist calculate the overtime for the security guard according to their shift group.
            - Assist check eligibility for list of employee that take leave for more than 7 days (not received Attendance Award).
            - Assist change work schedule in Excel file for shift employees (iMODA plant).
            """)
            
            # Two images side by side
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("images/payroll3.jpg", caption="Extra OT (in hour) calculation", width=250)
            with col2:
                st.image("images/payroll2.png", caption="Attendance Award Eligibility", width=250)
            with col3:
                st.image("images/payroll1.jpg", caption="Revise Work Schedule", width=250)

    
        # -------------------------------
        # Medical Management Section
        # -------------------------------
        with st.expander("🏥 Medical Management", expanded=True):
    
            st.markdown("""
            **Medical Benefits**
            - Inpatient
            - Outpatient
            - Dental
            - Spectacle
    
            **Documents Used in HR**
            | Document        | Purpose                                | Used By HR For                                      |
            |-----------------|----------------------------------------|-----------------------------------------------------|
            | Medical Invoice | Proof of medical expenses              | Claim reimbursement, payment verification, finance records |
            | Medical Report  | Medical condition information from doctor | Medical leave review, employee support, workplace arrangement |
        
    
            **My Involvement**
            - Assist in monthly medical invoice received from TPA (Third Party Administration).
            - Assist verifying invoice amount, stamp VOP, segregate according to company.
            - Standardize the format and compile the IP and OP medical report into each excel sheet.
            """)


            # Two images side by side
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("images/medical1.png", caption="Medical Invoices April", width=250)
            with col2:
                st.image("images/medical2.png", caption="Medical Invoices June", width=250)
            with col3:
                st.image("images/medical3.png", caption="Medical Report", width=250)
    
        # -------------------------------
        # Statutory Contribution & Other Deductions Section
        # -------------------------------
        with st.expander("📑 Statutory Contribution & Other Deductions", expanded=True):
    
            st.markdown("""
            **Statutory Contribution**
            - Mandatory deductions required by law.
            - Examples: EPF, SOCSO, Income Tax, Employment Insurance System (EIS).
    
            **Other Deductions**
            - Voluntary deductions by agreement.
            - Examples: Zakat, Tabung Haji, Motor Vehicle Loan (MVL).

            | Category                  | Purpose                                                    | Impact on HR / Payroll                          |
            |---------------------------|------------------------------------------------------------|-------------------------------------------------|
            | **Statutory Contribution**| Mandatory by law, ensures compliance with government rules.| HR must deduct EPF, SOCSO, EIS, Income Tax. To protects retirement, healthcare, and job security for the employees. |
            | **Other Deductions**      | Voluntary, based on employee agreement or choice.          | HR processes Zakat, Tabung Haji, ASNB, Union Fees, MVL. To supports religious, financial, and personal commitments of employees. |
            
    
            **My Involvement**
            - Stamp date received, segregate according to organization (LHDN, Tabung Haji, Zakat).
            - Identify the resignee employee in Excel file, and then update the resignee date in the Perkeso system (Perkeso Assist).
            - Filing the zakat, tabung haji, and lhdn documents according to the company.
            """)

            # Two images side by side
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("images/contribution1.png", caption="Statutory Contributions", use_container_width=True)
            with col2:
                st.image("images/contribution3.png", caption="Update Resignee Date in Perkeso System", use_container_width=True)
            with col3:
                st.image("images/contribution2.png", caption="Filing Voluntary Deductions Documents", use_container_width=True)
                                                                 

                                                               
    # ------------------------------------------------------
    # General Affairs
    # ------------------------------------------------------
    with tab2:
        
        st.subheader(" General Affairs")
    
        st.divider()
        # ------------------------------------------------------
        # Employee Benefits
        # ------------------------------------------------------
        with st.expander("🤝 Employee Benefits", expanded=True):
        
            # ------------------------------------------------------
            # Timeslip Organization
            # ------------------------------------------------------
            st.markdown(
                '<div class="ga-subtitle">⏰ Timeslip Organization</div>',
                unsafe_allow_html=True
            )
            
            st.markdown("""
            <div class="ga-text">
        
            **Responsibilities**
            - Assisted in sorting employee timeslips according to the respective months.
            - Organized timeslip records systematically for easier filing and retrieval.
            - Ensured timeslips were arranged accurately before filing.
        
            </div>
            """, unsafe_allow_html=True)
        
            col1, col2 = st.columns(2)
        
            with col1:
                st.image(
                    "images/timeslip1.jpg",
                    caption="Timeslip Sorting Process 1",
                    width=250
                )
                
            with col2:
                st.image(
                "images/timeslip2.jpg",
                caption="Timeslip Sorting Process 2",
                width=250
            )
        
        
        # ------------------------------------------------------
        # Event Management
        # ------------------------------------------------------
        with st.expander("🎉 Event Management", expanded=True):
        
            # ------------------------------------------------------
            # Corporate Wellness Programme
            # ------------------------------------------------------
            st.markdown(
                '<div class="ga-subtitle">💙 Corporate Wellness Programme</div>',
                unsafe_allow_html=True
            )
    
            st.markdown("""
            <div class="ga-text">
    
            **Overview**
            - Participated in corporate wellness initiatives to promote health, safety, and well-being of employees.
        
            **Activities**
            - Attended Kaneka Health Talk on **Sleep Apnea**.
            - Attended Kaneka Health Talk on **Mental Health, Stress & Well-being**.
            - Assist in identify the list of employees that paricipated in the both **Sleep Apnea** & **Mental Health, Stress & Well-being** health programme.
            - Gained awareness of workplace health and wellness initiatives through the **Corporate Wellness Programme**.
        
            </div>
            """, unsafe_allow_html=True)
        
            col1, col2, col3 = st.columns(3)
        
            with col1:
                st.image(
                    "images/welfare2.jpg",
                    caption="Kaneka Online Health Talk: Sleep Apnea",
                    width=250
                )
        
            with col2:
                st.image(
                    "images/welfare1.jpg",
                    caption="Kaneka Online Health Talk: Mental Health, Stress & Emotional Well-Being ",
                    width=250
                )
    
            with col3:
                st.image(
                    "images/welfare3.png",
                    caption="Overall Wellness Program Participation Record",
                    width=250
                )
    
        
            st.divider()
        
            # ------------------------------------------------------
            # Company Events
            # ------------------------------------------------------
            st.markdown(
                '<div class="ga-subtitle">🎊 Company Events</div>',
                unsafe_allow_html=True
            )
    
            st.markdown("""
            <div class="ga-text">
        
            **Overview**
            - Participated in company activities that strengthened employee engagement, collaboration, and teamwork.
        
            **Activities**
            - Prepare the draft poster of the events 
            - Participated in KAD2025 Committee Appreciation Luncheon at De Rhu Beach Resort and assist in preparing the token for KAD2025 committee.
            - Assisted in improving the cafeteria environment by organizing and removing outdated signage on table top.
            - Assisted in calculating participation fees for the Kaneka Run Ekiden.
            - Assist in preparing the token number for the winners.
            - Assist in sorting the Kaneka Tshirt and bit according to the respective departments/plants.
        
            </div>
            """, unsafe_allow_html=True)
        
            col1, col2, col3, col4, col5, col6 = st.columns(6)
        
            with col1:
                st.image(
                    "images/events1.jpg",
                    caption="Kaneka Run Ekiden Preparation 1",
                    width=250
                )
        
            with col2:
                st.image(
                    "images/events2.jpg",
                    caption="Kaneka Ekiden Preparation 2",
                    width=250
                )
    
            with col3:
                st.image(
                    "images/events3.jpg",
                    caption="Kaneka Ekiden Tshirt Distribution",
                    width=250
                )
    
            with col4:
                st.image(
                    "images/events4.png",
                    caption="Kaneka Health Programme Poster",
                    width=250
                )
        
            with col5:
                st.image(
                    "images/events5.png",
                    caption="KAD2025 Appreciation Token Preparation",
                    width=250
                )
    
            with col6:
                st.image(
                    "images/events6.png",
                    caption="Cafeteria Clean Signage",
                    width=250
                )
        
            st.divider()
    

    # ------------------------------------------------------
    # Additional Tasks
    # ------------------------------------------------------
    with tab3:
        
        st.subheader(" Additional Tasks")
    
        st.divider()
    
        st.markdown("""
        <div class="additional-text">
        Besides my daily responsibilities in the Reward Management department,
        I also participated in several company events and activities.
        </div>
        """, unsafe_allow_html=True)
    
        # ------------------------------------------------------
        # Jamuan Raya
        # ------------------------------------------------------
        with st.expander("🎉 Jamuan Raya 2026 (Admin 2 Committee)", expanded=True):
            st.markdown("""
            <div class="additional-text">
    
            **Activities**
            - Attended Hari Raya celebrations organized by various departments and production plants.
            - Assisted the **Admin 2 Committee** in organizing the Hari Raya celebration.
            - Supported event preparation including:
                1- Prepared beverages for the celebration.
                2- Arranged food according to the designated layout.
                3- Assisted in packing and distributing the remaining food to employees.
                4- Supported post-event clean-up and restored the venue after the celebration.
    
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)    
            with col1:
                st.image(
                    "images/raya11.png",
                    caption="Hari Raya Celebration - Admin 2",
                    width=250
                )
    
            with col2:
                st.image(
                    "images/raya22.png",
                    caption="Hari Raya Celebration - Admin 1",
                    width=250
                )
    
            with col3:
                st.image(
                    "images/raya33.png",
                    caption="Hari Raya Celebration - Maintenance",
                    width=250
                )
    
            with col4:
                st.image(
                    "images/raya44.jpg",
                    caption="Hari Raya Celebration - KAM Plant",
                    width=250
                )

            st.divider()
    
        # ------------------------------------------------------
        # Karakuri Competition
        # ------------------------------------------------------
        with st.expander("🏆 Karakuri Competition", expanded=True):
    
            st.markdown("""
            <div class="additional-text">
    
            **Achievement**
            - Assisted in assembling the PVC pipe trolley based on the approved design.
            - Presented the problem statement and explained the trolley design and its purpose.
            - Collaborated with team members throughout the competition.
            - **Won Second Place.**
    
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)
    
            with col1:
                st.image(
                    "images/karakuri2.png",
                    caption="Competition Project",
                    width=250
                )
    
            with col2:
                st.image(
                    "images/karakuri1.png",
                    caption="Project Presentation & Demonstration",
                    width=250
                )
    
            with col3:
                st.image(
                    "images/karakuri3.jpg",
                    caption="Award Ceremony",
                    width=250
                )
    
            with col4:
                st.image(
                    "images/karakuri4.jpg",
                    caption="Group Photo Session",
                    width=250
                )

            st.divider()    
        
    
        # ------------------------------------------------------
        # Kaneka Run Ekiden
        # ------------------------------------------------------
        with st.expander("🏃 Kaneka Run Ekiden", expanded=True):
    
            col1, col2, col3, col4 = st.columns(4)
    
            with col1:
                st.image(
                    "images/ekiden1.JPG",
                    caption="Warm-up Session",
                    width=250
                )
    
            with col2:
                st.image(
                    "images/ekiden2.JPG",
                    caption="Race Participation",
                    width=250
                )
    
            with col3:
                st.image(
                    "images/ekiden3.jpg",
                    caption="Award Ceremony",
                    width=250
                )
    
            with col4:
                st.image(
                    "images/ekiden4.png",
                    caption="Photo Session with Interns",
                    width=250
                )
    
            st.markdown("""
            <div class="additional-text">
    
            **Achievement**
            - Participated in the **Kaneka Run Ekiden**.
            - Represented the HR Department.
            - **Won Third Place.**
    
            </div>
            """, unsafe_allow_html=True)


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
    
        st.subheader(f"Steps {step}")
    
        # Display details with larger font
        st.markdown(f"""
        <div style="font-size:24px;">
        {details[step]}
        </div>
        """, unsafe_allow_html=True)
    
        st.progress(step / 8)
    
        # Example: Only Step 4 contains your activity
        if step == 4:
            st.success("Activities I was involved in")
            st.video("images/iv.mp4")
        else:
            st.info("This process was not directly handled by me.")


    # ------------------------------------------------------
    # Disciplinary & Misconduct 
    # ------------------------------------------------------
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
                <div style="font-size:24px;">
                <b>Definition</b><br><br>
                Misconduct refers to any act or behavior that violates the company's Terms and Conditions of Employment or Company Rules.<br><br>
            
                <b>Misconduct Categories</b><br><br>
                🔹 <b>Category 1 – Minor Misconduct</b><br>
                - Minor violations of company rules.<br>
                - Example: Late attendance.<br><br>
            
                🔹 <b>Category 2 – Serious Misconduct</b><br>
                - Repeated or more serious violations.<br>
                - Example: Habitual late attendance.<br><br>
            
                🔹 <b>Category 3 – Major Misconduct</b><br>
                - Severe misconduct that may lead to disciplinary action.<br>
                - Example: Unauthorized use or falsification of a signature.<br>
                </div>
                """, unsafe_allow_html=True)
            
                        
        
            # Employee Engagement & Support
            with st.expander("📢 Employee Engagement & Support", expanded=True):
                st.markdown("""
                <div style="font-size:24px;">
                <b>Support Channels</b><br>
                - 📞 Kaneka Care<br>
                - 📧 HR Helpdesk<br>
                - 🛡️ Whistleblower Hotline<br><br>
        
                <b>Employee Engagement</b><br>
                - HR Policy Briefings<br>
                - Business Code of Conduct Sessions<br>
                - Employee Awareness & Communication Programs<br>
                </div>
                """, unsafe_allow_html=True)
        
        
            # Activities Involved
            with st.expander("📝 Activities I Involved In", expanded=True):
                st.markdown("""
                <div style="font-size:24px;">
                Here are the activities I participated in under Discipline Management:<br><br>
            
                - Coordinated seating arrangements and prepared documents during domestic inquiry.<br>
                - Converted the Employee Engagement Survey into Google Form using the provided template to ease distribution.<br>
                - Participated in briefing sessions on the employee engagement survey.<br>
                - Attended briefing at the Modifier Plant covering:<br>
                  • Disciplinary procedures<br>
                  • Grievance handling<br>
                  • Harassment awareness<br>
                  • Business Code of Conduct<br>
                - Analyzed employee engagement survey data in Microsoft Excel. Calculated the count, total, and percentage for each <br>
                  response scale (Strongly Disagree, Disagree, Agree, and Strongly Agree). Created pie charts to visualize the response <br>
                  distribution for each survey section.<br><br>
            
                These activities provided me with valuable exposure to HR operations, grievance resolution, and workplace ethics.<br>
                </div>
                """, unsafe_allow_html=True)
            
                # Display related video instead of images
                st.video("images/discipline.mp4")


# ==========================================================
# Chapter 3 – Internship Journey Page
# ==========================================================
def hr_page():
    st.markdown("""
        <style>
        .chapter-title {
            font-family: 'Georgia', serif;
            font-size: 60px;
            color: #2c3e50;
            text-align: center;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }
        .chapter-caption {
            font-family: 'Courier New', monospace;
            font-size: 24px;
            color: #555;
            text-align: center;
            animation: fadeIn 3s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='chapter-title'>📖 Chapter 3 – Internship Journey IN HR Division</div>", unsafe_allow_html=True)
    st.markdown("<div class='chapter-caption'>✨ Flip through my internship journey as HR intern like a digital book ✨</div>", unsafe_allow_html=True)
    
    st.divider()
    
    
    # ======================================================
    # 🎯 Internship Objectives
    # ======================================================
    
    st.header("🎯 Internship Objectives")
    
    st.markdown("""
    Before exploring the HR Division processes, I would like to share my objectives 
    during my internship at **Kaneka Malaysia**.
    
    As an **HR Intern** with an **IT student background**, my objectives were:
    
    - 💻 **Apply IT skills in HR**  
      Support HR systems (Mendix, Oracle) and contribute to digital transformation.
    
    - 🏢 **Understand HR operations**  
      Gain practical exposure to recruitment, training, compensation, and employee relations.
    
    - 🤝 **Improve communication & teamwork**  
      Strengthen collaboration with HR staff, supervisors, and fellow interns.
    
    - 🚀 **Bridge HR and IT knowledge**  
      Explore how IT solutions can enhance HR efficiency, reporting, and employee engagement.
    """)
    
    st.divider()
    
    
    
    # ======================================================
    # 💻 Internship Contributions
    # ======================================================
    # -------------------------------
    # Custom CSS (placed at the top)
    # -------------------------------
    st.markdown(
        """
        <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
        }
        .medium-font {
            font-size:22px !important;
        }
        .small-font {
            font-size:16px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # -------------------------------
    # Headers using custom classes
    # -------------------------------
    st.markdown('<p class="big-font">💻 Internship Main Contributions</p>', unsafe_allow_html=True)
        
    # -------------------------------
    # Detailed Explanation
    # -------------------------------
    st.markdown("""
    During my internship at **Kaneka Malaysia**, I was assigned to develop and redesign 
    several learning and HR process materials. My contributions focused on two main areas:
    
    1. **Self-Paced Learning (SPL) Module Development**  
       - Designed and published interactive modules using iSpring Suite.  
       - Created both **internal modules** (for HR policies and assessments) and **external modules** (for general employee development).  
    
    2. **Flowchart Redesigns**  
       - Improved clarity and usability of HR-related process flowcharts.  
       - Enhanced visual communication for Learning & Development, Kaneka Crae, and Performance & Competency Assessment processes.  
    """)
    
    st.divider()
    
    # -------------------------------
    # Internal SPL Modules
    # -------------------------------
    st.markdown('<p class="medium-font">📚 Internal SPL Modules</p>', unsafe_allow_html=True)

    st.markdown("""
    These modules were designed to support HR policies and employee assessments:
    - **Baseline Assessment (BLA)**: Evaluate competency gaps and plan development activities.  
    - **Leave Provision**: Guide employees on leave entitlements and procedures.  
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/spl_bla.png", caption="Baseline Assessment (BLA)", width=250)
    with col2:
        st.image("images/spl_leave.png", caption="Leave Provision", width=250)
    
    st.success("These internal modules helped employees understand HR policies and competency frameworks more effectively.")
    
    st.divider()
    
    # -------------------------------
    # External SPL Modules
    # -------------------------------
    st.markdown('<p class="medium-font">🌍 External SPL Modules</p>', unsafe_allow_html=True)

    st.markdown("""
    These modules were developed to enhance employees' personal and professional skills:
    - **Stress Management**  
    - **Ethics At Work**  
    - **Time Management**  
    - **Presentation Skills**  
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/spl_stress.png", caption="Stress Management", width=200)
    with col2:
        st.image("images/spl_ethics.png", caption="Ethics At Work", width=200)
    with col3:
        st.image("images/spl_time.png", caption="Time Management", width=200)
    with col4:
        st.image("images/spl_presentation.png", caption="Presentation Skills", width=200)
    
    st.success("These external modules supported employee growth beyond HR policies, focusing on workplace well-being and skill development.")
    
    st.divider()
    
    # -------------------------------
    # Flowchart Redesigns
    # -------------------------------
    st.markdown('<p class="medium-font">📊 Flowchart Redesign Contributions</p>', unsafe_allow_html=True)

    st.markdown("""
    I redesigned several HR process flowcharts to improve clarity and communication:
    - **Learning & Development Process Flowchart**  
    - **Kaneka Crae Flowchart**  
    - **Performance & Competency Assessment Process Flowchart**  
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/onboarding_flowchart.png", caption="Learning & Development Flowchart", width=220)
    with col2:
        st.image("images/Kaneka_care_flowchart.png", caption="Kaneka Crae Flowchart", width=220)
    with col3:
        st.image("images/pc_flowchart.png", caption="Performance & Competency Assessment Flowchart", width=220)
    
    st.info("These redesigns improved communication, training efficiency, and employee understanding of HR workflows.")
    
    st.divider()
    
    
    # ======================================================
    # 🏢 HR Division
    # ======================================================
    
    # Custom CSS (define once at the top of your app)
    st.markdown(
        """
        <style>
        .big-font {
            font-size:32px !important;
            font-weight: bold;
        }
        .medium-font {
            font-size:24px !important;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Use styled markdown instead of st.header
    st.markdown('<p class="big-font">🏢 HR Division</p>', unsafe_allow_html=True)
    
    st.image(
        "images/hr_org_chart.png",
        caption="HR Organizational Structure",
        use_container_width=True
    )
    
    st.write("Select HR Department")
    
    department = st.radio(
        "",
        [
            "📚 Learning & Development",
            "💎 Reward Management",
            "🎯 Talent Acquisition & Industrial Relation"
        ],
        horizontal=True
    )
    
    st.divider()

    
    # ======================================================
    # 📚 Learning & Development
    # ======================================================
    
    if department == "📚 Learning & Development":
    
        learning_development()
    
    
    
    # ======================================================
    # 💎 Reward Management
    # ======================================================
    
    elif department == "💎 Reward Management":
    
        reward_management()
    
    
    
    # ======================================================
    # 🎯 TA & IR
    # ======================================================
    
    elif department == "🎯 Talent Acquisition & Industrial Relation":
    
        tair_management()
    
