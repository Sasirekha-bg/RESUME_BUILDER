from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf(resume_data):
    """Generate PDF from resume data"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Create custom styles without adding to global stylesheet
    title_style = ParagraphStyle(
        name='ResumeTitle',
        parent=styles['Heading1'],
        fontSize=24,
        alignment=1,  # Center alignment
        spaceAfter=20,
        textColor=colors.darkblue
    )
    
    section_style = ParagraphStyle(
        name='ResumeSection',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.darkslategray
    )
    
    content = []
    
    # Name with custom style
    content.append(Paragraph(resume_data['name'], title_style))
    
    # Summary
    if resume_data['summary']:
        content.append(Paragraph("Professional Summary", section_style))
        content.append(Paragraph(resume_data['summary'], styles['BodyText']))
        content.append(Spacer(1, 12))
    
    # Experience
    content.append(Paragraph("Work Experience", section_style))
    for exp in resume_data['experiences']:
        exp_text = f"<b>{exp['title']}</b> - {exp['company']} ({exp['duration']})"
        content.append(Paragraph(exp_text, styles['BodyText']))
        content.append(Spacer(1, 8))
    
    # Skills
    content.append(Paragraph("Technical Skills", section_style))
    skills = ListFlowable(
        [Paragraph(f"<bullet>&bull;</bullet> {skill}", styles['BodyText']) 
         for skill in resume_data['skills']],
        bulletType='bullet',
        leftIndent=20
    )
    content.append(skills)
    
    doc.build(content)
    buffer.seek(0)
    return buffer.getvalue()