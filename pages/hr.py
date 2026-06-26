import streamlit as st

def hr_page():
    st.title("📖 Chapter 3 – HR Organizational Flowchart")
    st.caption("✨ Explore HR processes, training, and internship flow ✨")

    # =====================================================
    # 🎓 Internship Process Flow
    # =====================================================
    st.subheader("🎓 Internship Process Flow")

    # --- Custom CSS for consistent buttons ---
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
            width: 100%;
            height: 100px;
            font-size: 16px;
            text-align: center;
            line-height: 1.2;
        }
        div.stButton > button:hover {
            background-color: #023e8a;
            color: #f1f1f1;
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "step" not in st.session_state:
        st.session_state.step = 1

    # Layout rows of buttons
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
    with c1: 
        if st.button("①\n📧\nApplication", use_container_width=True): st.session_state.step = 1
    with c2: st.button("➡️", disabled=True, use_container_width=True)
    with c3: 
        if st.button("②\n🔍\nScreening", use_container_width=True): st.session_state.step = 2
    with c4: st.button("➡️", disabled=True, use_container_width=True)
    with c5: 
        if st.button("③\n📝\nPlacement", use_container_width=True): st.session_state.step = 3
    with c6: st.button("➡️", disabled=True, use_container_width=True)
    with c7: 
        if st.button("④\n👩‍💼\nApproval", use_container_width=True): st.session_state.step = 4
    with c8: st.button("➡️", disabled=True, use_container_width=True)

    st.write("")
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1: 
        if st.button("⑤\n🎉\nConfirmation", use_container_width=True): st.session_state.step = 5
    with c2: st.button("➡️", disabled=True, use_container_width=True)
    with c3: 
        if st.button("⑥\n✅\nDocuments", use_container_width=True): st.session_state.step = 6
    with c4: st.button("➡️", disabled=True, use_container_width=True)
    with c5: 
        if st.button("⑦\n📄\nReport Duty", use_container_width=True): st.session_state.step = 7
    with c6: st.button("➡️", disabled=True, use_container_width=True)
    with c7: 
        if st.button("⑧\n🎓\nHandover", use_container_width=True): st.session_state.step = 8

    st.write("")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: 
        if st.button("⑨\n🤝\nInternship", use_container_width=True): st.session_state.step = 9
    with c2: st.button("➡️", disabled=True, use_container_width=True)
    with c3: 
        if st.button("⑩\n🎁\nAppreciation", use_container_width=True): st.session_state.step = 10
    with c4: st.button("➡️", disabled=True, use_container_width=True)
    with c5: 
        if st.button("⑪\n📊\nEvaluation", use_container_width=True): st.session_state.step = 11

    # Step details
    details = {
        1:"Students submit internship applications through email or the company website.",
        2:"HR segregates applications according to department requirements.",
        3:"Either HOD/Departments submit internship placement requests through e‑Mendix, or HR proposes suitable candidates.",
        4:"The Head of Department (HOD) reviews and approves the internship request.",
        5:"Successful candidates receive confirmation via a call from HR.",
        6:"HR prepares the Offer Letter (OL), Placement Letter (PL), and Reply Letter (RL) via email.",
        7:"Interns attend briefing sessions with MIS, HR, and Safety departments.",
        8:"The intern is handed over to the assigned department/plant.",
        9:"Interns undergo internships at Kaneka, performing assigned tasks.",
        10:"The intern receives a certificate of completion and an appreciation souvenir from Kaneka.",
        11:"The department evaluates the intern before completing the internship."
    }

    st.divider()
    st.markdown(f"## 📍 Step {st.session_state.step}")
    st.info(details[st.session_state.step])
    st.progress(st.session_state.step/11)

    # Videos for key steps
    if st.session_state.step == 7:
        st.success("⭐⭐ Activities I was directly involved in ⭐⭐")
        st.subheader("Briefing Session")
        st.video("videos/briefing_session.mp4")
    elif st.session_state.step == 8:
        st.success("⭐⭐ Activities I was directly involved in ⭐⭐")
        st.subheader("Handover Process")
        st.video("videos/handover_process.mp4")
    elif st.session_state.step == 10:
        st.success("⭐⭐ Activities I was directly involved in ⭐⭐")
        st.subheader("Appreciation Event")
        st.video("videos/appreciation_event.mp4")
    else:
        st.info("📌 These processes were part of the internship workflow, but I was not directly involved 📌.")

    # =====================================================
    # 🏫 Training
    # =====================================================
    st.subheader("🏫 Training Process Flow")
    st.image("images/training_flow.png", caption="Training Process Flow", use_container_width=True)
    st.divider()
    st.subheader("Activities Performed")
    st.markdown("**Training Registration**")
    st.video("videos/training/registration.mp4")
    st.markdown("**Training Coordination**")
    st.video("videos/training/coordination.mp4")
    st.markdown("**Training Execution**")
    st.video("videos/training/execution.mp4")

    # =====================================================
    # 📝 Baseline Assessment (BLA)
    # =====================================================
    st.subheader("📝 Baseline Assessment (BLA) Process Flow")
    st.image("images/bla_flow.png", caption="BLA Process Flow", use_container_width=True)

    # =====================================================
    # 🎯 Talent Acquisition
    # =====================================================
    st.subheader("🎯 Talent Acquisition & Industrial Relation")
    st.write("Handles recruitment, onboarding, and maintaining healthy employee relations.")
    st.metric("New Hires", 25, "+5 this month")

    # =====================================================
    # 💎 Reward Management
    # =====================================================
    st.subheader("💎 Reward Management")
    st.write("Ensures fair compensation and manages employee benefits.")
    st.subheader("💰 Compensation & Benefits")
    st.write("Salary structure, allowances, incentives, and employee perks.")
    st.progress(0.7)
    st.subheader("🏢 General Affairs")
    st.write("Workplace facilities, employee welfare, and administrative support.")
    st.slider("Employee Satisfaction Index", 0, 100, 85)
