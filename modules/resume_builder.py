# modules/resume_builder.py
import streamlit as st
from streamlit_tags import st_tags

def collect_resume_data():
    """Collect resume data through a form with fresher-friendly sections"""
    resume = {
        'personal_details': {
            'name': '',
            'email': '',
            'phone': '',
            'linkedin': '',
            'github': '',
            'location':''
        },
        'summary': '', 
        'education': [],
        'internships': [],
        'projects': [],
        'skills': [],
        'achievements': [],
        'certifications': []
    }
    
    with st.form("resume_form"):
        # Personal Details Section
        st.header("👤 Personal Details")
        col1, col2 = st.columns(2)
        with col1:
            resume['personal_details']['name'] = st.text_input("Full Name")
            resume['personal_details']['email'] = st.text_input("Email")
        with col2:
            resume['personal_details']['phone'] = st.text_input("Phone Number")
            resume['personal_details']['linkedin'] = st.text_input("LinkedIn")
        resume['personal_details']['github'] = st.text_input("GitHub")
        resume['personal_details']['location'] = st.text_input("Location")
        # Profile Summary Section
        st.header("📝 Profile Summary/Objective")
        resume['summary'] = st.text_area(
            "Write a brief summary (2-3 lines) or career objective:",
            placeholder="Example: 'Recent Computer Science graduate with hands-on experience in Python and ML. "
                        "Awarded Best Final Year Project for AI-powered inventory system. Seeking to apply...'",
            max_chars=300,
            help="Focus on key achievements, skills, and career goals"
        )
        # Education Section
        st.header("🎓 Education")
        edu_cols = st.columns([3, 2, 2])
        with edu_cols[0]:
            university = st.text_input("University/Institute")
        with edu_cols[1]:
            degree = st.text_input("Degree/Course")
        with edu_cols[2]:
            cgpa = st.text_input("CGPA/Percentage")
        resume['education'].append({
            'university': university,
            'degree': degree,
            'cgpa': cgpa,
            'duration': st.text_input("Duration (e.g., 2020-2024)")
        })

        # Internships Section - Using columns instead of expanders
        st.header("💼 Internships")
        internships_count = st.number_input("Number of Internships", 0, 5, 0)
        for i in range(internships_count):
            st.subheader(f"Internship {i+1}")
            cols = st.columns([2, 1, 1])
            resume['internships'].append({
                'company': cols[0].text_input(f"Company Name {i+1}", key=f"company_{i}"),
                'role': cols[1].text_input(f"Role {i+1}", key=f"role_{i}"),
                'duration': cols[2].text_input(f"Duration {i+1}", key=f"duration_{i}"),
                'description': st.text_area(f"Key Responsibilities/Achievements {i+1}", key=f"desc_{i}")
            })

        # Projects Section - Using containers instead of expanders
        st.header("📂 Projects")
        projects_count = st.number_input("Number of Projects", 1, 5, 1)
        for i in range(projects_count):
            with st.container():
                st.subheader(f"Project {i+1}")
                resume['projects'].append({
                    'title': st.text_input(f"Project Title {i+1}", key=f"title_{i}"),
                    'description': st.text_area(f"Project Description {i+1}", key=f"desc_{i}"),
                    'technologies': st_tags(
                        label=f"Technologies Used {i+1}",
                        text='Press enter to add',
                        suggestions=['Python', 'React', 'TensorFlow'],
                        key=f"tech_{i}"
                    ),
                    'github_link': st.text_input(f"Repository Link {i+1} (optional)", key=f"repo_{i}")
                })
                st.markdown("---")  # Add separator between projects

        # Skills & Achievements
        st.header("🛠️ Skills & Achievements")
        resume['skills'] = st_tags(
            label='Technical Skills',
            text='Press enter to add',
            suggestions=['Python', 'Machine Learning', 'SQL']
        )
        
        resume['achievements'] = st_tags(
            label='Achievements',
            text='Press enter to add',
            suggestions=['Won Hackathon XYZ', 'Published Paper on ABC']
        )

        if st.form_submit_button("💾 Save Resume"):
            return resume
    return None