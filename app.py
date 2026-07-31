import streamlit as st
from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_score
from utils.contact_extractor import extract_contact_info
from utils.education_extractor import extract_education
from utils.experience_extractor import extract_work_experience


st.title("📄 AI Resume Analyzer")
st.write("Welcome to the AI Resume Analyzer!")
st.header("Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a resume",
    type=["pdf"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    cleaned_text = clean_text(text)

    skills = extract_skills(cleaned_text)

    score = calculate_score(skills)

    contact = extract_contact_info(cleaned_text)

    education = extract_education(cleaned_text)

    experience = extract_work_experience(cleaned_text)

    st.subheader("Extracted Resume Text")
    st.write(cleaned_text)

    st.subheader("Detected Skills")

    for skill in skills:
        st.markdown(f"✅ {skill}")

    st.subheader("Resume Score")

    st.progress(score / 100)

    st.success(f"Resume Score : {score}/100")

    contact = extract_contact_info(cleaned_text)
    

    st.subheader("Contact Information")

    st.write(contact)

    st.subheader("🎓 Education")

    st.write("**Degree:**", education["Degree"])
    st.write("**Branch:**", education["Branch"])
    st.write("**University:**", education["University"])
    st.write("**CGPA:**", education["CGPA"])
    st.write("**Percentage:**", education["Percentage"])
    st.write("**Passing Year:**", education["Passing Year"])
    
    st.subheader("💼 Work Experience")

    st.write("**Years:**", experience["years"])
    st.write("**Titles:**", ", ".join(experience["titles"]))
    st.write("**Companies:**", ", ".join(experience["companies"]))

