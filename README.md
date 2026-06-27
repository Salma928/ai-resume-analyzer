#  AI Resume Analyzer

An AI-powered resume analyzer built with Streamlit and LLaMA 3 (via Groq API).

## Features
- Upload your resume as a PDF
- Paste any job description
- Get an instant AI analysis including:
  - Match Score (0-100)
  - Strengths & Weaknesses
  - Improvement suggestions
  - Verdict on whether to apply

## Tech Stack
- Python 3.13
- Streamlit
- Groq API (LLaMA 3.3 70B)
- PyPDF2

## Setup

1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install streamlit groq pypdf2`
4. Run the app: `streamlit run app.py`
5. Get a free Groq API key at https://console.groq.com

## Screenshots

![App Screenshot](screenshots/screenshot1.png)
