from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf(resume_data):
    """Generate fresher-friendly PDF resume"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        name='ResumeTitle',
        parent=styles['Heading1'],
        fontSize=20,
        alignment=1,
        textColor=colors.darkblue
    )
    
    section_style = ParagraphStyle(
        name='ResumeSection',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=12,
        textColor=colors.darkslategray
    )
    
    content = []
    
    # Header Section
    personal = resume_data['personal_details']
    header_text = f"{personal['name']}<br/>" \
                f"<font size=10>{personal['email']} | {personal['phone']}<br/>" \
                f"LinkedIn: {personal['linkedin']} | GitHub: {personal['github']}</font>"
    content.append(Paragraph(header_text, title_style))
    content.append(Spacer(1, 20))

    # Education
    content.append(Paragraph("Education", section_style))
    for edu in resume_data['education']:
        edu_text = f"<b>{edu['degree']}</b><br/>" \
                  f"{edu['university']}<br/>" \
                  f"CGPA/Percentage: {edu['cgpa']} | Duration: {edu['duration']}"
        content.append(Paragraph(edu_text, styles['BodyText']))
        content.append(Spacer(1, 10))

    # Internships
    if resume_data['internships']:
        content.append(Paragraph("Internships", section_style))
        for intern in resume_data['internships']:
            intern_text = f"<b>{intern['role']}</b> at {intern['company']} ({intern['duration']})<br/>" \
                         f"{intern['description']}"
            content.append(Paragraph(intern_text, styles['BodyText']))
            content.append(Spacer(1, 8))

    # Projects
    content.append(Paragraph("Projects", section_style))
    for project in resume_data['projects']:
        proj_text = f"<b>{project['title']}</b>"
        if project['github_link']:
            proj_text += f" [<link href='{project['github_link']}>GitHub</link>]"
        proj_text += f"<br/>Technologies: {', '.join(project['technologies'])}<br/>{project['description']}"
        content.append(Paragraph(proj_text, styles['BodyText']))
        content.append(Spacer(1, 8))

    # Skills & Achievements
    cols = [content]
    skills_col, achiev_col = [], []
    
    skills_col.append(Paragraph("Technical Skills", section_style))
    skills_col.append(ListFlowable(
        [Paragraph(skill, styles['BodyText']) for skill in resume_data['skills']],
        bulletType='bullet'
    ))
    
    achiev_col.append(Paragraph("Achievements", section_style))
    achiev_col.append(ListFlowable(
        [Paragraph(achiev, styles['BodyText']) for achiev in resume_data['achievements']],
        bulletType='bullet'
    ))
    
    content.append(Spacer(1, 10))
    content.append(ParallelFlowable([skills_col, achiev_col], [400, 400]))

    doc.build(content)
    buffer.seek(0)
    return buffer.getvalue()