# 📄 AI Resume Analyzer

An end-to-end resume parsing and analysis tool built with **Python** and **Streamlit**. Upload a PDF resume and instantly extract structured information — contact details, education, work experience, projects, certifications, and skills — then get an ATS compatibility score and AI-powered feedback on how to improve it.

---

## ✨ Features

- **PDF Parsing** — extracts raw text from uploaded resume PDFs
- **Text Cleaning** — normalizes extracted text for reliable downstream parsing
- **Skill Detection** — scans resume text against a curated skill list (Python, SQL, Machine Learning, TensorFlow, etc.)
- **Resume Scoring** — generates a 0–100 score based on detected skills
- **Contact Information Extraction** — name, email, phone, LinkedIn, GitHub, portfolio links
- **Education Extraction** — degree, branch/specialization, university, CGPA, percentage, passing year
- **Work Experience Extraction** — years of experience, job titles, companies
- **Project Extraction** — project names, technologies used, and descriptions
- **Certification Extraction** — certification name, issuing organization, year, credential URL
- **ATS Resume Analysis** — ATS compatibility score, section completeness, action-verb usage, quantified-achievement detection, and optional keyword matching against a job description
- **AI-Powered Resume Review** — LLM-generated strengths, weaknesses, skill gaps, and personalized improvement recommendations

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI / App Framework | [Streamlit](https://streamlit.io/) |
| PDF Parsing | Python (`pdfplumber` / `PyPDF2`) |
| Text Processing | `re` (Regular Expressions) |
| AI Review (Phase 12) | 
| Language | Python 3.10+ |

---

## 📂 Project Structure

```
Resume Analyzer Project/
├── app.py                          # Main Streamlit application — orchestrates the full pipeline
├── requirements.txt                # Python dependencies
├── README.md
│
├── utils/
│   ├── pdf_parser.py               # Extracts raw text from uploaded PDF
│   ├── text_cleaner.py             # Cleans/normalizes extracted text
│   ├── skill_extractor.py          # Detects known technical skills in resume text
│   ├── resume_score.py             # Calculates resume score from detected skills
│   ├── contact_extractor.py        # Extracts name, email, phone, LinkedIn, GitHub, portfolio
│   ├── education_extractor.py      # Extracts degree, branch, university, CGPA, percentage, year
│   ├── experience_extractor.py     # Extracts years of experience, job titles, companies
│   ├── project_extractor.py        # Extracts project name, technologies, description
│   ├── certification_extractor.py  # Extracts certification name, issuer, year, credential URL
│   ├── ats_analyzer.py             # Calculates ATS score, section completeness, keyword match
│   └── ai_analyzer.py              # Sends resume data to an LLM for qualitative feedback
│
├── uploaded_resume/                # Temporary storage for uploaded files
├── dataset/                        # Reference data (skill lists, degree/branch/university lists, etc.)
├── models/                         # Reserved for any future ML models
└── assets/                         # Static assets (icons, images)
```

---

## ⚙️ How It Works — Pipeline Overview

```
Upload PDF
    │
    ▼
extract_text()            → Raw text pulled from PDF
    │
    ▼
clean_text()               → Normalized, cleaned text
    │
    ├──▶ extract_skills()             → List of detected skills
    │         │
    │         ▼
    │    calculate_score()            → Resume score (0–100)
    │
    ├──▶ extract_contact_info()       → Name, email, phone, links
    ├──▶ extract_education()          → Degree, branch, university, CGPA, year
    ├──▶ extract_work_experience()    → Years, titles, companies
    ├──▶ extract_projects()           → Project name, tech stack, description
    ├──▶ extract_certifications()     → Certification name, issuer, year
    │
    ├──▶ calculate_ats_score()        → ATS score + improvement suggestions
    │
    └──▶ get_ai_resume_review()       → LLM-generated strengths/weaknesses/recommendations
```

Each extractor module is independent and testable on its own — they all take cleaned resume text as input and return a structured Python dict or list, which `app.py` then renders in the Streamlit UI.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Resume-Analyzer-Project.git
cd "Resume Analyzer Project"
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your Anthropic API key (required for the AI Review feature)
```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your-api-key-here"

# macOS/Linux
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 5. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 📖 Usage

1. Upload a resume in **PDF** format.
2. (Optional) Paste a job description to enable ATS keyword matching.
3. View extracted **Contact Info**, **Education**, **Work Experience**, **Projects**, and **Certifications**.
4. Check your **Resume Score** and **ATS Score**, along with specific improvement suggestions.
5. Click **"Generate AI Review"** for a qualitative breakdown of strengths, weaknesses, and personalized recommendations.

---

## 🧠 Design Notes

- **Rule-based extraction (regex + controlled vocabularies)** is used for structured fields like degree, university, and skills — this keeps the pipeline fast, free to run, and fully explainable (no black-box model deciding what your CGPA is).
- **LLM-based analysis** is reserved specifically for the qualitative feedback that regex genuinely can't do well — judging resume *quality*, not just extracting facts.
- Extractors are **kept modular** — each `utils/*.py` file does exactly one job, so any single extractor can be improved, tested, or swapped out without touching the rest of the pipeline.

---

## 🔭 Known Limitations

- Regex-based extraction is tuned to common resume formats; unusually formatted resumes (heavy graphics, multi-column layouts, non-standard section headers) may reduce extraction accuracy.
- Company/employer extraction works best for resumes with traditional "at Company Name" phrasing; project-based or freelance-style experience sections may return partial results.
- AI Review requires a valid Anthropic API key and incurs API usage costs per resume analyzed.

---

## 🗺️ Roadmap / Future Improvements

- [ ] Support for `.docx` resume uploads
- [ ] Resume-to-job-description similarity scoring using embeddings
- [ ] Downloadable PDF report of the full analysis
- [ ] Multi-resume batch comparison mode
- [ ] Editable extracted fields (in case of parsing errors) with `st.session_state`

---

## 👤 Author

**Mohit Khangar**
📧 mohitkhangar.job@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/mohitkhangar) · [GitHub](https://github.com/mohitkhangar)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
