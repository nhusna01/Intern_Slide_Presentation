import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def additional_page():
    st.title("📖 Chapter 4")
    st.write("Additional page content goes here.")

def esg_page():
    st.title("🌍 What is ESG?")
    st.write("Explore the three pillars of ESG interactively:")

    # Interactive buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌱 Environmental"):
            st.session_state["choice"] = "E"
    with col2:
        if st.button("🤝 Social"):
            st.session_state["choice"] = "S"
    with col3:
        if st.button("⚖️ Governance"):
            st.session_state["choice"] = "G"

    # Show content dynamically
    if "choice" in st.session_state:
        choice = st.session_state["choice"]

        if choice == "E":
            st.success("🌱 Environmental")
            st.write("Focuses on how a company impacts the planet.")
            st.progress(70)

        elif choice == "S":
            st.info("🤝 Social")
            st.write("Examines how a company treats people — employees, customers, and communities.")
            st.progress(50)

        elif choice == "G":
            st.warning("⚖️ Governance")
            st.write("Refers to leadership, ethics, and accountability.")
            st.progress(80)

    # Expanders
    with st.expander("📊 Why ESG matters"):
        st.write("ESG helps investors, regulators, and the public assess long-term sustainability and ethical impact.")

    with st.expander("💡 Fun fact"):
        st.write("Companies with strong ESG practices often outperform peers in resilience and reputation.")

    # Quiz
    st.subheader("📝 Quick Quiz")
    answer = st.radio(
        "Which ESG pillar focuses on leadership and ethics?",
        ["Environmental", "Social", "Governance"]
    )
    if answer == "Governance":
        st.success("✅ Correct! Governance is about leadership, ethics, and accountability.")
    else:
        st.error("❌ Not quite. Try again!")

    # Slider for personal preference
    st.subheader("📈 Your ESG Priority")
    priority = st.slider("Which pillar matters most to you?", 1, 3, 2,
                         format_func=lambda x: ["🌱 Environmental", "🤝 Social", "⚖️ Governance"][x-1])
    st.write("You selected:", ["🌱 Environmental", "🤝 Social", "⚖️ Governance"][priority-1])

    # --- Interactive Dashboard ---
    st.subheader("📊 ESG Dashboard")

    # Example scores (could be dynamic later)
    data = pd.DataFrame({
        "Pillar": ["Environmental", "Social", "Governance"],
        "Score": [70, 50, 80]
    })

    # Bar chart
    st.bar_chart(data.set_index("Pillar"))

    # Pie chart
    st.write("Relative importance of ESG pillars:")
    st.pyplot(data.plot.pie(y="Score", labels=data["Pillar"], autopct="%1.1f%%").figure)

# Example usage
if __name__ == "__main__":
    esg_page()
