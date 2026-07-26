import streamlit as st
from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_score
from utils.contact_extractor import extract_contact_info

# ------------------------------
# Title
# ------------------------------
st.title("📄 AI Resume Analyzer")
st.write("Welcome to the AI Resume Analyzer!")
st.header("Upload Resume")

# ------------------------------
# Upload PDF
# ------------------------------
uploaded_file = st.file_uploader(
    "Choose a resume",
    type=["pdf"]
)

# ------------------------------
# Process Resume
# ------------------------------
if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text from PDF
    resume_text = extract_text(uploaded_file)

    # Clean text
    resume_text = clean_text(resume_text)

    # Extract skills
    skills = extract_skills(resume_text)

    # Calculate score
    score = calculate_score(skills)

    # ------------------------------
    # Display Resume Text
    # ------------------------------
    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    # ------------------------------
    # Display Skills
    # ------------------------------
    st.subheader("Detected Skills")

    for skill in skills:
        st.markdown(f"✅ {skill}")

    # ------------------------------
    # Display Resume Score
    # ------------------------------
    st.subheader("Resume Score")

    st.progress(score / 100)

    st.success(f"Resume Score : {score}/100")


    contact = extract_contact_info(cleaned_text)

    st.subheader("Contact Information")

    st.write(contact)