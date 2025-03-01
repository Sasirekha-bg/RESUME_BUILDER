from .scoring import ATSEvaluator
from groq import Groq

# Initialize core components once
client = Groq(api_key="your-groq-key")
evaluator = ATSEvaluator()

def evaluate_resume(resume_data, jd_text):
    """Main function to be imported"""
    resume_text = _resume_to_text(resume_data)
    score = evaluator.calculate_score(resume_text, jd_text)
    recommendations = _get_llm_recommendations(resume_text, jd_text)
    return score, recommendations

def auto_improve(resume_data, jd_text):
    """Auto-improve functionality"""
    prompt = f"Improve this resume for JD: {jd_text}\nResume: {resume_data}"
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Helper functions (not exported)
def _resume_to_text(resume_data):
    text = f"Name: {resume_data['name']}\nSummary: {resume_data['summary']}\n"
    for exp in resume_data['experiences']:
        text += f"{exp['title']} at {exp['company']} ({exp['duration']})\n"
    return text + "\nSkills: " + ", ".join(resume_data['skills'])

def _get_llm_recommendations(resume_text, jd_text):
    prompt = f"Analyze resume against JD:\n{jd_text}\n\nResume:\n{resume_text}"
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content