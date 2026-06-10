import streamlit as st

def company_page():

    # Sidebar branding
    st.sidebar.image("images/kaneka_logo.png", use_container_width=True)
    st.sidebar.markdown("### Kaneka Corporate Portal")
    st.sidebar.caption("Kaneka Future")

    st.header("🏢 Kaneka Corporate Portal")
    st.image("images/Kaneka_logo.png", width=200)
    st.write("---")

    # ==============================
    # DATA
    # ==============================
    data = {
        "establishment": "September 1, 1949 (Osaka, Japan)",
        "founder": "Kanehide Sakurada",
        "address": "Lot 123, Industrial Zone, Selangor, Malaysia",
        "map_embed": "https://www.google.com/maps",

        "philosophy": """
        Kaneka aims to contribute to society through innovation in chemistry.
        We focus on sustainability, human well-being, and advanced materials
        that support global industries and daily life.
        """,

        "history": [
            ["Kaneka Malaysia (KM)", "1990", "PVC & Industrial Materials"],
            ["Kaneka Paste Polymers (KPP)", "1995", "Resins & Polymers"],
            ["Kaneka Eperan (KEP)", "2000", "Foam Technology"],
            ["Kaneka Innovative Fibers (KIF)", "2005", "Synthetic Fibers"],
            ["Kaneka Apical Malaysia (KAM)", "2010", "Advanced Chemicals"],
            ["Kaneka MS Malaysia (KMS)", "2015", "Specialty Materials"],
        ],

        "products": [
            {
                "name": "Kane Ace",
                "image": "images/kane_ace.png",
                "desc": "Impact modifier used to improve toughness of PVC and plastics.",
                "uses": ["PVC pipes", "Window frames", "Construction materials"]
            },
            {
                "name": "Graphite Sheet",
                "image": "images/graphite_sheet.png",
                "desc": "High thermal conductivity material for heat management.",
                "uses": ["Smartphones", "Laptops", "Automotive electronics"]
            }
        ]
    }

    # ==============================
    # SIDEBAR NAVIGATION
    # ==============================
    menu = st.sidebar.radio(
        "📌 Navigation",
        ["Kaneka Group", "Corporate Philosophy", "Location", "History", "Products"]
    )

    st.write("---")

    # ==============================
    # 1. KANEKA GROUP
    # ==============================
    if menu == "Kaneka Group":
        st.subheader("🏢 Kaneka Corporation Group")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Established", data["establishment"])

        with col2:
            st.metric("Founder", data["founder"])

        st.info(
            "Kaneka Corporation is a Japanese chemical company focusing on "
            "materials science, healthcare, and advanced polymers."
        )

    # ==============================
    # 2. PHILOSOPHY
    # ==============================
    elif menu == "Corporate Philosophy":
        st.subheader("🧭 Corporate Philosophy")

        st.success(data["philosophy"])

    # ==============================
    # 3. LOCATION
    # ==============================
    elif menu == "Location":
        st.subheader("📍 Company Location")

        st.write(f"**Address:** {data['address']}")

        st.map()

        st.link_button("🌍 Open in Google Maps", data["map_embed"])

    # ==============================
    # 4. HISTORY
    # ==============================
    elif menu == "History":
        st.subheader("📜 Company History in Malaysia")

        st.table(data["history"])

    # ==============================
    # 5. PRODUCTS (CARD STYLE UI)
    # ==============================
    elif menu == "Products":
        st.subheader("📦 Kaneka Products")

        for product in data["products"]:

            with st.container():
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image(product["image"], width=150)

                with col2:
                    st.markdown(f"### {product['name']}")
                    st.write(product["desc"])

                    st.write("**Uses:**")
                    st.write(" | ".join(product["uses"]))

            st.divider()
