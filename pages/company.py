import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def company_page():
    # ==============================
    # Company Page Logo
    # ==============================
    st.markdown(
        """
        <style>
        .big-title {
            font-size: 60px; /* Increase size */
            font-family: 'Poppins', sans-serif; /* Apply Poppins font */
            font-weight: bold;
            text-align: left;
            color: #023e8a; /* Optional: Kaneka blue tone */
            margin-bottom: 6px;
        }
        .subtitle-caption {
            font-size: 18px;
            font-family: 'Poppins', sans-serif;
            text-align: left;
            color: #444; /* softer corporate gray */
            margin-bottom: 20px; /* space before logo/next section */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title + caption
    st.markdown('<div class="big-title">About KANEKA</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-caption">Innovation • Sustainability • Human Well-being</div>', unsafe_allow_html=True)
     
    try:
        st.image("images/Kaneka_logo.png", width=350)
    except FileNotFoundError:
        st.warning("Kaneka logo not found.")
    
    st.divider()

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
    if "section" not in st.session_state:
        st.session_state.section = "Kaneka Group"

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🏢 Kaneka Group", use_container_width=True):
            st.session_state.section = "Kaneka Group"

    with col2:
        if st.button("🧭 Philosophy", use_container_width=True):
            st.session_state.section = "Corporate Philosophy"

    with col3:
        if st.button("📍 Location", use_container_width=True):
            st.session_state.section = "Location"

    with col4:
        if st.button("📜 History", use_container_width=True):
            st.session_state.section = "History"

    with col5:
        if st.button("📦 Products", use_container_width=True):
            st.session_state.section = "Products"

    st.divider()

    # ==============================
    # NAVIGATION CONTENT
    # ==============================
    section = st.session_state.section

    if section == "Kaneka Group":
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


    elif section == "Corporate Philosophy":
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

            .interpretation {
                font-size: 16px;
                line-height: 1.6;
                text-align: left;
                padding: 15px;
                margin-top: 15px;
                border-left: 4px solid #023e8a;
                background: #f9f9f9;
                color: #333;
                border-radius: 6px;
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

        
        # Centered Toggle Button
        # Initialize session state
        if "show_interpretation" not in st.session_state:
            st.session_state.show_interpretation = False
        
        # Center the button using CSS
        st.markdown(
            """
            <style>
            .centered-button {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 20px 0;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        # Place button inside centered div
        col1, col2, col3 = st.columns([1,2,1])  # middle column wider
        with col2:
            if st.button(
                "💡 Toggle My Interpretation",
                key="toggle_button"
            ):
                st.session_state.show_interpretation = not st.session_state.show_interpretation
        
        # Show/hide interpretation block
        if st.session_state.show_interpretation:
            st.markdown(
                """
                <div class="interpretation" style="
                    font-size:16px;
                    line-height:1.6;
                    text-align:left;
                    padding:15px;
                    margin-top:15px;
                    border-left:4px solid #023e8a;
                    background:#f9f9f9;
                    color:#333;
                    border-radius:6px;">
                <strong>My Interpretation:</strong><br>
                This philosophy highlights Kaneka’s commitment not only to innovation 
                but also to responsibility. To me, it means that technology should 
                always serve people and the planet, ensuring sustainability while 
                improving quality of life. It’s a reminder that progress must balance 
                creativity with care for the environment.
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


    elif section == "Location":
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
       


    elif section == "History":

        st.header("📜 Company History")

        history = pd.DataFrame({
            "Date": [
                "1995-08-01",
                "1996-07-01",
                "1999-01-01",
                "2010-09-01",
                "2012-02-01",
                "2015-05-01",
            ],
            "Companies": [
                "Kaneka (Malaysia)<br>Sdn. Bhd.",
                "Kaneka Eperan Sdn. Bhd.",
                "Kaneka Paste Polymers Sdn. Bhd.",
                "Kaneka Innovative Fibers Sdn. Bhd.",
                "Kaneka Apical Malaysia Sdn. Bhd.",
                "Kaneka MS Malaysia Sdn. Bhd."
            ]
        })
        
        history["Date"] = pd.to_datetime(history["Date"])
        history["Established"] = history["Date"].dt.strftime("%B %Y")
        history["Label"] = history["Date"].dt.strftime("%b\n%Y")
        
        # ----------------------------
        # Interactive Table
        # ----------------------------
        st.subheader("📊 Company List")
        
        st.dataframe(
            history[["Established", "Companies"]],
            use_container_width=True,
            hide_index=True
        )
        
        # ----------------------------
        # Timeline
        # ----------------------------
        st.subheader("📅 Company Timeline")
        
        fig = go.Figure()
        
        # Timeline line
        fig.add_trace(go.Scatter(
            x=history["Date"],
            y=[1] * len(history),
            mode="lines",
            line=dict(width=4, color="#023e8a"),
            hoverinfo="skip",
            showlegend=False
        ))
        
        # Milestones
        fig.add_trace(go.Scatter(
            x=history["Date"],
            y=[1] * len(history),
            mode="markers+text",
            text=history["Label"],
            textposition="bottom center",
            marker=dict(
                size=18,
                color="#023e8a",
                line=dict(color="white", width=2)
            ),
            customdata=history[["Companies", "Established"]],
            hovertemplate=
            "<b>%{customdata[0]}</b><br>"
            "Established: %{customdata[1]}"
            "<extra></extra>",
            showlegend=False
        ))
    
        fig.update_layout(
            title="Kaneka Malaysia Company History",
            height=350,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=30, r=30, t=60, b=40)
        )
    
        fig.update_xaxes(
            title="",
            tickformat="%Y",
            showgrid=False,
            showline=True,
            linecolor="lightgray",
            ticks="outside",
            range=[
                history["Date"].min() - pd.DateOffset(months=12),
                history["Date"].max() + pd.DateOffset(months=12)
            ]
        )
    
        fig.update_yaxes(
            visible=False,
            range=[0.95, 1.05]
        )
    
        st.plotly_chart(fig, use_container_width=True)

    
    elif section == "Products":

        st.header("📦 Kaneka Malaysia Products Showcase")

        st.markdown(
            """
            <style>
            .product-card {
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                margin-bottom: 20px;
                transition: all 0.3s ease-in-out;
                background-color: #fff;
            }
            .product-card:hover {
                transform: scale(1.02);
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }
            .product-expander .streamlit-expanderHeader {
                font-weight: bold;
                font-size: 16px;
                color: #023e8a;
            }
            .product-expander .streamlit-expanderContent {
                background: #f9f9f9;
                border-left: 4px solid #0096c7;
                padding: 10px;
                border-radius: 6px;
                animation: fadeIn 0.5s ease-in-out;
            }
            @keyframes fadeIn {
                from {opacity: 0;}
                to {opacity: 1;}
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        products = [
            {"name": "Modifiers", "image": "images/modifiers1.png",
             "desc": "Impact modifiers used in plastics for toughness and durability.",
             "link": "https://www.kaneka.com.my/product/modifier"},
            {"name": "Polyimide Film", "image": "images/polyimide_film1.png",
             "desc": "High-performance film for aerospace and electronics.",
             "link": "https://www.kaneka.com.my/product/polyimide-film"},
            {"name": "PVC Paste Resins", "image": "images/pvc_paste_resins.png",
             "desc": "Resins for flooring, wall coverings, and synthetic leather.",
             "link": "https://www.kaneka.com.my/product/pvc-paste-resin"},
            {"name": "Expandable Foam", "image": "images/expandable_foam.png",
             "desc": "Lightweight foam material for automotive and packaging.",
             "link": "https://www.kaneka.com.my/product/expandable-foam"},
            {"name": "Synthetic Fibers", "image": "images/synthetic_fibers.png",
             "desc": "Heat-resistant synthetic hair fiber for wigs and extensions.",
             "link": "https://www.kanekalon.com/en/"},
            {"name": "MS Polymer", "image": "images/ms_polymer1.png",
             "desc": "Base material for adhesives and sealants.",
             "link": "https://www.kaneka.com.my/product/ms-polymer/"}
        ]

        # Display products in a grid
        for row_start in range(0, len(products), 3):
            cols = st.columns(3)
            for i, col in enumerate(cols):
                if row_start + i < len(products):
                    product = products[row_start + i]
                    with col:
                        st.markdown('<div class="product-card">', unsafe_allow_html=True)
                        st.image(product["image"], caption=product["name"], use_column_width=True)
                        with st.expander(f"📖 **Learn more** about {product['name']}"):
                            st.write(product["desc"])
                            st.markdown(
                                f"<a href='{product['link']}' target='_blank' style='color:#0096c7; font-weight:bold;'>🔗 Read More</a>",
                                unsafe_allow_html=True
                            )
                        st.markdown('</div>', unsafe_allow_html=True)
        
