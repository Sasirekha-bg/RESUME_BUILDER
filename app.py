# app.py
import streamlit as st
from modules.resume_builder import collect_resume_data  # Correct import
from modules.ats_analyzer import evaluate_resume, auto_improve
from modules.pdf_generator import generate_pdf

st.title("AI-Powered ATS Resume Builder")

# Resume Creation Section
with st.expander("Build Your Resume"):
    resume_data = collect_resume_data()  # Direct function call

# Rest of your code...

# JD Analysis Section
jd = st.text_area("Paste Job Description")
if jd and resume_data:
    score, analysis = evaluate_resume(resume_data, jd)
    st.metric("ATS Score", f"{score}/100")
    
    with st.expander("Improvement Suggestions"):
        st.write(analysis["recommendations"])
    
    if st.button("Auto-Improve Resume"):
        improved_resume = auto_improve(resume_data, jd)
        st.session_state.resume_data = improved_resume

# Download Section

if resume_data:
    pdf_bytes = generate_pdf(resume_data)
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="resume.pdf",
        mime="application/pdf"
    )