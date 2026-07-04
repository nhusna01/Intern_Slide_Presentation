import streamlit as st

def additional_page():
    st.title("📖 Chapter 4")
    st.write("Additional page content goes here.")

def esg_page():
    st.title("🌍 What is ESG?")

    st.markdown("""
    <style>
    .esg-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-top: 40px;
    }
    .letter {
        font-size: 90px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.3s ease, color 0.3s ease;
        animation: bounce 2s infinite;
    }
    .letter:hover {
        transform: scale(1.3);
        color: #2E8B57;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    .card {
        display: none;
        margin-top: 30px;
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f8ff;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: left;
        font-size: 18px;
    }
    .card h3 {
        margin-top: 0;
        color: #2E8B57;
    }
    .reset-btn {
        margin-top: 20px;
        padding: 10px 20px;
        background-color: #2E8B57;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .reset-btn:hover {
        background-color: #246b45;
    }
    </style>

    <div class="esg-container">
        <div class="letter" onclick="showCard('E')">E</div>
        <div class="letter" onclick="showCard('S')">S</div>
        <div class="letter" onclick="showCard('G')">G</div>
    </div>

    <div id="card-E" class="card">
        <h3>🌱 Environmental</h3>
        <p>Focuses on how a company impacts the planet. Examples include carbon emissions, energy efficiency, waste management, and sustainable practices.</p>
    </div>

    <div id="card-S" class="card">
        <h3>🤝 Social</h3>
        <p>Examines how a company treats people — employees, customers, and communities. This includes diversity, labor practices, human rights, and community engagement.</p>
    </div>

    <div id="card-G" class="card">
        <h3>⚖️ Governance</h3>
        <p>Refers to leadership, ethics, and accountability. It covers board structure, transparency, anti-corruption policies, and compliance.</p>
    </div>

    <button class="reset-btn" onclick="resetCards()">Reset</button>

    <script>
    function showCard(letter) {
        // Hide all cards first
        document.getElementById("card-E").style.display = "none";
        document.getElementById("card-S").style.display = "none";
        document.getElementById("card-G").style.display = "none";
        // Show the selected card
        document.getElementById("card-" + letter).style.display = "block";
    }
    function resetCards() {
        document.getElementById("card-E").style.display = "none";
        document.getElementById("card-S").style.display = "none";
        document.getElementById("card-G").style.display = "none";
    }
    </script>
    """, unsafe_allow_html=True)

    st.info("✅ ESG helps investors, regulators, and the public assess long-term sustainability and ethical impact.")

