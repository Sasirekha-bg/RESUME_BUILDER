# RESUME_BUILDER

## Description
RESUME_BUILDER is an AI-powered, applicant tracking system (ATS)-friendly resume generator. This application helps job seekers create optimized resumes tailored to specific job descriptions, improving their chances of passing ATS screening. It evaluates resume quality, provides suggestions for improvement, and generates a polished PDF resume.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Sasirekha-bg/RESUME_BUILDER.git
    ```
2. Navigate to the project directory:
    ```bash
    cd RESUME_BUILDER
    ```
3. Create and activate a virtual environment (optional but recommended):
    ```bash
   conda create -p venv python==3.12
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Set up your environment variables in a `.env` file:
    ```env
    GROQ_API_KEY="your-groq-api-key"
    ```

## Usage
1. Run the application:
    ```bash
    streamlit run app.py
    ```
2. Open the app in your browser at `http://localhost:8501`.
3. Follow the on-screen instructions to:
   - Enter personal details, education, experience, and projects.
   - Upload job descriptions to evaluate your resume.
   - Receive an ATS-friendly score and improvement suggestions.
   - Download a well-structured PDF resume.

## Features
- **AI-Powered ATS Analysis:** Evaluates resumes against job descriptions and provides actionable feedback.
- **Automated Resume Improvement:** Suggests enhancements tailored to the job role.
- **PDF Resume Generation:** Creates clean, professional resumes ready for job applications.
- **User-Friendly Interface:** Built with Streamlit for intuitive form-based input.

## Tech Stack
- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Machine Learning:** scikit-learn
- **PDF Generation:** ReportLab
- **Environment Management:** virtualenv
- **API Integration:** OpenAI API (or GROQ API)

## Folder Structure
```
RESUME_BUILDER/
|-- .env
|-- .gitignore
|-- app.py
|-- requirements.txt
|-- modules/
    |-- __init__.py
    |-- ats_analyzer.py
    |-- pdf_generator.py
    |-- resume_builder.py
    |-- scoring.py
```

## Module Overview
- `app.py`: Streamlit-based frontend for user interaction.
- `modules/resume_builder.py`: Collects user resume data.
- `modules/ats_analyzer.py`: Matches resumes with job descriptions and provides recommendations.
- `modules/pdf_generator.py`: Generates a well-formatted PDF resume.
- `modules/scoring.py`: Uses machine learning to evaluate resume-job description similarity.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push the changes to your fork.
5. Submit a pull request.

