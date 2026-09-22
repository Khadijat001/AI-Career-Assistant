from src.pdf_reader import extract_text_from_pdf
from src.ai_analyzer import analyze_cv


# Read CV
pdf_path = "data/Khadijat_CV.pdf"
cv_text = extract_text_from_pdf(pdf_path)


# Read Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


# Analyze CV against Job Description
print("Analyzing CV...")
print("Please wait...\n")

result = analyze_cv(cv_text, job_description)

print("========== AI CAREER ANALYSIS ==========\n")
print(result)