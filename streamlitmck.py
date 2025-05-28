import streamlit as st
import time as t
#title - used
st.title("Welcome to Mayapur")

#Header
st.header("Mayapur:  The Beautiful Land of Lord Chaitanya")
          
#Image
st.image("https://t4.ftcdn.net/jpg/05/05/06/01/360_F_505060107_5Il48AH5B1Ov6zRZcYOJ2bA6P5dKKqWO.jpg", caption="Mayapur - A Spiritual Haven", use_container_width=True)

#Subheader
st.subheader("A place of spiritual significance and natural beauty")

#Information
st.info("Mayapur is a small town in West Bengal, India, known for its rich spiritual heritage and natural beauty. It is the birthplace of Lord Chaitanya Mahaprabhu, a revered saint in the Gaudiya Vaishnavism tradition.")
#Warning
st.warning("Mayapur is a sacred place, and visitors are expected to respect the local customs and traditions. Please dress modestly and maintain a respectful demeanor while visiting temples and other holy sites.")

#Error
st.error("Please note that Mayapur can get crowded during festival seasons. It is advisable to plan your visit in advance and book accommodations early to avoid any inconvenience.")
#Success
st.success("Mayapur is a peaceful and serene place, perfect for spiritual seekers and those looking to connect with nature. The town offers various ashrams, temples, and meditation centers for visitors to explore and experience the spiritual ambiance.")
#write
st.write("Mayapur is not just a place of worship, but also a hub of cultural and spiritual activities. The town hosts various festivals throughout the year, attracting devotees and tourists from around the world. The serene environment, lush greenery, and the sacred Ganges river add to the charm of this holy place.")
#Markdown
st.markdown("""
## Key Attractions in Mayapur
- **ISKCON Mayapur**: The International Society for Krishna Consciousness temple, a major pilgrimage site.
- **Chand Kazi's Samadhi**: The resting place of Chand Kazi, a historical figure in the life of Lord Chaitanya.
- **Yoga and Meditation Centers**: Various centers offering classes and retreats for spiritual growth.
- **Ganges River**: A sacred river where visitors can take boat rides and enjoy the serene environment.
""")
st.markdown(":moon:")

st.text_input("Enter your name", placeholder="Your Name")
st.text_area("Enter your message", placeholder="Your Message")
st.selectbox("Choose a language", ["English", "Hindi", "Bengali"])
st.multiselect("Select your interests", ["Spirituality", "Nature", "Culture", "History"])

#caption
st.caption("Mayapur is a place where spirituality meets natural beauty, offering a unique experience for all who visit.")

#to display mathematical equations
st.latex(r'''
    E = mc^2
''')

#widget
st.checkbox("I agree to the terms and conditions")

#button
if st.button("Click Me"):
    st.write("Button clicked!")
#radio button
st.radio("Select your gender", ["Male", "Female", "Other"])

#select slider
st.select_slider("Rating",["Bad", "Average", "Good", "Very Good", "Excellent"])

#slider
st.slider("Select a number", min_value=1, max_value=100, value=50)

#number input
st.number_input("Enter a number", min_value=0, max_value=100, value=50)

#date input
st.date_input("Select a date")
#time input
st.time_input("Select a time")

#file uploader
uploaded_file = st.file_uploader("Upload a file", type=["jpg", "png", "pdf"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

st.color_picker("Pick a color", "#00f900")
#progress bar
progress = st.progress(0) 
for i in range(100):
    progress.progress(i + 1)
    t.sleep(0.05)  # Simulate some work being done

#spinner
with st.spinner("Loading..."):
    t.sleep(2)  # Simulate a long-running process

#balloon
st.balloons()

#sidebar
st.sidebar.title("Sidebar")
st.sidebar.header("Explore Mayapur")
st.sidebar.image("https://t4.ftcdn.net/jpg/05/05/06/01/360_F_505060107_5Il48AH5B1Ov6zRZcYOJ2bA6P5dKKqWO.jpg", caption="Sreedham", use_container_width=True)
st.radio("Choose an option", ["Home", "About Mayapur", "Contact Us"])

#Data visulization
import pandas as pd
import numpy as np
st.title("Trends in Tourism")
data=pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)