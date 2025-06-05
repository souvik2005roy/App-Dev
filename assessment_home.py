import streamlit as st
from datetime import date

st.set_page_config(page_title="Student Assessment Portal", page_icon="📘", layout="centered")

# Session state to control page navigation
if "user_type" not in st.session_state:
    st.session_state.user_type = None

# Page 1: Choose User Type
if st.session_state.user_type is None:
    st.title("📘 Welcome to Evalzer0")
    st.subheader("An AI-driven platform to assess and improve learning outcomes.")
    st.markdown("---")
    
    st.header("Who are you?")
    user_choice = st.radio("Please select your role:", ["Student", "Organization"])

    if st.button("Continue"):
        st.session_state.user_type = user_choice
        st.rerun()

# Page 2: Organization or Student Specific Input
else:
    if st.session_state.user_type == "Organization":
        st.title("🏢 Organization Contact Form")
        st.markdown("Please provide your details so we can reach out to you.")

        org_name = st.text_input("Organization Name")
        contact_person = st.text_input("Your Name")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email Address")
        interest_reason = st.text_area("Why are you interested in this platform?")

        if st.button("Submit Request"):
            if org_name and contact_person and phone and email and interest_reason:
                st.success("Thank you! Our team will contact you shortly.")
            else:
                st.warning("Please fill all the fields.")

    elif st.session_state.user_type == "Student":
        st.title("👤 Student Profile")
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=10, max_value=100, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
        dob = st.date_input("Date of Birth", max_value=date.today())
        grade = st.selectbox("Current Grade/Class", ["Class 9", "Class 10", "Class 11", "Class 12", "Undergraduate", "Other"])

        st.header("📚 Academic Details")
        subjects = st.multiselect("Select Subjects", ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "Economics", "English"])
        institution = st.text_input("School / Institution Name")
        board = st.selectbox("Education Board", ["CBSE", "ICSE", "State Board", "IB", "Cambridge", "Other"])

        st.header("🧠 Learning Context")
        exam_target = st.selectbox("Target Exam (if any)", ["None", "JEE", "NEET", "SAT", "CUET", "Board Exams", "Olympiads"])
        study_medium = st.radio("Preferred Learning Medium", ["Videos", "Textbooks", "One-on-one classes", "Group classes"])
        revision_habit = st.radio("Do you revise regularly?", ["Yes", "Sometimes", "Rarely"])

        if st.button("Proceed to Assessment"):
            if name == "" or len(subjects) == 0:
                st.warning("Please fill out all required fields before continuing.")
            else:
                st.success(f"Welcome {name}! Preparing your personalized dashboard...")

# Footer
st.markdown("---")
st.caption("EduCheck Platform | Designed to help you track and improve your academic journey.")
