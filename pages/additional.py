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
            font-size: 20px;
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
    
    # Inject CSS for SDG cards + tooltips
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
        font-size: 30px;
        font-weight: bold;
    }
    
    .sdg-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.3);
    }
    
    /* Tooltip styling */
    .tooltip {
        position: absolute;
        top: 10px;
        right: 12px;
        cursor: pointer;
        font-size: 16px;
    }
    
    .tooltiptext {
        visibility: hidden;
        width: 160px;
        background-color: white;
        color: black;
        text-align: center;
        border-radius: 8px;
        padding: 8px;
        position: absolute;
        top: -5px;
        right: 25px;
        z-index: 1;
        font-size: 24px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
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
                    font-size:18px;
                    font-weight:bold;">
            {sdg}
            <div class="tooltip">❓
                <span class="tooltiptext">{description}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    # Layout
    col1, col2, col3, col4 = st.columns(4)
    with col1: sdg_card("SDG 3", "Good Health & Well-being ", "#4C9F38")
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
        ["🌱 Environmental", "👥 Social", "⚖️ Governance"]
    )
    
    with tab1:
        st.success("Environmental Initiatives - Focuses on how a company impacts the planet.")
        st.write("Kaneka Malaysia focuses on:")
        st.checkbox("70% GHG reduction target by 2030", value=True, disabled=True)
        st.checkbox("Net Zero Carbon by 2050", value=True, disabled=True)
        st.checkbox("Renewable Energy", value=True, disabled=True)
        st.checkbox("Energy Efficiency", value=True, disabled=True)
        st.checkbox("Recycling (3R)", value=True, disabled=True)
        st.checkbox("River Conservation Programmes", value=True, disabled=True)
    
    with tab2:
        st.info("Social Initiatives - Examines how a company treats employees, customers, and communities.")
        st.write("Kaneka Malaysia promotes:")
        st.checkbox("Health & Safety Programmes", value=True, disabled=True)
        st.checkbox("ESG Awareness Campaigns", value=True, disabled=True)
        st.checkbox("Diversity & Inclusion", value=True, disabled=True)
        st.checkbox("University Collaborations", value=True, disabled=True)
        st.checkbox("Internships", value=True, disabled=True)
        st.checkbox("Community Outreach", value=True, disabled=True)
    
    with tab3:
        st.warning("Governance Initiatives - Refers to leadership, ethics, and accountability.")
        st.write("Kaneka Malaysia strengthens governance through:")
        st.checkbox("Anti-Bribery & Anti-Corruption (ABAC)", value=True, disabled=True)
        st.checkbox("Financial Transparency", value=True, disabled=True)
        st.checkbox("Regulatory Compliance", value=True, disabled=True)
        st.checkbox("Risk Management", value=True, disabled=True)
        st.checkbox("Internal Audits", value=True, disabled=True)
        st.checkbox("Ethical Leadership", value=True, disabled=True)
    

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
