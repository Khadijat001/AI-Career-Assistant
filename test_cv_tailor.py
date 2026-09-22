from src.pdf_reader import extract_text_from_pdf
from src.cv_tailor import tailor_cv


pdf_path = "data/Khadijat_CV.pdf"

cv_text = extract_text_from_pdf(pdf_path)

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


print("Generating tailored CV...")
print("Please wait...\n")


tailored_cv = tailor_cv(
    cv_text,
    job_description
)


print("========== TAILORED CV ==========\n")
print(tailored_cv)