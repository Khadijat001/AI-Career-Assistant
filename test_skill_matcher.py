from src.skill_matcher import calculate_skill_match


# Skills required by the job
job_skills = [
    "Python",
    "SQL",
    "Power BI",
    "Excel",
    "Tableau",
    "Credit Risk",
    "Machine Learning"
]


# Skills demonstrated in the CV
cv_skills = [
    "Python",
    "SQL",
    "Power BI",
    "Excel",
    "Machine Learning"
]


# Calculate the match
result = calculate_skill_match(
    job_skills,
    cv_skills
)


print("========== SKILL MATCH RESULTS ==========\n")

print("Matched Skills:")

for skill in result["matched"]:
    print(f"✓ {skill}")


print("\nMissing Skills:")

for skill in result["missing"]:
    print(f"✗ {skill}")


print(f"\nSkill Coverage: {result['coverage']}%")