import streamlit as st
from modules.resume_builder import collect_resume_data
from modules.ats_analyzer import evaluate_resume, auto_improve
from modules.pdf_generator import generate_pdf

def main():
    st.title("AI-Powered ATS Resume Builder")
    
    # Initialize session state
    if 'resume_data' not in st.session_state:
        st.session_state.resume_data = None
    if 'improved_resume' not in st.session_state:
        st.session_state.improved_resume = None

    # Resume Creation Section
    with st.expander("📝 Build Your Resume", expanded=True):
        built_resume = collect_resume_data()
        if built_resume:
            st.session_state.resume_data = built_resume
            st.session_state.improved_resume = None  # Reset improvements on new resume
            st.success("Resume draft saved successfully!")

    # JD Analysis Section
    st.divider()
    jd = st.text_area("🔍 Paste Job Description (ATS Analysis)", height=150)
    
    current_resume = st.session_state.improved_resume or st.session_state.resume_data
    
    if jd and current_resume:
        try:
            score, analysis = evaluate_resume(current_resume, jd)
            st.metric("📊 ATS Score", f"{score}/100")
            
            with st.expander("💡 Improvement Suggestions"):
                st.write(analysis.get("recommendations", "No suggestions available"))
            
            if st.button("✨ Auto-Improve Resume"):
                st.session_state.improved_resume = auto_improve(current_resume, jd)
                st.rerun()
                
        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")

    # Download Section
    st.divider()
    if current_resume:
        try:
            pdf_bytes = generate_pdf(current_resume)
            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name="resume.pdf",
                mime="application/pdf",
                type="primary"
            )
        except Exception as e:
            st.error(f"PDF generation failed: {str(e)}")

    # Show improvement notice
    if st.session_state.improved_resume:
        st.info("✨ You're viewing an improved version of your resume. Close this alert to see the original.")
        if st.button("View Original Resume"):
            st.session_state.improved_resume = None
            st.rerun()

if __name__ == "__main__":
    main()