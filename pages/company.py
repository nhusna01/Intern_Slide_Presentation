import streamlit as st

def company_page():

    # ==============================
    # SIDEBAR BRANDING
    # ==============================
    st.sidebar.image("images/Kaneka_logo.png", use_container_width=True)
    st.sidebar.markdown("### Kaneka Corporate Portal")
    st.sidebar.caption("Kaneka Future")

    # ==============================
    # DATA
    # ==============================
    companies = {
        "Kaneka Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Lot 123, Industrial Zone, Selangor, Malaysia",
        },

        "Kaneka Innovative Fibers Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Penang Industrial Park, Malaysia",
        },

        "Kaneka Eperan Malaysia": {
            "establishment": "September 1, 1949 (Osaka, Japan)",
            "founder": "Kanehide Sakurada",
            "address": "Johor Industrial Zone, Malaysia",
        }
    }

    # ==============================
    # HEADER
    # ==============================
    st.header("🏢 Kaneka Corporate Portal")
    st.image("images/Kaneka_logo.png", width=200)
    st.write("---")

    # ==============================
    # SEARCH + SEE ALL
    # ==============================
    st.subheader("🔍 Search Company")

    search_term = st.text_input("Enter company name...")

    col1, col2 = st.columns(2)

    with col1:
        see_all = st.button("See All Companies")

    # ==============================
    # FILTER LOGIC
    # ==============================
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

    st.write("---")

    # ==============================
    # DISPLAY RESULTS
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
        st.info("🔎 Search a company or click 'See All Companies' to display results.")

    # ==============================
    # SIDEBAR NAVIGATION
    # (Optional structure for future expansion)
    # ==============================
    st.sidebar.write("---")
    menu = st.sidebar.radio(
        "📌 Navigation",
        ["Kaneka Group", "Corporate Philosophy", "Location", "History", "Products"]
    )

    # ==============================
    # NAV CONTENT (SIMPLE PLACEHOLDER)
    # ==============================
    if menu == "Kaneka Group":
        st.subheader("🏢 Kaneka Group")
        st.info("Kaneka Corporation is a Japanese chemical company founded in 1949.")

    elif menu == "Corporate Philosophy":
        st.subheader("🧭 Philosophy")
        st.success("Innovation, Sustainability, and Human Well-being.")

    elif menu == "Location":
        st.subheader("📍 Location")
        st.write("Malaysia & Global Sites")
        st.map()

    elif menu == "History":
        st.subheader("📜 History")
        st.table([
            ["Kaneka Malaysia", "1990"],
            ["Kaneka Fibers", "2005"],
            ["Kaneka Eperan", "2000"],
        ])

    elif menu == "Products":
        st.subheader("📦 Products")
        st.write("Product section coming soon...")
