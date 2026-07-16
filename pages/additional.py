import streamlit as st
import pandas as pd

def additional_page():
    # Stylized title
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
            font-size: 26px;
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

    st.markdown(
        "<div class='chapter-title'>📖 Chapter 4 – ESG</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='chapter-caption'>🌍 Building a sustainable future through Environmental, Social, and Governance (ESG) 🌍</div>",
        unsafe_allow_html=True
    )

    st.divider()

    # ===========================
    # ESG Intro Section
    # ===========================
    
    # Inject CSS for font size
    st.markdown("""
    <style>
    /* Header */
    h1 {
        font-size: 36px !important;
        font-weight: 700 !important;
    }
    
    /* Subheader */
    h2 {
        font-size: 28px !important;
        font-weight: 600 !important;
    }
    
    /* General text (st.write, st.info, st.success, etc.) */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 20px !important;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.header("🌍 What is ESG?")
    
    st.write(
        "Environmental, Social, and Governance (ESG) is a framework used to evaluate "
        "a company's sustainability, ethical practices, and long-term performance."
    )
    
    st.divider()
    
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
    
    # Inject CSS for SDG cards
    st.markdown("""
    <style>
    .sdg-card {
        background: linear-gradient(135deg, #003366, #3366CC);
        color: white;
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #FFD700;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        height: 150px;
        position: relative;
        font-size: 22px;
        font-weight: bold;
    }
    
    .sdg-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Function for SDG card
    def sdg_card(sdg, description, color):
        st.markdown(f"""
        <div style="background:{color};
                    color:white;
                    padding:25px 20px;
                    margin-bottom: 20px;
                    border-radius:20px;
                    text-align:center;
                    border:2px solid #FFD700;
                    box-shadow:0 8px 20px rgba(0,0,0,0.2);
                    transition:all 0.3s ease;
                    height:150px;
                    position:relative;
                    font-size:22px;
                    font-weight:bold;">
            {sdg}<br>
            <span style="font-size:18px; font-weight:normal;">{description}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Layout
    col1, col2, col3, col4 = st.columns(4)
    with col1: sdg_card("SDG 3", "Good Health & Well-being", "#4C9F38")
    with col2: sdg_card("SDG 4", "Quality Education", "#C5192D")
    with col3: sdg_card("SDG 7", "Affordable & Clean Energy", "#FCC30B")
    with col4: sdg_card("SDG 8", "Decent Work & Economic Growth", "#A21942")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: sdg_card("SDG 9", "Industry, Innovation, & Infrastructure", "#FD6925")
    with col6: sdg_card("SDG 12", "Responsible Consumption & Production", "#BF8B2E")
    with col7: sdg_card("SDG 13", "Climate Action", "#3F7E44")
    with col8: sdg_card("SDG 14", "Life Below Water", "#0A97D9")
    

    st.markdown(
    "<hr style='border:0; height:3px; background: linear-gradient(to right, #89CFF0, #7EC8E3);'>",
    unsafe_allow_html=True
    )

    # ===========================
    # ESG Initiatives Tabs
    # ===========================
    
    # Inject custom CSS
    st.markdown("""
        <style>
        /* General font size for all text */
        div[data-testid="stMarkdownContainer"] {
            font-size: 18px !important;
        }
        /* Environmental - Green */
        div[data-testid="stCheckbox"] label[data-testid="stMarkdownContainer"] {
            color: #2e7d32; /* Dark Green */
            font-weight: 600;
            font-size: 18px !important;
        }
        /* Social - Blue */
        div[data-testid="stCheckbox"]:nth-child(n+7):nth-child(-n+12) label[data-testid="stMarkdownContainer"] {
            color: #1565c0; /* Blue */
            font-weight: 600;
            font-size: 18px !important;
        }
        /* Governance - Orange */
        div[data-testid="stCheckbox"]:nth-child(n+13) label[data-testid="stMarkdownContainer"] {
            color: #ef6c00; /* Orange */
            font-weight: 600;
            font-size: 18px !important;
        }
        /* Tab headers */
        button[data-testid="stTab"] div[data-testid="stMarkdownContainer"] {
            font-size: 20px !important;
            font-weight: 700;
        }
        /* Radio buttons (Quiz) */
        div[data-testid="stRadio"] label[data-testid="stMarkdownContainer"] {
            font-size: 18px !important;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(
        ["🌱 Environmental", "👥 Social", "⚖️ Governance"]
    )
    
    with tab1:
        st.success("Environmental Initiatives - To looks at how a company protects the planet through energy use, waste management, and reducing pollution.")
        st.write("Kaneka Malaysia focuses on:")
        st.checkbox("Energy efficiency improvements", value=True, disabled=True)
        st.checkbox("Waste reduction initiatives", value=True, disabled=True)
        st.checkbox("Carbon footprint awareness", value=True, disabled=True)
    
    with tab2:
        st.info("Social Initiatives - Focuses on how a company cares for its people, customers, and the community.")
        st.write("Kaneka Malaysia promotes:")
        st.checkbox("Employee well-being programs", value=True, disabled=True)
        st.checkbox("Safety-first culture", value=True, disabled=True)
        st.checkbox("Community engagement activities", value=True, disabled=True)
    
    with tab3:
        st.warning("Governance Initiatives - About how a company is run which by making fair decisions, following rules, and leading with integrity.")
        st.write("Kaneka Malaysia strengthens governance through:")
        st.checkbox("Ethical business practices", value=True, disabled=True)
        st.checkbox("Transparency & compliance", value=True, disabled=True)
        st.checkbox("Responsible decision-making", value=True, disabled=True)
    
    # Expanders
    with st.expander("📊 Why ESG Matters"):
        st.write(
            "ESG matters because it helps organizations build trust, reduce risks, and achieve long-term sustainable growth through responsible environmental, social, and governance practices."
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


if __name__ == "__main__":
    additional_page()
