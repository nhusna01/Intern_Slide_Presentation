import streamlit as st
import pandas as pd

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Kaneka Malaysia",
    page_icon="🏢",
    layout="wide"
)


def company_page():

    # ==============================
    # COMPANY DATA
    # ==============================
    companies = {
        "Kaneka Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123, Industrial Zone, Selangor, Malaysia",
        },
        "Kaneka Innovative Fibers": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Penang Industrial Park, Malaysia",
        },
        "Kaneka Eperan": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Johor Industrial Zone, Malaysia",
        },
        "Kaneka MS Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Johor Industrial Zone, Malaysia",
        },
        "Kaneka Apical Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Johor Industrial Zone, Malaysia",
        },
        "Kaneka Paste Polymers Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Johor Industrial Zone, Malaysia",
        },
    }

    # ==============================
    # HEADER
    # ==============================
    st.title("🏢 Kaneka Malaysia")
    st.caption("Innovation • Sustainability • Human Well-being")

    st.header("🏢 Kaneka Corporate Portal")

    try:
        st.image("images/Kaneka_logo.png", width=200)
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

        st.info(
            """
            Kaneka Corporation is a Japanese chemical company founded in 1949.
            The company contributes to society through innovative technologies,
            healthcare, food products, and sustainable solutions.
            """
        )

    elif page == "Corporate Philosophy":

        st.header("🧭 Corporate Philosophy")

        st.success(
            """
            Innovation • Sustainability • Human Well-being

            Through our technologies and products,
            we aim to improve people's lives and create value for society.
            """
        )

    elif page == "Location":

        st.header("📍 Global Locations")

        st.write("Kaneka Malaysia Headquarters")

        location_data = pd.DataFrame({
            "lat": [3.1390],      # Kuala Lumpur
            "lon": [101.6869]
        })

        st.map(location_data)

    elif page == "History":

        st.header("📜 Company History")

        history = pd.DataFrame({
            "Year": [
                1990,
                2000,
                2005,
                2010,
                2015,
                2020,
            ],
            "Milestone": [
                "Kaneka Malaysia Established",
                "Kaneka Eperan Expansion",
                "Kaneka Innovative Fibers Development",
                "Kaneka MS Malaysia Growth",
                "Kaneka Paste Polymers Expansion",
                "Kaneka Apical Malaysia Development",
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
