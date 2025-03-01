from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class ATSEvaluator:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    def calculate_score(self, resume_text, jd_text):
        # Keyword Matching
        vectors = self.vectorizer.fit_transform([jd_text, resume_text])
        similarity = np.dot(vectors[0], vectors[1].T)
        
        # Structure Scoring
        structure_score = self.check_resume_structure(resume_text)
        
        return (similarity[0][0] * 60) + (structure_score * 40)

    def check_resume_structure(self, text):
        # Add your custom structure checking logic
        required_sections = ['experience', 'education', 'skills']
        return sum(1 for section in required_sections if section in text.lower())/len(required_sections)*100