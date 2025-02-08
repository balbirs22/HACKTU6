import csv
from jobspy import scrape_jobs

def search_jobs(job_role):
    """
    Searches for jobs using the provided job role as the search term.
    Location is set to 'Bangalore, India' and the country is set to 'India'.
    The google_search_term is automatically generated.
    
    Parameters:
        job_role (str): The job role to search for.
    
    Returns:
        DataFrame: A DataFrame containing the scraped job listings.
    """
    # Use the best-fit job role as the search term
    search_term = job_role
    # Generate a Google search term based on the job role
    google_search_term = f"{job_role} jobs near Bangalore, India since yesterday"
    location = "Bangalore, India"
    
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
        search_term=search_term,
        google_search_term=google_search_term,
        location=location,
        results_wanted=20,
        hours_old=72,
        country_indeed="India",
    )
    
    print(f"Found {len(jobs)} jobs")
    print(jobs.head())
    
    # Save the job listings to a CSV file (optional)
    jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    
    return jobs

if __name__ == "__main__":
    # For testing purposes, search for a sample role.
    search_jobs("Software Developer")
