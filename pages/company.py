import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import requests

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="About KANEKA",
    page_icon="",
    layout="wide"
)

# ==============================
# CUSTOM TITLE STYLING
# ==============================
st.markdown(
    """
    <style>
    .big-title {
        font-size: 48px; /* Increase size */
        font-family: 'Poppins', sans-serif; /* Apply Poppins font */
        font-weight: bold;
        text-align: center;
        color: #023e8a; /* Optional: Kaneka blue tone */
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use custom-styled title
st.markdown('<div class="big-title">🏢 About KANEKA</div>', unsafe_allow_html=True)


def company_page():

    # ==============================
    # COMPANY DATA
    # ==============================
    companies = {
        "Kaneka Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123-124, Gebeng Industrial Area, Kuantan,Pahang, Malaysia",
        },
        "Kaneka Innovative Fibers": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123-124, Gebeng Industrial Area, Kuantan,Pahang, Malaysia",
        },
        "Kaneka Eperan": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123-124, Gebeng Industrial Area, Kuantan,Pahang, Malaysia",
        },
        "Kaneka MS Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123-124, Gebeng Industrial Area, Kuantan,Pahang, Malaysia",
        },
        "Kaneka Apical Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123-124, Gebeng Industrial Area, Kuantan,Pahang, Malaysia",
        },
        "Kaneka Paste Polymers Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123-124, Gebeng Industrial Area, Kuantan,Pahang, Malaysia",
        },
    }

    # ==============================
    # HEADER
    # ==============================
    st.title("🏢 About KANEKA")
    st.caption("Innovation • Sustainability • Human Well-being")

    try:
        st.image("images/Kaneka_logo.png", width=350)
    except:
        st.warning("Kaneka logo not found.")

    st.divider()

    # ==============================
    # SEARCH SECTION
    # ==============================
    st.subheader("🔍 Search Company")

    search_term = st.text_input("Enter company name...")

    col1, col2 = st.columns([1, 4])

    with col1:
        see_all = st.button("See All Companies")

    if search_term:
        filtered = {
            name: data
            for name, data in companies.items()
            if search_term.lower() in name.lower()
        }

    elif see_all:
        filtered = companies

    else:
        filtered = {}

    # ==============================
    # DISPLAY COMPANY RESULTS
    # ==============================
    if filtered:

        st.subheader("🏭 Company List")

        for name, data in filtered.items():

            with st.container():

                st.markdown(f"### 🏢 {name}")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Established", data["establishment"])

                with col2:
                    st.metric("Founder", data["founder"])

                with col3:
                    st.metric("Country", "Malaysia")

                with st.expander("📍 View Company Details"):
                    st.write(f"**Address:** {data['address']}")

                st.divider()

    else:
        st.info(
            "🔎 Search a company or click 'See All Companies' to display results."
        )

    st.divider()

    # ==============================
    # NAVIGATION
    # ==============================
    if "page" not in st.session_state:
        st.session_state.page = "Kaneka Group"

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🏢 Kaneka Group", use_container_width=True):
            st.session_state.page = "Kaneka Group"

    with col2:
        if st.button("🧭 Philosophy", use_container_width=True):
            st.session_state.page = "Corporate Philosophy"

    with col3:
        if st.button("📍 Location", use_container_width=True):
            st.session_state.page = "Location"

    with col4:
        if st.button("📜 History", use_container_width=True):
            st.session_state.page = "History"

    with col5:
        if st.button("📦 Products", use_container_width=True):
            st.session_state.page = "Products"

    st.divider()

    # ==============================
    # NAVIGATION CONTENT
    # ==============================
    page = st.session_state.page

    if page == "Kaneka Group":
        st.header("🏢 Kaneka Group")
    
        # Hero block
        st.markdown(
            """
            <div style="background: linear-gradient(90deg, #023e8a, #0096c7);
                        padding: 20px; border-radius: 10px; color: white; text-align: center;">
                <h2>Kaneka Corporation</h2>
                <p>Founded in 1949 • Headquarters in Osaka & Tokyo</p>
                <p>Innovative technologies • Healthcare • Food • Sustainability</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add spacing
        st.markdown("<br>", unsafe_allow_html=True)
    
        # Interactive summary points
        with st.expander("📜 History"):
            st.write("- Established in 1st September 1949")
            st.write("- Originated with vinyl chloride production (Kanevinyl)")
    
        with st.expander("👤 Founder"):
            st.write("- Founded by Kanegafuchi Spinning Company spin‑off")
            st.write("- Initial capital: 200 million yen")
    
        with st.expander("📍 Headquarters"):
            st.write("- **Osaka Head Office:** Nakanoshima Festival Tower, Kita‑ku, Osaka")
            st.write("- **Tokyo Head Office:** Akasaka, Minato‑ku, Tokyo")
    
        with st.expander("🌍 Global Presence"):
            st.write("- Subsidiaries in USA, Europe, Malaysia, Singapore, Australia, Vietnam, Indonesia, Thailand, Korea, China")
    
        # Interactive metrics
        st.markdown("---")
        st.metric("Employees Worldwide", 10000, "+500 this year")
        st.metric("Global Subsidiaries", 10, "+2 in recent years")
        st.progress(0.8)  # Example sustainability progress bar
        st.slider("Employee Engagement Index", 0, 100, 85)


    elif page == "Corporate Philosophy":
        st.header("🧭 Corporate Philosophy")
    
        st.markdown(
            """
            <style>
            .philosophy {
                font-size: 18px;
                line-height: 1.6;
                text-align: center;
                padding: 20px;
                border-radius: 10px;
                background: linear-gradient(90deg, #0077b6, #00b4d8);
                color: white;
                animation: fadeIn 3s ease-in-out, glow 2s infinite alternate;
            }
    
            @keyframes fadeIn {
                from {opacity: 0;}
                to {opacity: 1;}
            }
    
            @keyframes glow {
                from {text-shadow: 0 0 5px #fff, 0 0 10px #00b4d8;}
                to {text-shadow: 0 0 20px #fff, 0 0 30px #0077b6;}
            }
            </style>
    
            <div class="philosophy">
                <strong>Innovation • Environmental • Sustainability</strong><br><br>
                With people and technology growing together into creative fusion,
                we will break fresh ground for the future and tie in to explore
                New Values. We are also committed to challenge the environmental
                issues of our planet and contribute to upgrade the quality of life.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # 🎬 Add Lottie animation here    
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
    
        lottie_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
        st_lottie(lottie_animation, height=250, key="innovation")


    elif page == "Location":
        st.header("📍 Kaneka Malaysia Locations")
    
        # Coordinates for Kaneka Malaysia sites
        location_data = pd.DataFrame({
            "lat": [
                3.98175,   # HQ Gebeng, Kuantan
                3.1390,    # Kuala Lumpur Office
                3.98200,   # Apical Malaysia (Gebeng)
                3.98220,   # Paste Polymer Malaysia (Gebeng)
                3.98240,   # Eperan Malaysia (Gebeng)
                3.98260,   # Innovative Fibers – FPW Plant (Gebeng)
                3.98280    # Innovative Fibers – iModa Plant (Gebeng)
            ],
            "lon": [
                103.3737,  # HQ Gebeng
                101.6869,  # KL Office
                103.3742,  # Apical
                103.3744,  # Paste Polymer
                103.3746,  # Eperan
                103.3748,  # FPW Plant
                103.3750   # iModa Plant
            ],
            "name": [
                "Kaneka Malaysia HQ (Gebeng, Kuantan)",
                "Kaneka Malaysia Office (Kuala Lumpur)",
                "Kaneka Apical Malaysia",
                "Kaneka Paste Polymer Malaysia",
                "Kaneka Eperan Malaysia",
                "Kaneka Innovative Fibers – FPW Plant",
                "Kaneka Innovative Fibers – iModa Plant"
            ]
        })
    
        # Display map with all company locations
        st.map(location_data, zoom=12, use_container_width=True)
       


    elif page == "History":

        st.header("📜 Company History")

        history = pd.DataFrame({
            "Date": [
                "August, 1995",
                "July, 1996",
                "January, 1999",
                "September, 2010",
                "February, 2012",
                "May, 2015",
            ],
            "Companies": [
                "Kaneka (Malaysia) Sdn. Bhd.",
                "Kaneka Eperan Sdn. Bhd.",
                "Kaneka Paste Polymers Sdn. Bhd.",
                "Kaneka Innovative Fibers Sdn. Bhd.",        
                "Kaneka Apical Malaysia Sdn. Bhd.",
                "Kaneka MS Malaysia Sdn. Bhd.",
            ]
        })
        st.table(history)


    elif page == "Products":

        st.header("📦 Products")

        products = [
            "Medical Devices",
            "Functional Polymers",
            "Food Products",
            "Expandable Polyolefin Foam",
            "Biodegradable Materials",
            "Innovative Fibers",
        ]

        for product in products:
            st.write(f"• {product}")

        st.info("More product details will be added soon.")


# Run page
company_page()
