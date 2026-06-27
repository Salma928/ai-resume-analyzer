import streamlit as st
from groq import Groq
import PyPDF2
import io

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 AI Resume Analyzer")
st.markdown("Upload your resume and paste a job description to get an AI-powered match analysis.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description here", height=200)
api_key = st.text_input("Your Groq API Key", type="password")

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if st.button("Analyze my Resume 🚀"):
    if not uploaded_file or not job_description or not api_key:
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            client = Groq(api_key=api_key)
            prompt = f"""
You are an expert recruiter and career coach. Analyze the following resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Please provide:
1. **Match Score** (0-100)
2. **Strengths** - what the candidate does well for this role
3. **Weaknesses** - what is missing or weak
4. **Improvements** - concrete suggestions to improve the resume for this job
5. **Verdict** - should they apply? (Yes / Maybe / No)

Be honest, specific, and actionable.
"""
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content

        st.markdown("---")
        st.markdown("## 📊 Analysis Results")
        st.markdown(result)
