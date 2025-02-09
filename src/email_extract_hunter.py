import pandas as pd
import requests
import time
import os

HUNTER_API_KEY = "YOUR_HUNTER_API_KEY"  
INPUT_CSV = os.path.join(os.path.dirname(__file__), "../src/jobs.csv")  
OUTPUT_CSV = os.path.join(os.path.dirname(__file__), "../src/emails.csv")  

def extract_emails():
    df = pd.read_csv(INPUT_CSV)

    if "company" not in df.columns:
        print("❌ CSV file must have a 'company' column!")
        return

    companies = df["company"].dropna().unique()
    results = []

    for company in companies:
        print(f"🔎 Searching for {company}...")
        domain = get_company_domain(company)
        if not domain:
            print(f"❌ No domain found for {company}")
            continue

        emails = get_company_emails(domain)
        if emails:
            for email in emails:
                results.append({"Company": company, "Domain": domain, "Email": email})
            print(f"📧 Found {len(emails)} emails for {company}")

        time.sleep(2)  # Prevent API rate limit issues

    if results:
        pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False)
        print(f"✅ Emails extracted and saved in {OUTPUT_CSV}")
    else:
        print("❌ No emails found.")

def get_company_domain(company_name):
    url = f"https://api.hunter.io/v2/domain-search?company={company_name}&api_key={HUNTER_API_KEY}"
    response = requests.get(url).json()
    return response.get("data", {}).get("domain")

def get_company_emails(domain):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    response = requests.get(url).json()
    return [email["value"] for email in response.get("data", {}).get("emails", [])]

if __name__ == "__main__":
    extract_emails()
