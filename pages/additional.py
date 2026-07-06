import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def additional_page():
    st.title("📖 Chapter 4")
    st.header("🌍 What is ESG?")

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
