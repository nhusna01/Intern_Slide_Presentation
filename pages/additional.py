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
    
    # ---------------- SDGs ----------------
    st.subheader("🎯 SDGs Focused by Kaneka Malaysia")
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Health", "SDG 3")
    col2.metric("Education", "SDG 4")
    col3.metric("Clean Energy", "SDG 7")
    col4.metric("Economic Growth", "SDG 8")
    
    col5, col6, col7, col8 = st.columns(4)
    
    col5.metric("Innovation", "SDG 9")
    col6.metric("Responsible Consumption", "SDG 12")
    col7.metric("Climate Action", "SDG 13")
    col8.metric("Life Below Water", "SDG 14")
    
    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )
    
    # ---------------- ESG Tabs ----------------
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
