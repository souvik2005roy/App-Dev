import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mayapur Map", layout="wide")

# Title and Instructions
st.title("📍 Sreedham Mayapur")
st.markdown("""
Welcome to the **Mayapur Map Viewer**  
This application shows an interactive map of Mayapur with:
- Points of Interest
- A red boundary highlighting the area of interest
""")
st.markdown("---")

# Sidebar interactivity
with st.sidebar:
    st.header("🧭 Map Options")
    show_map = st.checkbox("Display Map", value=True)
    show_info = st.checkbox("Show Map Information", value=True)

# Display the map
if show_map:
    with open("Mayapur_Map_With_Rajapur_Extended.html", 'r', encoding='utf-8') as f:
        map_html = f.read()

    components.html(map_html, height=800, width=1200)

# Optional info box
if show_info:
    with st.expander("ℹ️ About This Map"):
        st.markdown("""
        This map highlights the key Points of Interest across **Mayapur**.  
        The red boundary shows the broader area under consideration, including surrounding landmarks.  
        All locations are visualized using **Mapbox GL JS**, embedded seamlessly in this Streamlit app.
        """)