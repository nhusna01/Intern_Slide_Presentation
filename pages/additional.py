import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def additional_page():
    st.title("📖 Chapter 4")
    st.header("🌍 What is ESG?")

    st.write(
        "Environmental, Social, and Governance (ESG) is a framework used to evaluate "
        "a company's sustainability, ethical practices, and long-term performance."
    )
    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )
    
    st.subheader("🏢 ESG at Kaneka Malaysia")
    
    st.info(
        "Kaneka (Malaysia) Sdn. Bhd. aligns its ESG initiatives with the "
        "United Nations Sustainable Development Goals (SDGs), Malaysia's "
        "i-ESG Framework, and the Kaneka Corporation ESG Charter."
    )

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )
    
    # ===========================
    # SDGs
    # ===========================
    st.subheader("🎯 SDGs Focused by Kaneka Malaysia")

    st.markdown("""
    <div style="display:grid;
                grid-template-columns:repeat(2,1fr);
                gap:12px;">

        <div style="background:#4C9F38;color:white;padding:12px;border-radius:10px;">
            <b>🩺 SDG 3</b><br>
            Good Health & Well-being
        </div>

        <div style="background:#C5192D;color:white;padding:12px;border-radius:10px;">
            <b>🎓 SDG 4</b><br>
            Quality Education
        </div>

        <div style="background:#FCC30B;color:black;padding:12px;border-radius:10px;">
            <b>⚡ SDG 7</b><br>
            Affordable & Clean Energy
        </div>

        <div style="background:#A21942;color:white;padding:12px;border-radius:10px;">
            <b>💼 SDG 8</b><br>
            Decent Work & Economic Growth
        </div>

        <div style="background:#FD6925;color:white;padding:12px;border-radius:10px;">
            <b>🏭 SDG 9</b><br>
            Industry, Innovation & Infrastructure
        </div>

        <div style="background:#BF8B2E;color:white;padding:12px;border-radius:10px;">
            <b>♻️ SDG 12</b><br>
            Responsible Consumption & Production
        </div>

        <div style="background:#3F7E44;color:white;padding:12px;border-radius:10px;">
            <b>🌍 SDG 13</b><br>
            Climate Action
        </div>

        <div style="background:#0A97D9;color:white;padding:12px;border-radius:10px;">
            <b>🌊 SDG 14</b><br>
            Life Below Water
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
        unsafe_allow_html=True
    )

    # ===========================
    # ESG Initiatives
    # ===========================
    st.subheader("📌 Key ESG Initiatives")

    tab1, tab2, tab3 = st.tabs(
        ["🌱 Environmental", "🤝 Social", "⚖️ Governance"]
    )

    with tab1:
        st.success("Environmental")
        st.write("Kaneka Malaysia's environmental initiatives include:")
        st.checkbox("70% greenhouse gas (GHG) reduction target by 2030", value=True, disabled=True)
        st.checkbox("Net Zero Carbon target by 2050", value=True, disabled=True)
        st.checkbox("Renewable energy and energy efficiency", value=True, disabled=True)
        st.checkbox("Recycling (3R) programmes", value=True, disabled=True)
        st.checkbox("River conservation and pollution control", value=True, disabled=True)

    with tab2:
        st.info("Social")
        st.write("Kaneka Malaysia's social initiatives include:")
        st.checkbox("Workplace health and safety programmes", value=True, disabled=True)
        st.checkbox("ESG awareness campaigns", value=True, disabled=True)
        st.checkbox("Diversity and inclusion initiatives", value=True, disabled=True)
        st.checkbox("University collaborations and internships", value=True, disabled=True)
        st.checkbox("Community outreach programmes", value=True, disabled=True)

    with tab3:
        st.warning("Governance")
        st.write("Kaneka Malaysia's governance initiatives include:")
        st.checkbox("Anti-Bribery & Anti-Corruption (ABAC)", value=True, disabled=True)
        st.checkbox("Financial transparency", value=True, disabled=True)
        st.checkbox("Regulatory compliance", value=True, disabled=True)
        st.checkbox("Risk management", value=True, disabled=True)
        st.checkbox("Internal audits and ethical leadership", value=True, disabled=True)


    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )
    
    # ---------------- ESG Tabs ----------------
    # Inject custom CSS
    st.markdown("""
        <style>
        /* Environmental - Green */
        div[data-testid="stCheckbox"] label[data-testid="stMarkdownContainer"] {
            color: #2e7d32; /* Dark Green */
            font-weight: 600;
        }
        /* Social - Blue */
        div[data-testid="stCheckbox"]:nth-child(n+7):nth-child(-n+12) label[data-testid="stMarkdownContainer"] {
            color: #1565c0; /* Blue */
            font-weight: 600;
        }
        /* Governance - Orange */
        div[data-testid="stCheckbox"]:nth-child(n+13) label[data-testid="stMarkdownContainer"] {
            color: #ef6c00; /* Orange */
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(
        ["🌱 Environmental", "🤝 Social", "⚖️ Governance"]
    )
    
    with tab1:
        st.success("Environmental Initiatives")
        st.write("Kaneka Malaysia focuses on:")
        st.checkbox("70% GHG reduction target by 2030", value=True, disabled=True)
        st.checkbox("Net Zero Carbon by 2050", value=True, disabled=True)
        st.checkbox("Renewable Energy", value=True, disabled=True)
        st.checkbox("Energy Efficiency", value=True, disabled=True)
        st.checkbox("Recycling (3R)", value=True, disabled=True)
        st.checkbox("River Conservation Programmes", value=True, disabled=True)
    
    with tab2:
        st.info("Social Initiatives")
        st.write("Kaneka Malaysia promotes:")
        st.checkbox("Health & Safety Programmes", value=True, disabled=True)
        st.checkbox("ESG Awareness Campaigns", value=True, disabled=True)
        st.checkbox("Diversity & Inclusion", value=True, disabled=True)
        st.checkbox("University Collaborations", value=True, disabled=True)
        st.checkbox("Internships", value=True, disabled=True)
        st.checkbox("Community Outreach", value=True, disabled=True)
    
    with tab3:
        st.warning("Governance Initiatives")
        st.write("Kaneka Malaysia strengthens governance through:")
        st.checkbox("Anti-Bribery & Anti-Corruption (ABAC)", value=True, disabled=True)
        st.checkbox("Financial Transparency", value=True, disabled=True)
        st.checkbox("Regulatory Compliance", value=True, disabled=True)
        st.checkbox("Risk Management", value=True, disabled=True)
        st.checkbox("Internal Audits", value=True, disabled=True)
        st.checkbox("Ethical Leadership", value=True, disabled=True)
    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )
    
    # ---------------- Learn More ----------------
    with st.expander("📖 Why are these SDGs important?"):
        st.write("""
    These eight SDGs were selected because Kaneka Malaysia believes they are the
    areas where the company can make the greatest contribution to sustainable
    development through environmental protection, employee wellbeing,
    innovation, and ethical governance.
    """)
    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

    st.write("Explore the three pillars of ESG interactively:")

    # Initialize session state
    if "choice" not in st.session_state:
        st.session_state.choice = None

    # Interactive buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌱 Environmental"):
            st.session_state.choice = "E"

    with col2:
        if st.button("🤝 Social"):
            st.session_state.choice = "S"

    with col3:
        if st.button("⚖️ Governance"):
            st.session_state.choice = "G"

    # Display selected pillar
    if st.session_state.choice == "E":
        st.success("🌱 Environmental")
        st.write("Focuses on how a company impacts the planet.")
        st.progress(70)

    elif st.session_state.choice == "S":
        st.info("🤝 Social")
        st.write("Examines how a company treats employees, customers, and communities.")
        st.progress(50)

    elif st.session_state.choice == "G":
        st.warning("⚖️ Governance")
        st.write("Refers to leadership, ethics, and accountability.")
        st.progress(80)

    # Expanders
    with st.expander("📊 Why ESG Matters"):
        st.write(
            "ESG helps investors, regulators, and the public assess "
            "long-term sustainability and ethical impact."
        )

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    ) 
    
    # Quiz
    st.subheader("📝 Quick Quiz")

    answer = st.radio(
        "Which ESG pillar focuses on leadership and ethics?",
        ["Environmental", "Social", "Governance"],
    )

    if answer == "Governance":
        st.success("✅ Correct! Good Job.")
    else:
        st.error("❌ Try again! Don't give up.")

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )
    
    # Dashboard
    st.subheader("📊 ESG Dashboard")

    data = pd.DataFrame({
        "Pillar": ["Environmental", "Social", "Governance"],
        "Score": [70, 50, 80]
    })

    st.bar_chart(data.set_index("Pillar"))

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(
        data["Score"],
        labels=data["Pillar"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")

    st.pyplot(fig)


if __name__ == "__main__":
    additional_page()
