import streamlit as st

def company_page():
    st.header("🏢 Company Background")
    st.write("Kaneka Malaysia operates several companies under the Kaneka Group. Explore each company below:")

    # Dictionary of companies with descriptions and optional logo paths
    companies = {
        "Kaneka Malaysia": {
            "desc": "Produces Kane Ace (impact modifiers) and Graphite Sheet (thermal management).",
            "logo": "images/Kaneka_logo.png"
        },
        "Kaneka Innovative Fibers Malaysia – FPW Plant": {
            "desc": "Makes Kanekalon (FPW) synthetic fibers for wigs and hair extensions.",
            "logo": "images/fiber_logo.png"
        },
        "Kaneka Innovative Fibers Malaysia – iModa Plant": {
            "desc": "Specialized Kanekalon fibers for fashion and styling.",
            "logo": "images/imoda_logo.png"
        },
        "Kaneka Eperan Malaysia": {
            "desc": "Produces Eperan foam for automotive and packaging.",
            "logo": "images/eperan_logo.png"
        },
        "Kaneka Paste Polymer Malaysia": {
            "desc": "Manufactures Paste PVC resin for flooring, wall coverings, and synthetic leather.",
            "logo": "images/polymer_logo.png"
        },
        "Kaneka Apical Malaysia": {
            "desc": "Creates Apical Polyimide Film for aerospace and electronics.",
            "logo": "images/apical_logo.png"
        },
        "Kaneka MS Malaysia": {
            "desc": "Develops MS Polymer for adhesives and sealants.",
            "logo": "images/ms_logo.png"
        }
    }

    # Display companies in two columns
    cols = st.columns(2)
    i = 0
    for company, details in companies.items():
        with cols[i % 2]:
            st.markdown(f"### 📦 {company}")
            st.info(details["desc"])
            # Show logo if available
            try:
                st.image(details["logo"], width=120)
            except:
                st.write("🔹 Logo not available")
        i += 1

    # Reflection / Summary
    st.markdown(
        """
        ---
        **Kaneka Malaysia’s diverse operations** highlight its role in advanced materials, 
        polymers, and specialty chemicals — supporting industries from automotive to aerospace.
        """
    )
