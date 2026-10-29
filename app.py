# app.py
import streamlit as st
from domain_math import calculate_carbon_credit, optimize_htl_biofuel
import requests

st.set_page_config(page_title="QatarGPT-Edge", layout="wide")
st.title("🇶🇦 QatarGPT-Edge: Sovereign Offline Energy AI")
st.caption("Status: 🔴 Offline Mode (No Internet Needed)")

tab1, tab2, tab3 = st.tabs(["💬 Offline AI Assistant", "🍃 Carbon Credit Calculator", "⛽ Biofuel Optimization"])

with tab1:
    st.subheader("Offline AI Query Engine")
    user_query = st.text_input("Ask a question (works completely offline):", "How does offline AI help in the desert?")
    
    if st.button("Run Offline Query"):
        payload = {
            "model": "qwen2.5:3b",
            "prompt": f"Answer concisely: {user_query}",
            "stream": False
        }
        try:
            res = requests.post("http://localhost:11434/api/generate", json=payload)
            st.success(res.json()["response"])
        except Exception as e:
            st.error("Make sure Ollama is running on your computer!")

with tab2:
    st.subheader("On-Site Carbon Credit Calculator")
    col1, col2 = st.columns(2)
    energy = col1.number_input("Energy Output (MWh):", min_value=1.0, value=500.0)
    fuel = col2.selectbox("Fuel Source:", ["heavy_oil", "biofuel"])
    
    if st.button("Calculate Offsets"):
        res = calculate_carbon_credit(energy, fuel)
        st.metric("CO2 Avoided (Tons)", res["co2_avoided_tons"])
        st.metric("Carbon Credits Earned", res["carbon_credits"])

with tab3:
    st.subheader("HTL Biofuel & Green Hydrogen Yield Engine")
    feedstock = st.number_input("Organic Waste Feedstock (kg):", value=1000.0)
    temp = st.slider("Reactor Temperature (°C):", 200, 400, 330)
    
    if st.button("Optimize Reactor Yield"):
        res = optimize_htl_biofuel(feedstock, temp)
        st.json(res)