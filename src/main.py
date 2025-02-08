# main.py

# main.py

from file_extractor import extract_resume_text
from text_preprocessing import clean_text
from skill_extractor import extract_skills

def match_profiles(user_skills, job_profiles):
    """
    Compare the user's skills to a dictionary of job profiles.
    
    Parameters:
        user_skills (list): List of skills extracted from the user's resume.
        job_profiles (dict): Keys are job profile names and values are lists of required skills.
    
    Returns:
        dict: A dictionary where keys are job profiles and values are dicts with:
              - "match_count": number of skills the user has for that profile.
              - "ratio": the fraction of required skills the user possesses.
              - "missing_skills": list of skills missing for that profile.
    """
    results = {}
    # Convert user skills to a set of lowercased strings for case-insensitive matching
    user_set = set(skill.lower() for skill in user_skills)
    
    for profile, required_skills in job_profiles.items():
        # Lowercase all required skills for matching
        required_set = set(skill.lower() for skill in required_skills)
        match_count = len(user_set.intersection(required_set))
        ratio = match_count / len(required_set) if required_set else 0
        missing_skills = list(required_set - user_set)
        results[profile] = {"match_count": match_count, "ratio": ratio, "missing_skills": missing_skills}
    return results

def process_resume(file_path):
    """
    Process a resume file by extracting text, cleaning it, extracting skills,
    and matching the skills against predefined job profiles.

    Parameters:
        file_path (str): The path to the resume file.
    
    Returns:
        dict: A dictionary containing:
              - extracted_skills: List of skills found in the resume.
              - best_fit_profile: The job profile with the highest match.
              - best_profile_match_ratio: The match ratio (fraction) for the best-fit profile.
              - best_profile_missing_skills: List of missing skills for the best-fit profile.
              - alternative_matches: Top 5 alternative profile matches.
    """
    # 1. Extract text from the resume file
from skill_extractor import extract_skills

def match_profiles(user_skills, job_profiles):
    """
    Compare the user's skills to a dictionary of job profiles.
    
    Parameters:
        user_skills (list): List of skills extracted from the user's resume.
        job_profiles (dict): Keys are job profile names and values are lists of required skills.
    
    Returns:
        dict: A dictionary where keys are job profiles and values are dicts with:
              - "match_count": number of skills the user has for that profile.
              - "ratio": the fraction of required skills the user possesses.
              - "missing_skills": list of skills missing for that profile.
    """
    results = {}
    # Convert user skills to a set of lowercased strings
    user_set = set(skill.lower() for skill in user_skills)
    
    for profile, required_skills in job_profiles.items():
        # Lowercase all required skills for matching
        required_set = set(skill.lower() for skill in required_skills)
        match_count = len(user_set.intersection(required_set))
        ratio = match_count / len(required_set) if required_set else 0
        missing_skills = list(required_set - user_set)
        results[profile] = {"match_count": match_count, "ratio": ratio, "missing_skills": missing_skills}
    return results

def main():
    # Replace with the path to your resume file (PDF or DOCX)
    file_path = "data/ShauryaResume.pdf"
    
    # 1. Extract text from the resume file
    raw_text = extract_resume_text(file_path)
    if not raw_text:
        return {"error": "Failed to extract text from the resume."}

    # 2. Preprocess the extracted text
    # 2. Preprocess the extracted text (remove extra whitespaces, lowercasing, etc.)
    cleaned_text = clean_text(raw_text)
    
    # 3. Extract skills using spaCy's PhraseMatcher
    user_skills = extract_skills(cleaned_text)
    
    # 4. Define job profiles with required skills
    job_profiles = {
        "Software Developer": ["python", "java", "c++", "git", "algorithms", "data structures"],
        "Front-End Developer": ["javascript", "html", "css", "react", "angular", "vue", "responsive design", "ui design"],
        "Back-End Developer": ["python", "java", "node.js", "sql", "rest api", "microservices", "docker"],
        "Full Stack Developer": ["python", "javascript", "html", "css", "react", "node.js", "sql", "git"],
        "Mobile App Developer": ["java", "kotlin", "swift", "react native", "flutter", "android", "ios"],
        "Data Scientist": ["python", "machine learning", "data analysis", "statistics", "r", "pandas", "numpy", "scikit-learn", "tensorflow"],
        "Data Analyst": ["excel", "sql", "tableau", "data visualization", "python", "statistics"],
        "Machine Learning Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn", "data preprocessing"],
        "DevOps Engineer": ["docker", "kubernetes", "aws", "ci/cd", "jenkins", "terraform", "git", "linux"],
        "Cloud Engineer": ["aws", "azure", "gcp", "docker", "kubernetes", "linux", "cloud architecture"],
        "Cybersecurity Analyst": ["cybersecurity", "network security", "penetration testing", "risk management", "firewalls", "incident response"],
        "Network Engineer": ["networking", "tcp/ip", "routing", "switching", "cisco", "firewalls", "vpn"],
        "System Administrator": ["linux", "windows", "bash", "powershell", "networking", "troubleshooting"],
        "Database Administrator": ["sql", "mysql", "postgresql", "oracle", "database tuning", "backup and recovery"],
        "QA Engineer": ["testing", "automation", "selenium", "cypress", "manual testing", "bug tracking"],
        "UI/UX Designer": ["ui design", "ux research", "sketch", "figma", "adobe xd", "prototyping", "wireframing"],
        "Graphic Designer": ["photoshop", "illustrator", "indesign", "adobe creative suite", "branding", "layout design"],
        "Product Manager": ["product management", "roadmapping", "agile", "scrum", "communication", "market research"],
        "Project Manager": ["project management", "agile", "scrum", "kanban", "communication", "risk management"],
        "Business Analyst": ["business analysis", "requirements gathering", "data analysis", "documentation", "communication"],
        "Data Engineer": ["python", "sql", "spark", "hadoop", "etl", "data pipelines", "big data"],
        "Technical Writer": ["technical writing", "documentation", "communication", "research", "content creation"],
        "Game Developer": ["c++", "unity", "unreal engine", "game design", "3d modeling", "graphics programming"],
        "Embedded Systems Engineer": ["c", "c++", "embedded systems", "microcontrollers", "rtos", "hardware integration"],
        "IoT Engineer": ["iot", "embedded systems", "arduino", "raspberry pi", "python", "wireless communication"],
        "Blockchain Developer": ["blockchain", "solidity", "ethereum", "smart contracts", "cryptography", "decentralized applications"],
        "Digital Marketer": ["digital marketing", "seo", "content marketing", "social media", "analytics", "ppc"],
        "SEO Specialist": ["seo", "google analytics", "keyword research", "content optimization", "link building"],
        "Content Strategist": ["content strategy", "copywriting", "seo", "content marketing", "blogging", "research"],
        "Social Media Manager": ["social media", "content creation", "digital marketing", "analytics", "communication", "branding"],
        "E-commerce Specialist": ["ecommerce", "digital marketing", "seo", "conversion optimization", "analytics", "shopify"],
        "Salesforce Developer": ["salesforce", "apex", "visualforce", "crm", "lightning", "integration"],
        "CRM Specialist": ["crm", "salesforce", "data analysis", "customer service", "communication", "marketing automation"],
        "Enterprise Architect": ["enterprise architecture", "system design", "cloud computing", "it strategy", "business analysis"],
        "AI Researcher": ["artificial intelligence", "machine learning", "deep learning", "research", "python", "algorithm development"],
        "Robotics Engineer": ["robotics", "control systems", "c++", "python", "embedded systems", "machine vision"],
        "Augmented Reality Developer": ["augmented reality", "unity", "c#", "3d modeling", "vuforia", "ui design"],
        "Virtual Reality Developer": ["virtual reality", "unreal engine", "unity", "c#", "3d modeling", "vr design"],
        "GIS Analyst": ["gis", "arcgis", "data analysis", "mapping", "spatial analysis", "cartography"],
        "DevSecOps Engineer": ["devops", "cybersecurity", "automation", "docker", "kubernetes", "aws", "security compliance"],
        "Systems Engineer": ["systems engineering", "linux", "networking", "hardware", "troubleshooting", "documentation"],
        "Site Reliability Engineer": ["sre", "linux", "aws", "kubernetes", "monitoring", "automation", "python"],
        "Automation Engineer": ["automation", "selenium", "python", "robot framework", "ci/cd", "testing"],
        "Test Automation Engineer": ["test automation", "selenium", "cypress", "python", "java", "automation frameworks"],
        "Security Engineer": ["cybersecurity", "penetration testing", "network security", "risk management", "firewalls", "incident response"],
        "Infrastructure Engineer": ["infrastructure", "linux", "networking", "cloud computing", "automation", "virtualization"],
        "Cloud Architect": ["cloud architecture", "aws", "azure", "gcp", "docker", "kubernetes", "devops"],
        "UI Developer": ["html", "css", "javascript", "react", "angular", "ui design", "responsive design"],
        "UX Researcher": ["ux research", "usability testing", "user interviews", "prototyping", "data analysis", "communication"],
        "Network Administrator": ["networking", "tcp/ip", "routing", "switching", "cisco", "firewalls", "network security"]
    }
    
    # 5. Compare user skills to each job profile
    profile_matches = match_profiles(user_skills, job_profiles)
    
    # Sort profiles by match ratio (highest first)
    sorted_profiles = sorted(profile_matches.items(), key=lambda x: x[1]["ratio"], reverse=True)
    
    # Determine the best-fit profile
    best_profile, best_data = sorted_profiles[0]
    
    # Prepare the result dictionary to return
    result = {
        "extracted_skills": user_skills,
        "best_fit_profile": best_profile,
        "best_profile_match_ratio": best_data["ratio"],
        "best_profile_missing_skills": best_data["missing_skills"],
        "alternative_matches": sorted_profiles[1:6]  # Top 5 alternative profiles
    }
    
    print("\nBest Fit Profile:", best_profile)
    print("Match Ratio: {:.2f}%".format(best_data["ratio"] * 100))
    print("Missing Skills for this profile:", best_data["missing_skills"])
    
    print("\nOther Top Profile Matches:")
    for profile, data in sorted_profiles[1:6]:
        print(f"{profile}: {data['ratio']*100:.2f}% match, Missing: {data['missing_skills']}")
    
    return result
    # 3. Extract skills using spaCy's PhraseMatcher (from your skill_extractor module)
    user_skills = extract_skills(cleaned_text)
    print("Extracted Skills (spaCy):", user_skills)
    
    # 4. Define job profiles with required skills (around 50 profiles)
    job_profiles = {
        "Software Developer": ["python", "java", "c++", "git", "algorithms", "data structures"],
        "Front-End Developer": ["javascript", "html", "css", "react", "angular", "vue", "responsive design", "ui design"],
        "Back-End Developer": ["python", "java", "node.js", "sql", "rest api", "microservices", "docker"],
        "Full Stack Developer": ["python", "javascript", "html", "css", "react", "node.js", "sql", "git"],
        "Mobile App Developer": ["java", "kotlin", "swift", "react native", "flutter", "android", "ios"],
        "Data Scientist": ["python", "machine learning", "data analysis", "statistics", "r", "pandas", "numpy", "scikit-learn", "tensorflow"],
        "Data Analyst": ["excel", "sql", "tableau", "data visualization", "python", "statistics"],
        "Machine Learning Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn", "data preprocessing"],
        "DevOps Engineer": ["docker", "kubernetes", "aws", "ci/cd", "jenkins", "terraform", "git", "linux"],
        "Cloud Engineer": ["aws", "azure", "gcp", "docker", "kubernetes", "linux", "cloud architecture"],
        "Cybersecurity Analyst": ["cybersecurity", "network security", "penetration testing", "risk management", "firewalls", "incident response"],
        "Network Engineer": ["networking", "tcp/ip", "routing", "switching", "cisco", "firewalls", "vpn"],
        "System Administrator": ["linux", "windows", "bash", "powershell", "networking", "troubleshooting"],
        "Database Administrator": ["sql", "mysql", "postgresql", "oracle", "database tuning", "backup and recovery"],
        "QA Engineer": ["testing", "automation", "selenium", "cypress", "manual testing", "bug tracking"],
        "UI/UX Designer": ["ui design", "ux research", "sketch", "figma", "adobe xd", "prototyping", "wireframing"],
        "Graphic Designer": ["photoshop", "illustrator", "indesign", "adobe creative suite", "branding", "layout design"],
        "Product Manager": ["product management", "roadmapping", "agile", "scrum", "communication", "market research"],
        "Project Manager": ["project management", "agile", "scrum", "kanban", "communication", "risk management"],
        "Business Analyst": ["business analysis", "requirements gathering", "data analysis", "documentation", "communication"],
        "Data Engineer": ["python", "sql", "spark", "hadoop", "etl", "data pipelines", "big data"],
        "Technical Writer": ["technical writing", "documentation", "communication", "research", "content creation"],
        "Game Developer": ["c++", "unity", "unreal engine", "game design", "3d modeling", "graphics programming"],
        "Embedded Systems Engineer": ["c", "c++", "embedded systems", "microcontrollers", "rtos", "hardware integration"],
        "IoT Engineer": ["iot", "embedded systems", "arduino", "raspberry pi", "python", "wireless communication"],
        "Blockchain Developer": ["blockchain", "solidity", "ethereum", "smart contracts", "cryptography", "decentralized applications"],
        "Digital Marketer": ["digital marketing", "seo", "content marketing", "social media", "analytics", "ppc"],
        "SEO Specialist": ["seo", "google analytics", "keyword research", "content optimization", "link building"],
        "Content Strategist": ["content strategy", "copywriting", "seo", "content marketing", "blogging", "research"],
        "Social Media Manager": ["social media", "content creation", "digital marketing", "analytics", "communication", "branding"],
        "E-commerce Specialist": ["ecommerce", "digital marketing", "seo", "conversion optimization", "analytics", "shopify"],
        "Salesforce Developer": ["salesforce", "apex", "visualforce", "crm", "lightning", "integration"],
        "CRM Specialist": ["crm", "salesforce", "data analysis", "customer service", "communication", "marketing automation"],
        "Enterprise Architect": ["enterprise architecture", "system design", "cloud computing", "it strategy", "business analysis"],
        "AI Researcher": ["artificial intelligence", "machine learning", "deep learning", "research", "python", "algorithm development"],
        "Robotics Engineer": ["robotics", "control systems", "c++", "python", "embedded systems", "machine vision"],
        "Augmented Reality Developer": ["augmented reality", "unity", "c#", "3d modeling", "vuforia", "ui design"],
        "Virtual Reality Developer": ["virtual reality", "unreal engine", "unity", "c#", "3d modeling", "vr design"],
        "GIS Analyst": ["gis", "arcgis", "data analysis", "mapping", "spatial analysis", "cartography"],
        "DevSecOps Engineer": ["devops", "cybersecurity", "automation", "docker", "kubernetes", "aws", "security compliance"],
        "Systems Engineer": ["systems engineering", "linux", "networking", "hardware", "troubleshooting", "documentation"],
        "Site Reliability Engineer": ["sre", "linux", "aws", "kubernetes", "monitoring", "automation", "python"],
        "Automation Engineer": ["automation", "selenium", "python", "robot framework", "ci/cd", "testing"],
        "Test Automation Engineer": ["test automation", "selenium", "cypress", "python", "java", "automation frameworks"],
        "Security Engineer": ["cybersecurity", "penetration testing", "network security", "risk management", "firewalls", "incident response"],
        "Infrastructure Engineer": ["infrastructure", "linux", "networking", "cloud computing", "automation", "virtualization"],
        "Cloud Architect": ["cloud architecture", "aws", "azure", "gcp", "docker", "kubernetes", "devops"],
        "UI Developer": ["html", "css", "javascript", "react", "angular", "ui design", "responsive design"],
        "UX Researcher": ["ux research", "usability testing", "user interviews", "prototyping", "data analysis", "communication"],
        "Network Administrator": ["networking", "tcp/ip", "routing", "switching", "cisco", "firewalls", "network security"]
    }
    
    # 5. Compare user skills to each job profile
    profile_matches = match_profiles(user_skills, job_profiles)
    
    # Sort profiles by match ratio (highest first)
    sorted_profiles = sorted(profile_matches.items(), key=lambda x: x[1]["ratio"], reverse=True)
    
    # Determine the best-fit profile
    best_profile, best_data = sorted_profiles[0]
    print("\nBest Fit Profile:", best_profile)
    print("Match Ratio: {:.2f}%".format(best_data["ratio"] * 100))
    print("Missing Skills for this profile:", best_data["missing_skills"])
    
    # Optionally, show a few alternative profiles
    print("\nOther Top Profile Matches:")
    for profile, data in sorted_profiles[1:6]:
        print(f"{profile}: {data['ratio']*100:.2f}% match, Missing: {data['missing_skills']}")

if __name__ == "__main__":
    import sys
    # If a file path is provided as a command-line argument, use it; otherwise, use a default path.
    file_path = sys.argv[1] if len(sys.argv) > 1 else "data/ShauryaResume.pdf"
    
    # Process the resume and print the analysis result
    result = process_resume(file_path)
    print("Analysis Result:")
    print(result)
