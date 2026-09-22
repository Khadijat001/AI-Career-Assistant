import re


def normalize_skill(skill):
    """
    Convert a skill to lowercase and remove extra spaces.
    """
    skill = skill.lower().strip()
    skill = re.sub(r"\s+", " ", skill)

    return skill


def calculate_skill_match(job_skills, cv_skills):
    """
    Compare skills required by a job with skills found in a CV.
    """

    # Normalize skills
    job_skills = [normalize_skill(skill) for skill in job_skills]
    cv_skills = [normalize_skill(skill) for skill in cv_skills]

    matched = []
    missing = []

    for skill in job_skills:

        if skill in cv_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    # Calculate skill coverage
    if len(job_skills) > 0:
        coverage = (len(matched) / len(job_skills)) * 100
    else:
        coverage = 0

    return {
        "matched": matched,
        "missing": missing,
        "coverage": round(coverage, 1)
    }