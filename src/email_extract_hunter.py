import pandas as pd
import requests
import time

# === CONFIGURATION ===
HUNTER_API_KEY = "f5e89c54514dbafc19b8299baaff4e4da5fd271d"  # Replace with your Hunter.io API key
INPUT_CSV = "./jobs.csv"  # Path to your CSV file
OUTPUT_CSV = "emails.csv"  # Output file

# === STEP 1: Load CSV and Extract Company Names ===
df = pd.read_csv(INPUT_CSV)

if "company" not in df.columns:
    raise ValueError("CSV file must have a 'company' column!")

companies = df["company"].dropna().unique()

# === STEP 2: Get Company Domain from Hunter.io ===
def get_company_domain(company_name):
    url = f"https://api.hunter.io/v2/domain-search?company={company_name}&api_key={HUNTER_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "data" in data and "domain" in data["data"]:
        return data["data"]["domain"]
    return None

# === STEP 3: Get Emails from Hunter.io ===
def get_company_emails(domain):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
    response = requests.get(url)
    data = response.json()

    emails = []
    if "data" in data and "emails" in data["data"]:
        for email_info in data["data"]["emails"]:
            emails.append(email_info["value"])
    return emails

# === STEP 4: Loop Through Companies & Extract Emails ===
results = []
for company in companies:
    print(f"Searching for {company}...")
    
    domain = get_company_domain(company)
    if not domain:
        print(f"❌ No domain found for {company}")
        continue
    
    print(f"✅ Domain found: {domain}")

    emails = get_company_emails(domain)
    if emails:
        for email in emails:
            results.append({"Company": company, "Domain": domain, "Email": email})
        print(f"📧 Found {len(emails)} emails for {company}")
    else:
        print(f"❌ No emails found for {company}")

    time.sleep(2)  # Avoid hitting API limits

# === STEP 5: Save Results to CSV ===
if results:
    df_results = pd.DataFrame(results)
    df_results.to_csv(OUTPUT_CSV, index=False)
    print(f"\n✅ Email extraction completed! Results saved in {OUTPUT_CSV}")
else:
    print("\n❌ No emails found for any company.")

