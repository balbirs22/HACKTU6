import math
import datetime
import pandas as pd
import requests
import time

from file_extractor import extract_resume_text
from text_preprocessing import clean_text
from skill_extractor import extract_skills
import jobhunt  # jobhunt.search_jobs(job_role) must return a pandas DataFrame

def match_profiles(user_skills, job_profiles):
    """
    Compare the user's skills to a dictionary of job profiles.
    Returns a dictionary mapping each profile to its match ratio and missing skills.
    """
    results = {}
    user_set = set(skill.lower() for skill in user_skills)
    for profile, required_skills in job_profiles.items():
        required_set = set(skill.lower() for skill in required_skills)
        match_count = len(user_set.intersection(required_set))
        ratio = match_count / len(required_set) if required_set else 0
        missing_skills = list(required_set - user_set)
        results[profile] = {"match_count": match_count, "ratio": ratio, "missing_skills": missing_skills}
    return results

def process_resume(file_path):
    """
    Process a resume file:
      1. Extract and clean text.
      2. Extract skills.
      3. Match skills against predefined job profiles.
      4. Search for jobs using the best-fit profile.
      5. Return a dictionary with:
           - extracted_skills: List of skills.
           - best_fit_profile: Best-fit job role.
           - job_url: URL of the top job match.
           - job_title: Title of the top job match.
    """
    print(f"Processing resume: {file_path}")
    
    # Extract text from the resume.
    raw_text = extract_resume_text(file_path)
    if not raw_text:
        print("Error: Failed to extract text.")
        return {"error": "Failed to extract text from the resume."}
    
    # Clean the text.
    cleaned_text = clean_text(raw_text)
    
    # Extract skills.
    user_skills = extract_skills(cleaned_text)
    print("Extracted Skills:", user_skills)
    
    # Define a few job profiles.
    job_profiles = {
        "Software Developer": ["python", "java", "c++", "git", "algorithms", "data structures"],
        "Data Scientist": ["python", "machine learning", "data analysis", "statistics", "tensorflow", "scikit-learn"],
        "Machine Learning Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "data preprocessing"]
    }
    
    # Match profiles.
    profile_matches = match_profiles(user_skills, job_profiles)
    sorted_profiles = sorted(profile_matches.items(), key=lambda x: x[1]["ratio"], reverse=True)
    best_profile, best_data = sorted_profiles[0]
    
    print("Best Fit Profile:", best_profile)
    print("Match Ratio:", best_data["ratio"] * 100, "%")
    
    # Search for jobs using the best-fit profile.
    print("Searching for jobs for role:", best_profile)
    jobs_df = jobhunt.search_jobs(best_profile)
    top_job = None
    try:
        top_job_record = jobs_df.head(1).to_dict(orient="records")
        if top_job_record:
            top_job = top_job_record[0]
            # Convert datetime objects to ISO strings and NaNs to None.
            for key, value in top_job.items():
                if isinstance(value, (datetime.date, datetime.datetime)):
                    top_job[key] = value.isoformat()
                elif isinstance(value, float) and math.isnan(value):
                    top_job[key] = None
    except Exception as e:
        print("Error processing job data:", e)
    
    result = {
        "extracted_skills": user_skills,
        "best_fit_profile": best_profile,
        "job_url": top_job.get("job_url") if top_job else None,
        "job_title": top_job.get("title") if top_job else None
    }
    
    return result

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else "data/BalbirLatestResume.pdf"
    final_result = process_resume(file_path)
    print("Final Analysis Result:")
    print(final_result)
