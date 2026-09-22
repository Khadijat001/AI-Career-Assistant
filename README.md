#AI Career Assistant

**AI-powered CV analysis and career support tool built with Python, Streamlit, and Gemini.**

**Author:** Khadijat Abubakar
**Course:** MIT Universal AI Course

## About the Project

The **AI Career Assistant** helps job seekers understand how well their CV matches a specific job opportunity.

Users upload their CV and paste a job description. The application uses AI to identify genuine strengths, transferable skills, skill gaps, relevant experience, and interview preparation needs.

It can also create a **tailored version of the CV** for the selected job while keeping the candidate's qualifications truthful.

> **Tailor the CV, not the candidate's qualifications.**

## Problem

Job seekers often struggle to tailor their CVs to different job opportunities.

Manually comparing a CV with a job description takes time and can make it difficult to identify which skills and experience should be highlighted.

## Solution

My solution is an **AI Career Assistant** that compares a CV with a job description.

It:

* Identifies relevant skills and experience
* Highlights transferable skills
* Identifies skill gaps
* Suggests ways to improve the CV
* Generates interview questions
* Creates a tailored CV
* Allows the tailored CV to be downloaded as Word or PDF

## How It Works

```text
Upload CV
    ↓
Paste Job Description
    ↓
Extract CV Text
    ↓
AI Analysis with Gemini
    ↓
Identify Strengths & Skill Gaps
    ↓
Generate Interview Questions
    ↓
Create Tailored CV
    ↓
Download Word / PDF
```

## Features

### 1. CV Upload

Users can upload their CV as a PDF.

### 2. Job Description Analysis

Users paste the job description for the position they are interested in.

### 3. AI Career Analysis

The application analyzes the CV against the job description and provides:

* Match summary
* Requirement evidence
* Skills already demonstrated
* Skills not demonstrated
* Experience gaps
* Relevant experience
* CV improvement suggestions
* Interview questions

### 4. Tailored CV

The AI creates a version of the CV that emphasizes experience and skills that are genuinely relevant to the target position.

### 5. Word and PDF Export

Users can download their tailored CV as:

* `.docx`
* `.pdf`

### 6. Responsible AI

The application is designed to avoid fabricating qualifications.

The original CV is treated as the **source of truth**. The AI is instructed not to invent:

* Work experience
* Skills
* Certifications
* Education
* Achievements
* Job titles
* Employers
* Projects
* Dates
* Technologies or tools

The system also distinguishes between **direct experience**, **transferable skills**, and **skill gaps**.

## Responsible AI Approach

A key design principle of this project is:

> **The AI should tailor the CV, not change the candidate's qualifications.**

For example, if a candidate has data analysis experience but no digital marketing experience, the system should not present the candidate as a digital marketing professional.

Instead, it can identify data analysis as a **transferable skill** while clearly showing digital marketing as a **skill gap**.

This helps users understand what they genuinely have and what they may need to develop.

## Project Structure

```text
AI-Career-Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── ai_analyzer.py
│   ├── cv_exporter.py
│   ├── cv_tailor.py
│   ├── pdf_reader.py
│   └── skill_matcher.py
│
├── test_analyzer.py
├── test_cv_tailor.py
├── test_gemini.py
└── test_skill_matcher.py
```

## Technologies Used

* **Python** — application logic
* **Streamlit** — web application interface
* **Google Gemini** — AI analysis and CV tailoring
* **PyPDF** — PDF text extraction
* **python-docx** — Word document generation
* **ReportLab** — PDF generation
* **python-dotenv** — environment variable management

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Khadijat001/AI-Career-Assistant.git
```

### 2. Open the project folder

```bash
cd AI-Career-Assistant
```

### 3. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

**Do not upload your `.env` file to GitHub.**

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Privacy and Security

The project uses environment variables for the Gemini API key.

Personal CV files and local data are excluded from the GitHub repository using `.gitignore`.

Users should review their generated CV before using it for a job application.

## Course Project

This project was developed as part of the **MIT Universal AI Course** to demonstrate how generative AI can be applied to a practical career-support problem.

The project combines:

* AI
* Python programming
* Document processing
* Natural-language analysis
* Responsible AI principles
* User-focused application design

## Future Improvements

Possible future versions could include:

* Cover letter generation
* LinkedIn profile optimization
* Interview practice with AI
* Job application tracking
* Multiple CV versions
* Job recommendation based on demonstrated skills
* Improved CV formatting and templates

## Author

**Khadijat Abubakar**

Built with Python, Streamlit, and Gemini.

---

### Project Goal

The goal is not to make a candidate appear qualified for every job.

The goal is to help candidates **present their real qualifications in the most relevant way**.
