# modules/resume_builder.py
import streamlit as st
from streamlit_tags import st_tags

def collect_resume_data():
    """Collect resume data through a form"""
    resume = {
        'name': '',
        'summary': '',
        'experiences': [],
        'skills': []
    }
    
    with st.form("resume_form"):
        resume['name'] = st.text_input("Full Name")
        resume['summary'] = st.text_area("Professional Summary")
        
        # Experience Section - Using columns instead of expanders
        st.subheader("Work Experience")
        exp_count = st.number_input("Number of Positions", 1, 10, 1, key="exp_count")
        
        for i in range(exp_count):
            col1, col2, col3 = st.columns(3)
            with col1:
                title = st.text_input(f"Job Title {i+1}", key=f"title_{i}")
            with col2:
                company = st.text_input(f"Company {i+1}", key=f"company_{i}")
            with col3:
                duration = st.text_input(f"Duration {i+1}", key=f"duration_{i}")
            
            resume['experiences'].append({
                'title': title,
                'company': company,
                'duration': duration
            })
        
        # Skills Section
        st.subheader("Technical Skills")
        resume['skills'] = st_tags(
            label='Add skills (press enter after each)',
            text='Start typing...',
            suggestions=['Python', 'SQL', 'Project Management', 'Machine Learning']
        )
        
        if st.form_submit_button("Save Resume"):
            return resume
    return None