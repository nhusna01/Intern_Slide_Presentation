def hr_page():
    st.title("HR Organizational Flowchart")
    
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

                # --- Custom CSS for consistent, attractive buttons ---
                st.markdown("""
                    <style>
                    div.stButton > button {
                        background-color: #0096c7;
                        color: white;
                        border-radius: 10px;
                        padding: 12px;
                        font-weight: bold;
                        border: none;
                        transition: 0.3s;
                        width: 100%;          /* full width inside column */
                        height: 100px;         /* fixed height for consistency */
                        font-size: 16px;      /* consistent font size */
                        text-align: center;   /* center text */
                        line-height: 1.2;     /* spacing for multi-line labels */
                        overflow: hidden;
                    }
                    div.stButton > button:hover {
                        background-color: #023e8a;
                        color: #f1f1f1;
                        transform: scale(1.05);
                    }
                    div.stButton > button:active {
                        background-color: #0077b6;
                        transform: scale(0.98);
                    }
                    </style>
                """, unsafe_allow_html=True)
            
                # ---------- Row 1 ----------
                row1_c1, row1_c2, row1_c3, row1_c4, row1_c5, row1_c6, row1_c7, row1_c8 = st.columns(8)
            
                with row1_c1:
                    if st.button("①\n📧\nApplication", key="btn_step_1", use_container_width=True):
                        st.session_state.step = 1
            
                with row1_c2:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row1_c3:
                    if st.button("②\n🔍\nScreening", key="btn_step_2", use_container_width=True):
                        st.session_state.step = 2
            
                with row1_c4:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row1_c5:
                    if st.button("③\n📝\nPlacement", key="btn_step_3", use_container_width=True):
                        st.session_state.step = 3
            
                with row1_c6:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row1_c7:
                    if st.button("④\n👩‍💼\nApproval", key="btn_step_4", use_container_width=True):
                        st.session_state.step = 4

                with row1_c8:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                # ---------- Row 2 ----------
                st.write("")
            
                row2_c1, row2_c2, row2_c3, row2_c4, row2_c5, row2_c6, row2_c7 = st.columns(7)
            
                with row2_c1:
                    if st.button("⑤\n🎉\nConfirmation", key="btn_step_5", use_container_width=True):
                        st.session_state.step = 5
            
                with row2_c2:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row2_c3:
                    if st.button("⑥\n✅\nDocuments", key="btn_step_6", use_container_width=True):
                        st.session_state.step = 6
            
                with row2_c4:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row2_c5:
                    if st.button("⑦\n📄\nReport Duty", key="btn_step_7", use_container_width=True):
                        st.session_state.step = 7
            
                with row2_c6:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row2_c7:
                    if st.button("⑧\n🎓\nHandover", key="btn_step_8", use_container_width=True):
                        st.session_state.step = 8
            
                # ---------- Row 3 ----------
                st.write("")
            
                row3_c1, row3_c2, row3_c3, row3_c4, row3_c5 = st.columns(5)
            
                with row3_c1:
                    if st.button("⑨\n🤝\nInternship", key="btn_step_9", use_container_width=True):
                        st.session_state.step = 9
            
                with row3_c2:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row3_c3:
                    if st.button("⑩\n🎁\nAppreciation", key="btn_step_10", use_container_width=True):
                        st.session_state.step = 10
            
                with row3_c4:
                    st.markdown("<h1 style='text-align:center;'>➡️</h1>", unsafe_allow_html=True)
            
                with row3_c5:
                    if st.button("⑪\n📊\nEvaluation", key="btn_step_11", use_container_width=True):
                        st.session_state.step = 11
            
                if "step" not in st.session_state:
                    st.session_state.step = 1
            
                details = {
                    1: "Students submit internship applications through email or the company website.",
                    2: "HR segregates applications according to department requirements.",
                    3: "There are two options: either any HOD/Departments submit internship placement requests through e-Mendix, or HR proposes suitable candidates to the requesting department.",
                    4: "The Head of Department(HOD) reviews and approves the internship request.",
                    5: "Successful candidates receive confirmation via a call from HR.",
                    6: "HR prepares the Offer Letter(OL), Placement Letter(PL), and Reply Letter(RL) via email.",
                    7: "Interns attend briefing sessions with MIS, HR, and Safety departments.",
                    8: "The intern is handed over to the assigned department/plant.",
                    9: "Interns undergo internships at Kaneka.",
                    10: "The intern receives a certificate of completion and an appreciation souvenir from Kaneka.",
                    11: "The department evaluates the intern before completing the internship."         
                }
            
                st.divider()
            
                st.markdown(f"## 📍 Step {st.session_state.step}")
            
                st.info(details[st.session_state.step])
            
                st.progress(st.session_state.step / 11)
            
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

run(hr_page):

