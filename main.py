import streamlit as st

# --- Cover Page ---
st.title("Internship Presentation")
st.subheader("Kaneka Malaysia – HR & IT Internship")
st.write("Prepared by Husna, Year 4 Student at UMK")

# --- Welcome Message ---
st.markdown("""
Welcome to my interactive internship presentation built with **Streamlit**.  
Use the sidebar to navigate through different sections:
- Self Introduction
- Company Background
- HR Organizational Chart
- Internship Tasks
- Reflection
- Thank You
""")

# --- Visuals (Optional) ---
st.image("cover_image.png", caption="Kaneka Malaysia", use_column_width=True)

# --- Footer ---
st.markdown("---")
st.write("Navigate using the sidebar to explore each section.")
