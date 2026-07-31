import streamlit as st
from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.resume_score import calculate_score
from utils.contact_extractor import extract_contact_info
from utils.education_extractor import extract_education
from utils.experience_extractor import extract_work_experience
from utils.project_extractor import extract_projects
from utils.certification_extractor import extract_certifications
from utils.ats_analyzer import calculate_ats_score
from utils.ai_analyzer import get_ai_resume_review, parse_ai_review
from openai import RateLimitError, OpenAIError


st.title("📄 AI Resume Analyzer")
st.write("Welcome to the AI Resume Analyzer!")
st.header("Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste a job description (optional, improves ATS analysis)",
    height=150
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)
    cleaned_text = clean_text(text)

    skills = extract_skills(cleaned_text)
    score = calculate_score(skills)
    contact = extract_contact_info(cleaned_text)
    education = extract_education(cleaned_text)
    experience = extract_work_experience(cleaned_text)
    projects = extract_projects(cleaned_text)
    certifications = extract_certifications(cleaned_text)

    ats_result = calculate_ats_score(
    cleaned_text,
    skills,
    job_description if job_description else None)

    with st.expander("📄 View Extracted Resume Text"):
        st.write(cleaned_text)

    st.subheader("Detected Skills")
    for skill in skills:
        st.markdown(f"✅ {skill}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Resume Score", f"{score}/100")
        st.progress(score / 100)

    with col2:
        st.metric("ATS Score", f"{ats_result['ATS Score']}/100")

    st.subheader("📞 Contact Information")

    st.write("**Name:**", contact["Name"])
    st.write("**Email:**", contact["Email"])
    st.write("**Phone:**", contact["Phone"])
    st.write("**LinkedIn:**", contact["LinkedIn"])
    st.write("**GitHub:**", contact["GitHub"])

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


    st.subheader("📁 Projects")
    if projects:
        for p in projects:
            st.markdown(f"**{p['Project Name']}** ({p['Year']})")
            st.write("Technologies:", ", ".join(p["Technologies"]))
            for bullet in p["Description"]:
                st.markdown(f"- {bullet}")
            st.markdown("---")
    else:
        st.info("No distinct project entries detected.")


    st.subheader("🏆 Certifications")
    if certifications:
        for c in certifications:
            st.write(f"**{c['Certification Name']}** — {c['Issued By']} ({c['Year']})")
    else:
        st.info("No certifications section detected.")


    st.subheader("📊 ATS Resume Analysis")


    st.metric("ATS Score", f"{ats_result['ATS Score']}/100")

    st.subheader("✅ Section Completeness")

    for section, present in ats_result["Section Completeness"].items():
        if present:
            st.success(f"✅ {section}")
        else:
            st.error(f"❌ {section}")

    st.subheader("⚡ Action Verbs Detected")
    st.write(", ".join(ats_result["Action Verbs Used"]))

    st.subheader("📈 Quantified Achievements")
    st.write(ats_result["Quantified Achievements"])

    st.subheader("💡 Suggestions")

    if ats_result["Suggestions"]:
        for suggestion in ats_result["Suggestions"]:
            st.warning(suggestion)
    else:
        st.success("Excellent resume! No major ATS improvements detected.")

    st.subheader("🤖 AI Resume Review")

    if st.button("Generate AI Review"):

        try:
            with st.spinner("Analyzing your resume with AI..."):

                raw_review = get_ai_resume_review(
                    cleaned_text,
                    education,
                    experience,
                    skills
                )

                review = parse_ai_review(raw_review)

            st.markdown("### ✅ Strengths")
            for s in review["Strengths"]:
                st.success(s)

            st.markdown("### ⚠️ Weaknesses")
            for w in review["Weaknesses"]:
                st.warning(w)

            st.markdown("### 🔍 Skill Gaps")
            for g in review["Skill Gaps"]:
                st.info(g)

            st.markdown("### 💡 Recommendation")
            st.write(review["Recommendation"])

        except RateLimitError:
            st.warning("""
## 🚧 AI Review (Prototype)

The AI Resume Review feature has been fully integrated into this application.

However, this prototype cannot generate live AI feedback because the OpenAI API account currently has no available credits.

To enable this feature, simply add API credits to the OpenAI account and the integration will work without any code changes.

✅ All other Resume Analyzer features remain fully functional.
""")

        except OpenAIError as e:
            st.error(f"OpenAI Error: {e}")

        except Exception as e:
            st.error(f"Unexpected Error: {e}")

    st.divider()
    st.caption("Built with ❤️ using Python, Streamlit, Regex, NLP, and OpenAI API")