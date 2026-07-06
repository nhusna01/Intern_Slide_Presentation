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
    
    st.subheader("🌍 ESG at Kaneka Malaysia")
    
    st.markdown("""
    Kaneka (Malaysia) Sdn. Bhd. integrates **Environmental, Social, and Governance (ESG)** principles into its business operations by aligning with the **United Nations Sustainable Development Goals (SDGs)**, **Malaysia's i-ESG Framework**, and the **Kaneka Corporation ESG Charter**.
    
    ### 🎯 SDGs Focused by Kaneka Malaysia
    
    Kaneka Malaysia prioritises **8 Sustainable Development Goals (SDGs)** where it can create the greatest impact:
    
    - 🩺 SDG 3 – Good Health and Well-being
    - 🎓 SDG 4 – Quality Education
    - ⚡ SDG 7 – Affordable and Clean Energy
    - 💼 SDG 8 – Decent Work and Economic Growth
    - 🏭 SDG 9 – Industry, Innovation and Infrastructure
    - ♻️ SDG 12 – Responsible Consumption and Production
    - 🌍 SDG 13 – Climate Action
    - 🌊 SDG 14 – Life Below Water
    
    ### Key ESG Initiatives
    
    **🌱 Environmental**
    - 70% greenhouse gas (GHG) reduction target by 2030
    - Net Zero Carbon target by 2050
    - Renewable energy, energy efficiency, recycling (3R), and river conservation programmes
    
    **🤝 Social**
    - Workplace health and safety programmes
    - ESG awareness and diversity initiatives
    - University collaborations, internships, and community outreach
    
    **⚖️ Governance**
    - Anti-Bribery and Anti-Corruption (ABAC) policies
    - Financial transparency and regulatory compliance
    - Risk management, internal audits, and ethical leadership
    """)
    
    st.divider()


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

    with st.expander("💡 Fun Fact"):
        st.write(
            "Companies with strong ESG practices often outperform peers "
            "in resilience and reputation."
        )

    # Quiz
    st.subheader("📝 Quick Quiz")

    answer = st.radio(
        "Which ESG pillar focuses on leadership and ethics?",
        ["Environmental", "Social", "Governance"],
    )

    if answer == "Governance":
        st.success("✅ Correct!")
    else:
        st.error("❌ Try again!")

    # ESG Priority
    st.subheader("📈 Your ESG Priority")

    priority = st.select_slider(
        "Which pillar matters most to you?",
        options=[
            "🌱 Environmental",
            "🤝 Social",
            "⚖️ Governance",
        ],
    )

    st.write("You selected:", priority)

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
