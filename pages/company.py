import streamlit as st

def company_page():

    st.header("🏢 Company Background")

    # ==============================
    # DATA (Companies + Products)
    # ==============================
    companies = {
        "Kaneka Malaysia": {
            "establishment": "Established in Malaysia (Year not specified)",
            "group": "Kaneka Corporation Group",
            "products": [
                {
                    "name": "Kane Ace",
                    "image": "images/kane_ace.png",
                    "desc": "Impact modifier used to improve toughness of PVC and plastics.",
                    "uses": [
                        "PVC pipes",
                        "Window frames",
                        "Construction materials"
                    ]
                },
                {
                    "name": "Graphite Sheet",
                    "image": "images/graphite_sheet.png",
                    "desc": "Thermal management material with high heat conductivity.",
                    "uses": [
                        "Smartphones",
                        "Laptops",
                        "Automotive electronics"
                    ]
                }
            ]
        },

        "Kaneka Innovative Fibers Malaysia": {
            "establishment": "Established in Malaysia (Year not specified)",
            "group": "Kaneka Corporation Group",
            "products": [
                {
                    "name": "Kanekalon Fiber",
                    "image": "images/fiber.png",
                    "desc": "Synthetic fiber used for wigs and hair extensions.",
                    "uses": [
                        "Fashion wigs",
                        "Hair extensions",
                        "Cosmetics industry"
                    ]
                }
            ]
        },

        "Kaneka Eperan Malaysia": {
            "establishment": "Established in Malaysia (Year not specified)",
            "group": "Kaneka Corporation Group",
            "products": [
                {
                    "name": "Eperan Foam",
                    "image": "images/eperan.png",
                    "desc": "Lightweight foam material used for protection and packaging.",
                    "uses": [
                        "Automotive parts",
                        "Packaging",
                        "Shock absorption"
                    ]
                }
            ]
        }
    }

    # ==============================
    # SEARCH BAR
    # ==============================
    search_term = st.text_input("🔍 Search Company", placeholder="Enter company name...")

    # ==============================
    # SEE ALL BUTTON
    # ==============================
    see_all = st.button("See All Companies")

    st.write("---")

    # ==============================
    # FILTER LOGIC
    # ==============================
    if search_term:
        filtered_companies = {
            name: data
            for name, data in companies.items()
            if search_term.lower() in name.lower()
        }

    elif see_all:
        filtered_companies = companies

    else:
        filtered_companies = dict(list(companies.items())[:2])

    # ==============================
    # DISPLAY COMPANIES
    # ==============================
    for company_name, data in filtered_companies.items():

        with st.expander(f"🏭 {company_name}"):

            # ==============================
            # NEW: COMPANY INFO EXPANDER
            # ==============================
            with st.expander("📌 Company Info"):
                st.write(f"**Group:** {data.get('group', 'N/A')}")
                st.write(f"**Establishment:** {data.get('establishment', 'N/A')}")
                st.write("**Kaneka Company List:**")
                st.write("- Kaneka Malaysia")
                st.write("- Kaneka Innovative Fibers Malaysia")
                st.write("- Kaneka Eperan Malaysia")

            # ==============================
            # PRODUCTS EXPANDER
            # ==============================
            with st.expander("📦 Products"):
                for product in data["products"]:

                    st.markdown("### 📦 Product")

                    col1, col2 = st.columns([1, 2])

                    with col1:
                        st.image(product["image"], width=150)

                    with col2:
                        st.subheader(product["name"])

                        st.write("**Description**")
                        st.write(product["desc"])

                        st.write("**Kegunaan / Uses**")
                        for use in product["uses"]:
                            st.write(f"• {use}")

                    st.markdown("---")

    # ==============================
    # NO RESULT HANDLING
    # ==============================
    if search_term and len(filtered_companies) == 0:
        st.warning("No company found. Try another keyword.")
