import streamlit as st

# --- Setup ---
st.set_page_config(page_title="Mayapur Map", layout="wide")

# --- Title Bar Styling ---
st.markdown("""
    <style>
    .title-block {
        padding: 2rem;
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
        text-align: center;
        border-bottom: 2px solid #ddd;
    }
    .title-block h1 {
        font-size: 40px;
        color: #2c3e50;
        margin: 0;
    }
    .subtitle {
        color: #7f8c8d;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title Display ---
st.markdown("""
<div class="title-block">
    <h1>🗺️ Mayapur Points of Interest Map</h1>
    <div class="subtitle">Temples, Ghats, Restaurants, Institutes & More</div>
</div>
""", unsafe_allow_html=True)

# --- Embed the Final HTML Map ---
with open("mayapur_final_zoom_category_legend.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=720, scrolling=True)

# --- Footer ---
st.markdown("""
    <hr>
    <center style='color: grey; font-size: 14px;'>Made with ❤️ for pilgrims, visitors, and locals of Mayapur</center>
""", unsafe_allow_html=True)
# --- Additional Styling ---
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f4f8;
    }   
    .stMarkdown {
        margin: 0 auto;
        max-width: 800px;
    }

    .stButton button {

        background-color: #3498db;
        color: white;

        border: none;



        padding: 10px 20px; 
            

        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)
# --- Add a button to refresh the map ---
if st.button("Refresh Map"):
    st.experimental_rerun()
# --- Add a button to go back to the main page ---
if st.button("Back to Main Page"):
    st.write("Redirecting to the main page...")
    st.experimental_rerun()  # This will redirect to the main page if you have set it up
    


