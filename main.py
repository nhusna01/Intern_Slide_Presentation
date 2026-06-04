import streamlit as st

# --- Page Config (full screen effect) ---
st.set_page_config(
    page_title="Internship Presentation",
    layout="wide",
)

# --- Custom CSS for background & styling ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1507842217343-583bb7270b66");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Cover Page Content ---
st.markdown("<h1 style='text-align: center; color: white;'>Internship Presentation</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Kaneka Malaysia – HR & IT Internship</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Prepared by Husna, UMK</h3>", unsafe_allow_html=True)

st.markdown("---")

# --- Interactive Buttons ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👩 Self Introduction"):
        st.success("Navigate to Self Introduction in the sidebar!")
with col2:
    if st.button("🏢 Company Background"):
        st.success("Navigate to Company Background in the sidebar!")
with col3:
    if st.button("📊 HR Chart"):
        st.success("Navigate to HR Organizational Chart in the sidebar!")

# --- Fun Interactive Element ---
st.markdown("### 🎉 Click below to celebrate the start!")
if st.button("Start Presentation"):
    st.balloons()

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: white;'>Use the sidebar to explore each section</p>", unsafe_allow_html=True)
