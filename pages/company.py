import streamlit as st

def company_page():

    # ==============================
    # DATA
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

   import streamlit as st

st.set_page_config(page_title="Kaneka Malaysia", layout="wide")

st.title("🏢 Kaneka Malaysia")
st.caption("Innovation • Sustainability • Human Well-being")

st.divider()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Kaneka Group"

# Navigation Cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏢\nKaneka Group", use_container_width=True):
        st.session_state.page = "Kaneka Group"

with col2:
    if st.button("🧭\nPhilosophy", use_container_width=True):
        st.session_state.page = "Corporate Philosophy"

with col3:
    if st.button("📍\nLocation", use_container_width=True):
        st.session_state.page = "Location"

with col4:
    if st.button("📜\nHistory", use_container_width=True):
        st.session_state.page = "History"

with col5:
    if st.button("📦\nProducts", use_container_width=True):
        st.session_state.page = "Products"

st.divider()

page = st.session_state.page

if page == "Kaneka Group":
    st.header("🏢 Kaneka Group")
    st.info(
        "Kaneka Corporation is a Japanese chemical company founded in 1949."
    )

elif page == "Corporate Philosophy":
    st.header("🧭 Corporate Philosophy")
    st.success(
        "Innovation, Sustainability, and Human Well-being."
    )

elif page == "Location":
    st.header("📍 Global Locations")
    st.map()

elif page == "History":
    st.header("📜 Company History")

    st.timeline([
        {"content": "Kaneka (Malaysia) Sdn Bhd Established", "start": "1990"},
        {"content": "Kaneka Eperan Sdn Bhd Expansion", "start": "2000"},
        {"content": "Kaneka Innovative Fibers Sdn Bhd Development", "start": "2005"},
        {"content": "Kaneka MS Malaysia Sdn Bhd Established", "start": "1990"},
        {"content": "Kaneka Paste Polymers Expansion", "start": "2000"},
        {"content": "Kaneka Apical Malaysia Sdn Bhd", "start": "2005"},
        
    ])

elif page == "Products":
    st.header("📦 Products")
    st.write("Product section coming soon...")
